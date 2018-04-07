"""
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
            cnx=requests.get(self.url["animesave"],params=self.query["animesave"])
            soup=BeautifulSoup(cnx.text, "lxml")
            div=soup.find(class_="allgreen")
            link=div.find_all("a")
            for a in link:
                result.append(a["href"])
        except:
            result.append("404 Not Found")
        return result
    
    def meguminime(self):
        result=[]
        try:
            cnx=requests.get(self.url["meguminime"],params=self.query["meguminime"])
            soup=BeautifulSoup(cnx.text, "lxml")
            div=soup.find(class_="pst")
            link=div.find_all("h2")
            for h2 in link:
                result.append(h2.a["href"])
        except:
            result.append("404 Not Found")
        return result
    
    def drivenime(self):
        result=[]
        try:
            cnx=requests.get(self.url["drivenime"],params=self.query["drivenime"])
            soup=BeautifulSoup(cnx.text, "lxml")
            div=soup.find(id="content_box")
            link=div.find_all("h2")
            for h2 in link:
                result.append(h2.a["href"])
        except:
            result.append("404 Not Found")
        return result
    
    def bakacan(self):
        result=[]
        try:
            cnx=requests.get(self.url["bakacan"],params=self.query["bakacan"])
            soup=BeautifulSoup(cnx.text, "lxml")
            div=soup.find(class_="vinsmokebody")
            link=div.find_all("h2")
            for h2 in link:
                result.append(h2.a["href"])
        except:
            result.append("404 Not Found")
        return result
    
    def meownime(self):
        result=[]
        try:
            cnx=requests.get(self.url["meownime"],params=self.query["meownime"])
            soup=BeautifulSoup(cnx.text, "lxml")
            div=soup.find(class_="site-main")
            link=div.find_all(class_="entry-title")
            for h2 in link:
                result.append(h2.a["href"])
        except:
            result.append("404 Not Found")
        return result
    
    def wibudesu(self):
        result=[]
        try:
            cnx=requests.get(self.url["wibudesu"],params=self.query["wibudesu"])
            soup=BeautifulSoup(cnx.text, "lxml")
            div=soup.find(class_="rseries")
            link=div.find_all("h2")
            for h2 in link:
                result.append(h2.a["href"])
        except:
            result.append("404 Not Found")
        return result
    def kusonime(self):
        result=[]
        try:
            cnx=requests.get(self.url["kusonime"],params=self.query["kusonime"])
            soup=BeautifulSoup(cnx.text, "lxml")
            div=soup.find(class_="rseries")
            link=div.find_all("h2")
            for h2 in link:
                result.append(h2.a["href"])
        except:
            result.append("404 Not Found") 
        return result

    def awbatch(self):
        result=[]
        try:
            cnx=requests.get(self.url["awbatch"],params=self.query["awbatch"])
            soup=BeautifulSoup(cnx.text, "lxml")
            div=soup.find(class_="konten-tengah")
            link=div.find_all("h2")
            for h2 in link:
                result.append(h2.a["href"])
        except:
            result.append("404 Not Found") 
        return result

def command(argv=None):
    parse=argparse.ArgumentParser(description="tools untuk mencari link download anime")
    parse.add_argument("-s","--site",help="untuk menentukan website mana yang akan di ambil datanya. jika parameter site tidak diisi maka akan dicari diseluruh website yang ada(1.animesave 2.meguminime 3.drivenime 4.bakacan 5.meownime 6.wibudesu 7.kusonime)")
    parse.add_argument("-k","--keyword",help="kata kunci untuk mencari link")

    result=parse.parse_args(argv)
    return(result.site,result.keyword)

if __name__ == "__main__":
    site, keyword=command(sys.argv[1:])
    anime=animeLink()
    anime.search(keyword)
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

    for website in result:
        print("[+] %s"%website)
        for index in result[website]:
            print("\t[↪] %s"%index)