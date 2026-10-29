# Prerequisites
Python 3.11 64-bit or newer.

Original CD in lossless WAV/FLAC format

Official Instrumental in lossless WAV/FLAC format

Tip: You can rip your CD in lossless quality with iTunes on Windows/Mac
Rhythmbox on Linux

## I recommend using a declipper in Audacity on the CD.

Normalize peaks to -12dB, then use the declipper. Export as 16/24bit FLAC or WAV


<img width="540" height="360" alt="1 - effect normalize" src="https://github.com/user-attachments/assets/f203ebf4-3254-4d04-8a6b-f58fc456a82b" />
<img width="540" height="360" alt="2 - -12dB" src="https://github.com/user-attachments/assets/4af46d64-e8ee-42cf-82e2-497514aaf133" />
<img width="540" height="360" alt="3 - effect clip fix" src="https://github.com/user-attachments/assets/04c1cbff-efec-4542-8764-e8b5ec99e45a" />
<img width="540" height="360" alt="4 - setting up clip fix" src="https://github.com/user-attachments/assets/229c0d6d-539a-46da-99a0-520cd76f54aa" />
<img width="540" height="360" alt="5 - loudness normalize" src="https://github.com/user-attachments/assets/8345c454-b0ba-4513-a5b3-a16ca148b2e3" />


# Getting official lossless instrumentals 

Official lossless instrumentals for all albums are available DRM-free on this Website https://www.supraphonline.cz/umelec/346896-dance-gavin-dance (each album costs approximately 14USD). I am not going to link to torrents or illegal downloads, pay for your music.

# Folder structure

Script expects numbered WAV/FLAC files in two folders (Vocals & Instru), with filenames matching this exact pattern:



`Vocals/

1Voc.wav

2Voc.wav

...

13Voc.wav

Instru/

1Ins.wav

2Ins.wav

...

13Ins.wav``


Output/ — created automatically


# Setting up Python

LINUX

`python3 -m pip install numpy scipy soundfile pyloudnorm
`
### If you get an error on Linux, run it in a virtual environment

`sudo apt install python3-venv
python3 -m venv .venv
source .venv/bin/activate`

`python -m pip install numpy scipy soundfile pyloudnorm`

WINDOWS

Run:
`py -m pip install numpy scipy soundfile`


# Run the script

Linux:
`python3 dgd_vocalextract_normalized_wav_flac.py`

Windows:
`py dgd_vocalextract_normalized_wav_flac.py`



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

They sound terrible

Didn't test other albums
