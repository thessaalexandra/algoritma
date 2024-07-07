def selisihDiagonal(matriks):
    n = len(matriks)
    diagonalUtama = sum(matriks[i][i] for i in range(n))
    diagonalSekunder = sum(matriks[i][n-i-1] for i in range(n))
    return abs(diagonalUtama - diagonalSekunder)

matriks = [
    [1, 2, 0],
    [4, 5, 6],
    [7, 8, 9]
]
hasil = selisihDiagonal(matriks)
print(hasil)
