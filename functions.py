import os
import zipfile
from zipfile import BadZipfile
import shutil
import sys
from termcolor import colored, cprint


# Returns path to Zip File
def find_zip(show, season, episode, extension, path):
    for zip_file in os.listdir(path):
        if zip_file.lower().endswith(extension) and show.lower() in zip_file.lower() and (
                    ('s' + season + 'e' + episode) or (season + 'x' + episode)) in zip_file.lower():
            zip_path = os.path.join(path, zip_file)
            done('ZIP FILE PATH:')
            done_msg(zip_path + '\n')
            return zip_path
    else:
        sys.exit('Unable to find zip file' + '\n')


def find_torrent(show, season, episode, extension, path):
    for zip_file in os.listdir(path):
        if zip_file.lower().endswith(extension) and show.lower() in zip_file.lower() and (
                    ('s' + season + 'e' + episode) or (season + 'x' + episode)) in zip_file.lower():
            zip_path = os.path.join(path, zip_file)
            done('TORRENT FILE PATH:')
            done_msg(zip_path + '\n')
            return zip_path
    else:
        sys.exit('Unable to find TORRENT file' + '\n')


# Extracts subtitle and returns its name
def unzip_sub(src, dst):
    try:
        zip_ref = zipfile.ZipFile(src, 'r')
        zip_files = zip_ref.namelist()
        for arx in zip_files:
            if arx.lower().endswith('.srt'):
                zip_ref.extract(arx, dst)
                done('FILE EXTRACTED:')
                done_msg(arx + '\n')
                zip_ref.close()
                arx = os.path.join(dst, arx)
                return arx
    except zipfile.BadZipFile as e:
        print e
        sys.exit('Unable to extract srt' + '\n')


def remove_zip(file):
    try:
        os.remove(file)
        done('ZIP FILE REMOVED:')
        done_msg(file + '\n')
    except OSError:
        fail('Unable to delete zip file' + '\n')


def remove_torrent(file):
    try:
        os.remove(file)
        done('TORRENT FILE REMOVED:')
        done_msg(file + '\n')
    except OSError:
        fail('Unable to delete torrent file' + '\n')


def find_folder(show, season, episode, vuze_path):
    for dir in os.listdir(vuze_path):
        if show.lower() in dir.lower() and (('s' + season + 'e' + episode) or (season + 'x' + episode)) in dir.lower():
            dst_path = os.path.join(vuze_path, dir)
            done('VUZE FOLDER PATH:')
            done_msg(dst_path + '\n')
            return dst_path
    else:
        fail('Vuze destination folder not found' + '\n')


def find_movie(folder_path):
    for file in os.listdir(folder_path):
        if file.lower().endswith('.mp4') or file.endswith('.avi') or file.endswith('.mkv'):
            movie_name = os.path.splitext(file)[0]
            done('MOVIE NAME:')
            done_msg(movie_name + '\n')
            return movie_name
    else:
        fail('Could not find movie file' + '\n')


def find_sub(folder_path):
    for sub_file in os.listdir(folder_path):
        if sub_file.lower().endswith('.srt'):
            sub_file_path = os.path.join(folder_path, sub_file)
            return sub_file, sub_file_path
    else:
        return False, False


def move_srt(sub_file, dst, movie_name):
    destination = dst + '/' + movie_name + '.srt'
    try:
        shutil.move(sub_file, destination)
        done('SUBTITLES FILE CORRECTLY MOVED FROM:')
        done_msg(sub_file)
        done('TO: ')
        done_msg(destination + '\n')
    except IOError:
        sys.exit('Could not move srt file' + '\n')
    except TypeError:
        sys.exit('Could not move srt file' + '\n')


def done(text):
    cprint(text, 'blue', attrs=['reverse'])


def done_msg(text):
    cprint(text, 'blue', attrs=['bold'])


def fail(text):
    cprint(text, 'red', attrs=['reverse', 'bold'])
    