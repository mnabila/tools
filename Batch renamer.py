# bath renamer for youtube file from youtube-dl
import re
import os
import argparse
import sys


def rename(path):
    filename = [f for f in os.listdir(
        path) if os.path.isfile(os.path.join(path, f))]
    for a in filename:
        file = os.path.join(path, a)
        cari = re.findall(r"-.{11}.mp4", file)
        new = file.replace(cari[0], ".mp4")
        os.rename(file, new)
        print(new)


def cmd(argv):
    parse = argparse.ArgumentParser(
        description="tools buat rename file dari youtube-dl")
    parse.add_argument('-d', '--dir', help='directory')
    return parse.parse_args(argv)


if __name__ == "__main__":
    # rename(sys.argv[1])
    dir = cmd(sys.argv[1:])
    rename(dir.dir)
