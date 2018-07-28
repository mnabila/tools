from aniLink import animeLink
from flask import Flask,render_template,request
from aniForm import aniForm
from colorama import Fore, Back, Style
import time
import random
import binascii

app=Flask(__name__)
app.secret_key=binascii.hexlify(str(random.random()).encode("utf-8"))

def getData(website,keyword):
    anime=animeLink()
    result=dict()
    anime.search(keyword)
    if website == "animesave":
        result["animesave"]=anime.animesave()
    elif website == "meguminime":
        result["meguminime"]=anime.meguminime()
    elif website == "drivenime":
        result["drivenime"]=anime.drivenime()
    elif website == "bakacan":
        result["bakacan"]=anime.bakacan()
    elif website == "meownime":
        result["meownime"]=anime.meownime()
    elif website == "wibudesu":
        result["wibudesu"]=anime.wibudesu()
    elif website == "kusonime":
        result["kusonime"]=anime.kusonime()
    elif website == "awbatch":
        result["awbatch"]=anime.awbatch()
    elif website == "zonawibu":
        result["zonawibu"]=anime.zonawibu()
    elif website == "meowbatch":
        result["meowbatch"]=anime.meowbatch()
    else:
        result["animesave"]=anime.animesave()
        time.sleep(0.1)
        result["meguminime"]=anime.meguminime()
        time.sleep(0.1)
        result["drivenime"]=anime.drivenime()
        time.sleep(0.1)
        result["bakacan"]=anime.bakacan()
        time.sleep(0.1)
        result["meownime"]=anime.meownime()
        time.sleep(0.1)
        result["wibudesu"]=anime.wibudesu()
        time.sleep(0.1)
        result["kusonime"]=anime.kusonime()
        time.sleep(0.1)
        result["awbatch"]=anime.awbatch()
        time.sleep(0.1)
        result["zonawibu"]=anime.zonawibu()
        time.sleep(0.1)
        result["meowbatch"]=anime.meowbatch()
    return result

@app.route("/", methods=["POST","GET"])
def vIndex():
    form=aniForm(csrf_disabled=False)
    if request.method=="GET":
        return render_template("index.html",data={"form":form})
    elif request.method=="POST":
        if form.validate_on_submit():
            keyword=form.keyword.data
            website=form.listSite.data
            data=getData(website=website,keyword=keyword)
            waktu=time.strftime("%d-%m-%Y %H:%M:%S",time.localtime())
            for site in data:
                for b in data[site]:
                    if "error" in b :
                        print("{bRed}[{website}][{time}] {log}{bReset}".format(
                            website=site,
                            time=waktu,
                            log=b["error"],
                            bRed=Back.RED,
                            bReset=Back.RESET
                            )
                        )
                    else:
                        print("{fYellow}[{website}]{fReset}{fGreen}[{time}]{fReset} {log}".format(
                            website=site,
                            time=waktu,
                            log=b["title"],
                            fGreen=Fore.GREEN,
                            fYellow=Fore.YELLOW,
                            fReset=Fore.RESET
                            )
                        )
            return render_template("index.html",data={"form":form,"data":data})
        else:
            return render_template("index.html",data={"form":form})

if __name__ == "__main__":
    app.run(debug=True)