/**
 *  H - Index
 */

function solution(citations) {
  let answer = 0;
  let count = 0;

  // 에러 처리
  if (citations.length === 1) {
    if (citations[0] > 0) return 1;
    return 0;
  }

  citations.sort((a, b) => b - a);

  const isAnswer = citations.every((value) => {
    if (value <= count) {
      answer = count;
      return false;
    }
    count++;
    return true;
  });

  return isAnswer ? citations.length : answer;
}
