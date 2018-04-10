"""
author:Nabil
site:http://github.com/nabil48
membuat agc untuk download anime
list site
1.animesave
2.meguminime
3.drivenime
4.bakacan
5.meownime
6.wibudesu
7.kusonime
8.awbatch
"""
import requests
from bs4 import BeautifulSoup
import sys
import argparse
import time
from colorama import Fore,Back,Style

class animeLink:
    def __init__(self):
        self.url={
            "animesave":"http://www.animesave.com/",
            "meguminime":"http://meguminime.com/",
            "drivenime":"https://drivenime.com/",
            "bakacan":"http://bakacan.id/",
            "meownime":"http://meownime.com/",
            "wibudesu":"https://wibudesu.com/",
            "kusonime":"https://kusonime.com/",
            "awbatch":"http://awbatch.in/"
        }
        self.header={
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate",
            "Connection":"keep-alive",
            "User-Agent":"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
        }
    def search(self,keyword):
        self.query={
            "animesave":{
                "s":keyword
            },
            "meguminime":{
                "s":keyword
            },
            "drivenime":{
                "s":keyword
            },
            "bakacan":{
                "s":keyword,
                "post_type":"anime"
            },
            "meownime":{
                "s":keyword,
                "submit":"Search"
            },
            "wibudesu":{
                "s":keyword,
                "post_type":"post"
            },
            "kusonime":{
                "s":keyword,
                "post_type":"post"
            },
            "awbatch":{
                "s":keyword
            }
        }
    def animesave(self):
        result=[]
        try:
            cnx=requests.get(self.url["animesave"],params=self.query["animesave"], headers=self.header)
            soup=BeautifulSoup(cnx.text, "lxml")
            div=soup.find(class_="allgreen")
            link=div.find_all("a")
            for a in link:
                data={}
                data["link"]=a["href"]
                data["title"]=a["title"]
                result.append(data)
        except:
            data={}
            data["link"]="404 Not Found"
            data["title"]="404 Not Found"
            result.append(data)
        return result
    
    def meguminime(self):
        result=[]
        try:
            cnx=requests.get(self.url["meguminime"],params=self.query["meguminime"], headers=self.header)
            soup=BeautifulSoup(cnx.text, "lxml")
            div=soup.find(class_="pst")
            link=div.find_all("h2")
            for h2 in link:
                data={}
                data["link"]=h2.a["href"]
                data["title"]=h2.a["title"]
                result.append(data)
        except:
            data={}
            data["link"]="404 Not Found"
            data["title"]="404 Not Found"
            result.append(data)
        return result
    
    def drivenime(self):
        result=[]
        try:
            cnx=requests.get(self.url["drivenime"],params=self.query["drivenime"], headers=self.header)
            soup=BeautifulSoup(cnx.text, "lxml")
            div=soup.find(id="content_box")
            link=div.find_all("h2")
            for h2 in link:
                data={}
                data["link"]=h2.a["href"]
                data["title"]=h2.a["title"]
                result.append(data)
        except:
            data={}
            data["link"]="404 Not Found"
            data["title"]="404 Not Found"
            result.append(data)
        return result
    
    def bakacan(self):
        result=[]
        try:
            cnx=requests.get(self.url["bakacan"],params=self.query["bakacan"], headers=self.header)
            soup=BeautifulSoup(cnx.text, "lxml")
            div=soup.find(class_="vinsmokebody")
            link=div.find_all("h2")
            for h2 in link:
                data={}
                data["link"]=h2.a["href"]
                data["title"]=h2.a["title"]
                result.append(data)
        except:
            data={}
            data["link"]="404 Not Found"
            data["title"]="404 Not Found"
            result.append(data)
        return result
    
    def meownime(self):
        result=[]
        try:
            cnx=requests.get(self.url["meownime"],params=self.query["meownime"], headers=self.header)
            soup=BeautifulSoup(cnx.text, "lxml")
            div=soup.find(class_="site-main")
            link=div.find_all(class_="entry-title")
            for h2 in link:
                data={}
                data["link"]=h2.a["href"]
                data["title"]=h2.a["title"]
                result.append(data)
        except:
            data={}
            data["link"]="404 Not Found"
            data["title"]="404 Not Found"
            result.append(data)
        return result
    
    def wibudesu(self):
        result=[]
        try:
            cnx=requests.get(self.url["wibudesu"],params=self.query["wibudesu"], headers=self.header)
            soup=BeautifulSoup(cnx.text, "lxml")
            div=soup.find(class_="rseries")
            link=div.find_all("h2")
            for h2 in link:
                data={}
                data["link"]=h2.a["href"]
                data["title"]=h2.a["title"]
                result.append(data)
        except:
            data={}
            data["link"]="404 Not Found"
            data["title"]="404 Not Found"
            result.append(data)
        return result

    def kusonime(self):
        result=[]
        try:
            cnx=requests.get(self.url["kusonime"],params=self.query["kusonime"], headers=self.header)
            soup=BeautifulSoup(cnx.text, "lxml")
            div=soup.find(class_="rseries")
            link=div.find_all("h2")
            for h2 in link:
                data={}
                data["link"]=h2.a["href"]
                data["title"]=h2.a["title"]
                result.append(data)
        except:
            data={}
            data["link"]="404 Not Found"
            data["title"]="404 Not Found"
            result.append(data) 
        return result

    def awbatch(self):
        result=[]
        try:
            cnx=requests.get(self.url["awbatch"],params=self.query["awbatch"], headers=self.header)
            soup=BeautifulSoup(cnx.text, "lxml")
            div=soup.find(class_="konten-tengah")
            link=div.find_all("h2")
            for h2 in link:
                data={}
                data["link"]=h2.a["href"]
                data["title"]=h2.a["title"]
                result.append(data)
        except:
            data={}
            data["link"]="404 Not Found"
            data["title"]="404 Not Found"
            result.append(data) 
        return result

