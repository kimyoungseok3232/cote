def solution(strArr):
    return [st.upper() if idx%2 else st.lower() for idx, st in enumerate(strArr)]