# 220921 Django 1일차 개발 환경 설정 가이드

```
- 가상환경 생성 / 실행
- Django LTS 버전 설치
- Django 프로젝트 생성
- Django 실행
```

〰️

## 1. 폴더 하나를 만든다.
![폴더 만들기](image/01.png)

〰️

## 2. 터미널을 열어서 해당 폴더로 위치를 변경한다.
```bash
cd 해당 폴더 주소
```

![만든 폴더로 이동](image/02.png)

〰️

## 3. 파이썬이 깔려있는지 확인한다.
```bash
python --version
```

![파이썬 설치 확인](image/03.png)

〰️

## 4. 가상환경 폴더 생성
```bash
# 가상환경 폴더 생성
python -m venv server-venv

# 폴더가 만들어졌는지 확인하기
ls

# 목록을 전부 볼 수 있음
ls -a
```
![가상환경 폴더를 만듭시다](image/04.png)
![오타 조심..^^](image/04-1.png)

〰️

## 5. 가상환경 활성화하기
```bash
# 윈도우
source server-venv/Scripts/activate

# 맥
source server-venv/bin/activate

# 현재 위치에 따라 명령어가 바뀌니까 현재 위치 알아두고 활성화 명령하기!

# 하고 나면 이렇게 바뀜
(server-venv) 현재 위치 >

```

![가상환경 활성화](image/05.png)

❗️ 비활성화는?
```bash
deactive
```

〰️

## 6. 그리고 여기는 새로운(빈) 공간이기 때문에 django를 깔아줘야 한다.

![새로운 환경 설정 시작](image/06.png)

```bash
pip list
# 를 입력하면 제대로 깔린게 맞는지 확인할 수 있다.
```
![Django 설치 확인](image/06-1.png)

〰️

## 7. 설치가 끝났으면 새 프로젝트를 만든다.
```bash
django-admin startproject firstpjt .

# startproject는 명령어
# 그 다음에 오는 것은 프로젝트 이름
# . 은 현재 폴더를 의미한다.
```

![새 프로젝트 생성](image/07.png)
확인해보면 잘 생성된 것이 보인다.

〰️

## 8. vscode에서 확인하기
```bash
code .

# 을 입력하면 vscode에서 창이 열린다.
```
![vscode창](image/08.png)

〰️

## 9. 서버 구동하기
```bash
# 파이썬을 이용해 manage.py 파일을 열고 runserver 명령어를 실행시킨다.

python manage.py runserver

# 아래 사진처럼 뜬다면 성공!
```

![서버 활성화하기](image/09.png)

혹시 안되는 경우에는

[[트러블슈팅]"python manage.py runserver" 개발서버 start(시작)에러 - 작성자 WorldSeeker](https://atotw.tistory.com/313)

참고하기!

〰️

## 10. 인터넷 빈창을 띄우고 주소창에 `localhost:8000`를 입력해보면..!
![성공_00](image/10.png)
![성공_01](image/10-1.png)