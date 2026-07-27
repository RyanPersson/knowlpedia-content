+++
id = "noncommutative-geometry/order-zero-condition"
title = "Order-zero condition for a real spectral triple"
kind = "definition"
summary = "The requirement that the represented algebra commute with the opposite-algebra action induced by the real structure."
aliases = ["commutant condition", "zero-order condition"]
domains = ["noncommutative-geometry", "operator-algebras"]
section_mode = "progressive"
+++

Let \((\mathcal A,H,D,J)\) be spectral data with antiunitary \(J\), and define the represented [[operator-algebras/opposite-algebra|opposite-algebra action]] by
\[
b^\circ=Jb^*J^{-1}.
\]
The **order-zero condition** is
\[
[a,b^\circ]=0
\qquad\text{for every }a,b\in\mathcal A.
\]
Equivalently, the left representation of \(\mathcal A\) and the right representation of \(\mathcal A^{\mathrm{op}}\) have commuting ranges, so together they give a representation of \(\mathcal A\otimes\mathcal A^{\mathrm{op}}\) on \(H\). This condition involves only the two algebra actions and \(J\); it places no restriction on \(D\). The separate first-order condition controls commutators with \(D\).

## Bimodule interpretation

Define \(a\xi b=ab^\circ\xi\). The equality
\[
(a\xi)b=a(\xi b)
\]
holds precisely because \(a\) commutes with \(b^\circ\). Thus the order-zero axiom makes \(H\) an \(\mathcal A\)-bimodule in the represented sense. The involution in \(b^\circ=Jb^*J^{-1}\) is needed for this right action to be complex-linear and multiplicative [Connes, §2](https://doi.org/10.1063/1.531241).

## Example and near miss

For the spin [[noncommutative-geometry/spectral-triple|spectral triple]] of a compact manifold, both \(a\) and \(b^\circ\) act by multiplication by functions, so the condition holds.

By contrast, if \(J\) is chosen so that \(J\mathcal AJ^{-1}\) does not lie in the [[operator-algebras/commutant|commutant]] of \(\mathcal A\), then the displayed commutator can be nonzero. The data may still satisfy all spectral-triple axioms, but they do not define the required bimodule action and hence fail order zero.

## References

1. A. Connes, “Noncommutative Geometry and Reality,” *Journal of Mathematical Physics* 36 (1995), 6194–6231. [DOI record](https://doi.org/10.1063/1.531241). Relevant: §2, especially the opposite action and order-zero relation.
2. A. Connes and M. Marcolli, *Noncommutative Geometry, Quantum Fields and Motives*, American Mathematical Society, 2008. [DOI record](https://doi.org/10.1090/coll/055). Relevant: Definition 1.124 and equations (1.471)–(1.472).
