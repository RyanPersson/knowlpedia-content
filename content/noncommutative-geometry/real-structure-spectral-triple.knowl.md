+++
id = "noncommutative-geometry/real-structure-spectral-triple"
title = "Real structure on a spectral triple"
kind = "definition"
summary = "An antiunitary operator encoding charge conjugation, KO-dimensional signs, and the opposite-algebra action of a spectral triple."
aliases = ["charge conjugation", "real spectral data", "antiunitary J"]
domains = ["noncommutative-geometry", "operator-algebras"]
section_mode = "progressive"
+++

Let \((\mathcal A,H,D)\) be a [[noncommutative-geometry/spectral-triple|spectral triple]]. A **real structure of KO-dimension \(n\)** is an antiunitary \(J:H\to H\) for which
\[
J^2=\varepsilon,\qquad JD=\varepsilon' DJ,
\]
and, in the even case with grading \(\Gamma\),
\[
J\Gamma=\varepsilon''\Gamma J.
\]
The signs \(\varepsilon,\varepsilon',\varepsilon''\in\{1,-1\}\) are prescribed by \(n\bmod 8\). The operator also gives a complex-linear representation of the [[operator-algebras/opposite-algebra|opposite algebra]] by
\[
b^{\circ}=Jb^*J^{-1}.
\]
To obtain the standard real spectral-triple axioms, this right action must satisfy the [[noncommutative-geometry/order-zero-condition|order-zero]] and [[noncommutative-geometry/first-order-condition|first-order conditions]]. Those conditions are additional compatibility requirements, not consequences of antiunitarity or of the sign relations.

## Meaning of the data

The antiunitary \(J\) abstracts charge conjugation on spinors. The formula for \(b^\circ\) turns the [[linear-algebra/hilbert-space|Hilbert space]] into a candidate \(\mathcal A\)-bimodule: the represented algebra acts from the left and its opposite algebra acts from the right. The KO-sign relations record the real Clifford-module behavior of \(J\), \(D\), and the grading.

Multiplying \(J\) by a complex scalar of modulus one does not change \(J^2\), because \(J\) is antilinear.

## Canonical example and scope

For the canonical spin spectral triple of a closed Riemannian spin manifold, charge conjugation on the complex [[differential-geometry/spinor-bundle|spinor bundle]] supplies \(J\). Its commutation signs depend only on the dimension modulo eight. The opposite action of a function is again multiplication by that function, so it commutes with the left action.

**Warning.** A real structure is not merely an antilinear involution: \(J^2\) may equal \(-1\), and the relations with \(D\) and \(\Gamma\) are essential. Lorentzian and twisted real structures use modified axioms.

## References

1. A. Connes, “Noncommutative Geometry and Reality,” *Journal of Mathematical Physics* 36 (1995), 6194–6231. [DOI record](https://doi.org/10.1063/1.531241). Relevant: §2 on the real structure, opposite action, and sign relations.
2. A. Connes and M. Marcolli, *Noncommutative Geometry, Quantum Fields and Motives*, American Mathematical Society, 2008. [DOI record](https://doi.org/10.1090/coll/055). Relevant: Definition 1.124 and equations (1.470)–(1.473).
