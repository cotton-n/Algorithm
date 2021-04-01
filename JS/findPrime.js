/**
 *  소수 찾기
 */

function isPrime(num) {
  let result = false;
  if (num === 0 || num === 1) return false;
  if (num === 2 || num === 3) return true;

  for (let i = 2; i <= Math.floor(Math.sqrt(num)); i++) {
    if (num % i === 0) {
      result = false;
      break;
    } else result = true;
  }
  return result;
}

function getPermutations(arr, selectNumber) {
  const results = [];
  if (selectNumber === 1) return arr.map((value) => [value]);

  arr.forEach((fixed, index, origin) => {
    const rest = [...origin.slice(0, index), ...origin.slice(index + 1)];
    const permutations = getPermutations(rest, selectNumber - 1);
    const attached = permutations.map((permutation) => [fixed, ...permutation]);
    results.push(...attached);
  });

  return results;
}

function getCombinations(arr, selectNumber) {
  const results = [];
  if (selectNumber === 1) return arr.map((value) => [value]);

  arr.forEach((fixed, index, origin) => {
    const rest = origin.slice(index + 1);
    const combinations = getCombinations(rest, selectNumber - 1);
    const attached = combinations.map((combination) => [fixed, ...combination]);
    results.push(...attached);
  });

  return results;
}

function solution(numbers) {
  let answer = 0;
  const numberList = numbers.split("");
  const permutationList = [];

  for (let i = 1; i <= numberList.length; i++) {
    permutationList.push(...getPermutations(numberList, i));
  }

  const result = new Set(
    permutationList.map((value) => Number(value.join("")))
  );

  Array.from(result).forEach((value) => {
    if (isPrime(value)) answer++;
  });

  console.log(isPrime(3));

  return answer;
}
