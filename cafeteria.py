from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/급식', methods=['POST'])

def gethtml(url):
    _html = ""
    resp = requests.get(url)
    if resp.status_code == 200:
        _html = resp.text
    return _html

def todaybf(today):
    str = str
    int = int

    num = today + 1
    URL = ("https://stu.goe.go.kr/edusys.jsp?page=sts_m42320" % str, int)

    html = get_html(URL)
    soup = BeautifulSoup(html, 'html.parser')
    findfind = findfind.find.all("tr")
    findfind = findfind[2].find.all("td")
    
    for school in soup.select('<div id="genWeekDiet_1_txbMon" class="w2textbox "', ''):
       answer = (school.text)

def yesterdaybf(yesterday):
    str = str
    int = int

    num = yesterday + 1
    URL = ("https://stu.goe.go.kr/edusys.jsp?page=sts_m42320" % str, int)

    html = get_html(URL)
    soup = BeautifulSoup(html, 'html.parser')
    findfind = findfind.find.all("tr")
    findfind = findfind[2].find.all("td")
    
    for school in soup.select('<div id="genWeekDiet_1_txbMon" class="w2textbox "', ''):
       answer = (school.text)


def weekbf(week):
    str = str
    int = int

    num = week + 1
    URL = ("https://stu.goe.go.kr/edusys.jsp?page=sts_m42320" % str, int)

    html = get_html(URL)
    soup = BeautifulSoup(html, 'html.parser')
    findfind = findfind.find.all("tr")
    findfind = findfind[2].find.all("td")
    
    for school in soup.select('<div id="genWeekDiet_1_txbMon" class="w2textbox "', ''):
       answer = (school.text)

def maindef():
    req = request.get_json()

    mainbf = req["action"]["detaulParams"]["급식선택"]["value"]
    todaybf = req["action"]["detailParams"]["오늘급식"]["value"]
    yesterdaybf = req["action"]["detailParams"]["내일급식"]["value"]
    weekbf = req["action"]["detailParams"]["1주일급식"]["value"]

    if len(todaybf) <= 0 or len(mainbf) <= 0:
        answer = "ERROR_MESSAGE"
    else:
        answer = "현재 급식 정보입니다."
        answer = todaybf

    if len(yesterdaybf) <= 0 or len(mainbf) <= 0:
        answer = "ERROR_MESSAGE"
    else:
        answer = "현재 급식 정보입니다"
        answer = yesterdaybf

    if len(weekbf) <= 0 or len(mainbf) <= 0:
        answer = "ERROR_MESSAGE"
    else:
        answer = "현재 급식 정보입니다"
        answer = weekbf

    setmsg = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": answer
                    }
                }
            ]
        }
    }
    return jsonify(setmsg)


if __name__=='__main__':
    app.run(host='0.0.0.0', threaded=True)
