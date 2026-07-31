+++
id = "operator-algebras/quasi-equivalent-representations"
title = "Quasi-equivalent representations"
kind = "definition"
summary = "Representations whose generated von Neumann algebras are normally isomorphic by an isomorphism agreeing on the represented C-star algebra."
aliases = ["quasi-equivalence of representations", "normally equivalent representations"]
domains = ["operator-algebras", "algebra-representation-theory"]
section_mode = "progressive"
+++

Two [[operator-algebras/cstar-representation|representations]]
\(\pi_i:A\to\mathcal B(H_i)\) of the same \(C^*\)-algebra are
**quasi-equivalent** if the assignment
\[
\pi_1(a)\longmapsto\pi_2(a)
\]
extends to a \(*\)-isomorphism
\[
\Phi:\pi_1(A)''\longrightarrow\pi_2(A)''
\]
between their
[[operator-algebras/von-neumann-algebra-generated-by-representation|generated
von Neumann algebras]], and \(\Phi\) is a
[[operator-algebras/normal-star-homomorphism|normal \(*\)-homomorphism]] with
normal inverse. In particular, the two representations must have the same
kernel. Normality is essential: it requires the isomorphism to preserve the
weak-limit structure supplied by the two concrete representations, not only
their norm-closed images.

## Relation to unitary equivalence

[[operator-algebras/unitary-equivalence-cstar-representations|Unitary
equivalence]] implies quasi-equivalence by
\(\Phi(x)=UxU^*\). The converse fails because quasi-equivalence forgets
Hilbert-space multiplicity. For example, a nonzero representation \(\pi\)
and its amplification \(a\mapsto\pi(a)\otimes I_K\) are quasi-equivalent:
\(x\mapsto x\otimes I_K\) normally identifies the generated von Neumann
algebras. They need not be unitarily equivalent when the multiplicities
differ.

## Normal representation content

Quasi-equivalence says that the two weak closures carry the same normal
representation theory while retaining the distinguished copy of \(A\). It
preserves factoriality and the type of the [[operator-algebras/von-neumann-algebra-generated-by-representation|generated von Neumann algebra]].
For [[operator-algebras/nondegenerate-star-homomorphism|nondegenerate representations]] it is also characterized by equality of
the sets of [[operator-algebras/positive-linear-functional|positive functionals]] on \(A\) that are normal relative to the
representations [Takesaki, Chapter III, §2].

## Conventions and near misses

**Warning.** Isomorphic von Neumann algebras are not enough: the isomorphism
must send \(\pi_1(a)\) to \(\pi_2(a)\) for every \(a\in A\). Equality of
kernels is also insufficient because it compares only the norm-closed
quotient \(A/\ker\pi_i\), not which functionals and limits become normal in
the two weak closures.

## References

1. Jacques Dixmier, *C*-Algebras*, North-Holland, 1977. [Publisher record](https://www.sciencedirect.com/bookseries/north-holland-mathematical-library/vol/15/suppl/C). Relevant: Chapter 3 on equivalence and quasi-equivalence of representations.
2. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 2002. [Publisher record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter III, §2 on normal extensions and quasi-equivalence.
