
// Fetch the items from the JSON file
// https://developer.mozilla.org/ko/docs/Web/API/Fetch_API/Using_Fetch
function loadItems() {
  // fetch를 이용해 data를 성공적으로 받아오면 
  return fetch('data/data.json')
    // response의 body를 json API를 이용해서 json object로 변환
    .then(response => response.json())
    // json 안의 items를 return해준다.
    .then(json => json.items);
}

// Update the list with the given items
function displayItems(items) {
  const container = document.querySelector('.items');
  // items에 들어있는 각각의 item을 createHTMLString 함수를 이용해 li 요소, 문자열로 변환
  // 그리고 join을 이용해서 하나의 문자열로 병합
  container.innerHTML = items.map(item => createHTMLString(item)).join('');
  // const html = items.map(item => createHTMLString(item)).join('');
  // console.log(html)
}

// Create HTML list item from the given data item
function createHTMLString(item) {
  return `
  <li class="item">
    <img src="${item.image}" alt="${item.type}" class="item__thumbnail">
    <span class="item__description">${item.gender}, ${item.size}</span>
  </li>
  `;
}

function onButtonClick(event, items) {
  const dataset = event.target.dataset;
  const key = dataset.key;
  const value = dataset.value;

  if (key == null || value == null) {
    return;
  }

  const filtered = items.filter(item => item[key] === value);
  console.log(filtered)
  // filter를 이용해서 조건에 해당하는 값들만 불러오기
  displayItems(items.filter(item => item[key] === value))
}

function setEventListeners(items) {
  const logo = document.querySelector('.logo');
  const buttons = document.querySelector('.buttons');
  // 로고를 클릭하면 전체 품목을 보여주면 되니까 미리 만들어둔 displayItems를 이용한다.
  logo.addEventListener('click', () => displayItems(items));
  buttons.addEventListener('click', event => onButtonClick(event, items));
}


// main
// data.json의 데이터를 읽어와서 데이터를 전달해주는 역할
loadItems()
  .then(items => {
    // 보여주고
    displayItems(items);
    // 필터링
    setEventListeners(items)
  })
  .catch(console.log)
