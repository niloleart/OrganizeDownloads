import os
import zipfile
import shutil


# Returns path to Zip File
def find_zip_torent(serie, SxxExx, extension, path):
    for file in [x.lower() for x in os.listdir(path)]:
        print file
        if file.endswith(extension) and serie in file and SxxExx in file:
            zip_path = os.path.join(path, file)
            print 'Zip path: ' + zip_path
            return zip_path

# Extracts subtitle and returns its name
def unzip_sub(path, root):
    zip_ref = zipfile.ZipFile(path, 'r')
    llista = zip_ref.namelist()
    for sub_file in llista:
        if sub_file.endswith('.srt') or sub_file.endswith('.SRT'):
            try:
                zip_ref.extract(sub_file, root)
            finally:
                print 'Extraccio completada: ' + sub_file
    zip_ref.close()
    sub_file = os.path.join(root,sub_file)
    return sub_file


def remove_zip_torrent(file):
    try:
        os.remove(file)
    finally:
        print 'Eliminat correctament: ' + file


def find_folder(serie, SxxExx, folder_path):
    for dir in [x.lower() for x in os.listdir(folder_path)]:
        if serie in dir.lower() and SxxExx in dir.lower():
            if serie:
                folder_path = os.path.join(folder_path, dir)
                print 'Folder path: ' + folder_path
                return folder_path
            else:
                print 'Folder not found'


def find_movie(folder_path):
    for file in [x.lower() for x in os.listdir(folder_path)]:
        if file.endswith('.mp4') or file.endswith('.avi') or file.endswith('.MP4') or file.endswith('.AVI') or file.endswith('.mkv') or file.endswith('.MKV'):
            movie_name = os.path.splitext(file)[0]
            print 'Movie Name: ' + movie_name
            return movie_name


def find_sub(folder_path):
    for sub_file in os.listdir(folder_path):
            if sub_file.endswith('.srt') or sub_file.endswith('.SRT'):
                sub_file = os.path.join(folder_path, sub_file)
                return sub_file


def move_srt(src, dst, movie_name):
    print src
    print dst
    print movie_name
    try:
        shutil.move(src, dst + '/' + movie_name + '.srt')
    finally:
        print 'Mogut correctament'