import numpy as np


def generate_matrix(m, n):

    Z = np.random.randint(0, 100, (m, n))

    print("\nInput Sub-Matrix:\n")
    print(Z)
    print('\n')

    return Z


def get_greatest_sum(Z):

    greatest_sum = 0
    greatest_sum_direction = ''

    # Rows sums
    for i, row in enumerate(Z):
        row_sum = 0
        for element in row:
            row_sum += element
        print(f'Row {i} sum: {row_sum}')

        if row_sum > greatest_sum:
            greatest_sum = row_sum
            greatest_sum_direction = f'Row # {i}'
    
    # Columns sums
    # We iterate on Z.T
    for i, col in enumerate(Z.T):
        col_sum = 0
        for element in col:
            col_sum += element
        print(f'Col {i} sum: {col_sum}')

        if col_sum > greatest_sum:
            greatest_sum = col_sum
            greatest_sum_direction = f'Column # {i}'

    # Diagonals sum
    diagonal_sum = 0
    antidiagonal_sum = 0

    for index, element in np.ndenumerate(Z):
        
        if index[0] == index[1]:
            diagonal_sum += element

        if index[0] + index[1] == 4:
            antidiagonal_sum += element

    print(f'\nDiagonal sum: {diagonal_sum}')
    print(f'\nAntiDiagonal sum: {antidiagonal_sum}')

    if diagonal_sum > greatest_sum:
        greatest_sum = diagonal_sum
        greatest_sum_direction = f'Main Diagonal'

    if antidiagonal_sum > greatest_sum:
        greatest_sum = antidiagonal_sum
        greatest_sum_direction = f'AntiDiagonal'

    # X-Shape sums
    for index, element in np.ndenumerate(Z):

        if index[0] <= 2 and index[1] <= 2:
            xshape_sum = ( 
                element + 
                Z[index[0],(index[1]+2)] +
                Z[(index[0]+1),(index[1]+1)] +
                Z[(index[0]+2),(index[1])] +
                Z[(index[0]+2),(index[1]+2)]
                )
            print(f'X shape found starting at position ({index[0]},{index[1]}), sum: {xshape_sum}')
            if xshape_sum > greatest_sum:
                greatest_sum = xshape_sum
                greatest_sum_direction = f'X shape starting at position ({index[0]},{index[1]})'     

    print(f'\nGreatest sum: {greatest_sum} found on {greatest_sum_direction}\n')

    return greatest_sum


def get_total_sum(Z):
    total_sum = 0
    for element in Z.flat:
        total_sum += element
    print(f'\nThe Total Sum of all elements in the Sub Matrix is: {total_sum}\n')

    return total_sum


def main():

    # The size of the matrix:
    m = n = 5
    Z = generate_matrix(m, n)

    get_greatest_sum(Z)

    get_total_sum(Z)
    
    return

if __name__ == "__main__":
    main()
