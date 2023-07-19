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
  
  // 어떤 함수가 promise를 반환한다는 것은
  // 이 함수는 비동기 작업을 하고 그 작업의 결과를 promise 객체로 반환받아서 사용할 수 있는 함수라고 보면 된다.!
}

const res = isPositiveP(101);
// res라는 상수가 반환받은 promise 객체를 이용해서 
// 비동기 처리에 대한 resolve거나 reject의 결과값을 아무데서나 사용할 수 있게 된다.

res
  // promise 객체의 메소드인 then, catch
  .then((res)=>{
    console.log("작업 성공 : ", res);
  })
  .catch((err)=>{
    console.log("작업 실패 : ", err);
  });
```

<br>
<br>

이제 진짜 탈출해보실까..?

<br>

```javascript
function taskA(a, b) {

  // const executorA = (resolve, reject) => {
  //   set~~~ 
  // }
  // 이게 아래 코드와 같은~

  return new Promise((resolve, reject)=>{
    setTimeout(()=>{
      const res = a+b;
      resolve(res);
    }, 3000);
  });
}

function taskB(a) {
  return new Promise((resolve, reject) => {
    setTimeout(()=>{
      const res = a * 2;
      resolve(res);
    }, 1000);
  });
}

function taskC(a) {
  return new Promise((resolve, reject) => {
    setTimeout(()=>{
      const res = a * -1;
      resolve(res);
    }, 2000);
  });
}

// promise를 반환하는 함수를 만든 이유!
// 어떤 함수가 promise를 반환한다 
// == 비동기적으로 동작한다. + promise 객체를 이용해서 비동기 처리의 결과 값을, 위에서 만들었던 것처럼 then, catch로 이용할 수 있게 만들겠다!

// 콜백
// taskA(3, 4, (a_res)=>{
//   console.log("task A : ", a_res);
//   taskB(a_res, (b_res)=>{
//     console.log("task B : ", b_res);
//     taskC(b_res, (c_res)=>{
//       console.log("task C : ", c_res);
//     })
//   })
// })

// 를
// taskA(5, 1).then((a_res)=>{
//   console.log("A RESULT : ", a_res);
//   taskB(a_res).then((b_res)=>{
//     console.log("B RESULT : ", b_res);
//     taskC(b_res).then((c_res)=>{
//       console.log("task C : ", c_res);
//     })
//   })
// })
// 콜백식?
// 로 바꿀 수 있긴한데 이것은 promise 객체와 then을 사용하는 방법이 잘못된!(?)


taskA(5, 1).then((a_res)=>{
  console.log("A RESULT : ", a_res);
  return taskB(a_res); // 결과값(B Promise) 반환
}).then((b_res)=>{
  console.log("B RESULT : ", b_res);
  return taskC(b_res); // 반환(C Promise)
}).then((c_res)=>{
  console.log("C RESULT : ", c_res);
  // 더 이상 할게 없으니까 반환할 것 없음
})

// 위처럼 then 메서드를 계속 이어붙이는 것을 then 체이닝이라고 한다.


const bPromiseResult = taskA(5, 1).then((a_res)=>{
  console.log("A RESULT : ", a_res);
  return taskB(a_res);
}); // 비동기 처리 코드

console.log("kdkdkdkdk");
console.log("kdkdkdkdk");
console.log("kdkdkdkdk");
// 이런식으로 분리해서 중간에 다른 작업을 끼워넣는 것이 가능하다.
// 콜백식이 아니어서 promise를 써서? 좋은 이유

bPromiseResult  // 결과 호출하는 코드
  .then((b_res)=>{
    console.log("B RESULT : ", b_res);
    return taskC(b_res);
  }).then((c_res)=>{
    console.log("C RESULT : ", c_res);
  });
// 또, 비동기 처리 코드와 결과 호출 코드를 분리할 수 있어서 가독성 b, 깔끔하게 코드를 짤 수 있다!

```
