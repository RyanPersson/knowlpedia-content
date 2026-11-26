+++
id = "proofs/grh/upper-elementary-divisors/elementary-divisors-of-edge-hecke-operator"
title = "Theorem on elementary divisors of the edge Hecke operator"
kind = "theorem"
summary = "Under large degree, an operator Y intertwined with the edge Hecke operator maps the image lattice L into itself, and the colength of Y L + p^m L in L divides p^l with l at most (3 c_div + theta m) |X| |I|."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.elementary_divisors", "New.FrobeniusCycle.elementary_divisors_length"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean"]
proof_status = "full"
+++

**Theorem (elementary divisors).** Let \(W\) be a [[algebra-commutative/local-ring|local ring]], \(O\) a [[?c:Valuation ring|valuation ring]] that is an integral domain of characteristic \(0\), and \(T\) a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] for \((N,W,O)\), \(N\ge1\), whose prime \(p\) is not a unit of \(O\). Let \(k,n,r\in\mathbb{N}\) and \(\theta\in\mathbb{R}\) be such that the degree is [[proofs/grh/upper-elementary-divisors/large-degree-conditions|large]]:
\[
0<r,\quad2r\le k,\quad0<\theta\le1,\quad n^{4}\le q,\quad\Bigl(\frac{N\,k\,\log q}{\theta}\Bigr)^{5}P^{3r}\le n .
\]
Let \(X\) and \(H\) be finite sets, \(\mathfrak{E}\) [[proofs/grh/upper-elementary-divisors/edge-hecke-operator|edge coordinates]] for \((W,O,k,r,X,H)\) (the set of parahoric cosets being finite), \(I\) a finite set with a bijection \(J\colon I\to\mathcal{E}(N,k,n)\times H\), and \(\mathbb{A}\) the edge Hecke operator on \((O^{I})^{X}\). Let \(M\) be an \(O\)-module, \(f\colon(O^{I})^{X}\to M\) an \(O\)-linear map with image \(L\), and \(Y\) an \(O\)-linear endomorphism of \(M\) with \(Y\circ f=f\circ\mathbb{A}\). Then for every \(m\in\mathbb{N}\):

1. \(Y(L)\subseteq L\);
2. there is \(l\in\mathbb{N}\) with
\[
l\le\Bigl(3\,N\,n\Bigl(\frac1{P^{2r}}+\frac{r^{2}}{kP}\Bigr)+\theta\,m\Bigr)\cdot\#X\cdot\#I
\]
such that the colength of \(Y(L)+p^{m}L\) in \(L\) divides \(p^{l}\) in the sense of [[?lean:New.ColengthDvd|colength divisibility]]: every finite family in \(L\) is carried into \(Y(L)+p^{m}L\) by a square matrix over \(O\) whose determinant divides \(p^{l}\).

(Together, 1 and 2 are the statement that \(Y\) is [[?lean:New.IsOntoUpToColength|onto on \(L\) modulo \(p^{m}\) up to colength]] \((3\Delta_T(k,n,r)+\theta m)\#X\#I\).)

**Corollary (lengths).** If moreover \(O\) is a [[?c:Discrete valuation ring|discrete valuation ring]], then with the same \(l\) the length of the \(O\)-module \(L/(Y(L)+p^{m}L)\) is at most \(l\) times the length of \(O/pO\).

## Proof

(1) \(Y(f(F))=f(\mathbb{A}F)\in L\).

(2) Since \(n<q\) ([[proofs/grh/upper-elementary-divisors/consequences-of-large-degree|consequences of large degree]]), an [[proofs/grh/upper-elementary-divisors/edge-pairing|edge pairing]] \((b,b')\) exists. Put \(V=H\times X\), \(\mathrm{Ed}=X\times\mathcal{B}\), and let \(\mathrm{Res},\mathrm{Res}'\) and \(\mathbf{A}=\mathrm{Add}_{\mathrm{Res}'}\cdot\mathrm{Res}\) be as in [[proofs/grh/upper-elementary-divisors/hecke-operator-factors-through-edges|the factorisation of the operator]], so that \(\mathbb{A}(b\cdot F)=\mathbf{A}F\) after regrouping, for all \(F\in O^{V\times\mathcal{E}}\).

The hypotheses of [[proofs/grh/upper-elementary-divisors/colength-of-factored-operator|the colength proposition]] hold: for \(\mathrm{Res}\), every pair of an origin \((h,x')\in V\) and a parahoric coset occurs as \(\bigl((h,\operatorname{or}(e)),({}^to(e))^{-1}\mathrm{Par}_r\bigr)\), because \(e\mapsto(\operatorname{or}(e),({}^to(e))^{-1}\mathrm{Par}_r)\) is injective on the finite set \(X\times\mathcal{B}\) (axiom (ii) of edge coordinates), hence surjective; for \(\mathrm{Res}'\), the pair \(((h,x),\mathsf{b})\) is \(((h,x),t(\mathsf{b})^{-1}\mathrm{Par}_r)\) by axiom (i); and \(\#(H\times X\times\mathcal{B})=\#V\cdot[\mathrm{GL}_k(W):\mathrm{Par}_r(W)]\). Hence there is \(l\le(3\Delta_T+\theta m)\#V\#\mathcal{E}=(3\Delta_T+\theta m)\#X\#I\) such that the colength of \(\operatorname{im}\mathbf{A}+p^{m}O^{V\times\mathcal{E}}\) in \(O^{V\times\mathcal{E}}\) divides \(p^{l}\).

Let \(\pi=f\circ(\text{regrouping})\colon O^{V\times\mathcal{E}}\to M\); it has image \(L\). Push the colength bound forward along \(\pi\) ([[?lean:New.ColengthDvd.map|images of colength bounds]]): \(\pi(p^{m}O^{V\times\mathcal{E}})=p^{m}L\), and \(\pi(\operatorname{im}\mathbf{A})\subseteq Y(L)\), since \(\pi(\mathbf{A}F)=f(\mathbb{A}(b\cdot F))=Y(f(b\cdot F))\). Therefore the colength of \(Y(L)+p^{m}L\) in \(L\) divides \(p^{l}\).

*Corollary.* \(L\) is finitely generated, and over a discrete valuation ring a colength bound in the above sense bounds the length of the quotient ([[?lean:New.IsOntoUpToColength.exists_relLength_le|colength and length]]). \(\square\)

## Remarks

- The constant \(\Delta_T(k,n,r)=Nn(P^{-2r}+r^{2}/(kP))\) is the [[proofs/grh/upper-elementary-divisors/sum-of-dimensions-of-deep-forms|divisor constant]]. The head of the formal source file describes the theorem as a bound for the mean exponent of the elementary divisors of the edge Hecke operator outside a small proportion \(\theta\) of them.
- Colengths in the above sense replace lengths because \(O\) need not be discrete.
- In the larger argument the theorem is applied in the area on Hecke edges to the edge Hecke operator over an inert prime.

## References

1. Lean: `New.FrobeniusCycle.elementary_divisors`, `New.FrobeniusCycle.elementary_divisors_length` in `src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean`.
2. Related work named in the heads of the Lean files of this folder (for the ingredients): Green, Polynomial representations of GL_n, 1980; Benson–Doty, Schur–Weyl duality over finite fields, 2009; Bombieri, Counting points on curves over finite fields, Sém. Bourbaki 430, 1973; Forrester–Zhang, Corank-1 projections and the randomised Horn problem, 2021.
