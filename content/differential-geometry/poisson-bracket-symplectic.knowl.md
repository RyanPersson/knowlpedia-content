+++
id = "differential-geometry/poisson-bracket-symplectic"
title = "Poisson bracket on a symplectic manifold"
kind = "definition"
summary = "The Lie bracket on smooth functions induced by the inverse of a symplectic form."
aliases = ["symplectic Poisson bracket"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/symplectic-manifold", "differential-geometry/hamiltonian-vector-field"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((M,\omega)\) be a [[differential-geometry/symplectic-manifold|symplectic manifold]]. For \(f,g\in C^\infty(M,\mathbb R)\), let \(X_f,X_g\) be their [[differential-geometry/hamiltonian-vector-field|Hamiltonian vector fields]] under the convention \(\iota_{X_f}\omega=df\). The **Poisson bracket** is
\[
\{f,g\}=\omega(X_f,X_g)=X_g(f)=-X_f(g).
\]
This formula produces another smooth real-valued function. It fixes all signs: in Darboux coordinates with \(\omega=\sum_i dq_i\wedge dp_i\),
\[
\{f,g\}=\sum_i\left(
\frac{\partial f}{\partial q_i}\frac{\partial g}{\partial p_i}
-\frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q_i}
\right),
\]
so \(\{q_i,p_j\}=\delta_{ij}\).

## Poisson-algebra laws

The bracket is real-bilinear and antisymmetric, satisfies the Jacobi identity, and is a derivation in each argument:
\[
\{f,gh\}=\{f,g\}h+g\{f,h\}.
\]
Therefore \(C^\infty(M)\), with pointwise multiplication and this bracket, is a Poisson algebra.

## Vector fields and dynamics

With the plus-sign Hamiltonian convention, the correspondence from functions to [[fiber-bundles/vector-field|vector fields]] is a [[lie-groups/lie-algebra|Lie algebra]] anti-homomorphism:
\[
X_{\{f,g\}}=-[X_f,X_g].
\]
If \(H\) generates a Hamiltonian trajectory \(\gamma\), then
\[
\frac{d}{dt}f(\gamma(t))=\{f,H\}.
\]
Thus \(\{f,H\}=0\) precisely when \(f\) is constant along the [[differential-geometry/hamiltonian-flow|Hamiltonian flow]].

## Conventions

**Warning.** Authors who define \(\iota_{X_f}\omega=-df\) may arrange their Poisson bracket so that \(f\mapsto X_f\) is a homomorphism rather than an anti-homomorphism. Comparing only one displayed formula can therefore be misleading; the Hamiltonian-vector-field and bracket conventions must be compared together.

## References

1. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Springer, 2008. [DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: Lecture 18.3, Definition 18.5, Theorem 18.6, and Lecture 18.4, Theorem 18.9.
2. Ralph Abraham and Jerrold E. Marsden, *Foundations of Mechanics*, 2nd ed., AMS Chelsea, 2008. [DOI record](https://doi.org/10.1090/chel/364). Relevant: §3.3.
