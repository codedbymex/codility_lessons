def solution(A, K):
    if A:
        next_list = lambda x: x[-1:] + x[:-1]
        A = [next_list(A) for i in range(K)][-1]
    return A
