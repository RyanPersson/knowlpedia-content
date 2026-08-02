+++
id = "differential-geometry/shifting-trick"
title = "Shifting trick"
kind = "construction"
summary = "A construction that turns reduction at a coadjoint value into zero-level reduction using the opposite coadjoint orbit."
aliases = ["coadjoint-orbit shifting trick"]
domains = ["differential-geometry", "lie-groups"]
section_mode = "progressive"
+++

Let \(G\) have a [[differential-geometry/hamiltonian-lie-group-action|Hamiltonian action]] on \((M,\omega)\) with equivariant [[fiber-bundles/moment-map|moment map]] \(\mu:M\to\mathfrak g^*\), let \(\alpha\in\mathfrak g^*\), and let \(\mathcal O_\alpha\) be its [[differential-geometry/coadjoint-orbit|coadjoint orbit]]. Equip \(\mathcal O_\alpha^{-}\) with the negative of its [[differential-geometry/kirillov-kostant-souriau-form|Kirillov–Kostant–Souriau form]]. The diagonal action on
\[
(M\times\mathcal O_\alpha^{-},\,\omega\oplus-\omega_{\mathrm{KKS}})
\]
has moment map
\[
\widetilde\mu(m,\xi)=\mu(m)-\xi.
\]
The **shifting trick** replaces reduction at \(\alpha\) by zero-level reduction of this product. Set-theoretically, and symplectically whenever the regular-reduction hypotheses hold,
\[
\mu^{-1}(\alpha)/G_\alpha\cong\widetilde\mu^{-1}(0)/G.
\]
This construction keeps the original [[algebra-groups/group-action|group action]] while moving the chosen momentum level to zero.

## Construction of the identification

The zero set consists of pairs \((m,\xi)\) with \(\mu(m)=\xi\in\mathcal O_\alpha\). Every diagonal \(G\)-orbit in this set has a representative \((m,\alpha)\): choose \(g\) carrying \(\xi\) to \(\alpha\). Two such representatives \((m,\alpha)\) and \((m',\alpha)\) are in the same diagonal orbit exactly when they differ by an element of \(G_\alpha\). This gives the displayed bijection.

Equivalently, both sides identify with the orbit-reduction space
\[
\mu^{-1}(\mathcal O_\alpha)/G.
\]
Under free and proper regularity assumptions, the bijection is a diffeomorphism and the pullback characterizations of the reduced forms show that it is a [[differential-geometry/symplectomorphism|symplectomorphism]].

## Why the sign is negative

With the convention that inclusion \(\mathcal O_\alpha\hookrightarrow\mathfrak g^*\) is the moment map for the positive KKS form, the moment map on the oppositely symplectic orbit is \(-\xi\). Moment maps add under products, giving \(\widetilde\mu(m,\xi)=\mu(m)-\xi\). Consequently the zero equation is the desired equality \(\mu(m)=\xi\).

Changing the convention for the KKS form or for [[differential-geometry/hamiltonian-vector-field|Hamiltonian vector fields]] changes the displayed signs together. The invariant content is that the orbit factor is taken with the symplectic sign that makes the product moment map vanish exactly over \(\mu^{-1}(\mathcal O_\alpha)\).

## Uses and scope

The construction allows zero-level results, including [[differential-geometry/singular-symplectic-reduction|singular reduction]] theorems, to be applied at arbitrary coadjoint values. It also makes the coadjoint orbit itself part of the geometry instead of treating \(\alpha\) as a fixed parameter.

The shifting trick does not repair a failure of regularity or properness. If the original reduction is singular, the shifted zero-level reduction is singular as well, though the identification remains useful at the level of stratified quotients.

## References

1. Victor Guillemin and Shlomo Sternberg, *Symplectic Techniques in Physics*, Cambridge University Press, 1984. [DOI record](https://doi.org/10.1017/CBO9780511624112). Relevant: Chapter 5, reduction at coadjoint orbits and the shifting construction.
2. Juan-Pablo Ortega and Tudor S. Ratiu, *Momentum Maps and Hamiltonian Reduction*, Birkhäuser, 2004. [DOI record](https://doi.org/10.1007/978-1-4757-3811-7). Relevant: §4.3, equivalence of point, orbit, and shifted zero-level reduction.
