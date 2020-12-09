# P3_SCAV_VIDEO
Pràctica 3 - SCAV - VIDEO

**EXERCICI 1**

- Cut BBB into 1 minute only video.
ffmpeg -i bbb_1min.mp4 -ac 1 -acodec mp3 bbb_mp3.mp3

- Export BBB(1min) audio as a mono track.
fmpeg -i bbb_1min.mp3 -map 0:a:0 -b:a 96k bbb_1min_lowbitrate.mp3

- Export BBB(1min) audio in lower bitrate.
ffmpeg -i bbb_1min.mp3 -map 0:a:0 -b:a 16k bbb_1min_lowbitrate.mp3

- Get subtitles of BBB through the internet and cut only the first minute (sorry, I think this needs to be done manually)
bbb_subtitles.srt

- Now package everything in a .mp4 with FFMPEG!!
ffmpeg -i bbb_1min.mp4 -i bbb_1min_lowbitrate.mp3 -i bbb_subtitles.srt -c copy -map 0:v:0 -map 1:a:0 -c:s mov_text bbb_1min_audio_subtitles.mp4


**EXERCICI 2**

