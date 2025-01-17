
import mpmath  
import numpy as np


class FFT:

    def __init__(self, poly_a=None, poly_b=None):
        
        self.polyA = list(poly_a or [0])[:]
        self.polyB = list(poly_b or [0])[:]

        
        while self.polyA[-1] == 0:
            self.polyA.pop()
        self.len_A = len(self.polyA)

        while self.polyB[-1] == 0:
            self.polyB.pop()
        self.len_B = len(self.polyB)

        
        self.c_max_length = int(
            2 ** np.ceil(np.log2(len(self.polyA) + len(self.polyB) - 1))
        )

        while len(self.polyA) < self.c_max_length:
            self.polyA.append(0)
        while len(self.polyB) < self.c_max_length:
            self.polyB.append(0)
        
        self.root = complex(mpmath.root(x=1, n=self.c_max_length, k=1))

        
        self.product = self.__multiply()

    
    def __dft(self, which):
        dft = [[x] for x in self.polyA] if which == "A" else [[x] for x in self.polyB]
        
        if len(dft) <= 1:
            return dft[0]
        next_ncol = self.c_max_length // 2
        while next_ncol > 0:
            new_dft = [[] for i in range(next_ncol)]
            root = self.root**next_ncol

            
            current_root = 1
            for j in range(self.c_max_length // (next_ncol * 2)):
                for i in range(next_ncol):
                    new_dft[i].append(dft[i][j] + current_root * dft[i + next_ncol][j])
                current_root *= root
            
            current_root = 1
            for j in range(self.c_max_length // (next_ncol * 2)):
                for i in range(next_ncol):
                    new_dft[i].append(dft[i][j] - current_root * dft[i + next_ncol][j])
                current_root *= root
            
            dft = new_dft
            next_ncol = next_ncol // 2
        return dft[0]

    
    def __multiply(self):
        dft_a = self.__dft("A")
        dft_b = self.__dft("B")
        inverce_c = [[dft_a[i] * dft_b[i] for i in range(self.c_max_length)]]
        del dft_a
        del dft_b

        
        if len(inverce_c[0]) <= 1:
            return inverce_c[0]
        
        next_ncol = 2
        while next_ncol <= self.c_max_length:
            new_inverse_c = [[] for i in range(next_ncol)]
            root = self.root ** (next_ncol // 2)
            current_root = 1
            
            for j in range(self.c_max_length // next_ncol):
                for i in range(next_ncol // 2):
                    
                    new_inverse_c[i].append(
                        (
                            inverce_c[i][j]
                            + inverce_c[i][j + self.c_max_length // next_ncol]
                        )
                        / 2
                    )
                    
                    new_inverse_c[i + next_ncol // 2].append(
                        (
                            inverce_c[i][j]
                            - inverce_c[i][j + self.c_max_length // next_ncol]
                        )
                        / (2 * current_root)
                    )
                current_root *= root
            
            inverce_c = new_inverse_c
            next_ncol *= 2
        
        inverce_c = [round(x[0].real, 8) + round(x[0].imag, 8) * 1j for x in inverce_c]

        
        while inverce_c[-1] == 0:
            inverce_c.pop()
        return inverce_c

    
    def __str__(self):
        a = "A = " + " + ".join(
            f"{coef}*x^{i}" for coef, i in enumerate(self.polyA[: self.len_A])
        )
        b = "B = " + " + ".join(
            f"{coef}*x^{i}" for coef, i in enumerate(self.polyB[: self.len_B])
        )
        c = "A*B = " + " + ".join(
            f"{coef}*x^{i}" for coef, i in enumerate(self.product)
        )

        return f"{a}\n{b}\n{c}"



if __name__ == "__main__":
    import doctest

    doctest.testmod()
