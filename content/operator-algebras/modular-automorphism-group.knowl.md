+++
id = "operator-algebras/modular-automorphism-group"
title = "Modular automorphism group"
kind = "definition"
summary = "The modular automorphism group is the canonical one-parameter automorphism group associated with a faithful normal semifinite weight."
aliases = ["modular group", "modular flow"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(M\) be a [[operator-algebras/von-neumann-algebra|von Neumann algebra]]
and let \(\varphi\) be a
[[operator-algebras/normal-semifinite-faithful-weight|normal semifinite
faithful weight]]. The **modular automorphism group** of \(\varphi\) is the
unique ultraweakly continuous one-parameter group
\[
\sigma^\varphi:\mathbb R\longrightarrow\operatorname{Aut}(M)
\]
obtained from the [[operator-algebras/modular-operator|modular operator]] in
the weight's [[operator-algebras/gns-construction-for-weight|GNS construction]] or
[[operator-algebras/standard-form|standard representation]]:
\[
\pi_\varphi(\sigma_t^\varphi(x))
=\Delta_\varphi^{it}\pi_\varphi(x)\Delta_\varphi^{-it}.
\]
The [[operator-algebras/tomita-takesaki-theorem|Tomita–Takesaki theorem]]
ensures that the right-hand side again belongs to \(\pi_\varphi(M)\). Thus the
definition is independent, up to canonical equivalence, of the chosen
realization.

## Characterization by the KMS condition

The weight \(\varphi\) is invariant under its modular group. On the
\(\sigma^\varphi\)-analytic elements, the group is characterized by the
boundary relation
\[
\varphi(xy)=\varphi\!\left(y\,\sigma_{-i}^\varphi(x)\right)
\]
whenever the terms are in the weight's finite domains. This is the
Kubo–Martin–Schwinger condition at inverse temperature \(1\), and it
characterizes the modular dynamics under the standard continuity and
faithfulness hypotheses
[Takesaki, vol. II, Chapter VIII, §1].

## Traces and inner modular flows

If \(\varphi\) is a
[[operator-algebras/faithful-normal-semifinite-trace|faithful normal
semifinite trace]], then
\(\sigma_t^\varphi=\operatorname{id}_M\) for every \(t\). For a faithful
[[operator-algebras/normal-state|normal state]] on \(M_n(\mathbb C)\) with
density matrix \(\rho\),
\[
\sigma_t^\varphi(x)=\rho^{it}x\rho^{-it},
\]
so the modular group is inner and is trivial exactly when \(\rho\) is scalar.
In general, the outer class of modular flow carries essential information
about [[operator-algebras/type-iii-von-neumann-algebra|type III von Neumann algebras]].

## Dependence on the weight

Different [[operator-algebras/normal-semifinite-faithful-weight|n.s.f. weights]] generally produce different [[algebra-groups/automorphism-group|automorphism groups]].
Connes's Radon–Nikodym cocycle relates them by a time-dependent inner
perturbation, so their images in the [[algebra-groups/outer-automorphism-group|outer automorphism group]] agree in the
appropriate sense. This weight-independent outer flow underlies the flow of
weights and type III classification
[Takesaki, vol. II, Chapter VIII].

## Conventions and scope

**Warning.** Some authors define modular time with the opposite sign. Under
that convention the KMS boundary formula uses \(\sigma_i^\varphi\) where the
display above uses \(\sigma_{-i}^\varphi\). A modular group is attached to a
specified weight or faithful state; it is not, before passing to suitable
outer invariants, a canonical pointwise action determined by \(M\) alone.

## References

1. Masamichi Takesaki, *Theory of Operator Algebras II*, Springer, 2003. [DOI record](https://doi.org/10.1007/978-3-662-10451-4). Relevant: Chapter VIII, §1 on modular automorphism groups and the Radon–Nikodym theorem for weights.
