// require 함수와 경로를 이용해 내보내진 모듈을 가져와서 사용할 수 있다.
// require와 module.exports는 node.js에서만 사용할 수 있기 때문에 바닐라 자스에서 사용이 불가하다!
const calc = require('./calc');

// console.log(calc);
console.log(calc.add(1, 2));
console.log(calc.add(4, 5));
console.log(calc.sub(10, 2));