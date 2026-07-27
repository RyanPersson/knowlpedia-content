+++
id = "operator-algebras/continuous-core-von-neumann-algebra"
title = "Continuous core of a von Neumann algebra"
kind = "definition"
summary = "The semifinite crossed product of a von Neumann algebra by the modular automorphism group of a faithful normal semifinite weight."
aliases = ["continuous core", "core of a von Neumann algebra"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(M\) be a [[operator-algebras/von-neumann-algebra|von Neumann algebra]]
and choose a
[[operator-algebras/normal-semifinite-faithful-weight|normal semifinite
faithful weight]] \(\varphi\). The **continuous core** of \(M\), relative to
\(\varphi\), is the [[operator-algebras/von-neumann-crossed-product|von
Neumann crossed product]]
\[
c_\varphi(M)=M\rtimes_{\sigma^\varphi}\mathbb R
\]
by the [[operator-algebras/modular-automorphism-group|modular automorphism
group]]. It carries a
[[operator-algebras/dual-action-von-neumann-crossed-product|dual action]]
\(\theta:\mathbb R\curvearrowright c_\varphi(M)\) and a distinguished
[[operator-algebras/faithful-normal-semifinite-trace|faithful normal semifinite trace]] \(\tau_\varphi\), determined by the dual
weight, with \(\tau_\varphi\circ\theta_s=e^{-s}\tau_\varphi\) under the
Fourier convention used here.

## Independence of the weight

Another n.s.f. weight \(\psi\) gives a crossed product
\(c_\psi(M)\) canonically isomorphic to \(c_\varphi(M)\) after incorporating
the [[operator-algebras/connes-cocycle-derivative|Connes cocycle derivative]].
The isomorphism fixes the embedded copy of \(M\) and intertwines the dual
actions. Consequently the continuous core is usually written \(c(M)\) when
only this canonical isomorphism class matters, even though its concrete
presentation uses a weight.

## Semifiniteness and type III algebras

The core is semifinite even when \(M\) is type III and therefore has no
faithful normal semifinite trace itself. This converts modular scaling into
ordinary tracial integration on a larger algebra. Homogeneous measurable
operators in the core form the
[[operator-algebras/noncommutative-lp-space|Haagerup noncommutative
\(L^p\) spaces]], while the dual action on its center defines the
[[operator-algebras/flow-of-weights|flow of weights]].

## Conventions and scope

Some authors use the opposite modular action or Fourier character. Then the
dual action is time-reversed and the trace-scaling formula contains \(e^s\)
instead of \(e^{-s}\). These paired conventions produce isomorphic cores.
The continuous core should not be confused with the algebraic core of a
crossed product or with the core domain of a closed unbounded operator.

## References

1. Masamichi Takesaki, *Theory of Operator Algebras II*, Springer, 2003. [Publisher DOI record](https://doi.org/10.1007/978-3-662-10451-4). Relevant: Chapters X and XII on crossed products, dual weights, and the continuous decomposition.
2. Alain Connes and Masamichi Takesaki, “The Flow of Weights on Factors of Type III,” *Tohoku Mathematical Journal* 29 (1977), 473–575. [DOI record](https://doi.org/10.2748/tmj/1178240493). Relevant: §§4–5 on the core, its dual action, and the flow of weights.
