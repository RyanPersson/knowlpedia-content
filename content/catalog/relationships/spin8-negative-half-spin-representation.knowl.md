+++
id = "catalog/relationships/spin8-negative-half-spin-representation"
title = "The negative half-spin representation of Spin(8)"
kind = "knowl"
summary = "One of the two inequivalent eight-dimensional real half-spin representations."
aliases = ["The negative half-spin representation of Spin(8)"]
domains = ["catalog", "lie-groups", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["differential-geometry/clifford-algebra", "lie-groups/half-spin-representation"]
dependency_heuristic = "catalog-semantic-author-review-v1"
dependency_review_count = 1
+++

The **negative half-spin representation** \(8_-=\Delta^-\) of compact \(\operatorname{Spin}(8)\) is its action on one of the two irreducible real modules of the even [[differential-geometry/clifford-algebra|Clifford algebra]]
\[
\mathrm{Cl}^{0}_{0,8}\cong M_8(\mathbb R)\oplus M_8(\mathbb R).
\]
Here Clifford generators satisfy \(v^2=-\lVert v\rVert^2\). For an oriented orthonormal basis, put \(\omega=e_1\cdots e_8\). The negative module is the simple module on which \(\omega\) acts by \(-1\). The module has real dimension \(8\), and restriction to \(\operatorname{Spin}(8)\) is irreducible.

## Central kernel

The action has image \(SO(8)\) after choosing an oriented orthonormal basis. Its kernel is an order-two central subgroup different from both the kernel of the [[catalog/relationships/spin8-vector-representation|vector representation]] and that of the [[catalog/relationships/spin8-positive-half-spin-representation|positive half-spin representation]]. In particular, it does not descend through the fixed vector quotient \(\operatorname{Spin}(8)\to SO(8)\).

## Chirality convention

The labels \(+\) and \(-\) depend on orientation; reversing orientation exchanges them. This catalogue keeps both objects. [[lie-groups/spin8-triality|Triality]] changes the group action when it exchanges them.

## References

1. John C. Baez, “The Octonions,” §2.4, Table 4 and restriction from the even Clifford algebra. [Checked section](https://math.ucr.edu/home/baez/octonions/node7.html).
2. Schaposnik and Schulz, “Triality for Homogeneous Polynomials,” §2.2, p. 5. [Paper](https://sigma-journal.com/2021/079/sigma21-079.pdf).
