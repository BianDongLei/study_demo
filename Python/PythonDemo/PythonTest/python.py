import sys
from urllib import request
from urllib import parse
from urllib.request import urlopen

# from bs4 import BeautifulSoup as bs
import pymysql.cursors



# Urlib get请求例子 urlopen
# req = request.Request("http://www.baidu.com")
# req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0")
# resp = request.urlopen(req)
# print(resp.read().decode("utf-8"))

# Urllib post请求例子 （12306车票查询） parse.urlencode
# postUrl = "https://kyfw.12306.cn/otn/leftTicket/init"
# req2 = request.Request(postUrl)
# req2.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0")
# req2.add_header("Referer","https://kyfw.12306.cn/otn/leftTicket/init")
# postdata = parse.urlencode([
#     ("leftTicket.form_station", "CSQ"),
#     ("leftTicket.to_station", "SHH"),
#     ("leftTicket.train_date", "2018-07-29"),
#     ("purpose_codes", "ADULT")
# ])
# resp2 = request.urlopen(req2,postdata.encode("utf-8"))
# resp2Data = resp2.read().decode("utf-8")
# print(resp2Data)

# beautifulSoup 例子
# soup = bs(resp2Data, "html.parser")
# print(soup.prettify())

print(pymysql)

# 数据库查询
connect = pymysql.connect(
    host="127.0.0.1",
    port=3308,
    user="root",
    password="12345678",
    db="pythontest",
    charset="utf8mb4"
)
cursor = connect.cursor()
try:
    if cursor is not None:
        selectCmd = r"select imgname,imgsrc from av_imgs where id is not null"
        count = cursor.execute(selectCmd)
        print("\n")
        print(count)
        print("\n")
        # print(cursor.fetchone())
        # print("\n")
        # for result in cursor.fetchmany(size=10):
        #     print(result)
        # print("\n")
        outFile = open("av_imgs.txt","w")
        for result in cursor.fetchall():
            print(result)
            outFile.write(result[0]+" : "+result[1]+"\n")
        outFile.close()
    # 总结 fetch方法时按照指针移动获取数据的，
    # fetchone即时从当前指针开始向下取一条数据
    # fetchmany（size）即时从当前指针开始向下取size条数据
    # fetchall 即时从当前指针开始向下取剩下的所有数据
finally:
    cursor.close()
    connect.close()

# python 文件写入和读取
htmlData = urlopen("http://www.baidu.com/robots.txt")
print(htmlData.read().decode("utf-8"))

# 程序入口函数
# if __name__ == "__main__":
#     arg1 = sys.argv[1]
#     arg2 = sys.argv[2]
