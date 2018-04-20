def solution(A):
    # write your code in Python 3.6
    unique = set()
    for i in A:
        if i in unique:
            unique.remove(i)
        else:
            unique.add(i)
    return(list(unique)[0])
