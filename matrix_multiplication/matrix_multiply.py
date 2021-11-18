# MATRIX MULTIPLICATION - SQUARE MATRIX 
# FOR LOOP AND NUMPY dot() FUNCTION

import numpy as np
import time

# Function to multiply matrix
def matrix_multiply(n, A, B, C):
    for i in range (n):
        for j in range (n):
            C[i][j] = 0;
            for k in range (n):
                C[i][j] += A[i][k] * B[k][j]

# Function to print matrix
def print_matrix(n, C):
    for i in range (n):
        for j in range (n):
            print(C[i][j], end=" ")
        print()

# Assign array with list of lists
def main():
    
    A = [[1,2],
         [3,4]]
    B = [[0,1],
         [5,6]]
    C = [[0,0],
         [0,0]]
    n = len(A)

    start1 = time.perf_counter()
    matrix_multiply(n,A,B,C)
    end1 = time.perf_counter()
    print("Showing result for main: \n")
    print_matrix(n,C)
    print(f"MATRIX MULTIPLICATION ran in {end1-start1} seconds\n")


# Assign array with numpy
def main2():
    A = np.array([[1,2],[3,4]])
    B = np.array([[0,1],[5,6]])
    C = np.zeros((2,2), dtype=int)
    n = len(A)

    start2 = time.perf_counter()
    matrix_multiply(n,A,B,C)
    end2 = time.perf_counter()
    print("Showing result for main2: \n")
    print_matrix(n,C)
    print(f"MATRIX MULTIPLICATION ran in {end2-start2} seconds\n")
    

# numpy matrix multiplication
def main3():
    A = np.array([[1,2],[3,4]])
    B = np.array([[0,1],[5,6]])

    start2 = time.perf_counter()
    C = np.dot(A,B)
    end2 = time.perf_counter()
    print("Showing result for main3: \n")
    print(C)
    print(f"MATRIX MULTIPLICATION ran in {end2-start2} seconds\n")

main()
main2()
main3()
