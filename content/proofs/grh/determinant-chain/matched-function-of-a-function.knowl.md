+++
id = "proofs/grh/determinant-chain/matched-function-of-a-function"
title = "The matched function of a function"
kind = "lemma"
summary = "Every function on column blocks with the right support and equivariance has exactly one matched partner; matched pairs are stable under translation."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Exchange.matchOf", "New.Exchange.areMatched_matchOf", "New.Exchange.exists_firstCols_eq_mul_of_invLastRows_eq", "New.AreMatched.unique", "New.AreMatched.translate", "New.Exchange.blockInlGL"]
lean_files = ["src/New/Determinant/Chain/SquareLaw.lean"]
proof_status = "full"
+++

Let \(R\) be a commutative ring (finite where sums are taken), \(\chi\) a multiplicative character of \(R\), and \(e\colon b\sqcup a\to n\) a bijection of finite index sets. For \(\gamma\in\mathrm{GL}_n(R)\) write \(y_\gamma\in M_{n\times b}(R)\) for the columns \(e(b)\) of \(\gamma\) and \(x_\gamma\in M_{a\times n}(R)\) for the rows \(e(a)\) of \(\gamma^{-1}\). [[?lean:New.AreMatched|Matched functions]] \((\Phi,\Psi)\) are those with \(\Phi\) supported on the \(x_\gamma\), \(\Psi\) supported on the \(y_\gamma\), and \(\Phi(x_\gamma)=\chi(\det\gamma)\Psi(y_\gamma)\).

**Definition.** For \(\Psi\colon M_{n\times b}(R)\to\mathbb{C}\) the function \(\Psi^{\mathrm m}\colon M_{a\times n}(R)\to\mathbb{C}\) is \(0\) off the matrices \(x_\gamma\) and has the value \(\chi(\det\gamma)\,\Psi(y_\gamma)\) at \(x=x_\gamma\), for a chosen \(\gamma\) with \(x_\gamma=x\).

**Lemma.**

1. (*Existence.*) If \(\Psi\) vanishes off the matrices \(y_\gamma\) and \(\chi(\det h)\,\Psi(yh)=\Psi(y)\) for all \(y\) and all \(h\in\mathrm{GL}_b(R)\), then \((\Psi^{\mathrm m},\Psi)\) are matched; in particular the value of \(\Psi^{\mathrm m}\) does not depend on the choice of \(\gamma\).
2. (*Uniqueness.*) If \((\Phi,\Psi)\) and \((\Phi',\Psi)\) are matched, then \(\Phi=\Phi'\).
3. (*Translation.*) If \((\Phi,\Psi)\) are matched, \(c\in\mathbb{C}\) and \(g\in\mathrm{GL}_n(R)\), then \(x\mapsto c\,\chi(\det g)\,\Phi(xg)\) and \(y\mapsto c\,\Psi(g^{-1}y)\) are matched.

## Proof

*Key fact.* If \(x_\gamma=x_{\gamma'}\), there is \(h\in\mathrm{GL}_b(R)\) with \(y_{\gamma'}=y_\gamma h\) and \(\det\gamma'=\det\gamma\cdot\det h\). Indeed let \(z_\gamma\) be the rows \(e(b)\) of \(\gamma^{-1}\), so \(z_\gamma y_\gamma=1\) and \(x_\gamma y_\gamma=0\), and \(y_\gamma z_\gamma+(\text{columns }e(a)\text{ of }\gamma)\,x_\gamma=1\). Since \(x_\gamma y_{\gamma'}=x_{\gamma'}y_{\gamma'}=0\), the last relation gives \(y_\gamma(z_\gamma y_{\gamma'})=y_{\gamma'}\), and symmetrically \(y_{\gamma'}(z_{\gamma'}y_\gamma)=y_\gamma\). Hence \(h=z_\gamma y_{\gamma'}\) has the two-sided inverse \(z_{\gamma'}y_\gamma\). For the determinants, let \(P_\gamma\) be the matrix with rows \(z_\gamma\) and \(x_\gamma\) (that is \(\gamma^{-1}\), in the order given by \(e\)); the identity \(\det\begin{pmatrix}s\\x_\gamma\end{pmatrix}\det\gamma=\det(s\,y_\gamma)\), valid for every \(s\in M_{b\times n}(R)\) (a form of Jacobi's identity, [[?lean:New.det_fromRows_invLastRows|determinant of rows stacked on the last rows of the inverse]]), gives with \(s=z_\gamma\): \(d\det\gamma=1\) for \(d=\det P_\gamma\), and, using \(x_\gamma=x_{\gamma'}\), \(d\det\gamma'=\det(z_\gamma y_{\gamma'})=\det h\). Therefore \(\det\gamma'=\det\gamma\cdot d\det\gamma'=\det\gamma\det h\).

1. The support of \(\Psi^{\mathrm m}\) lies in the \(x_\gamma\) by definition, that of \(\Psi\) in the \(y_\gamma\) by hypothesis. The function \(\gamma\mapsto\chi(\det\gamma)\Psi(y_\gamma)\) factors through \(\gamma\mapsto x_\gamma\): with \(h\) as in the key fact, \(\chi(\det\gamma')\Psi(y_{\gamma'})=\chi(\det\gamma)\chi(\det h)\Psi(y_\gamma h)=\chi(\det\gamma)\Psi(y_\gamma)\). So \(\Psi^{\mathrm m}(x_\gamma)=\chi(\det\gamma)\Psi(y_\gamma)\) for every \(\gamma\).
2. Both vanish off the \(x_\gamma\), and at \(x_\gamma\) both equal \(\chi(\det\gamma)\Psi(y_\gamma)\).
3. For \(k,\gamma\in\mathrm{GL}_n(R)\) one has \(x_\gamma k=x_{k^{-1}\gamma}\) and \(k\,y_\gamma=y_{k\gamma}\). If \(\Phi(xg)\ne0\) then \(xg=x_\gamma\) for some \(\gamma\), so \(x=x_{g\gamma}\); if \(\Psi(g^{-1}y)\neq0\) then \(g^{-1}y=y_\gamma\), so \(y=y_{g\gamma}\). At \(\gamma\): \(c\,\chi(\det g)\Phi(x_\gamma g)=c\,\chi(\det g)\Phi(x_{g^{-1}\gamma})=c\,\chi(\det g)\chi(\det(g^{-1}\gamma))\Psi(y_{g^{-1}\gamma})=\chi(\det\gamma)\cdot c\,\Psi(g^{-1}y_\gamma)\). \(\blacksquare\)

## Remarks

The source also names the embedding \(\mathrm{GL}_b(R)\to\mathrm{GL}_n(R)\), \(g\mapsto g\oplus 1\) in the order of the basis given by \(e\); for \(a=\varnothing\) it is the identity.

## References

1. Lean: `New.Exchange.matchOf` in `src/New/Determinant/Chain/SquareLaw.lean`.
2. Lean: `New.Exchange.areMatched_matchOf` in `src/New/Determinant/Chain/SquareLaw.lean`.
3. Lean: `New.Exchange.exists_firstCols_eq_mul_of_invLastRows_eq` in `src/New/Determinant/Chain/SquareLaw.lean`.
4. Lean: `New.AreMatched.unique` in `src/New/Determinant/Chain/SquareLaw.lean`.
5. Lean: `New.AreMatched.translate` in `src/New/Determinant/Chain/SquareLaw.lean`.
6. Lean: `New.Exchange.blockInlGL` in `src/New/Determinant/Chain/SquareLaw.lean`.
