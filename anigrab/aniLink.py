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
9.meowbatch
"""
import requests
from bs4 import BeautifulSoup


class animeLink:
    def __init__(self):
        self.url = {
            "animesave": "http://www.animesave.com/",
            "meguminime": "http://meguminime.com/",
            "drivenime": "https://drivenime.com/",
            "bakacan": "http://bakacan.id/",
            "meownime": "http://meownime.com/",
            "wibudesu": "https://wibudesu.com/",
            "kusonime": "https://kusonime.com/",
            "awbatch": "http://awbatch.in/",
            "meowbatch": "http://meowbatch.com"
        }
        self.header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
        }

    def search(self, keyword):
        self.query = {
            "animesave": {
                "s": keyword
            },
            "meguminime": {
                "s": keyword
            },
            "drivenime": {
                "s": keyword
            },
            "bakacan": {
                "s": keyword,
                "post_type": "anime"
            },
            "meownime": {
                "s": keyword,
                "submit": "Search"
            },
            "wibudesu": {
                "s": keyword,
                "post_type": "post"
            },
            "kusonime": {
                "s": keyword,
                "post_type": "post"
            },
            "awbatch": {
                "s": keyword
            },
            "meowbatch": {
                "s": keyword
            }
        }

    def website(self, site=None):
        """
        list site
            1.animesave
            2.meguminime
            3.drivenime
            4.bakacan
            5.meownime
            6.wibudesu
            7.kusonime
            8.awbatch
            9.meowbatch
        """
        result = list()
        if site == "animesave":
            try:
                cnx = requests.get(
                    self.url["animesave"],
                    params=self.query["animesave"],
                    headers=self.header
                )
                soup = BeautifulSoup(cnx.text, "lxml")
                div = soup.find(class_="allgreen")
                link = div.find_all("a")
                for a in link:
                    data = dict()
                    data["link"] = a["href"]
                    data["title"] = a["title"]
                    result.append(data)
            except Exception as e:
                data = dict()
                data["error"] = "404 Not Found"
                result.append(data)
        elif site == "meguminime":
            try:
                cnx = requests.get(
                    self.url["meguminime"],
                    params=self.query["meguminime"],
                    headers=self.header
                )
                soup = BeautifulSoup(cnx.text, "lxml")
                div = soup.find(class_="pst")
                link = div.find_all("h2")
                for h2 in link:
                    data = dict()
                    data["link"] = h2.a["href"]
                    data["title"] = h2.a["title"]
                    result.append(data)
            except Exception as e:
                data = dict()
                data["error"] = "404 Not Found"
                result.append(data)
        elif site == "drivenime":
            try:
                cnx = requests.get(
                    self.url["drivenime"],
                    params=self.query["drivenime"],
                    headers=self.header
                )
                soup = BeautifulSoup(cnx.text, "lxml")
                div = soup.find(id="content_box")
                link = div.find_all("h2")
                for h2 in link:
                    data = dict()
                    data["link"] = h2.a["href"]
                    data["title"] = h2.a["title"]
                    result.append(data)
            except Exception as e:
                data = dict()
                data["error"] = "404 Not Found"
                result.append(data)
        elif site == "bakacan":
            try:
                cnx = requests.get(
                    self.url["bakacan"],
                    params=self.query["bakacan"],
                    headers=self.header
                )
                soup = BeautifulSoup(cnx.text, "lxml")
                div = soup.find(class_="vinsmokebody")
                link = div.find_all("h2")
                for h2 in link:
                    data = dict()
                    data["link"] = h2.a["href"]
                    data["title"] = h2.a["title"]
                    result.append(data)
            except Exception as e:
                data = dict()
                data["error"] = "404 Not Found"
                result.append(data)
        elif site == "meownime":
            try:
                cnx = requests.get(
                    self.url["meownime"],
                    params=self.query["meownime"],
                    headers=self.header
                )
                soup = BeautifulSoup(cnx.text, "lxml")
                div = soup.find(class_="site-main")
                link = div.find_all(class_="entry-title")
                for h2 in link:
                    data = dict()
                    data["link"] = h2.a["href"]
                    data["title"] = h2.a["title"]
                    result.append(data)
            except Exception as e:
                data = dict()
                data["error"] = "404 Not Found"
                result.append(data)
        elif site == "wibudesu":
            try:
                cnx = requests.get(
                    self.url["wibudesu"],
                    params=self.query["wibudesu"],
                    headers=self.header
                )
                soup = BeautifulSoup(cnx.text, "lxml")
                div = soup.find(class_="rseries")
                link = div.find_all("h2")
                for h2 in link:
                    data = dict()
                    data["link"] = h2.a["href"]
                    data["title"] = h2.a["title"]
                    result.append(data)
            except Exception as e:
                data = dict()
                data["error"] = "404 Not Found"
                result.append(data)
        elif site == "kusonime":
            try:
                cnx = requests.get(
                    self.url["kusonime"],
                    params=self.query["kusonime"],
                    headers=self.header
                )
                soup = BeautifulSoup(cnx.text, "lxml")
                div = soup.find(class_="rseries")
                link = div.find_all("h2")
                for h2 in link:
                    data = dict()
                    data["link"] = h2.a["href"]
                    data["title"] = h2.a["title"]
                    result.append(data)
            except Exception as e:
                data = dict()
                data["error"] = "404 Not Found"
                result.append(data)
        elif site == "awbatch":
            try:
                cnx = requests.get(
                    self.url["awbatch"],
                    params=self.query["awbatch"],
                    headers=self.header
                )
                soup = BeautifulSoup(cnx.text, "lxml")
                div = soup.find(class_="konten-tengah")
                link = div.find_all("h2")
                for h2 in link:
                    data = dict()
                    data["link"] = h2.a["href"]
                    data["title"] = h2.a["title"]
                    result.append(data)
            except Exception as e:
                data = dict()
                data["error"] = "404 Not Found"
                result.append(data)
        elif site == "meowbatch":
            try:
                cnx = requests.get(
                    self.url["meowbatch"],
                    params=self.query["meowbatch"],
                    headers=self.header
                )
                soup = BeautifulSoup(cnx.text, "lxml")
                div = soup.find(class_="post-content-container")
                link = div.find_all("a", attrs={"class": "post-title"})
                data = dict()
                for url in link:
                    data["link"] = url["href"]
                    data["title"] = url.h4.text.strip()
                    result.append(data)
            except Exception as e:
                data = dict()
                data["error"] = "404 Not Found"
                result.append(data)
        return result
