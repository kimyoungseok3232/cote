def solution(book_time):
    answer = 0
    book_time.sort()
    room_list = {1:0}
    for st, ed in book_time:
        sth, stm = st.split(":")
        st = int(sth)*60+int(stm)
        edh, edm = ed.split(":")
        ed = int(edh)*60+int(edm)+10
        for room in room_list:
            if room_list[room] <= st:
                room_list[room] = ed
                break
        else:
            room_list[room+1] = ed
    
    return len(room_list)