+++
id = "proofs/grh/determinant-chain/gram-form-of-a-full-chain"
title = "Gram form of a full chain in a triangle"
kind = "theorem"
summary = "The Gram form of the weighted chain of length m - i of row i is that of the product of the Gram operators of the first arrows, times a ratio of weights and a constant whose modulus is the product of the moduli of all squares crossed."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Exchange.IsTriangle.exists_inner_weightedChain_eq", "New.Exchange.IsTriangle.inner_weightedChain_succ"]
lean_files = ["src/New/Determinant/Chain/TriangleNorms.lean"]
proof_status = "full"
+++

**Theorem.** Let \((F,V,a,d,w,j)\) be a [[proofs/grh/determinant-chain/triangle-of-arrows|triangle of size \(m\)]] with all weights \(w_t(n)\neq0\) that [[proofs/grh/determinant-chain/square-moduli|has square moduli \(L\)]] for a relation \(\mathcal M\). Let \(U\) be a complex vector space, \(s\colon U\to V\) a map, \(S_{t,i}\) (\(t\in I\), \(i\ge0\)) linear endomorphisms of \(U\), and \(C_i\colon I\to\mathbb{C}\) functions with \(\mathcal M(C_i,1)\), such that for all \(i<m\), \(t\in I\), \(x\in V\), \(y\in U\)
\[
w_t(0)\,\big\langle a_{t,i,0}\,j_ix,\ a_{t,i,0}\,j_i\,s(y)\big\rangle=C_i(t)\,\big\langle x,\ s(S_{t,i}\,y)\big\rangle .
\]
Then for all \(i,n\) with \(i+n=m\) there is \(\kappa\colon I\to\mathbb{C}\) with
\[
\mathcal M\Big(\kappa,\ \prod_{i<r\le m}\ \prod_{r<k\le m}L_{r,k}\Big)
\]
and, for all \(t\in I\), \(x\in V\), \(y\in U\),
\[
\big\langle X_{t,i,n}\,j_ix,\ X_{t,i,n}\,j_i\,s(y)\big\rangle=\kappa(t)\,\frac{w_t(0)\,w_t(1)^n}{w_t(n)}\,\big\langle x,\ s\big(S_{t,i}S_{t,i+1}\cdots S_{t,i+n-1}\,y\big)\big\rangle .
\]

## Proof

*One step.* Let \(i+n<m\), and let \(\beta,\kappa'\) satisfy \(\mathrm{CC}(i,n,\beta)\) and \(\mathrm{CA}(i,n,\kappa')\) of [[proofs/grh/determinant-chain/chains-commute-and-adjoint-in-a-triangle|chains and descent]]. Let \(x,z\in V\) and \(x'\in V\) with \(j_{i+1}x'=d_{t,i,0}a_{t,i,0}j_ix\). We claim
\[
\langle X_{t,i,n+1}j_ix,\ X_{t,i,n+1}j_iz\rangle=\kappa'(t)\beta(t)\,\frac{w(0)w(1)w(n)}{w(n+1)}\ \langle X_{t,i+1,n}j_{i+1}x',\ X_{t,i+1,n}j_{i+1}z\rangle .
\]
If \(V=0\) both sides vanish. Otherwise \(\beta(t)\neq0\) by [[proofs/grh/determinant-chain/weighted-chains-are-injective|nonvanishing of the constants]]. Put \(X=X_{t,i,n+1}j_ix\), \(X'=X_{t,i+1,n}j_{i+1}x'\), \(Y=X_{t,i+1,n}j_{i+1}z\). By \(\mathrm{CC}\), \(X'=\frac{w(n+1)}{w(1)w(0)\overline\beta}\,d_{t,i,n}X\), hence (conjugate-linearity in the first variable) \(\langle X',Y\rangle=\frac{w(n+1)}{w(1)w(0)\beta}\langle d_{t,i,n}X,Y\rangle\). By \(\mathrm{CA}\) with \(z:=X\),
\[
\langle X,\ X_{t,i,n+1}j_iz\rangle=w(n)\,\langle X,\ a_{t,i,n}X_{t,i,n}j_iz\rangle=w(n)\,\kappa'\,\langle d_{t,i,n}X,\ Y\rangle ,
\]
and substituting \(\langle d_{t,i,n}X,Y\rangle=\frac{w(1)w(0)\beta}{w(n+1)}\langle X',Y\rangle\) gives the claim.

*Induction on \(n\), descending in \(i=m-n\).* For \(n=0\), \(i=m\): \(X_{t,m,0}=\mathrm{id}\), \(j_m\) is an isometry, the product of operators and the product of moduli are empty, and \(\kappa=1\) works since \(w(0)\cdot w(1)^0/w(0)=1\).

For \(n+1\), \(i+n+1=m\): the induction hypothesis for row \(i+1\) gives \(\kappa\) of modulus \(\prod_{i+1<r\le m}\prod_{r<k\le m}L_{r,k}\). The cited lemma gives \(\beta\) with \(\mathrm{CC}(i,n,\beta)\) of modulus \(\prod_{i+1<k\le m}L_{i+1,k}\) (note \(i+1+n=m\)) and \(\kappa'\) of modulus \(1\) with \(\mathrm{CA}(i,n,\kappa')\). Put \(\kappa_{\mathrm{new}}=\kappa'\beta\kappa C_i\); its modulus is \(\prod_{i<r\le m}\prod_{r<k\le m}L_{r,k}\), the factor \(r=i+1\) coming from \(\beta\). Fix \(t,x,y\), let \(T=S_{t,i+1}\cdots S_{t,i+n}\), and choose \(x'\) with \(j_{i+1}x'=d\,a\,j_ix\) (condition 3 of a triangle). By the step with \(z=s(y)\) and the induction hypothesis at \((x',y)\),
\[
\langle X_{t,i,n+1}j_ix,\ X_{t,i,n+1}j_is(y)\rangle=\kappa'\beta\,\frac{w(0)w(1)w(n)}{w(n+1)}\cdot\kappa\,\frac{w(0)w(1)^n}{w(n)}\ \langle x',\ s(Ty)\rangle
=\kappa'\beta\kappa\,\frac{w(0)w(1)^{n+1}}{w(n+1)}\cdot w(0)\langle x',s(Ty)\rangle .
\]
Finally, since \(j_{i+1}\) is an isometry and by condition 2 of a triangle (with \(z=a\,j_ix\)) and the hypothesis on \(S\),
\[
w(0)\langle x',s(Ty)\rangle=w(0)\langle d\,a\,j_ix,\ j_{i+1}s(Ty)\rangle=w(0)\langle a_{t,i,0}j_ix,\ a_{t,i,0}j_i\,s(Ty)\rangle=C_i(t)\,\langle x,\ s(S_{t,i}Ty)\rangle .
\]
This is the claim with \(\kappa_{\mathrm{new}}\). \(\blacksquare\)

## References

1. Lean: `New.Exchange.IsTriangle.exists_inner_weightedChain_eq` in `src/New/Determinant/Chain/TriangleNorms.lean`.
2. Lean: `New.Exchange.IsTriangle.inner_weightedChain_succ` in `src/New/Determinant/Chain/TriangleNorms.lean`.
