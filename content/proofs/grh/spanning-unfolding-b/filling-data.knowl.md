+++
id = "proofs/grh/spanning-unfolding-b/filling-data"
title = "Filling data"
kind = "definition"
summary = "The data of the filling theorem: a CM field, a shape, a split prime N, two level primes with chosen places, a generator of the different, a free level and Bessel systems, with size conditions in a parameter b."
aliases = ["filling datum", "data of the filling theorem"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling", "New.Filling.M", "New.Filling.ratMiddle", "New.Filling.latticeMiddle", "New.Filling.BesselCoord", "New.Filling.deltaE_ne_zero"]
lean_files = ["src/New/Spanning/Unfolding/Setup.lean"]
+++

Let \(E\) be a [[?c:CM field|CM field]] with a fixed [[?c:CM type|CM type]], that is, one complex embedding \(\Phi_v\colon E\to\mathbb{C}\) for each [[?c:Infinite place of a number field|infinite place]] \(v\) of \(E\); write \(x\mapsto\bar x\) for complex conjugation on \(E\), \(f\) for the number of infinite places, \(\mathbb{A}_f\) for the [[?c:Finite adele ring|finite adeles]] of \(E\) and \(\widehat{\mathcal{O}}\subset\mathbb{A}_f\) for the integral finite adeles. Let \(\mathfrak{s}=(\varrho,\kappa,k_0)\) be a [[?lean:New.Shape|shape]]: a number \(\varrho\ge 0\), a finite set \(\kappa\) and an element \(k_0\in\kappa\); put \(k=\lvert\kappa\rvert\), \(n=\varrho+1\) and \(r=2\varrho+k+1\).

A **filling datum** \(S\) over \(E\) of shape \(\mathfrak{s}\) consists of

* a natural number \(N\) and a finite idele \(\pi\in\mathbb{A}_f^\times\);
* two natural numbers \(p_0,p_1\), with product \(M=p_0p_1\), and for \(i=0,1\) a finite set \(C_i\) of [[?c:Finite place of a number field|finite places]] of \(E\) (the *chosen places*);
* an element \(\varpi\) of the [[algebra-fields-galois/ring-of-integers|ring of integers]] \(\mathcal{O}_E\);
* a real number \(b\);
* a subgroup \(L\) (the *source level*) of the group \(U(X_0)(\mathbb{A}_f)\) of finite adelic points of the [[?c:Unitary group of a hermitian form|unitary group]] of the standard hermitian form \(\sum_{i\in\kappa}\bar x_i y_i\) on \(X_0=E^\kappa\);
* for each infinite place \(v\) a [[?lean:New.BesselSystem|Bessel system]] \(\mathcal{B}_v\) of shape \(\mathfrak{s}\) with parameters \(b\) and \(f\), with finite index set \(I_v\);

subject to the following conditions.

**Arithmetic conditions.**

1. \(N\) is prime, \(\pi\bar\pi=N\) in \(\mathbb{A}_f\), \(\pi\in\widehat{\mathcal{O}}\), and at each finite place \(w\) either \(\pi_w\) is a unit, or \(w\) has residue cardinality \(N\) and \(\pi_{\bar w}\) is a unit.
2. \(p_0,p_1\) are primes different from \(N\), and \(b^{10}\le p_i\le b^{11}\).
3. Every place in \(C_i\) has residue cardinality \(p_i\); \(C_0\cap C_1=\varnothing\); if \(w\in C_i\) then \(\bar w\notin C_j\) for all \(i,j\); and \(\lvert C_i\rvert=f\).
4. For \(x\in\widehat{\mathcal{O}}\): \(M\mid x\) if and only if \(x\) and \(\bar x\) vanish modulo every chosen place.
5. \(\bar\varpi=-\varpi\), and \(\varpi\) generates the [[?c:Different ideal|different]] of \(E/\mathbb{Q}\). (In particular \(\varpi\ne0\).)
6. \(L\) satisfies the conditions of a [[?lean:New.IsLevel|level]], and it is *free*: for every \(g\in U(X_0)(\mathbb{A}_f)\) the group \(U(X_0)(E^+)\cap gLg^{-1}\) of rational points in the conjugate is trivial ([[?lean:New.classAut|automorphism group of a class]]).

**Size conditions.** With \(\mathrm{rd}_E\) the [[?c:Root discriminant|root discriminant]] of \(E\):

\[
\begin{gathered}
10^5\le\varrho,\qquad 2^{-\varrho}\le b^{-6},\qquad (\varrho+1)\,[E:\mathbb{Q}]\le 2^{2\varrho},\\
1000\,(2\varrho+2)^9\le k,\qquad 1000\,(2\varrho+2)\le k,\qquad k\le f,\\
\bigl(200\,f\,k\,\mathrm{rd}_E\bigr)^{1000}\le b,\qquad f\le b/1000,\qquad k\le b,\qquad \mathrm{rd}_E\le b,\qquad \varrho+1\le b,\qquad 1000\le b,\\
b^{19}\le M\le b^{23},\qquad 5\le N,\\
10^{10}n^4\le n^6,\qquad 3n^6+12\le n^7,\qquad n^7\le k .
\end{gathered}
\]

## Associated notation

* \(M=p_0p_1\) is the *level*.
* For a commutative ring \(R\), the *rational middle form* is the diagonal matrix \(T_R=\operatorname{diag}(1,\dots,1,-N)\) indexed by \(\kappa\sqcup\{z\}\), and the *lattice middle form* \(T^{\mathrm{lat}}_R\) is the [[?lean:New.latticeMiddleGram|Gram matrix of the same form in the lattice basis]], in which \(x_{k_0}\) is replaced by \(x_{k_0}/\bar\pi+z/N\).
* A *Bessel coordinate* is a tuple \(i=(i_v)_v\) with \(i_v\in I_v\) for every infinite place \(v\); the set of Bessel coordinates is \(I=\prod_v I_v\).

## Remarks

Several size conditions are redundant with one another (for instance \(1\le b\) is also a field of the Lean structure); they are stored separately because the proofs quote them separately. The conditions on \(\varrho\), \(k\), \(f\) and \(b\) are those that the data of the main argument satisfy; see [[?lean:New.Data.filling|the filling datum of admissible data]].

## References

1. Lean: `New.Filling` in `src/New/Spanning/Unfolding/Setup.lean`.
