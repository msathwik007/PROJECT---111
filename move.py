import shutil
import os

from_dir = "C:/Users/saisa/Downloads"
to_dir = "C:/Users/saisa/OneDrive/Desktop/DOCUMENTS"
audio_dir = "C:/Users/saisa/OneDrive/Desktop/audio"
app_dir = "C:/Users/saisa/OneDrive/Desktop/applications"

files = os.listdir(from_dir)

for file_name in files:
    name,ext = os.path.splitext(file_name)
    if ext == '':
        continue
    if ext in ['.pdf','.doc','.xls','.txt']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + file_name
        shutil.move(path1,path2)

    elif ext in ['.m4a','.mp4','.mp3']:
        path1 = from_dir + '/' + file_name
        path2 = audio_dir + '/' + file_name
        shutil.move(path1,path2)
    elif ext in ['.exe']:
        path1 = from_dir + '/' + file_name
        path2 = app_dir + '/' + file_name
        shutil.move(path1,path2)


    

