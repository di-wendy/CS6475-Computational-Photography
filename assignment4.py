    for i in range(0,N):
        for j in range(0,2*N+width):
            if j < N:
                output[N-i][N-j]=image[i+1][j+1]
            elif j in range(N,N+width):
                output[N-i][j]=image[i+1][j-N]
            else:
                output[N-i][j]=image[i+1][width-j]
