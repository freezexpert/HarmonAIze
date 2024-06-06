import os

path_dir = '.\\GTZAN\\genres\\'
file_list = os.listdir(path_dir)
for file_name in file_list:
    print(file_name)
    if file_name.endswith(".au"):  # Or the audio file format you have
        full_path = os.path.join(path_dir, file_name)
        print(full_path)
        if os.path.exists(full_path):
            os.remove(full_path)