# 한입 크기로 잘라 먹는 리액트(React.js) : 기초부터 실전까지

# 11일차 강의 내용 정리

## Promise 콜백 지옥에서 탈출하기~

<br>

promise : JS 비동기를 돕는 객체! 비동기 처리의 결과값을 핸들링하는 코드를 비동기 함수로부터 분리할 수 있다.   
쉽고 빠르고 직관적으로 비동기 처리를 할 수 있게 된다.

<br>

비동기 작업이 가질 수 있는 3가지 상태

<br>

Pending(대기 상태) : 현재 비동기 작업이 진행중이거나, 작업을 시작할 수 없는 문제가 발생했음을 의미한다.   
Fulfilled(성공) : 비동기 작업이 의도한대로 정상적으로 완료된 상태를 의미한다.   
Rejected(실패) : 비동기 작업이 모종의 이유로 실패했음을 의미한다.    
(서버가 응답하지 않는 경우, 응답이 너무 오래걸려서 자동으로 취소되는 경우 등이 해당)

<br>

비동기 처리작업은 위의 셋 중 하나의 상태를 갖는다.   
비동기 작업은 한 번 성공하거나 실패하면 그것으로 작업이 끝난다.   

<br>

pending 상태에서 fulfilled 상태로 변화하는 과정을 resolve(해결)이라고 한다.   
그리고, pending 상태에서 rejected 상태로 변화하는 과정을 reject(거부)라고 한다.   

<br>

```javascript
// 콜백함수를 이용해서 비동기 처리를 하는 함수 만들기~~
function isPositive(number, resolve, reject){
  setTimeout(()=>{
    if(typeof number === 'number'){
      // 성공 -> resolve
      resolve(number >= 0 ? "양수" : "음수");
    } else{
      // 실패 -> reject
      reject("주어진 값이 숫자형 값이 아닙니다.");
    }
  }, 2000);
}

// isPositive(10, (res)=>{
//   console.log("성공적으로 수행됨 : ", res);
// }, (err)=>{
//   console.log("실패하였음 : ", err);
// });

function isPositiveP(number){
  const executor = (resolve, reject) => { 
  // executor = 실행자
  // 비동기 작업을 실질적으로 수행하는 함수다! 라고 이해하고 있으면 됨
    setTimeout(() => {
      if(typeof number === 'number') {
        // 성공 -> resolve
        console.log(number);
        resolve(number >= 0 ? "양수" : "음수");
      } else {
        // 실패 -> reject
        reject("주어진 값이 숫자형 값이 아닙니다.");
      }
    }, 2000);
  };

  // 비동기 작업 자체인 Promise를 저장할 상수 asyncTask를 만들어
  // new 키워드를 사용해 Promise 객체를 생성하면서 그것의 생성자로 
  // 비동기 작업의 실질적인 실행자 함수인 executor를 넣어주게 되면
  // 넣어주는 순간 자동으로 바로 executor 함수가 실행이 된다.
  // 그니까 실행해!! 라는 말을 안해도 냅다 수행이 되어버리는 것임!
  const asyncTask = new Promise(executor);
  return asyncTask; // 그럼 이제 상수 리턴만 해줘도 isPositiveP 함수의 반환값이 Promise로 바뀌게 됨.
}

isPositiveP(101);
```


<br>
<br>



```javascript
```

```javascript
```

```javascript
```
