from urllib import request
from bs4 import BeautifulSoup
import pymysql.cursors

# import re

class Spider_Main(object):
    def __init__(self):
        self.urlManager = UrlManager()
        self.htmlDowner = HtmlDowloader()
        self.htmlParser = HtmlParser()

    def craw(self, base_url, target_url):
        self.urlManager.add_new_url(target_url)
        count = 0
        while self.urlManager.has_new_url():
            newUrl = self.urlManager.get_new_url()
            html_data = self.htmlDowner.download(newUrl)
            urls = self.htmlParser.parse(base_url,html_data)
            self.urlManager.add_new_urls(urls)
            count += 1
            if count == 10000:
                break
            # print(html_data)
        pass


class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None or url in self.old_urls:
            return
        elif url not in self.new_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url


class HtmlDowloader(object):
    def download(self, url):
        if url is not None:
            # url = request.quote(url.encode("utf-8"))
            try:
                req = request.Request(url)
                req.add_header("User-Agent", "Mozilla/5.0")
                response = request.urlopen(req)
                if response.getcode() == 200:
                    html_data = response.read().decode("utf-8")
                    return html_data
                else:
                    return None
            except BaseException:
                print("Url request failed: "+url)
        else:
            return None

class HtmlParser(object):
    def __init__(self):
        self.datas = {}
        self.urls = set()

    def parse(self, baseUrl ,htmlData):
        if htmlData is None:
            return None
        soup = BeautifulSoup(htmlData,"html.parser")
        count = 1
        for link in soup.find_all("a"):
            # print(link)
            linkUrl = link.get("href")
            if "/item/" in str(linkUrl):
                url = baseUrl+str(linkUrl)
                # print(url)
                count += 1
                self.urls.add(url)
        if "AV女优" in htmlData:
            name = ""
            nameContent = soup.find("dd", class_="lemmaWgt-lemmaTitle-title").find("h1")
            if nameContent is not None:
                self.datas["name"] = nameContent.get_text()
                name =  nameContent.get_text()
            # imageLinks = set()
            for imageLink in soup.find_all("img",class_="picture"):
                # print(imageLink)
                name_alt = name+"-"+imageLink.get("alt")
                src = imageLink.get("src")
                print(name_alt+" : "+src)

                # 将读取到的数据存入数据库中
                connection = pymysql.connect(
                    host="127.0.0.1",
                    port=3308,
                    user="root",
                    password="12345678",
                    db="pythontest",
                    charset="utf8mb4"
                )
                # 为了保证数据库操作的一致性和可控性，需要关闭自动commit
                connection.autocommit(False)
                cursor = connection.cursor()
                try:
                    if cursor is not None:
                        insertCmd = r"insert into av_imgs(imgname, imgsrc) values (%s, %s)"
                        cursor.execute(insertCmd,(name_alt, src))
                        connection.commit()
                except Exception as E:
                    print(E)
                    connection.rollback()
                    # 数据库操作出错后需要回滚
                finally:
                    cursor.close()
                    connection.close()

        return self.urls
        # print(count)



if __name__ == "__main__":
    baseUrl = "https://baike.baidu.com"
    url = "https://baike.baidu.com/item/AV%E5%A5%B3%E4%BC%98"
    spiderMain = Spider_Main()
    spiderMain.craw(baseUrl, url)
