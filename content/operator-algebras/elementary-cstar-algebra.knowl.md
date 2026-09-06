+++
id = "operator-algebras/elementary-cstar-algebra"
title = "Elementary C*-algebra"
kind = "definition"
summary = "A C*-algebra isomorphic to the compact operators on a nonzero Hilbert space."
aliases = ["algebra of compact operators", "K(H)-algebra"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/cstar-algebra", "linear-algebra/hilbert-space", "operator-algebras/star-isomorphism", "operator-algebras/compact-operator-cstar-algebra", "functional-analysis/unitary-operator"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

An **elementary \(C^*\)-algebra** is a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]] \(A\) for which there are a nonzero [[linear-algebra/hilbert-space|Hilbert space]] \(H\) and a [[operator-algebras/star-isomorphism|\(*\)-isomorphism]]
\[
A\longrightarrow K(H).
\]
Thus \(A\) is \(*\)-isomorphic to the [[operator-algebras/compact-operator-cstar-algebra|compact-operator algebra]] on \(H\). The Hilbert space is determined up to [[functional-analysis/unitary-operator|unitary isomorphism]] by \(A\). Some authors include the zero algebra by allowing \(H=\{0\}\); excluding it makes every elementary algebra nonzero and simple.

## Structure

Every elementary \(C^*\)-algebra is simple and liminal. Its nonzero [[algebra-representation-theory/irreducible-representation|irreducible representations]] are all unitarily equivalent to the defining action of \(K(H)\) on \(H\). [[operator-algebras/minimal-projection|Minimal projections]] correspond to rank-one projections, and any one of them generates the whole algebra as a [[operator-algebras/closed-two-sided-ideal|closed two-sided ideal]].

The [[operator-algebras/multiplier-algebra|multiplier algebra]] of \(K(H)\) is \(B(H)\). Consequently an infinite-dimensional elementary algebra is nonunital even though its multiplier algebra is unital.

## Examples

The matrix algebra \(M_n(\mathbb C)\) is elementary because
\[
M_n(\mathbb C)=K(\mathbb C^n).
\]
For infinite-dimensional separable \(H\), the algebra \(K(H)\) is an infinite-dimensional elementary algebra. By contrast, \(B(H)\) is not elementary when \(H\) is infinite-dimensional, and a nontrivial direct sum \(K(H_1)\oplus K(H_2)\) is not elementary because it is not simple.

## Role in type I theory

Elementary algebras are the irreducible local building blocks of type I and continuous-trace \(C^*\)-algebras. In particular, the image of every irreducible representation of a liminal algebra is elementary. Bundles whose fibers are elementary algebras provide a geometric model for continuous-trace algebras and carry the twisting measured by the Dixmier–Douady invariant.

## References

1. Kenneth R. Davidson, *C*-Algebras by Example*, Fields Institute Monographs 6, American Mathematical Society, 1996. [AMS publisher record](https://bookstore.ams.org/fim-6). Relevant: §I.4 on compact-operator algebras.
2. Iain Raeburn and Dana P. Williams, *Morita Equivalence and Continuous-Trace C*-Algebras*, Mathematical Surveys and Monographs 60, American Mathematical Society, 1998. [DOI record](https://doi.org/10.1090/surv/060). Relevant: Chapter 3 on elementary bundles and continuous trace.
