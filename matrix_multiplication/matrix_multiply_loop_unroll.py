"""
 MATRIX-MATRIX MULTIPLICATION (MM)

 STRUCTURE OF MATRIX: Dense square matrix
 
 METHODS - For loop and numpy dot() function
 
           There are two versions for the "For loop" - optimized (loop unrolling) and not optimized (native matrix multiplication)

 ARRAY ASSIGNMENT - List of lists and numpy.ndarray()

 COMPARISON -
 
            A. Optimized MM versus not optimized MM for list of lists assignment of array
            
            B. Optimized MM versus not optimized MM for numpy.ndarray assignment of array

            C. A versus B; A,B versus np.dot()
            
 @author: Oluwatosin S. Oluseyi <olutosinbanjo@gmail.com>
 
"""

# Libraries
import numpy as np
import random
import time

#Global variable - size of matrix, unroll factor and arrays

n = 30
unroll = 15
m = n - (n % unroll) # if unroll factor is not a multiple of n, get highest possible even quotient of unroll factor from n

# List comprehension to use list of lists it assign array
A_list = [ [ random.randint(1,20) for i in range (n) ] for j in range(n)]
B_list = [ [ random.randint(1,20) for i in range (n) ] for j in range(n)]

# Convert List to numpy array
A_np = np.array(A_list)
B_np = np.array(B_list)

# Function for native matrix multiplication
def notopt_matrix_multiply(A_list , B_list, C):
    for i in range (n):
        for j in range (n):
            C[i][j] = 0
            for k in range (n):
                C[i][j] +=  A_list[i][k] * B_list[k][j]
    return C


# Functions for optimized matrix multiplication
def opt_matrix_multiply_multiple(A_list, B_list, C):
    for i in range (n):
        for j in range (n):
            sum = 0
            for k in range (0,m,unroll):
                sum = sum + A_list[i][k] * B_list[k][j]
                sum = sum + A_list[i][k+1] * B_list[k+1][j]
                sum = sum + A_list[i][k+2] * B_list[k+2][j]
                sum = sum + A_list[i][k+3] * B_list[k+3][j]
                sum = sum + A_list[i][k+4] * B_list[k+4][j] # stop here for unroll = 5
                sum = sum + A_list[i][k+5] * B_list[k+5][j]
                sum = sum + A_list[i][k+6] * B_list[k+6][j]
                sum = sum + A_list[i][k+7] * B_list[k+7][j]
                sum = sum + A_list[i][k+8] * B_list[k+8][j]
                sum = sum + A_list[i][k+9] * B_list[k+9][j] # stop here for unroll = 10
                sum = sum + A_list[i][k+10] * B_list[k+10][j]
                sum = sum + A_list[i][k+11] * B_list[k+11][j]
                sum = sum + A_list[i][k+12] * B_list[k+12][j]
                sum = sum + A_list[i][k+13] * B_list[k+13][j]
                sum = sum + A_list[i][k+14] * B_list[k+14][j]
            C[i][j] = sum
    return C

def opt_matrix_multiply_not_multiple(A_list, B_list, C):
    for i in range (n):
        for j in range (n):
            sum = 0
            for k in range (0,m,unroll):
                sum = sum + A_list[i][k] * B_list[k][j]
                sum = sum + A_list[i][k+1] * B_list[k+1][j]
                sum = sum + A_list[i][k+2] * B_list[k+2][j]
                sum = sum + A_list[i][k+3] * B_list[k+3][j]
                sum = sum + A_list[i][k+4] * B_list[k+4][j] # stop here for unroll = 5
                sum = sum + A_list[i][k+5] * B_list[k+5][j]
                sum = sum + A_list[i][k+6] * B_list[k+6][j]
                sum = sum + A_list[i][k+7] * B_list[k+7][j]
                sum = sum + A_list[i][k+8] * B_list[k+8][j]
                sum = sum + A_list[i][k+9] * B_list[k+9][j] # stop here for unroll = 10
                sum = sum + A_list[i][k+10] * B_list[k+10][j]
                sum = sum + A_list[i][k+11] * B_list[k+11][j]
                sum = sum + A_list[i][k+12] * B_list[k+12][j]
                sum = sum + A_list[i][k+13] * B_list[k+13][j]
                sum = sum + A_list[i][k+14] * B_list[k+14][j]
            for k in range (m,n,1):
                sum = sum + A_list[i][k] * B_list[k][j]
                 # store in result in C array
            C[i][j] = sum
    return C
            

# Function to print matrix
def print_matrix(C):
    for i in range (n):
        for j in range (n):
            print(C[i][j], end=" ")
        print()

# Assign array with list of lists
def main1_notoptimized():
    
    C = [ [ [] for i in range (n) ] for j in range(n) ]

    start1 = time.perf_counter()
    notopt_matrix_multiply(A_list,B_list,C)
    end1 = time.perf_counter()
    print("Showing result for main1_notoptimized: \n")
    print_matrix(C)
    print(f"NOT OPTIMIZED MATRIX MULTIPLICATION ran in {end1-start1} seconds\n")


def main1_optimized():
    
    C = [ [ [] for i in range (n) ] for j in range(n) ]

    if(n % unroll == 0):
        start11 = time.perf_counter()
        opt_matrix_multiply_multiple(A_list,B_list,C)
        end11 = time.perf_counter()
    elif(n % unroll != 0):
        start11 = time.perf_counter()
        opt_matrix_multiply_not_multiple(A_list,B_list,C)
        end11 = time.perf_counter()
        
    print("Showing result for main1_optimized: \n")
    print_matrix(C)
    print(f"OPTIMIZED MATRIX MULTIPLICATION ran in {end11-start11} seconds\n")


# Assign array with numpy
def main2_notoptimized():
    
    C = np.zeros((n,n), dtype=int)

    start2 = time.perf_counter()
    notopt_matrix_multiply(A_np,B_np,C)
    end2 = time.perf_counter()
    print("Showing result for main2_notoptimized: \n")
    print_matrix(C)
    print(f"NOT OPTIMIZED MATRIX MULTIPLICATION ran in {end2-start2} seconds\n")


def main2_optimized():
    
    C = np.zeros((n,n), dtype=int)
    
    if(n % unroll == 0):
        start21 = time.perf_counter()
        opt_matrix_multiply_multiple(A_np,B_np,C)
        end21 = time.perf_counter()
    elif(n % unroll != 0):
        start21 = time.perf_counter()
        opt_matrix_multiply_not_multiple(A_np,B_np,C)
        end21 = time.perf_counter()
        
    print("Showing result for main2_optimized: \n")
    print_matrix(C)
    print(f"OPTIMIZED MATRIX MULTIPLICATION ran in {end21-start21} seconds\n")


# numpy matrix multiplication
def main3():

    start3 = time.perf_counter()
    C = np.matmul(A_np,B_np)
    end3 = time.perf_counter()
    print("Showing result for main3: \n")
    print(C)
    print(f"NUMPY dot() MATRIX MULTIPLICATION ran in {end3-start3} seconds\n")


main1_notoptimized()
main1_optimized()
main2_notoptimized()
main2_optimized()
main3()
