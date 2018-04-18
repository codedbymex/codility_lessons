def solution(A, K):
    if A:
        A = [A[-1:] + A[:-1] for i in range(K)][-1]
    return A
