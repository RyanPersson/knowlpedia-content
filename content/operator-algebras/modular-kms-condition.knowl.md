+++
id = "operator-algebras/modular-kms-condition"
title = "Modular KMS condition"
kind = "definition"
summary = "The modular KMS condition is the analytic boundary relation that characterizes a faithful normal state's modular dynamics."
aliases = ["KMS characterization of modular flow"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(M\) be a [[operator-algebras/von-neumann-algebra|von Neumann algebra]],
let \(\varphi\) be a [[operator-algebras/faithful-normal-state|faithful normal state]], and let \(\sigma^\varphi\) be its
[[operator-algebras/modular-automorphism-group|modular automorphism group]].
The **modular KMS condition** is the boundary identity
\[
\varphi(xy)=\varphi\!\left(y\,\sigma_{-i}^\varphi(x)\right)
\]
for elements \(x,y\) that are
[[operator-algebras/entire-analytic-element-one-parameter-automorphism|entire
analytic]] for \(\sigma^\varphi\).
Equivalently, the real-time correlation functions admit bounded analytic
continuations to a strip whose two boundary values are related by cyclically
interchanging \(x\) and \(y\). With the displayed sign convention, this is
the KMS condition at inverse temperature \(1\).

## Characterization of modular dynamics

The state is invariant under its modular group:
\(\varphi\circ\sigma_t^\varphi=\varphi\). More strongly, among suitably
continuous one-parameter [[algebra-groups/automorphism-group|automorphism groups]], the KMS boundary relation
determines the modular group of a faithful normal state. This is why modular
flow can be described intrinsically, without choosing a particular GNS
realization.

For a
[[operator-algebras/normal-semifinite-faithful-weight|normal semifinite faithful weight]], the analogous identity is imposed on the analytic elements
lying in the weight's finite left and right domains. That domain
qualification is essential because a weight may take the value \(+\infty\).

## Tracial and finite-dimensional cases

If \(\varphi\) is tracial, its modular group is trivial, and the boundary
identity reduces to \(\varphi(xy)=\varphi(yx)\). On
\(M_n(\mathbb C)\), let
\(\varphi(x)=\operatorname{Tr}(\rho x)\) for an invertible density matrix
\(\rho\). Then
\[
\sigma_t^\varphi(x)=\rho^{it}x\rho^{-it},
\]
and the modular KMS identity follows by ordinary trace cyclicity. This example
also shows that KMS cyclicity is twisted by modular evolution when \(\rho\)
is not scalar.

## Conventions and scope

**Warning.** Authors who define modular evolution by
\(\sigma_t(x)=\Delta^{-it}x\Delta^{it}\) reverse modular time. Their boundary
formula contains \(\sigma_i(x)\) where the core uses \(\sigma_{-i}(x)\).
Changing only one sign produces an inconsistent convention. The general KMS
condition may use an arbitrary inverse temperature \(\beta\); modular theory
canonically gives \(\beta=1\) after the time parameter is normalized.

## References

1. Masamichi Takesaki, *Theory of Operator Algebras II*, Springer, 2003. [DOI record](https://doi.org/10.1007/978-3-662-10451-4). Relevant: Chapter VIII, §1 on modular automorphism groups and their KMS characterization.
2. Ola Bratteli and Derek W. Robinson, *Operator Algebras and Quantum Statistical Mechanics 2: Equilibrium States, Models in Quantum Statistical Mechanics*, 2nd ed., Springer, 1997. [DOI record](https://doi.org/10.1007/978-3-662-03444-6). Relevant: §5.3 on KMS states and analytic boundary conditions.
