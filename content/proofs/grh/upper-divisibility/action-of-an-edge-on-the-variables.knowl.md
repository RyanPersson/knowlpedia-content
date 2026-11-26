+++
id = "proofs/grh/upper-divisibility/action-of-an-edge-on-the-variables"
title = "Action of the rational part of an edge on the weight space"
kind = "lemma"
summary = "At the a-places inducing a marked prime or its conjugate, the rational part of an edge acts on monomials by letter matrices and powers of p; elsewhere it acts integrally."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Columns.kroneckerPi_symPowMatrix_eq_letterRep", "New.Columns.smul_transpose_map_eq_letterMatrix", "New.Columns.exists_weylIndex_equiv", "New.Columns.exists_schur_eq_symPowMatrix", "New.Columns.exists_schur_eq_map", "New.Columns.weightRep_column_apply"]
lean_files = ["src/New/UpperBound/Divisibility/HeckeEdges.lean"]
proof_status = "outline"
+++

Let \(W\) be the valuation ring in \(E\) of a finite place \(\mathfrak l\) at which the prime \(p\) is a uniformiser, \(O\subset\mathbb{C}\) a valuation ring, and \(T\) a [[?lean:New.FrobeniusCycle|Frobenius cycle]] on \(W\) with values in \(O\) and prime \(p\): ring maps \(\iota_s\colon W\to O\) for letters \(s\in\mathbb{Z}/N\), alternately even and odd, with \(\iota_{s+1}\equiv\iota_s^{P}\bmod p\), \(P=p^{\text{frobExp}}\), the residue field of \(W\) having \(P^{N}\) elements. For \(g\in\mathrm{GL}_k(W)\) the **letter matrix** of \(g\) at \(s\) is \(\iota_s(g)\) for even \(s\) and \(\iota_s(g)^{-T}\) for odd \(s\). A variable \((i,s)\), \(i<k\), is **deep** if \(r\le i\) and \(s\) is even, or \(i<r\) and \(s\) is odd. Let \(d=\operatorname{diag}(p,\dots,p,1,\dots,1)\) with \(r\) entries \(p\), in a numbering \(q\) of the coordinates.

**Lemma.**

1. Let \(\varphi_s\colon E\to\mathbb{C}\) be embeddings with \(\iota_s=\varphi_s|_W\) for even \(s\) and \(\iota_s=(\varphi_s\circ\mathrm{conj})|_W\) for odd \(s\). Let \(\gamma\) be a rational unitary matrix (\(\gamma^{-1}=\gamma^{*}\)) with \(\gamma^{-1}=g\,d^{-1}\beta\), \(g,\beta\in\mathrm{GL}_k(W)\). Then for each \(s\)
\[
\epsilon_s\cdot\bigl((\varphi_s\circ\mathrm{conj})(\gamma)\bigr)^{T}=L_s(g)\cdot\operatorname{diag}\bigl(p^{[(i,s)\ \text{deep}]}\bigr)_{i}\cdot L_s(\beta),\qquad\epsilon_s=\begin{cases}p&s\text{ even}\\1&s\text{ odd,}\end{cases}
\]
where \(L_s\) is the letter matrix. Consequently, for \(a\ge0\), the tensor product over \(s\) of the \(a\)-th symmetric powers of the left sides equals \(\mathrm{Let}_a(g)\cdot\mathrm{Dep}\cdot\mathrm{Let}_a(\beta)\), where \(\mathrm{Let}_a\) is the [[?lean:New.FrobeniusCycle.letterRep|letter representation]] on the monomials of degree \(a\) in each letter and \(\mathrm{Dep}\) is the [[?lean:New.FrobeniusCycle.depthPower|diagonal matrix]] with entry \(p^{\text{(total degree in the deep variables)}}\) at a monomial.

