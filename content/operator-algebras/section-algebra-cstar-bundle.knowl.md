+++
id = "operator-algebras/section-algebra-cstar-bundle"
title = "Section algebra of a C*-bundle"
kind = "definition"
summary = "The C*-algebra of continuous bundle sections that vanish at infinity."
aliases = ["C_0-sections of a C*-bundle", "Gamma_0(X,A)"]
domains = ["operator-algebras", "topology"]
section_mode = "progressive"
+++

Let \(p\colon\mathcal A\to X\) be an [[operator-algebras/upper-semicontinuous-cstar-bundle|upper-semicontinuous \(C^*\)-bundle]] over a [[topology/locally-compact-space|locally compact]] [[topology/hausdorff-space|Hausdorff space]]. Its **section algebra** is
\[
\Gamma_0(X,\mathcal A)
=\{s\colon X\to\mathcal A:p\circ s=\operatorname{id}_X,\ s
\text{ is continuous, and }\lVert s(x)\rVert\to0\text{ at infinity}\}.
\]
Pointwise algebraic operations, pointwise involution, and the norm \(\lVert s\rVert=\sup_x\lVert s(x)\rVert\) make this a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]].
Completeness follows from the bundle axioms and the uniform norm on sections.

## Vanishing at infinity

The norm function of a section vanishes at infinity when, for every \(\varepsilon>0\), the set
\[
\{x\in X:\lVert s(x)\rVert\geq\varepsilon\}
\]
is compact. Compactly supported continuous sections therefore belong to \(\Gamma_0(X,\mathcal A)\). The subscript \(0\) records this condition; bounded continuous sections need not vanish at infinity.

## The C_0(X)-action

For \(f\in C_0(X)\) and \(s\in\Gamma_0(X,\mathcal A)\), define
\[
(fs)(x)=f(x)s(x).
\]
This gives a central nondegenerate action of \(C_0(X)\), so the section algebra is a [[operator-algebras/c0-x-algebra|\(C_0(X)\)-algebra]]. Evaluation at \(x\) maps a section to \(s(x)\) and identifies the corresponding quotient fiber with \(\mathcal A_x\).

## Examples and reconstruction

For the trivial bundle \(X\times B\to X\), one obtains
\[
\Gamma_0(X,X\times B)\cong C_0(X,B).
\]
For a general upper-semicontinuous bundle, the section algebra retains enough information to reconstruct both its fibers and total-space topology. This is the bundle-to-algebra direction of the [[operator-algebras/c0-x-algebra-bundle-equivalence|\(C_0(X)\)-algebra bundle correspondence]].

## References

1. May Nilsen, “C*-Bundles and \(C_0(X)\)-Algebras,” *Indiana University Mathematics Journal* 45 (1996), 463–477. [DOI record](https://doi.org/10.1512/iumj.1996.45.1086). Relevant: section algebras and the sectional representation theorem.
2. Dana P. Williams, *Crossed Products of C*-Algebras*, Mathematical Surveys and Monographs 134, American Mathematical Society, 2007. [DOI record](https://doi.org/10.1090/surv/134). Relevant: Appendix C on sections of upper-semicontinuous bundles.
