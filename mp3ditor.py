import argparse
import sys
import subprocess


try:
    from mutagen.easyid3 import EasyID3
except ImportError:
    print("installing mutagen")
    subprocess.Popen(["pip3", "install", "mutagen", "--user"]).communicate()


def editor(**kwargs):
    """
    file_path = None,
    title = None,
    artist = None,
    albumartist = None,
    album = None,
    date = None,
    tracknumber = None,
    genre = None,
    composer = None,
    performer = None,
    bpm = None,
    """
    audio = EasyID3(filename=kwargs["file_path"])
    for keys, value in kwargs.items():
        if keys != "file_path":
            if value is not None:
                audio[keys] = value
                audio.save()



def commandPromt(args=None):
    parse = argparse.ArgumentParser(
        description=" program untuk mengubah meta data pada music yang berformat mp3")
    parse.add_argument("-f", "--file_path", help="music files")
    parse.add_argument("-t", "--title", help="title")
    parse.add_argument("-ar","--artist", help="artist")
    parse.add_argument("-aa","--albumartist", help="album artist")
    parse.add_argument("-al","--album", help="album")
    parse.add_argument("-d", "--date", help="date")
    parse.add_argument("-tn","--tracknumber", help="track number")
    parse.add_argument("-g", "--genre", help="genre")
    parse.add_argument("-c", "--composer", help="composer")
    parse.add_argument("-p", "--performer", help="performer")
    parse.add_argument("-b", "--bpm", help="bpm")
    parse.add_argument("-v", "--version", help="print version about this programs", action="store_true")
    return parse.parse_args(args)


def main():
    data = commandPromt(sys.argv[1:])
    if data.version:
        print("""
version   : 0.1
code name : alpha
author    : https://github.com/nabil48
        """)
    else:
        editor(
            file_path=data.file_path,
            title=data.title,
            artist=data.artist,
            albumartist=data.albumartist,
            album=data.album,
            date=data.date,
            tracknumber=data.tracknumber,
            genre=data.genre,
            composer=data.composer,
            performer=data.performer,
            bpm=data.bpm
        )


if __name__ == "__main__":
    main()
