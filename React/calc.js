// 계산 기능을 하는 파일

const add = (a, b) => a + b;
const sub = (a, b) => a - b;

// 모듈 = 어떤 기능을 담당하는 분리된 파일 각각

// 모듈 내보내기 기능을 이용해서 다른 곳에서도 이 기능을 쓸 수 있게 해줌
// node.js에서는 module.exports를 이용해서 객체 단위로 모듈을 내보낼 수 있다.
module.exports = {
  moduleName: "calc module",
  add: add,
  sub: sub,
}