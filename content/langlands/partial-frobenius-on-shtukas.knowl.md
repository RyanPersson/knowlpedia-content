+++
id = "langlands/partial-frobenius-on-shtukas"
title = "Partial Frobenius on shtukas"
kind = "knowl"
summary = "The operation that applies Frobenius to selected shtuka legs and cyclically rotates the corresponding modification."
aliases = ["partial Frobenius morphism", "partial Frobenii", "Frobenius on selected shtuka legs"]
domains = ["langlands", "algebraic-geometry-foundations", "number-theory"]
prerequisites = ["langlands/g-shtuka", "algebra-fields-galois/frobenius-endomorphism"]
dependency_review_count = 1
section_mode = "progressive"
+++

For a multiple-leg [[langlands/g-shtuka|\(G\)-shtuka]] with legs indexed by
\(I\), a **partial Frobenius** associated to a subset \(J\subset I\) applies
the \(q\)-power
[[algebra-fields-galois/frobenius-endomorphism|Frobenius endomorphism]] to
the leg coordinates in \(J\) while leaving the
other legs fixed, together with the corresponding rotation of the
Frobenius-modification chain.

On the base \(X^I\), the map is

\[
{\rm Frob}_J((x_i)_{i\in I})=(x_i')_{i\in I},
\qquad
x_i'=
\begin{cases}
{\rm Frob}_X(x_i),&i\in J,\\
x_i,&i\notin J.
\end{cases}
\]

## Modification-chain description

For an ordered partition \(I=I_1\sqcup\cdots\sqcup I_k\), a shtuka is a
chain from \(\mathcal G_0\) to
\({}^\tau\mathcal G_0\). Partial Frobenius for the first block moves that
block to the end, replaces \(\mathcal G_0\) by the next bundle in the chain,
and applies Frobenius to the moved legs. This gives a morphism between the
appropriately ordered shtuka stacks.

## Relations

Partial Frobenius operators for disjoint individual legs commute. Their
product over all legs is the total Frobenius action. On the inductive system
of truncated shtuka cohomology, an operator may enlarge the
[[algebraic-geometry-foundations/harder-narasimhan-filtration|Harder–Narasimhan
bound]]; it is therefore naturally a map in that inductive
system rather than always an endomorphism of one finite-type truncation.

## From Frobenius to Galois

[[langlands/drinfeld-lemma|Drinfeld's lemma]] turns a
[[algebraic-geometry-foundations/lisse-ell-adic-sheaf|lisse
\(\ell\)-adic sheaf]] over a power of a curve equipped with commuting
partial Frobenius structures into a representation of a product of
[[topology/fundamental-group|fundamental groups]]. This is the source of the
independent Galois actions
\((\gamma_i)_{i\in I}\) in an
[[langlands/excursion-operator|excursion operator]].

## References

1. Vincent Lafforgue, “Chtoucas pour les groupes réductifs et
   paramétrisation de Langlands globale,” §§0.2–0.4 and Chapter 3.
   [arXiv](https://arxiv.org/abs/1209.5352).
2. Cong Xue, “Smoothness of cohomology sheaves of stacks of shtukas,” 2020.
   [arXiv](https://arxiv.org/abs/2012.12833).
