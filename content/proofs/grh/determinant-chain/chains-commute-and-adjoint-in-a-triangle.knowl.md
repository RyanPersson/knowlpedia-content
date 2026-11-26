+++
id = "proofs/grh/determinant-chain/chains-commute-and-adjoint-in-a-triangle"
title = "Chains commute with the descent and are adjoint to it"
kind = "lemma"
summary = "In a triangle the descent moves past the weighted chain of a row up to a constant whose modulus is the product of the moduli of the squares crossed, and the next arrow is adjoint to the descent on chains."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Exchange.ChainCommutes", "New.Exchange.ChainAdjoint", "New.Exchange.ChainCommutes.succ", "New.Exchange.ChainAdjoint.succ", "New.Exchange.IsTriangle.exists_chainAdjoint", "New.Exchange.chainCommutes_zero", "New.Exchange.IsTriangle.exists_chainCommutes", "New.Exchange.HasSquareModuli.exists_chainCommutes", "New.Exchange.IsTriangle.exists_chainCommutes_and_chainAdjoint"]
lean_files = ["src/New/Determinant/Chain/TriangleNorms.lean"]
proof_status = "full"
+++

Let \((F,V,a,d,w,j)\) be a [[proofs/grh/determinant-chain/triangle-of-arrows|triangle of size \(m\)]] with all weights \(w_t(n)\neq0\), and \(X_{t,i,n}\) its weighted chains. For \(\beta,\kappa\colon I\to\mathbb{C}\) consider the statements

- \(\mathrm{CC}(i,n,\beta)\): for all \(t\) and \(y\in F_{i,0}\),
\[
X_{t,i+1,n}\,d_{t,i,0}\,a_{t,i,0}\,y=\frac{w_t(n+1)}{w_t(1)\,w_t(0)\,\overline{\beta(t)}}\ d_{t,i,n}\,X_{t,i,n+1}\,y
\]
(the quotient is \(0\) where \(\beta(t)=0\));
- \(\mathrm{CA}(i,n,\kappa)\): for all \(t\), \(y\in V\), \(z\in F_{i,n+1}\),
\[
\langle z,\ a_{t,i,n}X_{t,i,n}\,j_iy\rangle=\kappa(t)\,\langle d_{t,i,n}z,\ X_{t,i+1,n}\,j_{i+1}y\rangle .
\]

**Lemma.** Let \(i+n<m\).

1. There is \(\beta\) with \(\mathrm{CC}(i,n,\beta)\).
2. If the triangle [[proofs/grh/determinant-chain/square-moduli|has square moduli \(L\)]] for a relation \(\mathcal M\), then \(\beta\) in 1 can be chosen with \(\mathcal M\big(\beta,\ \prod_{i+1<k\le i+1+n}L_{i+1,k}\big)\), and there is \(\kappa\) with \(\mathcal M(\kappa,1)\) and \(\mathrm{CA}(i,n,\kappa)\).

## Proof

Induction on \(n\).

*\(n=0\).* \(\mathrm{CC}(i,0,1)\) reads \(d\,a\,y=\frac{w(1)}{w(1)w(0)}\,d\,(w(0)\,a\,y)\), true since the weights are nonzero; the empty product of moduli is \(1\) and \(\mathcal M(1,1)\). \(\mathrm{CA}(i,0,1)\) is condition 2 of a triangle.

*Step for CC.* Assume \(\mathrm{CC}(i,n,\beta)\) and that the square at \((i,n)\) commutes up to \(\beta'\) (it does for some \(\beta'\) since \(i+n+2\le m\); under square moduli \(\beta'\) has modulus \(L_{i+1,i+n+2}\)). Put \(Y=X_{t,i,n+1}y\) and \(c=w(n+1)/(w(1)w(0)\overline{\beta})\). Then
\[
X_{t,i+1,n+1}\,d\,a\,y=w(n)\,a_{t,i+1,n}\big(c\,d_{t,i,n}Y\big)=c\,\frac{w(n+2)}{\overline{\beta'}}\,d_{t,i,n+1}\,a_{t,i,n+1}Y
=\frac{w(n+2)}{w(1)w(0)\overline{\beta\beta'}}\,d_{t,i,n+1}X_{t,i,n+2}\,y,
\]
using \(X_{t,i,n+2}y=w(n+1)\,a_{t,i,n+1}Y\). This is \(\mathrm{CC}(i,n+1,\beta\beta')\), and the modulus of \(\beta\beta'\) is the product over \(i+1<k\le i+2+n\) by multiplicativity of \(\mathcal M\).

*Step for CA.* Assume \(\mathrm{CA}(i,n,\kappa)\) and the adjoint law of the square at \((i,n)\) with constant \(\kappa'\). Given \(z\in F_{i,n+2}\), let \(x\) be its adjoint vector. With \(X=X_{t,i,n}j_iy\), \(Y=X_{t,i+1,n}j_{i+1}y\),
\[
\langle z,\ a_{t,i,n+1}\,w(n)\,a_{t,i,n}X\rangle=w(n)\langle x,\ a_{t,i,n}X\rangle=w(n)\,\kappa\,\langle d_{t,i,n}x,\ Y\rangle
=\kappa\kappa'\,\langle d_{t,i,n+1}z,\ w(n)\,a_{t,i+1,n}Y\rangle,
\]
which is \(\mathrm{CA}(i,n+1,\kappa\kappa')\); and \(\mathcal M(\kappa\kappa',1)\). \(\blacksquare\)

## Remarks

The source also records the combined form: there are \(\beta,\kappa\) with \(\mathrm{CC}(i,n,\beta)\) such that, if the triangle has square moduli, \(\mathcal M(\kappa\beta,\prod_{i+1<k\le i+1+n}L_{i+1,k})\) and \(\mathrm{CA}(i,n,\kappa)\).

## References

1. Lean: `New.Exchange.ChainCommutes` in `src/New/Determinant/Chain/TriangleNorms.lean`.
2. Lean: `New.Exchange.ChainAdjoint` in `src/New/Determinant/Chain/TriangleNorms.lean`.
3. Lean: `New.Exchange.ChainCommutes.succ` in `src/New/Determinant/Chain/TriangleNorms.lean`.
4. Lean: `New.Exchange.ChainAdjoint.succ` in `src/New/Determinant/Chain/TriangleNorms.lean`.
5. Lean: `New.Exchange.IsTriangle.exists_chainAdjoint` in `src/New/Determinant/Chain/TriangleNorms.lean`.
6. Lean: `New.Exchange.chainCommutes_zero` in `src/New/Determinant/Chain/TriangleNorms.lean`.
7. Lean: `New.Exchange.IsTriangle.exists_chainCommutes` in `src/New/Determinant/Chain/TriangleNorms.lean`.
8. Lean: `New.Exchange.HasSquareModuli.exists_chainCommutes` in `src/New/Determinant/Chain/TriangleNorms.lean`.
9. Lean: `New.Exchange.IsTriangle.exists_chainCommutes_and_chainAdjoint` in `src/New/Determinant/Chain/TriangleNorms.lean`.