# untuk command line
class commandLine:
    def command(self,argv=None):
        parse=argparse.ArgumentParser(description="tools untuk mencari link download anime")
        parse.add_argument("-s","--site",help="untuk menentukan website mana yang akan di ambil datanya. jika parameter site tidak  diisi maka akan dicari diseluruh website yang ada")
        parse.add_argument("-k","--keyword",help="kata kunci untuk mencari link")
        parse.add_argument("-ls","--listSite",help="daftar website yang dapat di ambil datanya",action="store_true")
        parse.add_argument("-g", "--gui",help="untuk menampilkan versi web dengan port 8080",action="store_true")
        parse.add_argument("-p","--port",help="untuk mengatur port yang versi GUI")
        parse.add_argument("-H","--host",help="untuk mengatur host yang akan digunaka untuk server")

        result=parse.parse_args(argv)
        return(result.site,result.keyword,result.listSite,result.gui,result.port, result.host)
    def banner(self):
        banner="            _  ____           _                \n"\
            "  __ _ _ __ (_)/ ___|_ __ __ _| |__   _ __  _   _ \n"\
            " / _` | '_ \| | |  _| '__/ _` | '_ \ | '_ \| | | |\n"\
            "| (_| | | | | | |_| | | | (_| | |_) || |_) | |_| |\n"\
            " \__,_|_| |_|_|\____|_|  \__,_|_.__(_) .__/ \__, |\n"\
            "  author: Nabil                      |_|    |___/ \n"\
            "  link: https://github.com/nabil48"
        return banner
    def listSite(self):
        site="[+] daftar website\n"\
        "\t[1] animesave\n"\
        "\t[2] meguminime\n"\
        "\t[3] drivenime\n"\
        "\t[4] bakacan\n"\
        "\t[5] meownime\n"\
        "\t[6] wibudesu\n"\
        "\t[7] kusonime\n"\
        "\t[8] awbatch"
        return site
    # ambil data
    def getData(self,site,keyword):
        anime=animeLink()
        anime.search(keyword.lower())
        result={}
        if site == "animesave":
            result["animesave"]=anime.animesave()
        elif site == "meguminime":
            result["meguminime"]=anime.meguminime()
        elif site == "drivenime":
            result["drivenime"]=anime.drivenime()
        elif site == "bakacan":
            result["bakacan"]=anime.bakacan()
        elif site == "meownime":
            result["meownime"]=anime.meownime()
        elif site == "wibudesu":
            result["wibudesu"]=anime.wibudesu()
        elif site == "kusonime":
            result["kusonime"]=anime.kusonime()
        elif site == "awbatch":
            result["awbatch"]=anime.awbatch()
        else:
            result["animesave"]=anime.animesave()
            time.sleep(1)
            result["meguminime"]=anime.meguminime()
            time.sleep(1)
            result["drivenime"]=anime.drivenime()
            time.sleep(1)
            result["bakacan"]=anime.bakacan()
            time.sleep(1)
            result["meownime"]=anime.meownime()
            time.sleep(1)
            result["wibudesu"]=anime.wibudesu()
            time.sleep(1)
            result["kusonime"]=anime.kusonime()
            time.sleep(1)
            result["awbatch"]=anime.awbatch()
        return result
    # untuk versi CLI
    def cliOutput(self,data):
        for website in data:
            print("[+] %s"%website)
            for index in data[website]:
                print(Fore.YELLOW,"\t[↪] %s"%index["title"],Fore.RESET)
                print("\t    %s"%index["link"])

    # untuk versi gui
    def guiOutput(self, port=8080,debug=True, host="0.0.0.0"):
        from flask import Flask, render_template, request
        app=Flask(__name__)
        @app.route("/", methods=["POST","GET"])
        def vIndex():
            if request.method == "GET":
                return render_template("index.html")
            else:
                keyword=request.form["keyword"]
                site=request.form["site"]
                result=self.getData(site,keyword)
                return render_template("index.html",data=result)
        @app.route("/404 Not Found")
        def vError():
            return render_template("error.html")
        app.run(port=port,debug=debug,host=host)



if __name__ == "__main__":
    cmd=commandLine()
    site,keyword,listSite,gui,port,host=cmd.command(sys.argv[1:])
    if listSite:
        print(cmd.listSite())
    else:
        if gui:
            if host and port:
                    cmd.guiOutput(host=str(host), port=int(port))
            else:
                cmd.guiOutput()
        else:
            print(Fore.GREEN,cmd.banner(),Fore.RESET)
            data=cmd.getData(site,keyword)
            cmd.cliOutput(data)