def solution(record):
    answer = []
    last_nickname = {}
    for rec in record:
        rec = rec.split()
        if rec[0] == "Leave": continue 
        last_nickname[rec[1]] = rec[2]
    
    for rec in record:
        rec = rec.split()
        if rec[0] == "Enter":
            answer.append(f"{last_nickname[rec[1]]}님이 들어왔습니다.")
        elif rec[0] == "Leave":
            answer.append(f"{last_nickname[rec[1]]}님이 나갔습니다.")
        
    return answer