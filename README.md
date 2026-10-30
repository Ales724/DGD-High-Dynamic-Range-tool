<img width="700" height="300" alt="Screenshot from 2026-10-30 14-11-12" src="https://github.com/user-attachments/assets/6a9c621c-3262-4265-a11d-81fc1d48a4d0" />
<img width="700" height="300" alt="image" src="https://github.com/user-attachments/assets/41700f3d-21a2-414d-8409-1dbc8c9fb1b4" />


# Prerequisites
Python 3.11 64-bit or newer.

Original CD in lossless WAV/FLAC format

Official Instrumental in lossless WAV/FLAC format

Tip: You can rip your CD in lossless quality with iTunes on Windows/Mac
Rhythmbox on Linux

## I recommend using a declipper in Audacity on the CD.

Normalize the original CD tracks peaks to −12 dB before applying Clip Fix. This provides headroom and prevents artifacting.


<img width="540" height="360" alt="1 - effect normalize" src="https://github.com/user-attachments/assets/f203ebf4-3254-4d04-8a6b-f58fc456a82b" />
<img width="540" height="360" alt="2 - -12dB" src="https://github.com/user-attachments/assets/4af46d64-e8ee-42cf-82e2-497514aaf133" />
<img width="540" height="360" alt="3 - effect clip fix" src="https://github.com/user-attachments/assets/04c1cbff-efec-4542-8764-e8b5ec99e45a" />
<img width="540" height="360" alt="4 - setting up clip fix" src="https://github.com/user-attachments/assets/abbe75a7-f845-4b91-a493-2acaf1eff411" />
<img width="540" height="360" alt="6 - export" src="https://github.com/user-attachments/assets/75575dd4-99dd-4834-a340-d55523ac24e4" />
<img width="480" height="360" alt="7 - export" src="https://github.com/user-attachments/assets/91afe8fc-b277-4ce4-9d56-6141d846c0ad" />



Export at 24bit FLAC/WAV 44.1kHz

# Getting official lossless instrumentals 

Official lossless instrumentals for all albums are available DRM-free on these Websites 

https://www.supraphonline.cz/umelec/346896-dance-gavin-dance (each album costs approximately 14USD)
https://www.qobuz.com/us-en/interpreter/dance-gavin-dance/313471/page/3. (15.09USD)

I am not going to link to torrents or illegal downloads, pay for your music.

# Folder structure

Script expects numbered WAV/FLAC files in two folders (`Vocals` & `Instru`), with filenames matching this exact pattern:

```text
YourFolder/
├── dgd_vocalextract_reversed_cancellation.py
├── Vocals/
│   ├── 1Voc.wav
│   ├── 2Voc.wav
│   ├── ...
│   └── 18Voc.wav
├── Instru/
│   ├── 1Ins.wav
│   ├── 2Ins.wav
│   ├── ...
│   └── 18Ins.wav
└── Output/
    ├── 1VocalExtract.flac
    ├── 2VocalExtract.flac
    └── ...
```
<img width="800" height="480" alt="Screenshot from 2026-10-30 14-10-44" src="https://github.com/user-attachments/assets/c7b48329-3947-4b7b-ae4a-2f2571c0ed49" />


Output folder — created automatically


# Setting up Python

**Requirements:** Python 3.11 (64-bit) or newer.

Required Python libraries:
- numpy
- scipy
- soundfile
- pyloudnorm

## LINUX (Linux Mint / Ubuntu)

Open a terminal in the folder containing the script and the `Vocals` and `Instru` folders.

For example:

```bash
cd ~/Music/DGD
```

Create a Python virtual environment:

```bash
sudo apt install python3-venv
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install the required libraries:

```bash
python -m pip install numpy scipy soundfile pyloudnorm
```

## WINDOWS

Open Command Prompt or PowerShell in the folder containing the script and the `Vocals` and `Instru` folders.

Install the required libraries:

```powershell
py -m pip install numpy scipy soundfile pyloudnorm
```

# Running the script

**Linux:**

Activate the virtual environment first:

```bash
source .venv/bin/activate
```

Then run:

```bash
python dgd_vocalextract_reversed_cancellation.py
```

**Windows:**

```powershell
py dgd_vocalextract_reversed_cancellation.py
```

*note: i only tested the script on Linux, but the instructions should work on Windows. Open an issue or send me a DM with an error so i can work around it

# Output

The script automatically creates an `Output` folder.

Processed tracks are saved as 24-bit FLAC files:

```text
Output/
├── 1VocalExtract.flac
├── 2VocalExtract.flac
├── 3VocalExtract.flac
└── ...
```

The script processes tracks numbered 1 through 18. Missing input pairs are skipped






The output files will be saved in Output, named 1VocalExtract.flac through 13VocalExtract.flac.

# Important limitations
- Both WAV files in each pair must have the same sample rate and channel count. The script checks these requirements.
- Synchronization searches for an offset of up to ±10 seconds.
- Gain matching uses the first 30 seconds, and cancellation is performed across the entire aligned track.
- The final FLAC output uses 24-bit PCM.
- The script processes tracks numbered 1 through 18 only. Missing pairs are skipped.


Known Issues:

3rd track from Downtown Battle Mountain
5th track from self-titled

They sound weird.

I ONLY TESTED FIRST TWO ALBUMS
