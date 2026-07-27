+++
id = "lie-groups/projective-unitary-representation"
title = "Projective unitary representation"
kind = "definition"
summary = "A continuous group representation by unitary operators modulo scalar phases."
aliases = ["unitary projective representation", "projective representation on a Hilbert space", "unitary ray representation"]
domains = ["lie-groups", "functional-analysis"]
section_mode = "progressive"
+++

Let \(G\) be a [[topology/topological-group|topological group]] and \(H\) a complex [[linear-algebra/hilbert-space|Hilbert space]]. Write
\[
PU(H)=U(H)/\{\lambda I:|\lambda|=1\},
\]
with the quotient of the [[operator-algebras/strong-operator-topology|strong operator topology]] on \(U(H)\). A **projective unitary representation** is a continuous [[algebra-groups/group-homomorphism|group homomorphism]]
\[
\overline\pi:G\longrightarrow PU(H).
\]
Thus each \(g\) acts by a [[functional-analysis/unitary-operator|unitary operator]] determined only up to a scalar phase, while multiplication is exact after passing to projective classes. Equivalently, it is an action of \(G\) on the rays of \(H\) induced by unitaries; it need not admit a globally continuous choice of unitary representatives.

## Multipliers

If representatives \(U_g\in U(H)\) can be chosen, then
\[
U_gU_h=\sigma(g,h)U_{gh}
\]
for phases \(\sigma(g,h)\in\mathbb T\). Associativity gives the cocycle identity
\[
\sigma(g,h)\sigma(gh,k)=\sigma(h,k)\sigma(g,hk).
\]
Changing representatives by \(U_g\mapsto b(g)U_g\) changes \(\sigma\) by a coboundary. The resulting cohomology class records the obstruction to replacing the projective representation by a genuine one.

## Lifts and central extensions

In a category where the chosen multiplier is continuous or Borel as required, the projective representation lifts to a genuine unitary representation of \(G\) exactly when its multiplier class is trivial. Even when it does not lift on \(G\), it gives a genuine representation of the associated [[algebra-groups/central-extension|central extension]] by \(\mathbb T\). Global lifts and continuous representatives require hypotheses beyond the bare quotient-valued definition [Varadarajan, Chapter VIII](https://doi.org/10.1007/978-0-387-49386-2).

## Example

The spin-\(\tfrac12\) representation of \(SU(2)\) does not descend to an ordinary representation of \(SO(3)=SU(2)/\{\pm I\}\), because the nontrivial central element acts as \(-I\). After quotienting operators by phases, it does descend to a projective unitary representation of \(SO(3)\).

## References

1. V. S. Varadarajan, *Geometry of Quantum Theory*, 2nd ed., Springer, 1985. [DOI record](https://doi.org/10.1007/978-0-387-49386-2). Relevant: Chapter VIII, “Multipliers.”
2. V. Bargmann, “On Unitary Ray Representations of Continuous Groups,” *Annals of Mathematics* 59 (1954), 1–46. [DOI record](https://doi.org/10.2307/1969831). Relevant: multipliers, ray representations, and lifting.
