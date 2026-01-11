# Types of Matrices in Mathematics

Matrices are an important part of Linear Algebra and are widely used in
Mathematics, Computer Science, AI, Machine Learning, Data Science, and Engineering.

A matrix is a rectangular arrangement of numbers arranged in rows and columns.

## 1. Row Matrix
A matrix having only one row is called a row matrix.

Example:
[ 1  2  3  4 ]

Order: 1 × n

## 2. Column Matrix
A matrix having only one column is called a column matrix.

Example:
[ 1 ]
[ 2 ]
[ 3 ]

Order: m × 1

## 3. Horizontal Matrix
A horizontal matrix is a matrix where the number of columns (\(n\)) is greater than the number of rows (\(m\)), making it wider than it is tall, like a row matrix (1xN) or any matrix where \(n>m\) (e.g., 2x3, 3x4), 
Examples of Horizontal Matrices:

- A Row Matrix (1 x n): Has only one row.
   
    A = [ 1  2  3  4 ]

- A 2 x 4 Matrix: More columns than rows.

  B = [ 1  2  3  4 ]
    [ 5  6  7  8 ]


- A 3 x 5 Matrix: A broader example.

  C = [ 2  4  12  -1  0 ]
    [ 3  5  -2  7  9 ]
    [ 1  0  3   2  5 ]




## 4. Vertical Matrix
A vertical matrix (or column matrix) is a matrix where the number of rows (\(m\)) is greater than the number of columns (\(n\)), making it taller than it is wide

Example 1 (3 rows, 2 columns - 3x2)

Example 2 (4 rows, 2 columns - 4x2)

## 5. Rectangular Matrix
A matrix in which number of rows is not equal to number of columns.

Example:
[ 1  2  3 ]
[ 4  5  6 ]

## 6. Square Matrix
A matrix having equal number of rows and columns.

Example:
[ 1  2 ]
[ 3  4 ]

## 7. Diagonal Matrix
A square matrix in which all non-diagonal elements are zero.

Example:
[ 3  0  0 ]
[ 0  5  0 ]
[ 0  0  7 ]

## 8. Non-Diagonal Matrix
A matrix having at least one non-zero element outside the main diagonal.

## 9. Null Matrix
A matrix in which all elements are zero.

Example:
[ 0  0 ]
[ 0  0 ]

## 10. Identity / Unit Matrix
A square matrix with 1s on diagonal and 0s elsewhere.

Example:
[ 1  0 ]
[ 0  1 ]

## 11. Symmetric Matrix
A square matrix equal to its transpose.
A = Aᵀ

## 12. Determinant of a Matrix
A scalar value calculated for square matrices.

For 2x2 matrix:
|A| = ad − bc

## 13. Minor
Determinant obtained after removing the row and column of an element.

## 14. Cofactor
Cᵢⱼ = (−1)ⁱ⁺ʲ × Minor

## 15. Adjoint of a Matrix
Transpose of the cofactor matrix.

## 16. Inverse of a Matrix
A⁻¹ = Adj(A) / |A|
|A| ≠ 0

## 17. Orthogonal Matrix
Aᵀ = A⁻¹

## 18. Idempotent Matrix
A² = A

## 19. Involutory Matrix
A² = I

End of Notes.
