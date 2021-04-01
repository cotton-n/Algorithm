/**
 *  기능개발
 */

function solution(progresses, speeds) {
  const answer = [];

  const remainDays = progresses.map((value, i) =>
    Math.ceil((100 - value) / speeds[i])
  );

  let standard = remainDays[0];
  let count = 0;

  remainDays.forEach((day) => {
    if (standard < day) {
      answer.push(count);
      count = 0;
      standard = day;
    }
    count += 1;
  });
  answer.push(count);

  return answer;
}
