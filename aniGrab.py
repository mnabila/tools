"""
membuat agc untuk download anime
list site
1.animesave
2.meguminime
3.drivenime
4.bakacan
5.meownime
"""
import requests
from bs4 import BeautifulSoup
import sys
import argparse

class animeLink:
    def __init__(self):
        self.url={
            "animesave":"http://www.animesave.com/",
            "meguminime":"http://meguminime.com/",
            "drivenime":"https://drivenime.com/",
            "bakacan":"http://bakacan.id/",
            "meownime":"http://meownime.com/"
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

def command(argv=None):
    parse=argparse.ArgumentParser(description="tools untuk mencari link download anime")
    parse.add_argument("-s","--site",help="untuk menentukan website mana yang akan di ambil datanya. jika parameter site tidak diisi maka akan dicari diseluruh website yang ada(1.animesave 2.meguminime 3.drivenime 4.bakacan 5.meownime)")
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
    else:
        result["animesave"]=anime.animesave()
        result["meguminime"]=anime.meguminime()
        result["drivenime"]=anime.drivenime()
        result["bakacan"]=anime.bakacan()
        result["meownime"]=anime.meownime()

    for website in result:
        print("[+] %s"%website)
        for index in result[website]:
            print("\t[↪] %s"%index)
