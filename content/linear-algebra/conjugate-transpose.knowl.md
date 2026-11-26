+++
id = "linear-algebra/conjugate-transpose"
title = "Conjugate transpose"
kind = "definition"
summary = "Exchange a complex matrix's row and column indices and conjugate each entry."
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/matrix","linear-algebra/matrix-transpose","shared-foundations/complex-conjugate","linear-algebra/inner-product","linear-algebra/determinant"]
+++

For a complex [[linear-algebra/matrix|matrix]] \(A\in M_{m,n}(\mathbb C)\), its **conjugate transpose** is \(A^*\in M_{n,m}(\mathbb C)\) with \((A^*)_{ij}=\overline{A_{ji}}\). It combines [[linear-algebra/matrix-transpose|transposition]] with entrywise [[shared-foundations/complex-conjugate|complex conjugation]].

## Inner products

For column vectors with the usual complex [[linear-algebra/inner-product|inner product]], \(\langle Ax,y\rangle=(Ax)^*y=x^*A^*y=\langle x,A^*y\rangle\). For a square matrix, \(\det A^*=\overline{\det A}\) since transposition preserves the [[linear-algebra/determinant|determinant]] and its coefficients are integers.
