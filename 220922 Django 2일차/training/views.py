from django.shortcuts import render
import random

# Create your views here.
def menu(request):
    menus = ['갈비탕', '삼겹살', '떡볶이', '보쌈', '치킨', '마라탕', '파스타', '피자', '햄버거', '초밥', '김밥', '만두']
    menu_imgs = {
        '갈비탕' : 'https://img-cf.kurly.com/shop/data/goodsview/20200803/gv40000025492_1.jpg',
        '삼겹살' : 'https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/201702/27/117f5b49-1d09-4550-8ab7-87c0d82614de.jpg',
        '떡볶이' : 'https://image.wingeat.com/item/templates/bc4e642e579445eabc05d05a2ba07097-w970-v2.jpg',
        '보쌈' : 'https://hobbyen.co.kr/news/data/20191213/p179558688114647_907.png',
        '치킨' : 'http://www.bhc.co.kr/images/new/img_menu.png',
        '마라탕' : 'http://img.danawa.com/prod_img/500000/653/027/img/8027653_1.jpg?_v=20220530173400',
        '파스타' : 'https://simg.ssgcdn.com/trans.ssg?src=/cmpt/edit/202007/13/152020071315432284358190797819_355.jpg&w=830&t=8e090d9479adc35c25bb3ffcaf9c79272857a617',
        '피자' : 'https://www.koreatimes.net/images/attach/144664/20220125-09014607.jpg',
        '햄버거' : 'http://img.danawa.com/prod_img/500000/180/650/img/10650180_1.jpg?_v=20200225164904',
        '초밥' : 'https://rimage.gnst.jp/livejapan.com/public/article/detail/a/00/00/a0000370/img/basic/a0000370_main.jpg?20201002142956&q=80&rw=750&rh=536',
        '김밥' : 'https://recipe1.ezmember.co.kr/cache/recipe/2016/06/29/e7401296033ab8e4297cd53d71e1bba91.jpg',
        '만두' : 'https://upsomandoo.com/data/item/1632365034/thumb-6rOg6riw67O166eM65GQ_600x600.jpg',
    }

    menu = random.choice(menus)

    context = {
        'menu' : menu,
        'menu_img' : menu_imgs.get(menu)
    }

    return render(request, "menu.html", context)


def lotto(request):
    numbers = []
    list_ = []
    result = []

    for i in range(1, 46):
        # numbers는 1~46까지 들어있는 리스트
        numbers.append(i)

    for _ in range(5):
        while len(list_) < 6:
            # 랜덤으로 숫자 뽑기
            number = random.choice(numbers)
            # 리스트에 숫자 6개 저장
            if number not in list_:
                list_.append(number)
        result.append(list_)
        list_ = []

    context = {
        'result' : result,
        'winning' : [3, 11, 15, 29, 35, 44]
    }

    return render(request, "lotto.html", context)