def solution(N, big_gap = 0, gap = 0):
    
    for i in '{0:1b}'.format(N):
        if i == '0':
            gap += 1
        elif big_gap <= gap:
            big_gap = gap
            gap = 0
        else:
            gap = 0

    return(big_gap)