2. (**Splitting of the weight space.**) Let \(D\) be admissible data and \(Q\) a set of a-places, numbered by \(t\colon\mathbb{Z}/N\simeq Q\). In the weight of \(X_0\) the diagram at an a-place is one row of length \(a\), and at the other places has no column of height below \(k\) except of height \(k\). There is a bijection \(J\) from the basis of the weight space to pairs (a family of monomials of degree \(a\) in \(k\) variables, one for each \(s\); a basis index for the places outside \(Q\)) such that for all scalars \(c_s\) and all families \(z\) of matrices
\[
\Bigl(\prod_sc_s\Bigr)^{a}\,\mathrm{Schur}(z)_{ij}=\mathrm{Schur}_{\notin Q}(z)_{J(i)_2,J(j)_2}\cdot\Bigl(\bigotimes_s\operatorname{Sym}^{a}\bigl(c_s\,z_{t(s)}^{T}\bigr)\Bigr)_{J(j)_1,J(i)_1}.
\]
3. (**Integrality off \(Q\).**) Let \(S\) be a set of places and \(\gamma\in\mathrm{GL}_{k}(E)\) integral, with integral inverse, at \(\overline{w_\tau}\) for every a-place \(\tau\in S\) (\(w_\tau\) the prime induced by \(\tau\) at \(\iota\colon\mathbb{C}\to\mathbb{C}_p\)). Then the Schur matrix at the places of \(S\) of the family \(((\tau\circ\mathrm{conj})(\gamma))_{\tau\in S}\) is an invertible matrix over the ring \(\{z\in\mathbb{C}:\lvert\iota z\rvert_p\le1\}\).

## Proof

(1) Let \(\psi=\varphi_s\) for even \(s\) and \(\varphi_s\circ\mathrm{conj}\) for odd \(s\), so \(\psi|_W=\iota_s\). *Odd \(s\):* \(\gamma=\beta^{-1}dg^{-1}\), and \((\varphi_s\circ\mathrm{conj})(\gamma)^{T}=\psi(g)^{-T}\,\psi(d)\,\psi(\beta)^{-T}=L_s(g)\,d\,L_s(\beta)\); \(d\) has \(p\) at \(i<r\), the deep variables for odd \(s\). *Even \(s\):* as \(\gamma\) is unitary, \((\mathrm{conj}\,\gamma)^{T}=\gamma^{-1}=gd^{-1}\beta\), so \(p\,\varphi_s(\gamma^{-1})=\iota_s(g)\,(p\,d^{-1})\,\iota_s(\beta)\), and \(pd^{-1}\) has \(p\) at \(i\ge r\). Symmetric powers and tensor products are multiplicative, and the symmetric power of a diagonal matrix is diagonal with the monomials in its entries.

(2) For a diagram with one row of length \(b\) the Weyl module is the \(b\)-th symmetric power and the Schur matrix of \(z\) is, in a suitable matching of bases, the transpose of \(\operatorname{Sym}^{b}(z^{T})\) ([[?lean:New.exists_equiv_schur_one_row_eq_symPowMatrix|`exists_equiv_schur_one_row_eq_symPowMatrix`]], quoted); the scalar \(c^{b}\) is absorbed by homogeneity. The Schur matrix of a family is the product over the places of the Schur matrices; split the places into \(Q\) and the rest.

(3) At an a-place \(\tau\in S\) the embedding \(\tau\circ\mathrm{conj}\) induces the prime \(\overline{w_\tau}\), hence maps its valuation ring into the integral complex numbers; so \((\tau\circ\mathrm{conj})(\gamma)\) is an invertible integral matrix. At the other places of \(S\), the relevant part of the weight (heights below \(k\), read as a one-row diagram of length \(0\) in this bookkeeping) makes the Schur matrix independent of its argument, and one may replace it by \(1\). The Schur matrix of invertible integral matrices is invertible and integral, since the Weyl module is a representation defined over \(\mathbb{Z}\). \(\blacksquare\)

*Status.* The identification of a one-row Schur matrix with a symmetric power and the product formula for Schur matrices are quoted. In (3), the treatment of the places that are not a-places follows the Lean proof (`exists_schur_eq_symPowMatrix` with \(b=0\)) and relies on the Lean convention that the Schur matrix reads only the columns of height below the rank; I did not verify this convention in the defining file.

## References

1. Lean: the declarations listed in the front matter, in `src/New/UpperBound/Divisibility/HeckeEdges.lean`.
