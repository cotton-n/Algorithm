/**
 *  완주하지 못한 선수
 */

function solution(participant, completion) {
  let answer = "";
  const map = new Map();

  participant.forEach((value) => {
    if (map.has(value)) map.set(value, map.get(value) + 1);
    else map.set(value, 1);
  });

  completion.forEach((value) => map.set(value, map.get(value) - 1));

  map.forEach((value, key) => {
    if (value === 1) answer = key;
  });
  return answer;
}
