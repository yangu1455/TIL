from multiprocessing import context
from sre_parse import State
from django.shortcuts import render
import random

# Create your views here.


def index(request):
    # render는 새로운 페이지를 만들어서 리턴하는~
    return render(request, "index.html")


def ping(request):
    return render(request, "ping.html")


def pong(request):
    # print(request)
    # print(dir(request))
    # print(request.get_full_path)
    # print(request.GET.get('ball'))

    # ball = request.GET.get('ball')
    # context = {
    #     'name' : ball,
    # }

    return render(request, "pong.html", {"name": request.GET.get("ball")})


def is_odd_even(request, number_):

    if number_ != 0:
        # 홀수인 경우
        if number_ % 2 == 1:
            is_ = "홀수"
        # 짝수인 경우
        else:
            is_ = "짝수"
    # 0인 경우
    else:
        is_ = "0"

    context = {"number": number_, "is": is_}

    return render(request, "is-odd-even.html", context)


def calculate(request, number1, number2):
    plus = number1 + number2
    minus = number1 - number2
    multiply = number1 * number2
    divide = number1 // number2

    context = {
        "number1": number1,
        "number2": number2,
        "plus": plus,
        "minus": minus,
        "multiply": multiply,
        "divide": divide,
    }

    return render(request, "calculate.html", context)


def input(request):
    return render(request, "input.html")


def output(request):
    state_list = [
        "겁이 많은",
        "돈이 많은",
        "세상에서 가장 못생긴",
        "무표정한",
        "성격이 안좋은",
        "친구가 하나도 없는",
        "초긍정적인",
        "사랑스러운",
        "말이 많아 일을 그르치는",
        "언행이 거친",
        "로맨틱한",
    ]
    creature_list = [
        "당나귀",
        "잡초",
        "원숭이",
        "고릴라",
        "앵무새",
        "전쟁의 영웅",
        "왕비",
        "민들레 씨앗",
        "생후 1개월 미만의 아기",
        "거지",
        "백만장자",
        "평민",
    ]

    img_list = {
        "당나귀": "https://mblogthumb-phinf.pstatic.net/20150508_83/sydney1954_1431054455235BGii2_JPEG/donkey_friends___photo_by_the_donkey_sanctuary.jpg?type=w2",
        "잡초": "http://www.newsfm.kr/data/photos/20180522/art_15275892129558_7ba326.jpg",
        "원숭이": "http://c.files.bbci.co.uk/A48B/production/_106132124_grady-2.jpg",
        "고릴라": "https://i.ytimg.com/vi/uWfq7QJpfbA/maxresdefault.jpg",
        "앵무새": "https://w.namu.la/s/cdceb59ca1d84be6fb9a5ade3971965aea90b9c83b4ace8c66fd45657d4f87869e794e9d7ee7915ce59fac42af811330af14dd4e9ae9579d53cb8304ef714554f3e9bcf0053773668b0a0e878c10a202d2e5cb83047f05ecc86d45ac5534828e",
        "전쟁의 영웅": "https://blog.kakaocdn.net/dn/bFD3QE/btrai7CcQn0/T41fag8eziYor8TcfQS50k/img.jpg",
        "왕비": "http://i2.wp.com/madameguillotine.files.wordpress.com/2010/12/chaumet_vendome_07.jpg",
        "민들레 홀씨": "https://t1.daumcdn.net/cfile/tistory/99AD8C4A5CA9BDCD2D",
        "생후 1개월 미만의 아기": "https://www.maeili.com/editor/upload/63e34c56-882e-4337-93c5-96ffd64a7eec.jpg",
        "거지": "https://as2.ftcdn.net/v2/jpg/02/32/41/29/1000_F_232412909_XrF1MKAU0wbEsxybN4YrWZPTMuLFcbJ0.jpg",
        "백만장자": "http://www.sisajournal-e.com/news/photo/first/201710/img_174597_1.png",
        "서민": "https://w.namu.la/s/4fe541b5a296582f4badd3a5e56c79915042a7fdb953b203315ecd5e8b1ae2d8cff50b0d754ccdea92d45cc05188bd857f4e0b5e356c0c3c0150c6110068755680de08caef6f71e6849af3806fb3ce202767f3a5121ada05b7a02ae5f57b8c6c9eefe493326cbeef4f6ef9a879751893",
    }

    state = random.choice(state_list)
    creature = random.choice(creature_list)
    name = request.GET.get("name")

    context = {
        "name": name,
        "state": state,
        "creature": creature,
        "img_src": img_list.get(creature),
    }
    return render(request, "output.html", context)


def lorem(request):
    return render(request, "lorem.html")
