import argparse
import subprocess

# podem executarlo des de terminal posant el video en questio
# EXEMPLE:
# python3 readMP4container.py 'video.mp4'

parser = argparse.ArgumentParser(description='Get video information')
parser.add_argument('in_filename', help='Input filename')
args = parser.parse_args()


def broadcastFit(filename): # guardem codecs

    print('Broacdasting Standards compatibles amb', filename)
    codec_video = subprocess.getoutput('ffprobe -v error -select_streams v:0 -show_entries stream=codec_name -of '
                                       'default=nokey=1:noprint_wrappers=1 {}'.format(filename))
    codec_audio = subprocess.getoutput('ffprobe -v error -select_streams a:0 -show_entries stream=codec_name -of '
                                       'default=nokey=1:noprint_wrappers=1 {}'.format(filename))
    # print(codec_video)
    # print(codec_audio)

    # comparem els codecs del video amb els standards
    if codec_video == 'h264' or 'mpeg2':

        if codec_audio == 'mp3':
            broadcast = 'Compatible amb: DVB i DTMB'
            print(broadcast)

        elif codec_audio == 'aac':
            broadcast = 'Compatible amb: DVB i ISDB i DTMB'
            print(broadcast)

        elif codec_audio == 'ac-3':
            broadcast = 'Comaptible amb: DVB i ATSC i DTMB'
            print(broadcast)

        else:
            print('No és compatible amb cap Standard')

    elif codec_video == 'avs' or 'avs+':

        if codec_audio == 'mp2' or 'dra':
            broadcast = 'Compatible amb: DTMB'
            print(broadcast)

    else:
        print('No és compatible amb cap Standard')


broadcastFit(args.in_filename)


