# HTML 개념과 요소 🔍

## HTML: Hypertext Markup Language 💬

HTML(Hypertext Markup Language, 하이퍼텍스트 마크업 언어)은 웹을 이루는 가장 기초적인 구성 요소로, 웹페이지의 구조를 지정하는 기술적인 언어이다. 작성하고자 하는 웹 콘텐츠가 문단인지, 리스트인지, 헤드라인인지, 링크인지, 이미지인지, 멀티미디어 플레이어인지, 폼 요소인지 아니면 기타 사용 가능한 다른 요소들 중의 하나인지, 혹은 새롭게 정의한 요소인지를 명확하기 인지할 수 있도록 하는데 사용된다.

* "Hypertext(하이퍼텍스트)"란 웹 페이지를 다른 페이지로 연결하는 링크를 말한다.
(링크: 웹의 근본적인 속성)

HTML 문서는 요소로 구조화한 일반 텍스트 문서이다. 요소는 한 쌍의 태그로 열고 닫으며, 각각의 태그는 부등호`<>`로 감싼다. `<img>`처럼 텍스트를 감싸지 못하는 "빈 태그"도 있다. HTML 태그는 특성을 사용해 확장할 수 있고, 브라우저가 요소를 읽어들일 때 추가 정보를 제공한다. 태그 안의 요소 이름은 대소문자를 구분하지 않는다.

HTML은 보통 `.htm`이나 `.html` 확장자로 저장해 웹 서버로 제공하며, 아무 브라우저로 렌더링할 수 있다.

HTML은 웹 브라우저에 표시되는 글과 이미지 등의 다양한 콘텐츠를 표시하기 위해 "마크업"을 사용한다. HTML 마크업은 다양한 "요소"를 사용하는데, 요소에는 `<head>`, `<title>`, `<body>`, `<header>`, `<footer>`, `<article>`, `<section>`, `<p>`, `<div>`, `<span>`, `<img>`, `<aside>`, `<audio>`, `<canvas>`, `<datalist>`, `<details>`, `<embed>`, `<nav>`, `<output>`, `<progress>`, `<video>`, `<ul>`, `<ol>`, `<li>` 등 많은 종류가 존재한다.

------

## HTML 요소 (Element) 💬

◾️ 여는 태그(Opening tag): 요소의 이름과, 열고 닫는 꺽쇠 괄호로 구성된다.

◾️ 닫는 태그(Closing tag): 요소의 이름 앞에 슬래시`/`가 있는것을 제외하면 여는 태그(opening tag)와 형식이 같다. 요소의 끝에 위치한다.

◾️ 내용(Content): 요소의 내용이다.

◾️ 요소(Element): 여는 태그, 닫는 태그, 내용을 통틀어 요소(element)라고 한다.

-------

## 블럭 레벨 요소 vs 인라인 요소(Block versus inline elements) ❗️

HTML에는 블록 레벨 요소(Block level element)와 인라인 요소(Inline element), 두가지 종류의 요소(Element)가 있다.

블록 레벨 요소(Block-level elements)는 웹페이지 상에 블록(Block)을 만드는 요소이다. 블록 레벨 요소는 앞뒤 요소 사이에 새로운 줄(Line)을 만들고 나타난다. 즉 블록 레벨 요소 이전과 이후 요소사이의 줄을 바꾼다. 블록 레벨 요소는 일반적으로 페이지의 구조적 요소를 나타낼 때 사용된다. 

* 예를 들어 개발자는 블록 레벨 요소를 사용하여 단락(Paragraphs), 목록(lists), 네비게이션 메뉴(Navigation Menus), 꼬리말(Footers) 등을 표현할 수 있다. 블록 레벨 요소는 인라인 요소(Inline elements)에 중첩될(Nested inside)수 없다. 그러나 블록 레벨 요소는 다른 블록 레벨 요소에 중첩될 수 있다.

인라인 요소(Inline elements)는 항상 블록 레벨 요소내에 포함되어 있다. 인라인 요소는 문서의 한 단락같은 큰 범위에는 적용될 수 없고 문장, 단어 같은 작은 부분에 대해서만 적용될 수 있다. 인라인 요소는 새로운 줄(Line)을 만들지 않는다. 즉 인라인 요소를 작성하면 그것을 작성한 단락내에 나타나게 된다. 

* 예를 들어, 인라인 요소에는 하이퍼링크를 정의하는 요소인 `<a>` , 텍스트(Text)를 강조하는 요소인 `<em>`,`<strong>` 등이 있다.

〰️
```html
 <!-- 예시 -->

<em>first</em><em>second</em><em>third</em>

<p>fourth</p><p>fifth</p><p>sixth</p>
```

`<em>` 은 인라인 요소(inline element) 이므로, 위와 같이 처음 세 개의 요소는 서로 같은 줄에, 사이에 공백이 없이 위치한다. 한편, `<p>` 는 블록 레벨 요소이므로, 각 요소들은 새로운 줄에 나타나며, 위와 아래에 여백이 있다(여백은 브라우저가 문단에 적용하는 기본 CSS styling 때문에 적용된다).

-------

## 빈 요소 (Empty elements) ❗️

주로 문서에 무언가를 첨부하기 위해 단일 태그(Single tag)를 사용하는 요소도 있다. 
예를 들어 `<img>` 요소는 해당 위치에 이미지를 삽입하기 위한 요소이다.
```html
<img src="https://raw.githubusercontent.com/mdn/beginner-html-site/gh-pages/images/firefox-icon.png">
```

-------

더 알아보기
* [HTML 요소 참고서 📚]("https://developer.mozilla.org/ko/docs/Web/HTML/Element")