import numpy as np
from num2words import num2words


def generate_matrix(M, N):

    # Create a one row matrix with zeros
    Z = np.zeros( (N), dtype=np.int16 )
    max_zeros_next_row = N

    for row in range(M):
        # Generate number of zeros and ones:
        if max_zeros_next_row == 0:
            zeros_this_row = 0
        else:
            zeros_this_row = np.random.randint( 0, max_zeros_next_row )

        ones_this_row = N - zeros_this_row
        max_zeros_next_row = zeros_this_row

        zeros = np.zeros( (zeros_this_row), dtype=np.int16 )
        ones = np.ones( (ones_this_row), dtype=np.int16 )
        the_row = np.hstack( (zeros,ones) )

        # Add the new row to the matrix
        if row == 0:
            Z = Z + the_row
        else:
            Z = np.row_stack( (Z,the_row) )

    print("\nInput Matrix:\n")
    print(Z)
    return Z

def count_zeros(Z):
    total_zeros = 0
    for element in Z.flat:
        if element == 0:
            total_zeros += 1

    if total_zeros > 1:
        print(f'\n{num2words(total_zeros).capitalize()} ({total_zeros}) zeros are present.\n')
    else:
        print(f'\n{num2words(total_zeros).capitalize()} ({total_zeros}) zero is present.\n')
    return

def main():

    # The size of the matrix:
    M = int( input("\nEnter number of rows (1 to 1000): ") )
    N = int( input("\nEnter number of columns (1 to 1000): ") )

    Z = generate_matrix(M, N)

    count_zeros(Z)

    return

if __name__ == "__main__":
    main()
