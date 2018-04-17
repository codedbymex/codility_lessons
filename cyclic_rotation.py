def solution(A, K):
    if A:
        for i in range(K):
            next_list = [A[-1]]
            next_list.extend(A[:-1])
            A = next_list
        return(A)
    return A
