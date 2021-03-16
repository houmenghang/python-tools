import os
from read_excel import load_data
from video_download import get_video
from video_to_audio import video_process
 
video_output = r'\\192.168.1.100\data\houmenghang\test\video'
audio_output = r'\\192.168.1.100\data\houmenghang\test\audio'

if __name__ == "__main__":
    excel_file = 'data_list\小品节目单.xlsx'
    data = load_data(excel_file)
    for i in range(1, len(data)):
        video_path = os.path.join(video_output, '{}.mp4'.format(data[i][0]))
        audio_path = os.path.join(audio_output, '{}.mp3'.format(data[i][0]))
        if os.path.exists(video_path):
            if not os.path.exists(audio_path):
                video_process(video_path, audio_path)
        else:
            get_video(video_output, data[i][0], data[i][1])
