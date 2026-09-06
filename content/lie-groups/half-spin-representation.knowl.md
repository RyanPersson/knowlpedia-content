+++
id = "lie-groups/half-spin-representation"
title = "Half-spin representation"
kind = "definition"
summary = "Either irreducible chiral summand of the complex spin representation in even dimension."
aliases = ["half-spin module", "chiral spin representation", "positive half-spin representation", "negative half-spin representation"]
domains = ["lie-groups", "representation-theory", "differential-geometry"]
prerequisites = ["linear-algebra/quadratic-form", "differential-geometry/clifford-algebra", "differential-geometry/chirality-operator", "differential-geometry/spinor-module", "differential-geometry/clifford-module"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(V\) be an oriented complex [[linear-algebra/quadratic-form|quadratic space]] of even dimension \(2m\), and let \(\Delta\) be an irreducible module for its [[differential-geometry/clifford-algebra|complex Clifford algebra]]. The [[differential-geometry/chirality-operator|chirality operator]] decomposes the [[differential-geometry/spinor-module|spinor module]] as
\[
\Delta=\Delta^+\oplus\Delta^-.
\]
The two eigenspaces \(\Delta^+\) and \(\Delta^-\) are invariant under \(\operatorname{Spin}(V)\) and carry the two **half-spin representations**. Each has complex dimension \(2^{m-1}\), and [[differential-geometry/clifford-module|Clifford multiplication]] by a vector interchanges them.

## Highest weights

For \(m\geq4\), the complex [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak{so}_{2m}(\mathbb C)\) has Dynkin type \(D_m\). With a standard labeling of its two spin nodes, the half-spin modules have [[lie-groups/highest-weight|highest weights]]
\[
\omega_{m-1}\quad\text{and}\quad\omega_m.
\]
They are therefore the two spin [[lie-groups/fundamental-representation|fundamental representations]]. Which weight is called \(+\) and which is called \(-\) depends on the orientation, the labeling of the \(D_m\) diagram, and the normalization of the Clifford volume element.

The central element \(-1\in\operatorname{Spin}(2m)\) acts nontrivially on spinors. Consequently, half-spin representations are genuine representations of the [[lie-groups/spin-group|spin group]] and do not descend to \(SO(2m)\).

## Low-dimensional examples

The accidental isomorphism \(\operatorname{Spin}(4)\cong SU(2)\times SU(2)\) identifies \(\Delta^+\) and \(\Delta^-\) with the defining two-dimensional representations of the two respective factors. Under \(\operatorname{Spin}(6)\cong SU(4)\), the two half-spin representations become the defining four-dimensional representation and its dual. In dimension eight, the two half-spin representations and the [[lie-groups/defining-representation-of-a-classical-lie-algebra|vector representation]] all have dimension eight and participate in [[lie-groups/spin8-triality|triality]].

## Chirality and real forms

The complex decomposition into \(\Delta^+\) and \(\Delta^-\) is intrinsic only after the relevant orientation and chirality conventions are fixed; reversing orientation exchanges the labels. For a real group \(\operatorname{Spin}(p,q)\), whether either complex half-spin module admits an invariant real or quaternionic structure depends on \(p-q\) modulo eight. A statement about “real half-spinors” must therefore specify the signature.

## References

1. H. Blaine Lawson Jr. and Marie-Louise Michelsohn, *Spin Geometry*, Princeton University Press, 1989, Chapter I, §§4–5. [Publisher record](https://doi.org/10.1515/9781400883912).
2. William Fulton and Joe Harris, *Representation Theory: A First Course*, Springer, 1991, §20. [Publisher record](https://doi.org/10.1007/978-1-4612-0979-9).
