def solution(sticker):
    if len(sticker) < 3: return max(sticker)

    dp1 = [0]*len(sticker)
    for idx in range(len(sticker)-1):
        dp1[idx] = max(dp1[idx-3], dp1[idx-2]) + sticker[idx]

    dp2 = [0]*len(sticker)
    for idx, num in enumerate(sticker[1:]):
        dp2[idx] = max(dp2[idx-3], dp2[idx-2]) + num
    
    return max(max(dp1), max(dp2))