import  re

def add100(match):
    strMatch = match.group()
    num = int(strMatch) + 100
    return str(num)

str1 = "I love denglanlan I i"

print(str1.find("I"))
pa = re.compile(r"I", re.I)
ma = pa.match(str1)
print(ma)
print(ma.span())
print(ma.group())

ma = re.match(r"(I)", str1)
print(ma)
print(ma.groups())

# 正则表达式的基本语法
ma = re.match(r"([A-Z]+[a-z\s]*)", "I love lanlan, What?")
print(ma)
print(ma.groups())

ma = re.match(r"\ABian[a-z0-9\s_]+@(qq|163).com\Z  ", "Biandonglei@163.com")
print(ma)
# print(ma.group())

ma = re.match(r"<(?P<Tag>\w+>)[\w\s\d]*</(?P=Tag)","<html>卞栋磊的主页</html>")
print(ma)
print(ma.group())

maFindall = re.findall(r"\d+","100+200+7888+1000")
print(maFindall)
print(sum([int(x) for x in maFindall]))