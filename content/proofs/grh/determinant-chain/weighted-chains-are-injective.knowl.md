+++
id = "proofs/grh/determinant-chain/weighted-chains-are-injective"
title = "Weighted chains of a triangle are injective"
kind = "lemma"
summary = "In a triangle with nonzero weights the weighted chain of each row is injective on the copy of V, and the constants of the squares do not vanish."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Exchange.IsTriangle.eq_zero_of_weightedChain_eq_zero", "New.Exchange.IsTriangle.ne_zero_of_chainCommutes", "New.Exchange.IsTriangle.ne_zero_of_squareCommutes"]
lean_files = ["src/New/Determinant/Chain/TriangleNorms.lean"]
proof_status = "full"
+++

**Lemma.** Let \((F,V,a,d,w,j)\) be a [[proofs/grh/determinant-chain/triangle-of-arrows|triangle of size \(m\)]] with all weights \(w_t(n)\ne0\).

1. If \(i+n\le m\), \(t\in I\), \(y\in V\) and \(X_{t,i,n}\,j_iy=0\), then \(y=0\).
2. Assume \(V\neq0\). If \(i+n<m\) and \(\beta\) satisfies the commutation law \(\mathrm{CC}(i,n,\beta)\) of [[proofs/grh/determinant-chain/chains-commute-and-adjoint-in-a-triangle|chains and descent]], then \(\beta(t)\neq0\) for all \(t\). If \(i+n+2\le m\) and the square at \((i,n)\) commutes up to \(\beta'\), then \(\beta'(t)\ne0\) for all \(t\).

## Proof

1. Induction on \(n\), for all \(i\). For \(n=0\), \(j_i\) is an isometry, hence injective. For \(n+1\): choose \(\beta\) with \(\mathrm{CC}(i,n,\beta)\) and \(x\in V\) with \(j_{i+1}x=d\,a\,j_iy\) (condition 3). Then \(X_{t,i+1,n}j_{i+1}x\) is a scalar multiple of \(d_{t,i,n}X_{t,i,n+1}j_iy=0\). By induction (row \(i+1\), \(i+1+n\le m\)) \(x=0\), so \(d\,a\,j_iy=0\) and \(y=0\) by condition 4.
2. Suppose \(\beta(t)=0\). Take \(y\ne0\) in \(V\) and \(x\) with \(j_{i+1}x=d\,a\,j_iy\). The scalar in \(\mathrm{CC}\) is a quotient by \(0\), read as \(0\), so \(X_{t,i+1,n}j_{i+1}x=0\); by part 1, \(x=0\), and by condition 4, \(y=0\), a contradiction. For the square: choose \(\beta\) with \(\mathrm{CC}(i,n,\beta)\); then \(\mathrm{CC}(i,n+1,\beta\beta')\) by the induction step of the cited lemma, so \(\beta(t)\beta'(t)\neq0\). \(\blacksquare\)

## References

1. Lean: `New.Exchange.IsTriangle.eq_zero_of_weightedChain_eq_zero` in `src/New/Determinant/Chain/TriangleNorms.lean`.
2. Lean: `New.Exchange.IsTriangle.ne_zero_of_chainCommutes` in `src/New/Determinant/Chain/TriangleNorms.lean`.
3. Lean: `New.Exchange.IsTriangle.ne_zero_of_squareCommutes` in `src/New/Determinant/Chain/TriangleNorms.lean`.
