# import sys
# from urllib import request
# from flask import Flask, render_template
# from bs4 import BeautifulSoup
#
# app = Flask(__name__)
#
# # @app.route('/')
# # def hello():
# #     return "<h1> Hello World! </h1>"
#
# @app.route("/")
# def home():
#     return render_template('index.html', subject="안녕하세요. 반갑습니다. 김혜린입니다.")
#
# @app.route('/<user>')
# def hello(user):
#     return '<h1> hello ' + user
#
# @app.route("/about")
# def about():
#     return render_template('result.svg', subject="2020 부산 5대 범죄 현황")
#
# @app.route("/show1")
# def show1():
#     return render_template('img_test1.html', image_file='img/1.jpg')
#
# if __name__ == "__main__" :
#     app.run()

from flask import Flask, render_template
import sys
from urllib import request
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html', subject="안녕하세요. 반갑습니다. OOO입니다")

@app.route('/<user>')
def hello(user):
    return '<h1> hello ' + user

# 2 html 연결
@app.route("/about")
def about():
    return render_template('busan1.html', subject="부산중위연령시각화")


# 3 이미지2
@app.route("/show1")
def show1():
    return render_template('img_test1.html', image_file='img/1.jpg')


# 4 기상청1(전국중기예보)

@app.route("/kma")
def kma():
    # urlopen() 함수로 기상청의 전국 날씨를 읽습니다.
    target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stdId=108")
    # BeautifulSoup를 사용해 웹 페이지를 분석합니다.
    soup = BeautifulSoup(target, "html.parser")
    output = ""

    # item 태그를 찾습니다.

    #
    #

    # location 태그를 찾습니다.
    for location in soup.select("location"):
        # 내부의 city, wf, tmn, tmx, tmEf 태그를 찾아 출력합니다.
        output += "<h3>{}</h3>".format(location.select_one("city").string)
        output += "날씨: {}</br>".format(location.select_one("wf").string)
        output += "날짜: {}</br>".format(location.select_one("tmEf").string)
        output += "최저/최고 기온: {}/{}".format(location.select_one("tmn").string, location.select_one("tmx").string)
        output += "<hr/>"
        #
    #
    #
    return output


# 5 기상청2(경상남북도 중기예보)
@app.route("/kma1")
def kma1():
    # urlopen() 함수로 기상청의 전국 날씨를 읽습니다.
    target = request.urlopen("https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=159")

    # BeautifulSoup를 사용해 웹 페이지를 분석합니다.
    soup = BeautifulSoup(target, "html.parser")
    # location 태그를 찾습니다.
    output = ""

    for item in soup.select("item"):
        output += "<h2>{}</h2><hr/>".format(item.select_one("title").string)

    for location in soup.select("location"):
        # 내부의 city, wf, tmn, tmx, tmEf 태그를 찾아 출력합니다.
        output += "<h3>{}</h3>".format(location.select_one("city").string)
        output += "날짜: {}</br>".format(location.select_one("tmEf").string)
        output += "날씨: {}</br>".format(location.select_one("wf").string)
        output += "최저/최고 기온: {}/{}".format(location.select_one("tmn").string, location.select_one("tmx").string)
        output += "<hr/>"

    output += "{}</br>".format(soup.select_one("title").string)
    output += "날짜: {}</br>".format(location.select_one("tmEf").string)
    output += "지역: {}</br>".format(soup.select_one("province").string)

    return output

if __name__ == "__main__" :
    app.run()