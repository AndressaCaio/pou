import os 
import shutitl
from_dir = 'C:\Users\andressa\Downloads'
to_dir = 'C:\Users\andressa\Downloads\;'
list_of_files = os.listdir(from_dir)
for file_name list_of_files:
    name,extesion = os.path.splitext(file_name)
    if extesion == "":
        continue
    if extesion in [".jpg",".png",".gif",".jfif"]:
        path1 = to_dir+'C:\Users\andressa\Downloads\;'+file_name
        path2 = to_dir+'C:\Users\andressa\Downloads\;'+file_name
        path3 = to_dir+'C:\Users\andressa\Downloads\;'+file_name
        path4 = to_dir+'C:\Users\andressa\Downloads\;'+file_name
        path5 = to_dir+'C:\Users\andressa\Downloads\;'+file_name
        path6 = to_dir+'C:\Users\andressa\Downloads\;'+file_name
        path7 = to_dir+'C:\Users\andressa\Downloads\;'+file_name
        if os.vices.os.path.exists(path7):
            shutli.move(path1,path7)
        else:
            shutil.move(path1,path7)
    