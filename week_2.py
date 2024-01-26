import numpy as np


def tridiag(a_l, a_c, a_r, n):
    # Exercise 2.4
    """
    :param a_l: Element for lower diagonal of matrix
    :param a_c: Element for center diagonal of matrix
    :param a_r: Element for upper diagonal of matrix
    :param n: Size of matrix
    :return: Tridiagonal matrix
    """
    a_l_array = [a_l] * (n-1)
    a_c_array = [a_c] * n
    a_r_array = [a_r] * (n-1)

    return np.diag(a_l_array, k=-1) + np.diag(a_c_array) + np.diag(a_r_array, k=1)


def special_matrix(m, n):
    M = np.zeros((m,n))
    for i in range(1, m):
        for j in range(1, n):
            M[i,j] = (1/(i+j-1))
    return(M)


def frobenius(Matrix):
    return 3


def main():
    # Exercise 2.5
    n = 10
    A = tridiag(-1, 2, -1, n)
    # Ascending sort
    print(np.sort(np.linalg.eigvals(A)))

    # Numerical verification of eigenvalues
    for k in range(1, n):
        e_val = 2 - 2*np.cos(((k)*np.pi)/(n+1))
        print(e_val)

    #Exercise 2.6
    special_matrix(5, 6)


if __name__ == "__main__":
    main()
