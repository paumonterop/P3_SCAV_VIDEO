import argparse
import subprocess

# podem executarlo des de terminal posant el video en questio
# EXEMPLE:
# python3 readMP4container.py 'video.mp4'

parser = argparse.ArgumentParser(description='Get video information')
parser.add_argument('in_filename', help='Input filename')
args = parser.parse_args()


def broadcastFit(filename): # guardem codecs
    cmnd = ['ffprobe', '-show_format', '-show_streams', '-loglevel', 'quiet', filename]
    p = subprocess.Popen(cmnd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print('Broacdasting Standards compatibles amb', filename)
    out, err = p.communicate()
    out_string = out.decode()
    outstring = out_string.split('\n')
    codec_video = outstring[2]
    codec_audio = outstring[59]
    # print(codec_video)
    # print(codec_audio)

# comaprem els codecs del video amb els standards
    if codec_video == 'codec_name=h264' or 'codec_name=mpeg2':

        if codec_audio == 'codec_name=mp3':
            broadcast = 'Compatible amb: DVB i DTMB'
            print(broadcast)

        elif codec_audio == 'codec_name=acc':
            broadcast = 'Compatible amb: DVB i ISDB i DTMB'
            print(broadcast)

        elif codec_audio == 'codec_name=ac-3':
            broadcast = 'Comaptible amb: DVB i ATSC i DTMB'
            print(broadcast)

        else:
            print('No és compatible amb cap Standard')

    elif codec_video == 'codec_name=avs' or 'codec_name=avs+':

        if codec_audio == 'codec_name=mp2' or 'codec_name=dra':
            broadcast = 'Compatible amb: DTMB'
            print(broadcast)

    else:
        print('No és compatible amb cap Standard')


broadcastFit(args.in_filename)


