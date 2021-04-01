/**
 *  위장
 */

function solution(clothes) {
  let answer = 1;
  const map = new Map();

  clothes.forEach((value) => {
    if (map.has(value[1])) map.set(value[1], map.get(value[1]) + 1);
    else map.set(value[1], 1);
  });

  map.forEach((value, key) => {
    answer *= value + 1;
  });

  return answer - 1;
}
