import numpy as np


def generate_matrix(m, n):
    
    Z = np.random.randint(0, 100, (m, n))

    # Matrix for testing
    """
    Z = np.array([
        (1, 2, 3, 5), 
        (2, 1, 2, 3), 
        (3, 2, 1, 2), 
        (4, 3, 2, 1),
        (5, 4, 3, 2)
        ])
    """

    print(Z)
    return Z


def is_toepliz(Z, m, n):
    
    toe = True

    for index, element in np.ndenumerate(Z):

        # print(index, element)
        row_index, col_index = 1, 1
        
        while ( (index[0] + row_index) <= (m-1) ) and ( (index[1] + col_index) <= (n-1) ):
            assert (element == Z[(index[0] + row_index), (index[1] + col_index)]), "Not matching element(s) detected."
            row_index += 1
            col_index += 1
        
    return toe
    

def main():

    # The size of the matrix:
    m = int( input("\nEnter number of rows (1 to 1000): ") )
    n = int( input("\nEnter number of columns (1 to 1000): ") )

    Z = generate_matrix(m, n)

    try:
        is_toepliz(Z, m, n)
        print("The matrix is Toeplitz")
    except AssertionError as error:
        print(error)
        print("The matrix is not Toeplitz")
    
    return

if __name__ == "__main__":
    main()
