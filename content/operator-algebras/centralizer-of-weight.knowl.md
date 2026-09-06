+++
id = "operator-algebras/centralizer-of-weight"
title = "Centralizer of a weight"
kind = "definition"
summary = "The centralizer is the fixed-point von Neumann subalgebra of the modular automorphism group of a faithful normal semifinite weight."
aliases = ["fixed-point algebra of modular flow"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/von-neumann-algebra", "operator-algebras/normal-semifinite-faithful-weight", "operator-algebras/modular-automorphism-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\) be a [[operator-algebras/von-neumann-algebra|von Neumann algebra]]
and let \(\varphi\) be a
[[operator-algebras/normal-semifinite-faithful-weight|normal semifinite faithful weight]]. The **centralizer of \(\varphi\)** is
\[
M_\varphi=\{x\in M:\sigma_t^\varphi(x)=x\text{ for every }t\in\mathbb R\},
\]
where \(\sigma^\varphi\) is the
[[operator-algebras/modular-automorphism-group|modular automorphism group]].
It is therefore the fixed-point algebra of the modular flow. In particular,
\(M_\varphi\) is a von Neumann subalgebra of \(M\). The notation records the
chosen weight: different weights on the same algebra can have different
centralizers.

## Tracial behavior

Elements of \(M_\varphi\) commute with the weight in the following sense:
\[
\varphi(xy)=\varphi(yx)
\]
whenever \(x\in M_\varphi\) and the products lie in the finite domain on
which both sides are defined. Conversely, this commutation property
characterizes the centralizer when formulated on the standard finite ideal of
\(\varphi\). Thus the restriction of \(\varphi\) to its centralizer is a
faithful normal semifinite [[operator-algebras/tracial-weight|tracial weight]].

## Examples and consequences

If \(\varphi\) is a
[[operator-algebras/faithful-normal-semifinite-trace|faithful normal semifinite trace]], its modular group is trivial and \(M_\varphi=M\). For a
[[operator-algebras/faithful-normal-state|faithful normal state]] on
\(M_n(\mathbb C)\) of the form
\(\varphi(x)=\operatorname{Tr}(\rho x)\), with \(\rho\) positive and
invertible, the modular flow is
\(\sigma_t^\varphi(x)=\rho^{it}x\rho^{-it}\). Hence
\[
M_\varphi=\{x\in M_n(\mathbb C):x\rho=\rho x\}.
\]
Repeated eigenvalues of \(\rho\) produce matrix blocks in this centralizer;
if \(\rho\) is scalar, the centralizer is all of \(M_n(\mathbb C)\).

## Conventions and scope

The centralizer is not the center of \(M\): its elements need only be fixed by
the modular flow, and need not commute with every element of \(M\). For a
nonfaithful [[operator-algebras/normal-weight|normal weight]], one commonly
passes to its support corner before forming modular data. The faithfulness
hypothesis in the core avoids this
support-corner convention.

## References

1. Masamichi Takesaki, *Theory of Operator Algebras II*, Springer, 2003. [DOI record](https://doi.org/10.1007/978-3-662-10451-4). Relevant: Chapter VIII, §2 on the centralizer of a weight.
