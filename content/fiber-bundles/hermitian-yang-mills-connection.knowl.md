+++
id = "fiber-bundles/hermitian-yang-mills-connection"
title = "Hermitian Yang–Mills connection"
kind = "definition"
summary = "A unitary integrable connection whose curvature has constant central contraction with the Hermitian form."
aliases = ["Hermitian–Einstein connection", "HYM connection"]
domains = ["fiber-bundles", "differential-geometry"]
section_mode = "progressive"
+++

Let \((X,\omega)\) be a [[differential-geometry/hermitian-manifold|Hermitian manifold]] and \(E\to X\) a Hermitian [[fiber-bundles/complex-vector-bundle|complex vector bundle]]. A [[fiber-bundles/hermitian-connection|Hermitian connection]] \(A\) is a **Hermitian Yang–Mills connection** if
\[
F_A^{0,2}=0
\qquad\text{and}\qquad
\sqrt{-1}\,\Lambda_\omega F_A=\lambda\,\operatorname{id}_E
\]
for a real constant \(\lambda\), where \(\Lambda_\omega\) is contraction with \(\omega\). The first equation makes \(A\) compatible with a holomorphic structure; relative to that structure, \(A\) is its [[fiber-bundles/chern-connection|Chern connection]]. The second says that the contracted [[fiber-bundles/chern-curvature|Chern curvature]] is a constant central endomorphism.

## Meaning of the equations

Integrability \(F_A^{0,2}=0\) is a separate requirement: constant central contraction alone does not define a Hermitian Yang–Mills connection. When the holomorphic structure and Hermitian metric are fixed from the outset, authors often omit the first equation because it is automatic for the Chern connection.

On a compact [[differential-geometry/kahler-manifold|Kähler manifold]], the constant \(\lambda\) is determined by the degree, rank, and volume of \(E\), with its numerical factor depending on the convention for \(\Lambda_\omega\) and volume. The [[differential-geometry/kahler-identities|Kähler identities]] imply that a Hermitian Yang–Mills connection satisfies the ordinary Yang–Mills equation [Kobayashi, Chapter IV, §1](https://doi.org/10.1515/9781400858682).

## Examples and consequences

A flat unitary connection is Hermitian Yang–Mills with \(\lambda=0\) whenever its \((0,1)\)-part defines the chosen holomorphic structure. On a [[differential-geometry/holomorphic-line-bundle|holomorphic line bundle]], the equation asks the scalar contraction of the Chern curvature to be constant.

For compact Kähler manifolds, the Kobayashi–Hitchin correspondence relates Hermitian Yang–Mills metrics to polystability of holomorphic bundles. This is an existence theorem, not part of the definition, and its precise hypotheses vary with the setting [Lübke–Teleman, Chapter 2](https://doi.org/10.1142/9789812811750).

## Conventions and scope

“Hermitian–Einstein” and “Hermitian Yang–Mills” are commonly synonymous here. Some authors write \(\Lambda_\omega F_A=-\sqrt{-1}\lambda I\), absorbing \(\sqrt{-1}\) or a sign into the constant. The definition makes sense on a Hermitian base, but the strongest Yang–Mills and stability consequences generally require Kähler or Gauduchon hypotheses stated separately.

## References

1. Shoshichi Kobayashi, *Differential Geometry of Complex Vector Bundles*, Princeton University Press, 1987. [Publisher record](https://doi.org/10.1515/9781400858682). Relevant: Chapter IV, especially §1, Einstein–Hermitian connections.
2. Martin Lübke and Andrei Teleman, *The Kobayashi–Hitchin Correspondence*, World Scientific, 1995. [Publisher record](https://doi.org/10.1142/9789812811750). Relevant: Chapter 2, Hermitian–Einstein connections and stability.
