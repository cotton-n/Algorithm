'''
오픈채팅방
'''

def solution(record):
    user = {}
    answer = []
    
    for r in record: 
        data = r.split()
        if data[0] == 'Enter':
            user[data[1]] = data[2]
        elif data[0] == 'Change':
            user[data[1]] = data[2]
            
    for r in record: 
        data = r.split()
        if data[0] == 'Enter':
            s = user[data[1]] + '님이 들어왔습니다.'
            answer.append(s)
        elif data[0] == 'Leave':
            s = user[data[1]] + '님이 나갔습니다.'
            answer.append(s)
    
    return answer