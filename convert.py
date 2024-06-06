import os
from pydub import AudioSegment

path_dir = '.\\GTZAN\\genres\\'
file_list = os.listdir(path_dir)
for file_name in file_list:
    print(file_name)
    if file_name.endswith(".au"):  # Or the audio file format you have
        full_path = os.path.join(path_dir, file_name)
        print(full_path)
        if os.path.exists(full_path):
            mp3_file = AudioSegment.from_file(full_path)
            mp3_file.export(f'{full_path[:-3]}.wav', format='wav')
        else:
            print(f"File not found: {full_path}")
