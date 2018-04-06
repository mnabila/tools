import os
import argparse
import sys
def command(argv=None):
    "untuk melakukan perintah cli "
    parse=argparse.ArgumentParser(description="mp42mp3 is a simple CLI program using ffmpeg for convert mp4 video to mp3")
    parse.add_argument("-i","--input",help="name file video (.mp4) will be convert to mp3")
    parse.add_argument("-o","--output", help="result file")
    
    result=parse.parse_args(argv)
    return(result.input,result.output)

def convert(masuk, keluar):
    # ffmpeg -i "ZAYN - Dusk Till Dawn ft. Sia.mp4" -q:a 0 -map a "ZAYN - Dusk Till Dawn ft. Sia.mp3";
    "fungsi untuk konversi dari video ke mp3 file"
    query='ffmpeg -i "{0}" -q:a 0 -map a "{1}";'.format(masuk,keluar)
    result = os.system(query)
    return result

if __name__ == "__main__":
    masuk,keluar=command(sys.argv[1:])
    convert(masuk,keluar)

