def solution(tickets):
    answer = []
    sortTickets = sorted(tickets, key=lambda t: t[1], reverse=True)
    visited = [False for _ in sortTickets]
    stack = ["ICN"]

    while stack:
        count = 0
        current = stack.pop()
        for i, ticket in enumerate(sortTickets):
            if visited[i]:
                continue
            if ticket[0] == current:
                stack.append(ticket[1])
                visited[i] = True
                count += 1
        answer.append(current)
        if count == 0 and (False in visited):
            # 더 갈곳도 없는데 가지 않은 곳도 있을 때
            # 되돌아가야하는데 어떻게 되돌아가 ㅡ.ㅡ
            # 백트래킹
            break
    return answer


if __name__ == '__main__':
    # [ICN, JFK, HND, IAD]
    print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
    # [ICN, ATL, ICN, SFO, ATL, SFO]
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
    print(solution([["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]))
