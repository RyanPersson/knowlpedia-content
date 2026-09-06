+++
id = "lie-groups/harish-chandra-isomorphism"
title = "Harish–Chandra isomorphism"
kind = "theorem"
summary = "The theorem identifying the center of a semisimple enveloping algebra with Weyl-invariant polynomials on a Cartan subalgebra."
aliases = ["radial component isomorphism for Z(U(g))", "Harish-Chandra homomorphism"]
domains = ["lie-groups", "algebra-representation-theory"]
prerequisites = ["lie-groups/semisimple-lie-algebra", "lie-groups/cartan-subalgebra", "lie-groups/positive-root", "lie-groups/center-of-universal-enveloping-algebra", "lie-groups/weyl-group"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(\mathfrak g\) be a complex [[lie-groups/semisimple-lie-algebra|semisimple Lie algebra]], let \(\mathfrak h\) be a [[lie-groups/cartan-subalgebra|Cartan subalgebra]], and choose [[lie-groups/positive-root|positive roots]] with half-sum \(\rho\). The Poincaré–Birkhoff–Witt decomposition defines a projection from [[lie-groups/center-of-universal-enveloping-algebra|\(Z(U(\mathfrak g))\)]] to \(U(\mathfrak h)\cong S(\mathfrak h)\). Composing it with the translation \(H\mapsto H-\rho(H)\) gives the **Harish–Chandra homomorphism**
\[
\gamma:Z(U(\mathfrak g))\longrightarrow S(\mathfrak h).
\]
The **Harish–Chandra isomorphism theorem** states that \(\gamma\) is an algebra isomorphism from \(Z(U(\mathfrak g))\) onto \(S(\mathfrak h)^{W}\), where \(W\) is the [[lie-groups/weyl-group|Weyl group]].

## Construction

For the triangular decomposition \(\mathfrak g=\mathfrak n^-\oplus\mathfrak h\oplus\mathfrak n^+\), the [[lie-groups/pbw-theorem|PBW theorem]] gives a direct-sum complement to \(U(\mathfrak h)\) containing \(\mathfrak n^-U(\mathfrak g)+U(\mathfrak g)\mathfrak n^+\). Projecting a central element along this complement gives its unshifted Harish–Chandra projection. The \(\rho\)-translation converts invariance for the shifted Weyl action into ordinary \(W\)-invariance.

## Consequences for central characters

[[algebra-modules/algebra-homomorphism|Algebra homomorphisms]] \(Z(U(\mathfrak g))\to\mathbb C\) are thereby parameterized by \(W\)-orbits in \(\mathfrak h^*\). If a highest-weight module has [[lie-groups/highest-weight|highest weight]] \(\lambda\), then its central character is obtained by evaluating \(\gamma(z)\) at \(\lambda+\rho\). Thus highest weights in the same shifted Weyl orbit have the same [[lie-groups/infinitesimal-character|infinitesimal character]].

## Conventions

Some authors call the unshifted PBW projection the Harish–Chandra homomorphism and state that its image is invariant for the dot action \(w\mathbin{\cdot}\lambda=w(\lambda+\rho)-\rho\). Others incorporate the shift, as above, and obtain ordinary Weyl invariants. The two formulations are equivalent, but their evaluation formulas differ by \(\rho\).

## References

1. Jacques Dixmier, *Enveloping Algebras*, Graduate Studies in Mathematics 11, American Mathematical Society, 1996. [DOI record](https://doi.org/10.1090/gsm/011). Relevant: §7.4 on the Harish–Chandra homomorphism.
2. Anthony W. Knapp, *Lie Groups Beyond an Introduction*, 2nd ed., Birkhäuser, 2002. [DOI record](https://doi.org/10.1007/978-1-4757-2453-0). Relevant: Chapter V, §5 on the center of the enveloping algebra.
