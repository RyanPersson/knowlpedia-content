+++
id = "operator-algebras/unique-predual-theorem"
title = "Unique predual theorem"
kind = "theorem"
summary = "The Banach-space predual of a von Neumann algebra is uniquely determined up to its canonical isometry."
aliases = ["uniqueness of the von Neumann algebra predual"]
domains = ["operator-algebras", "functional-analysis"]
section_mode = "progressive"
+++

Let \(M\) be a [[operator-algebras/von-neumann-algebra|von Neumann algebra]].
The **unique predual theorem** states that its
[[operator-algebras/predual|predual]] \(M_*\) is the unique Banach space
predual of \(M\), up to the canonical isometric isomorphism compatible with
the dual pairing. More explicitly, if a Banach space \(E\) and a linear
isometry \(\Phi:M\to E^*\) exhibit \(M\) as a dual Banach space, then \(E\)
identifies isometrically with \(M_*\) through the functionals it induces on
\(M\). Consequently the
[[functional-analysis/weak-star-topology|weak-star topology]]
\(\sigma(M,M_*)\) is intrinsic to the von Neumann algebra's normed
\(*\)-algebra structure.

## Meaning of uniqueness

The assertion is stronger than the existence of some abstract isometry
between two predual spaces. Each element of a proposed predual determines a
bounded functional on \(M\), and the theorem says that the resulting
subspace of \(M^*\) is exactly \(M_*\). Thus the dual pairing, and not merely
the Banach-space isomorphism class, is fixed.

## Consequences for normality

Because the weak-star topology is unique, weak-star continuous functionals
on \(M\) are exactly the
[[operator-algebras/normal-functional|normal functionals]], independently of
which dual presentation is initially chosen. Weak-star continuous
\(*\)-homomorphisms, normal states, and weak-star compactness are therefore
intrinsic notions rather than artifacts of a concrete representation on a
Hilbert space.

## Context and caution

Many dual Banach spaces have inequivalent preduals, so uniqueness is a
special rigidity property of von Neumann algebras. The theorem concerns
isometric dual realizations. It should not be weakened to a claim that every
Banach space merely isomorphic to \(M\) as a Banach space carries the same
predual or weak-star topology.

## References

1. Shôichirô Sakai, *C*-Algebras and W*-Algebras*, Springer, 1998. [Publisher record](https://doi.org/10.1007/978-3-642-61993-9). Relevant: Theorem 1.13.2 on uniqueness of the predual.
2. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 2002. [Publisher record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter III, §2 on the predual and normal functionals.
