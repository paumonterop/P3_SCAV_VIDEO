# P3_SCAV_VIDEO
Pràctica 3 - SCAV - VIDEO

**EXERCICI 1**

- Cut BBB into 1 minute only video.
*Amb el comando que ja haviem vist a les pràctiques anteriors*

- Export BBB(1min) audio as a mono track.
ffmpeg -i bbb_1min.mp4 -ac 1 -acodec mp3 bbb_mp3.mp3

- Export BBB(1min) audio in lower bitrate.
ffmpeg -i bbb_1min_mp3.mp3 -map 0:a:0 -b:a 16k bbb_1min_lowbitrate.mp3

- Get subtitles of BBB through the internet and cut only the first minute (sorry, I think this needs to be done manually)
bbb_subtitles.srt

- Now package everything in a .mp4 with FFMPEG!!
ffmpeg -i bbb_1min.mp4 -i bbb_1min_lowbitrate.mp3 -i bbb_subtitles.srt -c copy -map 0:v:0 -map 1:a:0 -c:s mov_text bbb_1min_audio_subtitles.mp4


**EXERCICI 2**

Aquest script permet crear un container MP4 directament executant-lo des del terminal posant el videoInput, AudioInput, subtitulsInput i el nom del fitxer de sortida. També es pot executar només er ajuntar audio al container de l'arxiu.
El podem executar des del terminal de la seguent manera:
EXEMPLE: *python3 MP4container.py 'bbb_1min.mp4' 'bbb_mp3.mp3' 'bbb_subtitles.srt' 'outputFile.mp4'*

**EXERCICI 3**

Aquest script et diu en quins Standards s'ajusta el video en questio tenint en compte el video i l'audio.
Es pot executar directament des del terminal de la seguent manera:
EXEMPLE: *python3 readMP4container.py 'video.mp4'*

**EXERCICI 4**

Aquest script permet rear containers i saber amb quin standard s'ajusten
Es pot executar des de terminal de la seguent manera
EXEMPLE: *python3 testContainer.py 'bbb_1min.mp4' 'bbb_mp3.mp3' 'bbb_subtitles.srt' 'outputFile.mp4'*


