# HTML 속성 🔍

## 속성(Attributes) 💬
속성은 요소에 실제론 나타내고 싶지 않지만 추가적인 내용을 담고 싶을 때 사용합니다. 위에는 나중에 스타일에 관련된 내용이나 기타 내용을 위해 해당 목표를 구분할 수 있는 `class` 속성을 부여했습니다.

속성을 사용할 때에는 아래 내용을 지켜야 합니다:

요소 이름 다음에 바로 오는 속성은 요소 이름과 속성 사이에 공백이 있어야 되고, 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백이 있어야 합니다.
속성 이름 다음엔 등호(=)가 붙습니다.
속성 값은 열고 닫는 따옴표로 감싸야 합니다.

요소 중 하나인 `<a>` 요소는 "anchor"를 의미하는데, 닻이 배를 항구로 연결하듯 텍스트를 감싸서 하이퍼링크로 만듭니다. 이 요소는 여러 속성을 가질 수 있지만 아래에 있는 두 개가 주로 사용됩니다:

`href`: 이 속성에는 당신이 연결하고자 하는 웹 주소를 지정합니다. 그 예로, `href="https://www.mozilla.org/"`.
`title`: `title` 속성은 링크에 대한 추가 정보를 나타냅니다. 그 예로, `title="The Mozilla homepage"`. 이 내용은 링크 위로 마우스를 옮겼을 때 나타날 것입니다.
`target`: `target` 속성은 링크가 어떻게 열릴 것인지를 지정합니다. 예를 들어, `target="_blank"` 는 링크를 새 탭에서 보여줍니다. 당신이 현재 탭에서 링크를 보여주고싶다면 이 속성을 생략하면 됩니다.



------

## 참과 거짓 속성(Boolean attributes) 💬

◾️ 여는 태그(Opening tag): 요소의 이름과, 열고 닫는 꺽쇠 괄호로 구성된다.

때때로 값이 없는 속성을 볼 수 있을텐데 이것은 허용되는 것입니다. 이를 불 속성이라고 하며, 일반적으로 그 속성의 이름과 동일한 하나의 값만을 가질 수 있습니다. 예를 들어 [`disabled`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/Input#attr-disabled) 속성을 양식 입력 요소에 할당하면 사용자가 데이터를 입력할 수 없도록 비활성화(회색으로 표시) 할 수 있습니다.

```
<input type="text" disabled="disabled">
```

이것은 다음과 같이 줄여쓸 수 있습니다. (당신이 참고할 수 있도록 비활성화를 하지 않은 형태도 포함했습니다.)

```
<input type="text" disabled>

<input type="text">
```

Copy to Clipboard

이 둘은 다음과 같은 결과를 보여줍니다.
-------

## 블럭 레벨 요소 vs 인라인 요소(Block versus inline elements) ❗️



〰️


-------

## 빈 요소 (Empty elements) ❗️

-------

더 알아보기
* [HTML 요소 참고서 📚]("https://developer.mozilla.org/ko/docs/Web/HTML/Element")