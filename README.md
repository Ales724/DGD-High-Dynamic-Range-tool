Prerequisites:
Operating system capable of
Python 3.11 64-bit or more.

Original CD in lossless WAV format
Official Instrumental

Tip: You can rip your CD in lossless quality with iTunes on Windows/Mac
Rhythmbox on Linux

I recommend using a declipper in Audacity on the CD.
Normalize peaks to -12dB, then use the declipper. Export as 16/24bit FLAC or WAV


The official lossless instrumentals are available DRM-free on this Website https://www.supraphonline.cz/umelec/346896-dance-gavin-dance. Each instrumental album costs approximately 14USD. There are other ways to get the instrumentals, but this is the method i used. I am not going to link to torrents or illegal downloads, pay for your music.



Setting up Python to work on Windows

Run:
py -m pip install numpy scipy soundfile

Verify the installation:
py -c "import numpy, scipy, soundfile; print('All dependencies installed')"

If it prints All dependencies installed, the required libraries are available.


Folder structure

The script expects numbered WAV files in two folders, with filenames matching this exact pattern:
VocalExtraction/

Vocals/

1Voc.wav

2Voc.wav

...

13Voc.wav

Instru/

1Ins.wav

2Ins.wav

...

13Ins.wav

Output/ — created automatically



The original mixes go in Vocals, and their corresponding instrumental versions go in Instru.

Run the script
Save the Python script in VocalExtraction, then open Command Prompt in that folder and run:
py dgd_vocalextract_reversed_cancellation(1).py


Alternatively, specify the directory explicitly:
py "C:\Audio\VocalExtraction\dgd_vocalextract_reversed_cancellation(1).py" "C:\Audio\VocalExtraction"


The output files will be saved in Output, named 1VocalExtract.flac through 13VocalExtract.flac.
5. Important limitations
- Both WAV files in each pair must have the same sample rate and channel count. The script checks these requirements.
- Synchronization searches for an offset of up to ±10 seconds.
- Gain matching uses the first 30 seconds, and cancellation is performed across the entire aligned track.
- The final FLAC output uses 24-bit PCM.
- The script processes tracks numbered 1 through 13 only. Missing pairs are skipped.


Known Issues:

3rd track from Downtown Battle Mountain
5th track from self-titled

Didn't test other albums
