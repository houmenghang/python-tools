import os
import librosa
from librosa.core import audio
import datetime

work_path = r'C:\Users\houme\Desktop\于丹'


def load_audio_playtime(audiofile):
    time = librosa.get_duration(filename=audiofile)
    return time


def time_format(time):
    m, s = divmod(time, 60)
    h, m = divmod(m, 60)
    return("%d:%02d:%02d" % (h, m, s))
    # return h, m, s


def cut_audio(time, audio, file):
    cut_list = ['上', '中', '下']
    filename, filetype = os.path.splitext(file)
    cut_time = int(time / 3 + 0.5)
    start_time = 0
    for cut_point in cut_list:
        out_audio = 'audio\output\{}_{}.mp3'.format(
            filename.replace(' ', ''), cut_point)
        end_time = start_time + cut_time
        if end_time > time:
            end_time = time
        shell = 'ffmpeg -y -i "{}" -ss {} -t {} "{}"'.format(
            audio, time_format(start_time), time_format(end_time), out_audio)
        # print(time_format(start_time), time_format(end_time))
        # print(shell)
        os.system(shell)
        # print(time, start_time, end_time)
        start_time += cut_time
    end_time = 0


def main():
    for file in os.listdir(work_path):
        audio_file = os.path.join(work_path, file)
        time = load_audio_playtime(audio_file)
        cut_audio(time, audio_file, file)


if __name__ == '__main__':
    main()
