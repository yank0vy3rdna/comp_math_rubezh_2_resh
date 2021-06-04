def print_matrix(A, B):
    print()
    print("---------")
    for i in range(len(A)):
        print(' '.join([str(r) for r in A[i]]), B[i])
    print("---------")
    print()
