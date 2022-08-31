# [FLEXBOX FROGGY 🐸](https://flexboxfroggy.com/#ko)

## 등장하는 CSS 속성 정리 📝
---
☀️ `justify-content` : 요소들을 가로선 상에서 정렬하며 다음의 값들을 인자로 받는다.

* `flex-start` (default) : 요소들을 컨테이너의 왼쪽으로 정렬.
* `flex-end` : 요소들을 컨테이너의 오른쪽으로 정렬.
* `center` : 요소들을 컨테이너의 가운데로 정렬.
* `space-between` : 요소들 사이에 동일한 간격을 둠.
* `space-around` : 요소들 주위에 동일한 간격을 둠.

〰️

☀️ `flex-direction` : 다음의 값들을 인자로 받아 컨테이너 안에서 요소들이 정렬해야할 방향을 지정한다.

* `row` (default) : 요소들을 텍스트의 방향과 동일하게 정렬.
* `row-reverse` : 요소들을 텍스트의 반대 방향으로 정렬.
* `column` : 요소들을 위에서 아래로 정렬.
* `column-reverse` : 요소들을 아래에서 위로 정렬.

〰️

☀️ `flex-wrap`

* `nowrap` (default) : 모든 요소들을 한 줄에 정렬.
* `wrap` : 요소들을 여러 줄에 걸쳐 정렬.
* `wrap-reverse` : 요소들을 여러 줄에 걸쳐 반대로 정렬.

〰️

☀️ `align-items` : 다음의 값들을 받아 요소들을 세로선 상에서 정렬한다.

* `flex-start` : 요소들을 컨테이너의 꼭대기로 정렬.
* `flex-end` : 요소들을 컨테이너의 바닥으로 정렬.
* `center` : 요소들을 컨테이너의 세로선 상의 가운데로 정렬.
* `baseline` : 요소들을 컨테이너의 시작 위치에 정렬.
* `stretch` (default) : 요소들을 컨테이너에 맞도록 늘림.

〰️

☀️ `align-self` : 지정된 `align-items` 값을 무시하고 flex 요소를 세로선 상에서 정렬

* `flex-start` : 여러 줄들을 컨테이너의 꼭대기에 정렬.
* `flex-end` :  여러 줄들을 컨테이너의 바닥에 정렬.
* `center` : 여러 줄들을 세로선 상의 가운데에 정렬.
* `baseline` : 여러 줄들을 컨테이너의 시작 위치에 정렬.
* `stretch` : 여러 줄들을 컨테이너에 맞도록 늘림.

〰️

☀️ `align-content` : 여러 줄 사이의 간격을 지정, 다음의 값을 인자로 받는다.

* `flex-start` : 여러 줄들을 컨테이너의 꼭대기에 정렬.
* `flex-end` :  여러 줄들을 컨테이너의 바닥에 정렬.
* `center` : 여러 줄들을 세로선 상의 가운데에 정렬.
* `space-between` : 여러 줄들 사이에 동일한 간격을 둠.
* `space-around` : 여러 줄들 주위에 동일한 간격을 둠.
* `stretch` (default) : 여러 줄들을 컨테이너에 맞도록 늘림.

〰️

```
❗️ 주의 ❗️
align-content는 여러 줄들 사이의 간격을 지정, 
align-items는 컨테이너 안에서 어떻게 모든 요소들이 정렬하는지를 지정. 
한 줄만 있는 경우, align-content는 효과를 보이지 않는다.
```

〰️

☀️ `flex-flow` : `flex-direction` 과 `flex-wrap` 합친 것

* `flex-direction` : 다음의 값들을 인자로 받아 컨테이너 안에서 요소들이 정렬해야할 방향을 지정.
* `flex-wrap` :  요소들을 한줄 혹은 여러줄에 걸쳐 정렬.

〰️

☀️ `order` : flex 요소의 순서를 지정하는 속성. 기본 값은 0이며, 양수나 음수로 바꿀 수 있음.

〰️

![FROGGY 완료](/220831%20WEB%203%EC%9D%BC%EC%B0%A8/FLEXBOX%20FROGGY.png)