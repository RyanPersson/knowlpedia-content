+++
id = "operator-algebras/unitization"
title = "Unitization of a C*-algebra"
kind = "definition"
summary = "The canonical unital C*-algebra formed by adjoining an identity to a nonunital C*-algebra."
aliases = ["minimal unitization", "adjoining an identity to a C*-algebra", "A tilde", "unitisation"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) be a nonunital
[[operator-algebras/cstar-algebra|\(C^*\)-algebra]]. Its **unitization**
\(\widetilde A\) is the [[linear-algebra/vector-space|vector space]] \(A\oplus\mathbb C\) with
\[
(a,\lambda)(b,\mu)=(ab+\lambda b+\mu a,\lambda\mu),
\qquad
(a,\lambda)^*=(a^*,\overline\lambda).
\]
It has the canonical \(C^*\)-norm extending the norm of \(A\), identity
\((0,1)\), and an isometric embedding \(a\mapsto(a,0)\). Under this embedding,
\(A\) is a closed essential ideal of the
[[operator-algebras/unital-cstar-algebra|unital \(C^*\)-algebra]]
\(\widetilde A\), and the scalar map
\((a,\lambda)\mapsto\lambda\) identifies \(\widetilde A/A\) with
\(\mathbb C\).

## Universal extension property

For every \(*\)-homomorphism \(\varphi:A\to B\) into a unital \(C^*\)-algebra,
there is a unique unital \(*\)-homomorphism
\[
\widetilde\varphi:\widetilde A\to B,
\qquad
\widetilde\varphi(a,\lambda)=\varphi(a)+\lambda1_B,
\]
extending \(\varphi\). This property characterizes the unitization up to
canonical unital \(*\)-isomorphism. It also records why the algebraic
construction must be equipped with its \(C^*\)-norm and involution rather than
treated as merely adjoining a ring identity
[Murphy, §2.1].

## Spectra, characters, and multipliers

For \(a\in A\), the spectrum used in nonunital \(C^*\)-algebra theory is
computed from \((a,0)\) in \(\widetilde A\); zero necessarily belongs to this
spectrum. The scalar quotient is a character
\(\epsilon:\widetilde A\to\mathbb C\). The unitization embeds canonically in
the [[operator-algebras/multiplier-algebra|multiplier algebra]] \(M(A)\), but it can be strictly smaller: for example,
the unitization of the [[linear-algebra/compact-operator|compact operators]] is
\(\mathcal K(H)+\mathbb C I_H\), whereas their multiplier algebra is \(B(H)\).

## Conventions for already unital algebras

When \(A\) already has an identity, some authors define its unitization to be
\(A\) itself. Others retain the formula \(A\oplus\mathbb C\), which adjoins a
new identity and is then isomorphic to \(A\oplus\mathbb C\) as a unital
algebra by a change of coordinates. The core definition assumes \(A\) is
nonunital, so these conventions do not conflict. “Minimal” distinguishes this
construction from the generally larger multiplier algebra.

## References

1. Gerard J. Murphy, *C*-Algebras and Operator Theory*, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §2.1 on adjoining an identity and nonunital spectra.
2. Gert K. Pedersen, *C*-Algebras and Their Automorphism Groups*, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: §1.3 on unitization and its canonical \(C^*\)-norm.
