+++
id = "differential-geometry/canonical-moment-map-cotangent-lift"
title = "Canonical moment map for a cotangent-lifted action"
kind = "theorem"
summary = "The cotangent lift of a Lie group action is Hamiltonian with moment map given by pairing covectors with infinitesimal generators."
aliases = ["cotangent-lift moment map"]
domains = ["differential-geometry", "lie-groups"]
section_mode = "progressive"
+++

Let \(G\) act on \(Q\) by a [[fiber-bundles/smooth-action-of-a-lie-group-on-a-manifold|smooth Lie group action]], and let it act on \(T^*Q\) by the [[differential-geometry/cotangent-lift|cotangent lift]]. With \(\omega_{\mathrm{can}}=-d\theta\) and \(\xi_Q(q)=\left.\frac{d}{dt}\right|_0\exp(t\xi)\cdot q\), define
\[
\langle J(\alpha_q),\xi\rangle
=\alpha_q\bigl(\xi_Q(q)\bigr).
\]
Then \(J:T^*Q\to\mathfrak g^*\) is an [[differential-geometry/equivariant-moment-map|equivariant moment map]]:
\[
d\langle J,\xi\rangle=\iota_{\xi_{T^*Q}}\omega_{\mathrm{can}},
\qquad
J(g\cdot\alpha_q)=\operatorname{Ad}_g^*J(\alpha_q).
\]
Consequently the cotangent-lifted action is a [[differential-geometry/hamiltonian-lie-group-action|Hamiltonian Lie group action]]. No connection, metric, or trivialization is involved: the pairing defining \(J\) is determined entirely by the original action and the tautological cotangent geometry. The construction is canonical.

## Why the formula is canonical

The tautological one-form satisfies
\[
\theta_{\alpha_q}(\xi_{T^*Q})=\alpha_q(\xi_Q(q))
=\langle J(\alpha_q),\xi\rangle.
\]
Every cotangent lift preserves \(\theta\). Cartan's formula therefore gives
\[
\iota_{\xi_{T^*Q}}(-d\theta)
=d\bigl(\theta(\xi_{T^*Q})\bigr)=dJ^\xi,
\]
which proves the moment-map identity without coordinates. Naturality of the infinitesimal generators under the [[algebra-groups/group-action|group action]] proves coadjoint equivariance.

## Coordinate example

For translations of \(Q=\mathbb R^n\) by \(G=\mathbb R^n\), identify \(T^*\mathbb R^n\) with pairs \((q,p)\). The infinitesimal generator of \(\xi\in\mathbb R^n\) is the constant vector \(\xi\), so
\[
\langle J(q,p),\xi\rangle=p\cdot\xi.
\]
Thus \(J(q,p)=p\): linear momentum is the [[fiber-bundles/moment-map|moment map]] for translations.

## Conventions and scope

**Warning.** If the canonical symplectic form is defined as \(d\theta\), or if [[differential-geometry/infinitesimal-generator-lie-action|fundamental vector fields]] use \(\exp(-t\xi)\), the formula for \(J\) acquires a minus sign. The theorem concerns the genuine cotangent lift; an arbitrary [[differential-geometry/symplectic-lie-group-action|symplectic action]] on a [[fiber-bundles/cotangent-bundle|cotangent bundle]] need not have this particular moment map.

## References

1. Ralph Abraham and Jerrold E. Marsden, *Foundations of Mechanics*, 2nd ed., AMS Chelsea, 2008. [DOI record](https://doi.org/10.1090/chel/364). Relevant: §4.2, lifted actions and momentum mappings.
2. Jerrold E. Marsden and Tudor S. Ratiu, *Introduction to Mechanics and Symmetry*, 2nd ed., Texts in Applied Mathematics 17, Springer, 1999. [DOI record](https://doi.org/10.1007/978-0-387-21792-5). Relevant: §12.1, momentum maps for cotangent-lifted actions.
