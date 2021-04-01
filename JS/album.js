/**
 *  베스트 앨범
 */

function solution(genres, plays) {
  const answer = [];
  const musicMap = new Map();

  const genresMap = genres.reduce((prev, value, i) => {
    if (musicMap.has(value)) musicMap.get(value).push([i, plays[i]]);
    else musicMap.set(value, [[i, plays[i]]]);
    if (prev.has(value)) return prev.set(value, prev.get(value) + plays[i]);
    return prev.set(value, plays[i]);
  }, new Map());

  const genresMapSort = new Map(
    [...genresMap.entries()].sort((a, b) => b[1] - a[1])
  );

  musicMap.forEach((value, key) => value.sort((a, b) => b[1] - a[1]));

  genresMapSort.forEach((value, key) => {
    let count = 0;
    musicMap.get(key).map((value, i) => {
      if (count < 2) answer.push(musicMap.get(key)[i][0]);
      count += 1;
    });
  });

  return answer;
}
