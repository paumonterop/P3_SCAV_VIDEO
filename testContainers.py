# Aquest script permet rear containers i saber amb quin standard s'ajusten
# Es pot executar des de terminal de la seguent manera
# EXEMPLE: python3 testContainer.py 'bbb_1min.mp4' 'bbb_mp3.mp3' 'bbb_subtitles.srt' 'outputFile.mp4'

import os
import sys


if len(sys.argv) == 4:  # nomes video i audio
    os.system('ffmpeg -i {} -i {} -c:v copy -c:a -map 0:v:0 -map 1:a:0 {}'.format(sys.argv[1],
              sys.argv[2], sys.argv[3]))

elif len(sys.argv) == 5:  # video, audio i subtitols
    os.system('ffmpeg -i {} -i {} -i {} -c:v copy -c:a -c:s mov_text -map 0:v:0 -map 1:a:0 -map 2:s:0 {}'.format(
              sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]))

else:
    print('Masses arguments')

os.system('python3 readMP4container.py', sys.argv[4])