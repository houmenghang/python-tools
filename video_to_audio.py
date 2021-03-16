import os

def video_process(video, audio_name):
    shell = 'ffmpeg -i "{}" -f mp3 "{}"'.format(video, audio_name.replace(' ', ''))
    os.system(shell)
