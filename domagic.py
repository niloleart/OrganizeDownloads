import functions as f

DOWNLOADS_SRC = '/Users/niloleart/Desktop/test_mv_files'
VUZE_SRC = '/Users/niloleart/Desktop/test_vuze_files'


# show = 'Young'
# season = '01'
# episode = '09'
# zip_file_path = '/Users/niloleart/Desktop/test_mv_files/Young.Sheldon.S01E05.HDTV.x264-SVA.zip'
# sub_file_name = 'Young.Sheldon.S01E05.720p.HDTV.HEVC.x265-RMTeam.srt'
# dst_path = '/Users/niloleart/Desktop/test_vuze_files/Young.Sheldon.S01E05.HDTV.x264-SVA[rarbg]'
# movie_name = 'Young.Sheldon.S01E05.HDTV.x264-SVA'


def domagic():
    show = raw_input("Show: ").lower()
    season = raw_input("Season: ").lower()
    episode = raw_input("Episode: ").lower()

    sub_file, sub_file_path = f.find_sub(DOWNLOADS_SRC)
    if sub_file_path:
        ### VUZE HANDLINGS
        dst_path = f.find_folder(show, season, episode, VUZE_SRC)
        movie_name = f.find_movie(dst_path)
        f.move_srt(sub_file_path, dst_path, movie_name)

        ### TORRENT FILE HANDLING
        torrent_file_path = f.find_torrent(show, season, episode, '.torrent', DOWNLOADS_SRC)
        f.remove_torrent(torrent_file_path)


    else:
        ### EXTRACT SRT FILE AND REMOVE ZIP
        zip_file_path = f.find_zip(show, season, episode, 'zip', DOWNLOADS_SRC)
        sub_file_name = f.unzip_sub(zip_file_path, DOWNLOADS_SRC)

        dst_path = f.find_folder(show, season, episode, VUZE_SRC)
        movie_name = f.find_movie(dst_path)
        f.move_srt(sub_file_name, dst_path, movie_name)


        ### REMOVE ZIP AND TORRENT
        torrent_file_path = f.find_torrent(show, season, episode, '.torrent', DOWNLOADS_SRC)
        f.remove_zip(zip_file_path)
        f.remove_torrent(torrent_file_path)

domagic()
