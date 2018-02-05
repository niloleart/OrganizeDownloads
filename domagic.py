import functions as f

DOWNLOADS_SRC = '/Users/niloleart/Downloads/'
VUZE_SRC = '/Users/niloleart/Documents/Vuze Downloads/'


def domagic():
    print 'Enter Serie Name and Episode (in format S__E__)'
    serie = raw_input("Serie: ").lower()
    episode = raw_input("Episode: ").lower()

    zip_file_path = f.find_zip_torent(serie, episode, '.zip', DOWNLOADS_SRC)

    if zip_file_path:

        sub_file = f.unzip_sub(zip_file_path, DOWNLOADS_SRC)

        f.remove_zip_torrent(zip_file_path)

        folder_path = f.find_folder(serie, episode, VUZE_SRC)

        movie_name = f.find_movie(folder_path)

        f.move_srt(sub_file,folder_path,movie_name)

        torrent_file_path = f.find_zip_torent(serie, episode, '.torrent', DOWNLOADS_SRC)

        f.remove_zip_torrent(torrent_file_path)

    else:
        sub_file = f.find_sub(DOWNLOADS_SRC)
        if sub_file:
            folder_path = f.find_folder(serie, episode, VUZE_SRC)

            movie_name = f.find_movie(folder_path)

            f.move_srt(sub_file, folder_path, movie_name)

            torrent_file_path = f.find_zip_torent(serie, episode, '.torrent', DOWNLOADS_SRC)

            f.remove_zip_torrent(torrent_file_path)

        else:
            print 'No trobat'

domagic()