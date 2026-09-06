+++
id = "operator-algebras/connes-cocycle-derivative"
title = "Connes cocycle derivative"
kind = "definition"
summary = "The Connes cocycle derivative is a unitary cocycle that compares the modular automorphism groups of two faithful normal semifinite weights."
aliases = ["cocycle Radon–Nikodym derivative"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/normal-semifinite-faithful-weight", "operator-algebras/von-neumann-algebra", "operator-algebras/spatial-derivative", "operator-algebras/modular-automorphism-group"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(\varphi\) and \(\psi\) be
[[operator-algebras/normal-semifinite-faithful-weight|normal semifinite faithful weights]] on a [[operator-algebras/von-neumann-algebra|von Neumann algebra]] \(M\). Their **Connes cocycle derivative** is the strongly
continuous family of unitaries
\[
u_t=(D\psi:D\varphi)_t\in M,\qquad t\in\mathbb R,
\]
supplied by the noncommutative Radon–Nikodym theorem. In a faithful
representation, choose an n.s.f. weight \(\chi\) on \(M'\). In terms of
[[operator-algebras/spatial-derivative|spatial derivatives]],
\[
u_t=(d\psi/d\chi)^{it}(d\varphi/d\chi)^{-it};
\]
it lies in \(M\), independently of \(\chi\). It satisfies
\[
u_{s+t}=u_s\,\sigma_s^\varphi(u_t)
\quad\text{and}\quad
\sigma_t^\psi(x)=u_t\sigma_t^\varphi(x)u_t^*
\]
for \(s,t\in\mathbb R\), \(x\in M\). It is a
\(\sigma^\varphi\)-cocycle changing the
[[operator-algebras/modular-automorphism-group|modular flow]] of \(\varphi\)
to that of \(\psi\).

## Radon–Nikodym role

The cocycle derivative is the noncommutative replacement for a ratio of
densities. If \(M\) is semifinite with
[[operator-algebras/faithful-normal-semifinite-trace|faithful normal semifinite trace]] \(\tau\), and
\(\varphi(x)=\tau(h_\varphi x)\), \(\psi(x)=\tau(h_\psi x)\) for positive
invertible affiliated densities, then
\[
(D\psi:D\varphi)_t=h_\psi^{it}h_\varphi^{-it}.
\]
The formula remains meaningful even when the two densities do not commute:
the resulting family is generally a cocycle rather than a one-parameter
group.

## Chain and inversion rules

For a third normal semifinite faithful weight \(\theta\), cocycle derivatives
obey the [[real-analysis/chain-rule|chain rule]]
\[
(D\psi:D\varphi)_t
=(D\psi:D\theta)_t(D\theta:D\varphi)_t.
\]
They also satisfy
\[
(D\psi:D\varphi)_t^*=(D\varphi:D\psi)_t.
\]
These identities make changes of reference weight coherent and show that no
preferred weight is required to compare modular dynamics. Connes used this
Radon–Nikodym theory in the structure and classification of
[[operator-algebras/type-iii-factor|type III factors]].

## Examples and scope

When \(\psi=\varphi\), the cocycle is constantly \(1\). If
\(\psi=\lambda\varphi\) for a scalar \(\lambda>0\), then
\((D\psi:D\varphi)_t=\lambda^{it}1\); the modular automorphism groups are
equal even though the cocycle is not constant unless \(\lambda=1\).
Faithfulness makes each cocycle value unitary. For nonfaithful weights the
general theory uses [[functional-analysis/partial-isometry|partial isometries]] and support projections, so the unitary formulation in the core
should not be applied unchanged. Moreover, the cocycle and implementation
identities alone do not distinguish the derivative from every other
implementing cocycle; the Radon–Nikodym normalization in the core is
essential.

## References

1. Masamichi Takesaki, *Theory of Operator Algebras II*, Springer, 2003. [DOI record](https://doi.org/10.1007/978-3-662-10451-4). Relevant: Chapter VIII, §3 on the Connes cocycle derivative.
2. Alain Connes, “Une classification des facteurs de type III,” *Annales scientifiques de l’École Normale Supérieure* 6 (1973), 133–252. [DOI record](https://doi.org/10.24033/asens.1247). Relevant: §1 on the cocycle Radon–Nikodym derivative and modular automorphisms.
