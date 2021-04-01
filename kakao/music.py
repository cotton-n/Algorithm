'''
방금그곡
'''

from datetime import datetime

change = {
    'C#': 'I', 'D#': 'J', 'F#': 'K', 'G#': 'L', 'A#': 'M', 'E#': 'H'
}

def init(m):
    temp = []
    
    for a in m:
        if a == '#':
            d = temp.pop() + '#'
            temp.append(change[d])
        else:
            temp.append(a)
    return ''.join(temp)

def solution(m, musicinfos):
    answer = ''
    answerMelody = ''
    newM = init(m)
    
    for music in musicinfos:
        info = music.split(',')
        start = datetime.strptime(info[0], "%H:%M")
        end = datetime.strptime(info[1], "%H:%M")
        time = int((end - start).seconds/60)
        name = info[2]
        melody = init(info[3])
        musicSize = len(melody)
        newMelody = ''
        for i in range(time):
            newMelody += melody[i % musicSize]
        if newMelody.find(newM) != -1:
            if len(answerMelody) < len(newMelody):
                answer = name
                answerMelody = newMelody
    if answer == '': answer = '(None)'
    return answer