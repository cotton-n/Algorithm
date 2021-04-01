/**
 *  다리를 지나는 트럭
 */

function solution(bridge_length, weight, truck_weights) {
  let answer = 0;

  const bridge = new Array(bridge_length).fill(0);
  let totalWeight = 0;

  while (!(totalWeight === 0 && truck_weights.length === 0)) {
    totalWeight -= bridge[0];
    bridge.shift();
    if (totalWeight + truck_weights[0] <= weight) {
      totalWeight += truck_weights[0];
      bridge.push(truck_weights.shift());
    } else {
      bridge.push(0);
    }
    answer++;
  }

  return answer;
}

solution(2, 10, [7, 4, 5, 6]);
