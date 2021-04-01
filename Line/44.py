def solution(snapshots, transactions):
  answer = []
  accounts = {}
  
  for snap in snapshots:
    accounts[snap[0]] = int(snap[1])
  
  transactions.sort(key=lambda x: x[0])
  id = -1
  for transaction in transactions:
    if transaction[0] != id:
      if transaction[1] == 'SAVE':
        try:
          accounts[transaction[2]] += int(transaction[3])
        except KeyError:
          accounts[transaction[2]] = int(transaction[3])
      elif transaction[1] == 'WITHDRAW':
        accounts[transaction[2]] -= int(transaction[3])
      id = transaction[0]
  
  for account, money in accounts.items():
    answer.append([account, str(money)])
  
  answer.sort(key=lambda x:x[0])
  return answer

print(solution([
  ["ACCOUNT1", "100"], 
  ["ACCOUNT2", "150"]
], [
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["2", "WITHDRAW", "ACCOUNT1", "50"], 
  ["1", "SAVE", "ACCOUNT2", "100"], 
  ["4", "SAVE", "ACCOUNT3", "500"], 
  ["3", "WITHDRAW", "ACCOUNT2", "30"]
]))