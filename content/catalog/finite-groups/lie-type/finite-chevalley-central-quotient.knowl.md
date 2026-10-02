+++
id = "catalog/finite-groups/lie-type/finite-chevalley-central-quotient"
title = "Finite Chevalley central quotient"
kind = "definition"
summary = "The finite fixed points of a split simply connected group, modulo their finite center."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["lie-groups/root-system", "algebraic-geometry-foundations/simply-connected-semisimple-group", "algebraic-geometry-foundations/chevalley-lattice-integral-model", "algebra-fields-galois/frobenius-endomorphism", "algebra-groups/center-of-group", "algebra-groups/finite-group", "algebra-groups/quotient-group"]
dependency_heuristic = "finite-lie-type-core-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

For a reduced irreducible [[lie-groups/root-system|root system]] \(\Phi\), prime \(p\), and \(q=p^f\) with \(f\geq1\), the **finite Chevalley central quotient** is
\[
 G_\Phi(q)=\mathbf G_{\Phi,\mathrm{sc}}(\overline{\mathbb F}_p)^{F_q}/Z\bigl(\mathbf G_{\Phi,\mathrm{sc}}(\overline{\mathbb F}_p)^{F_q}\bigr).
\]
Here \(\mathbf G_{\Phi,\mathrm{sc}}\) is the split [[algebraic-geometry-foundations/simply-connected-semisimple-group|simply connected semisimple algebraic group]] with root system \(\Phi\), constructed from its [[algebraic-geometry-foundations/chevalley-lattice-integral-model|Chevalley integral model]]. The [[algebra-fields-galois/frobenius-endomorphism|Frobenius map]] \(F_q\) raises coordinates to their \(q\)-th powers; superscript \(F_q\) means its fixed points. The denominator is the [[algebra-groups/center-of-group|center]] of that [[algebra-groups/finite-group|finite group]]. Multiplication is multiplication of cosets, making this a [[algebra-groups/quotient-group|quotient group]].

## Why the finite center matters

Taking fixed points of the adjoint [[algebraic-geometry-foundations/algebraic-group|algebraic group]] can produce a larger finite group than this quotient. For example, this convention gives \(\operatorname{PSL}_n(q)\), whereas adjoint type \(A_{n-1}\) has fixed points \(\operatorname{PGL}_n(q)\). They need not coincide.

This is a construction, not an unconditional simplicity assertion. The small cases \(A_1(2),A_1(3),B_2(2),G_2(2)\) require separate treatment.

## References

1. [Robert Steinberg, Lectures on Chevalley Groups (Yale, 1967)](https://www.math.utah.edu/~ptrapa/math-library/steinberg/steinberg-yale-notes.pdf), §3 construction; §4 Theorem 5, PDF pp. 52–54; §9 Theorems 24–25, PDF pp. 136–138.
