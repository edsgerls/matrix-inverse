import numpy as np
import math


def get_inverse(sq_mat):
    # Check if matrix is indeed square
    m, n = np.shape(sq_mat)

    # TODO Add robustness when a row of 0s is found
    if m == n:
        aug_mat = np.hstack((sq_mat, np.identity(n)))
        print(aug_mat)
        m2, n2 = np.shape(aug_mat)

        # Forma escalonada reducida por renglones (TODO: se requiere pivote parcial?)
        for j in range(m2): # Watchout! Up to m2, not n2

            print('j:', j)
            # TIP 1: Generar la secuencia sin el elemento de la diag donde i=j
            idx = [number for number in range(m2) if number != j]
            print(idx)

            # TIP 2: Saca ese bloque afuera, al cabo solo se usa una vez
            # First step: ensure the diag element is 1 (we are only sure that j = i, so you can use j instead)
            if not (aug_mat[j, j] == 1):
                aug_mat[j, :] = aug_mat[j, :] / aug_mat[j, j]
                pivot_row = aug_mat[j, :]

            for i in idx:
                print('i:', i)

                print('Make zero')
                coeff = (-1) * aug_mat[i, j]
                aug_mat[i, :] = aug_mat[i, :] + coeff * pivot_row
                print('idx a final:', idx)




        print(aug_mat)

    else:
        print('Inverse is not defined for non square matrices')






def main():
    A = np.array([[2, 4, 6], [4, 5, 6], [3, 1, -2]], dtype=float)
    get_inverse(A)

if __name__ == '__main__':
    main()
