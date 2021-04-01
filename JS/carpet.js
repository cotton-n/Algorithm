/**
 *  카펫
 */

function solution(brown, yellow) {
  let answer = [];

  for (let h = 1; h <= yellow; h++) {
    if (yellow % h === 0) {
      const w = yellow / h;
      if (w * 2 + h * 2 + 4 === brown) {
        answer = w >= h ? [w + 2, h + 2] : [h + 2, w + 2];
        break;
      }
    }
  }

  return answer;
}
