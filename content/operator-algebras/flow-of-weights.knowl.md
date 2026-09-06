+++
id = "operator-algebras/flow-of-weights"
title = "Flow of weights"
kind = "definition"
summary = "The canonical flow induced by the dual action on the center of the continuous core of a von Neumann algebra."
aliases = ["Connes–Takesaki flow"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/von-neumann-algebra", "operator-algebras/normal-semifinite-faithful-weight", "operator-algebras/continuous-core-von-neumann-algebra", "operator-algebras/von-neumann-crossed-product", "operator-algebras/modular-automorphism-group", "operator-algebras/dual-action-von-neumann-crossed-product", "operator-algebras/center-of-von-neumann-algebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\) be a [[operator-algebras/von-neumann-algebra|von Neumann algebra]]
with separable predual and choose a
[[operator-algebras/normal-semifinite-faithful-weight|normal semifinite faithful weight]] \(\varphi\). Form the [[operator-algebras/continuous-core-von-neumann-algebra|continuous core]]
\[
c_\varphi(M)=M\rtimes_{\sigma^\varphi}\mathbb R
\]
as the [[operator-algebras/continuous-core-von-neumann-algebra|continuous
core]], hence a
[[operator-algebras/von-neumann-crossed-product|von Neumann crossed product]]
by the [[operator-algebras/modular-automorphism-group|modular automorphism
group]]. Let \(\theta:\mathbb R\curvearrowright c_\varphi(M)\) be its
[[operator-algebras/dual-action-von-neumann-crossed-product|dual action]].
The [[operator-algebras/center-of-von-neumann-algebra|center]]
\(Z(c_\varphi(M))\) is \(\theta\)-invariant. The **flow of weights** of \(M\)
is the restricted action
\[
\theta|_{Z(c_\varphi(M))}:\mathbb R\curvearrowright Z(c_\varphi(M)).
\]
Changing \(\varphi\) produces a conjugate flow, so its conjugacy class is an
isomorphism invariant of \(M\).

## Factor types

When \(M\) is a [[operator-algebras/von-neumann-factor|factor]], its flow of
weights is ergodic. For a type \(\mathrm{III}_1\) factor the flow is the
one-point flow. For type
\(\mathrm{III}_\lambda\), \(0<\lambda<1\), it is periodic; in the logarithmic
translation normalization its least positive period is
\(\lvert\log\lambda\rvert\). Type \(\mathrm{III}_0\) gives a properly
ergodic, nonperiodic flow. These correspondences connect the flow with the
[[operator-algebras/connes-type-iii-classification|Connes type III classification]].

## Why the center of the core appears

The continuous core is semifinite even when \(M\) is type III. Its center
retains the residual scaling information carried by modular automorphisms,
while the dual action records how that information changes with time.
Restricting to the center converts modular data that initially depends on a
weight into a flow intrinsic to \(M\).

## Classification scope

The flow is much finer than the single parameter
\(\lambda\) in the type label. In the separable approximately
finite-dimensional type \(\mathrm{III}_0\) case, its conjugacy class is a
complete isomorphism invariant.
It is not a complete invariant for arbitrary
[[operator-algebras/type-iii-factor|type III factors]].

## Conventions and scope

**Warning.** Replacing \(\sigma_t^\varphi\) or the dual action by the
opposite-sign convention reverses time in the displayed flow. Fourier
normalizations can also rescale the action parameter by \(2\pi\). Statements
about a numerical period must therefore declare the normalization, as the
factor-type paragraph does.

## References

1. Alain Connes and Masamichi Takesaki, “The Flow of Weights on Factors of Type III,” *Tohoku Mathematical Journal* 29 (1977), 473–575. [DOI record](https://doi.org/10.2748/tmj/1178240493). Relevant: §§4–5 on the canonical flow and its relation to type III invariants.
2. Masamichi Takesaki, *Theory of Operator Algebras II*, Springer, 2003. [DOI record](https://doi.org/10.1007/978-3-662-10451-4). Relevant: Chapter XII, §4 on the flow of weights and §5 on approximately finite-dimensional type III₀ factors.
