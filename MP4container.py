# script per crear containers d'arxius MP4 amb video, audio i subtitols

import sys
import subprocess

# aquest script permet crear un container MP4 directament executant-lo des del terminal posant
# el videoInput, AudioInput, subtitulsInput i el nom del fitxer de sortida
# EXEMPLE: python3 MP4container.py 'bbb_1min.mp4' 'bbb_1min_lowbitrate.mp3' 'bbb_subtitles.srt' 'outputFile.mp4'

# print('ffmpeg', '-i', sys.argv[1], '-i', sys.argv[2], '-i', sys.argv[3], ' -c copy', ' -map 0:v:0',
#                 ' -map 1:a:0', ' -c:s mov_text', sys.argv[4])
subprocess.call(['ffmpeg', '-i', sys.argv[1], '-i', sys.argv[2], '-i', sys.argv[3], ' -c copy', ' -map 0:v:0',
                 ' -map 1:a:0', '-c:s mov_text', sys.argv[4]])

