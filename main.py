import os
from read_excel import load_data
from video_download import get_video
from video_to_audio import video_process

video_output = r'\\192.168.1.100\data\houmenghang\test\video\海贼王'
audio_output = r'\\192.168.1.100\data\houmenghang\test\audio\海贼王'

if __name__ == "__main__":
    os.makedirs(video_output, exist_ok=True)
    os.makedirs(audio_output, exist_ok=True)
    excel_file = 'data_list\海贼王.xlsx'
    data = load_data(excel_file)
    for i in range(1, len(data)):
        video_path = os.path.join(
            video_output, '{}.mp4'.format(data[i][0].replace(' ', '')))
        audio_path = os.path.join(
            audio_output, '{}.mp3'.format(data[i][0].replace(' ', '')))
        if os.path.exists(video_path):
            if not os.path.exists(audio_path):
                video_process(video_path, audio_path)
        else:
            get_video(video_output, data[i][0], data[i][1])
            video_process(video_path, audio_path)
