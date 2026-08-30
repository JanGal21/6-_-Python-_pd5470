from cmath import nan

import numpy as np

macierz_ekspresji = np.array([[5.1, 3.2, 6.3],
                               [2.3, 4.5, 5.6],
                               [7.8, 3.9, 2.2],
                               [4.4, 5.5, 6.6]])
print(macierz_ekspresji*1.05) #zwiększenie ekspresji wszystkich genów o 5%
print(np.mean(macierz_ekspresji,axis = 1))
print(np.sum(macierz_ekspresji,axis=0))
macierz_ekspresji[[0,1,2,3],[1,0,2,1]] = np.nan
print(macierz_ekspresji)
print(np.nanmean(macierz_ekspresji, axis=1))