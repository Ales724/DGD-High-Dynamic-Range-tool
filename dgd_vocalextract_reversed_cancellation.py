#!/usr/bin/env python3

import argparse
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy.signal import correlate


def find_offset(original, instrumental, sr, max_offset_seconds=10):
    """Find the sample offset giving the strongest correlation."""

    a = original.mean(axis=1)
    b = instrumental.mean(axis=1)

    # Use the first 30 seconds for synchronization.
    n = min(len(a), len(b), sr * 30)

    a = a[:n]
    b = b[:n]

    # Remove DC.
    a -= np.mean(a)
    b -= np.mean(b)

    max_lag = int(max_offset_seconds * sr)

    correlation = correlate(
        a,
        b,
        mode="full",
        method="fft"
    )

    center = len(b) - 1

    start = max(0, center - max_lag)
    end = min(len(correlation), center + max_lag + 1)

    region = correlation[start:end]

    best = start + np.argmax(np.abs(region))

    return best - center


def align(original, instrumental, offset):

    if offset > 0:
        original = original[offset:]

    elif offset < 0:
        instrumental = instrumental[-offset:]

    length = min(
        len(original),
        len(instrumental)
    )

    return (
        original[:length],
        instrumental[:length]
    )


def find_gain(original, instrumental):
    """Find the instrumental gain that best matches the original mix."""

    x = original.reshape(-1)
    y = instrumental.reshape(-1)

    denominator = np.dot(y, y)

    if denominator == 0:
        return 1.0

    return np.dot(x, y) / denominator


def process_track(
    instrumental_path,
    original_path,
    output_path
):

    print()
    print("=" * 60)
    print(f"Instrumental : {instrumental_path.name}")
    print(f"Original     : {original_path.name}")

    print("Loading...")

    instrumental, sr_i = sf.read(
        instrumental_path,
        dtype="float64",
        always_2d=True
    )

    original, sr_o = sf.read(
        original_path,
        dtype="float64",
        always_2d=True
    )

    if sr_i != sr_o:
        raise RuntimeError(
            f"Sample rates differ: "
            f"{sr_i} vs {sr_o}"
        )

    if instrumental.shape[1] != original.shape[1]:
        raise RuntimeError(
            f"Channel counts differ: "
            f"{instrumental.shape[1]} vs "
            f"{original.shape[1]}"
        )

    sr = sr_i

    print(f"Sample rate: {sr} Hz")

    print("Finding synchronization...")

    offset = find_offset(
        original,
        instrumental,
        sr
    )

    print(
        f"Offset: {offset:+d} samples "
        f"({offset / sr:+.6f} seconds)"
    )

    original, instrumental = align(
        original,
        instrumental,
        offset
    )

    print("Finding cancellation gain...")

    # Use first 30 seconds for gain calculation.
    n = min(
        len(original),
        sr * 30
    )

    gain = find_gain(
        original[:n],
        instrumental[:n]
    )

    print(
        f"Gain: {gain:.10f}"
    )

    print("Performing cancellation...")

    # Original full mix - gain-matched instrumental
    # This leaves the original mix as-is and subtracts the instrumental.
    vocal = original - gain * instrumental

    # Remove tiny numerical DC offset.
    vocal -= np.mean(
        vocal,
        axis=0,
        keepdims=True
    )

    print(
        f"Writing: {output_path.name}"
    )

    # Write temporary floating-point WAV.
    temp_wav = output_path.with_suffix(".tmp.wav")

    sf.write(
        temp_wav,
        vocal.astype(np.float32),
        sr,
        format="WAV",
        subtype="FLOAT"
    )

    # Convert to FLAC through soundfile.
    # PCM_24 gives plenty of precision for the final file.
    sf.write(
        output_path,
        vocal,
        sr,
        format="FLAC",
        subtype="PCM_24"
    )

    temp_wav.unlink(missing_ok=True)

    print("Done.")


def main():

    parser = argparse.ArgumentParser(
        description=(
            "Batch vocal extraction using "
            "instrumental/master cancellation."
        )
    )

    parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="Directory containing Vocals and Instru."
    )

    args = parser.parse_args()

    base = Path(args.directory)

    vocals_dir = base / "Vocals"
    instru_dir = base / "Instru"
    output_dir = base / "Output"

    if not vocals_dir.is_dir():
        raise SystemExit(
            f"Missing folder: {vocals_dir}"
        )

    if not instru_dir.is_dir():
        raise SystemExit(
            f"Missing folder: {instru_dir}"
        )

    output_dir.mkdir(
        exist_ok=True
    )

    for number in range(1, 14):

        vocal_file = vocals_dir / f"{number}Voc.wav"
        instru_file = instru_dir / f"{number}Ins.wav"

        if not vocal_file.exists():
            print(
                f"[SKIP] Missing {vocal_file}"
            )
            continue

        if not instru_file.exists():
            print(
                f"[SKIP] Missing {instru_file}"
            )
            continue

        output_file = (
            output_dir /
            f"{number}VocalExtract.flac"
        )

        try:

            process_track(
                instru_file,
                vocal_file,
                output_file
            )

        except Exception as e:

            print(
                f"[ERROR] Track {number}: {e}"
            )

    print()
    print("=" * 60)
    print("All tracks processed.")
    print(f"Output folder: {output_dir}")


if __name__ == "__main__":
    main()
