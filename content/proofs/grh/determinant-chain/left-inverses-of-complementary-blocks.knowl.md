+++
id = "proofs/grh/determinant-chain/left-inverses-of-complementary-blocks"
title = "Left inverses of complementary blocks"
kind = "lemma"
summary = "If a block of rows of the first columns of an invertible matrix has a left inverse, so has the complementary block of columns of the last rows of its inverse; and matrices with such a block are first columns of invertible matrices."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Exchange.hasLeftInv_toCols_of_hasLeftInv_toRows", "New.Exchange.hasLeftInv_submatrix_invLastRows", "New.Exchange.exists_eq_firstCols"]
lean_files = ["src/New/Determinant/Chain/SquareLaw.lean"]
proof_status = "full"
+++

Let \(R\) be a commutative ring, \(N,n,a,b\) finite index sets, \(e\colon b\sqcup a\to N\sqcup n\) a bijection. For \(k\in\mathrm{GL}_{N\sqcup n}(R)\) let \(y_k\) be the columns \(e(b)\) of \(k\) and \(x_k\) the rows \(e(a)\) of \(k^{-1}\). A matrix \(X\) *has a left inverse* if \(LX=1\) for some matrix \(L\).

**Lemma.**

1. If the rows \(N\) of \(y_k\) have a left inverse, then the columns \(n\) of \(x_k\) have a left inverse; if the rows \(n\) of \(y_k\) have a left inverse, then the columns \(N\) of \(x_k\) have one.
2. Suppose that for any two \(r,s\in R\) there is an [[algebra-rings/idempotent-element|idempotent]] \(\varepsilon\in R\) such that both \(r\) and \(s\) are multiples of \(r-\varepsilon(r-s)\). If the rows \(N\) or the rows \(n\) of \(y\in M_{(N\sqcup n)\times b}(R)\) have a left inverse, then \(y=y_\gamma\) for some \(\gamma\in\mathrm{GL}_{N\sqcup n}(R)\).

## Proof

1. More generally let \(s\in M_{b\times(N\sqcup n)}(R)\) satisfy \(s\,y_k=1\), and let \(f\) be an injection of an index set into \(N\sqcup n\) such that the columns \(f\) of \(s\) vanish. Let \(P\) be the square matrix with rows \(s\) and \(x_k\). By Jacobi's identity \(\det P\cdot\det k=\det(s\,y_k)=1\) ([[?lean:New.det_fromRows_invLastRows|determinant of rows stacked on the last rows of the inverse]]), so \(P\) is invertible and \(P^{-1}P=1\). Reading this at rows and columns in the image of \(f\): \(\delta_{ij}=\sum_{t\in b}P^{-1}_{f(i),t}\,s_{t,f(j)}+\sum_{u\in a}P^{-1}_{f(i),u}(x_k)_{u,f(j)}\), and the first sum vanishes. So the columns \(f\) of \(x_k\) have the left inverse \((P^{-1}_{f(i),u})\). Apply this with \(s=(L\ \ 0)\) for a left inverse \(L\) of the rows \(N\) of \(y_k\) and \(f\) the inclusion of \(n\); and with \(s=(0\ \ L)\) and the inclusion of \(N\).
2. A left inverse \(M\) of a block of rows of \(y\), extended by zero, is a left inverse of \(y\); so \(y\) is a primitive matrix over \(R\) (it and a left inverse have entries in \(R\)). Under the stated hypothesis on \(R\) the primitive matrices are exactly the matrices \(y_\gamma\) ([[?lean:New.IsValuationPair.exists_firstCols_iff|primitive matrices are first columns]], proved by a Hermite normal form). \(\blacksquare\)

## References

1. Lean: `New.Exchange.hasLeftInv_toCols_of_hasLeftInv_toRows` in `src/New/Determinant/Chain/SquareLaw.lean`.
2. Lean: `New.Exchange.hasLeftInv_submatrix_invLastRows` in `src/New/Determinant/Chain/SquareLaw.lean`.
3. Lean: `New.Exchange.exists_eq_firstCols` in `src/New/Determinant/Chain/SquareLaw.lean`.
