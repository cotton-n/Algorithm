/**
 *  프린터
 */

function solution(priorities, location) {
  let answer = 0;

  const prioritiesLoc = priorities.map((value, i) => [value, i]);

  while (true) {
    const doc = prioritiesLoc.shift();
    const isOut = prioritiesLoc.every((value) => {
      if (doc[0] < value[0]) {
        prioritiesLoc.push(doc);
        return false;
      }
      return true;
    });
    if (isOut) {
      answer++;
      if (doc[1] === location) break;
    }
  }

  return answer;
}
