# script per crear containers d'arxius MP4 amb video, audio i subtitols

import os
import sys

# aquest script permet crear un container MP4 directament executant-lo des del terminal posant
# el videoInput, AudioInput, subtitulsInput i el nom del fitxer de sortida
# EXEMPLE: python3 MP4container.py 'bbb_1min.mp4' 'bbb_1min_lowbitrate.mp3' 'bbb_subtitles.srt' 'outputFile.mp4'

if len(sys.argv) == 4:  # nomes video i audio
    os.system('ffmpeg -i {} -i {} -c:v copy -c:a -map 0:v:0 -map 1:a:0 {}'.format(sys.argv[1],
              sys.argv[2], sys.argv[3]))

elif len(sys.argv) == 5:  # video, audio i subtitols
    os.system('ffmpeg -i {} -i {} -i {} -c:v copy -c:a -c:s mov_text -map 0:v:0 -map 1:a:0 -map 2:s:0 {}'.format(
              sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]))

else:
    print('Masses arguments')