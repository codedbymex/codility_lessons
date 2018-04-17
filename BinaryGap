def solution(N):
    big_gap = 0
    gap = 0
    
    for idx, i in enumerate('{0:1b}'.format(N)):
        if i == '0':
            gap += 1
    
        elif i != 0 and idx > 0:
            if big_gap <= gap:
                big_gap = gap
                gap = 0
            gap = 0

    return(big_gap)
