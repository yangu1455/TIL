## 221221 모르는 부분 무작정 정리~

<br>

```css
a[href*=‘'] {...}
는 url에 ‘’가 포함된!
$=
는 ‘’로 끝나는!
```

말고도 [MDN 특성선택자](https://developer.mozilla.org/ko/docs/Web/CSS/Attribute_selectors) 보면 모르는 것들 겁내 많음

<br>

---

<br>

`Nth-of-type()`  
n마다 바뀜  
`.post:nth-of-type(3n){}`  
이런식으로 씀 표같은거 할때 좀 유용할지도?  
`#id .class`

<br>

---

<br>

`::first-letter`  
`::first-line`  
`::selection`

<br>

---

<br>

후에 정의 하는 것들이 나중에 덮어쓰여져서 결과는 후에 정의한 것들로 나온다  
스타일시트도 뒤에 붙인 것들이 결과로 나온다  
구체적으로 정의된 속성들이 우선시 됨

https://specificity.keegan.st/  
여기 넣고 우선순위 점수 먹여서 높은 점수가 좀더 구체적, 우선시 되는걸 확인할 수 있음

<br>

---

<br>

인라인스타일 직접 적용하는건데 지양하래  
css파일에 안들어있으니까 혼란이 올수있으니 > Id > 클래스 선택자 > 요소 선택자

!important 쓰면 가ㅏㅏ장 우선이 됨  
이것도 사용 지양…

<br>

---

<br>

Inherit 상위항목의 특성 받아오기  
상속이 불가한 것들도 있음 예를 들어서 테두리

<br>

---

<br>

그냥 인라인 요소는 가로세로가 적용이 되지 않는다

<br>

---

<br>

투명도  
Opacity, hex + 00~FF

<br>

---

em, rem

---

<br>

Transition ~시간에 걸쳐서 변화를 일으키게  
속성을 정할수도 이따

```css
transition: 애니메이션 효과를 줄 특성 이름 지속 시간(s, ms 단위) 타이밍 기능;
```

timing-function 더 많은 효과는 여기서 👉🏻 [https://easings.net/](https://easings.net/)

---

transform 속성  
`rotate` `scale` `translate` `skew`  
`transform-origin`  
`cursor`
