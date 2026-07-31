+++
id = "differential-geometry/maslov-index"
title = "Maslov index"
kind = "definition"
summary = "The integer measuring the winding of a loop of Lagrangian subspaces, equivalently its signed intersection with a Maslov cycle."
aliases = ["Maslov index of a path", "Lagrangian path index"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

For a loop \(\ell:S^1\to\Lambda(V)\) in the [[differential-geometry/lagrangian-grassmannian|Lagrangian Grassmannian]] of a real [[differential-geometry/symplectic-vector-space|symplectic vector space]], let \(\mu_\Lambda\) denote the [[differential-geometry/maslov-class-lagrangian-grassmannian|universal Maslov class]]. The **Maslov index** of \(\ell\) is
\[
\mu(\ell)=\left\langle\mu_\Lambda,[\ell]\right\rangle\in\mathbb Z.
\]
Equivalently, fix \(L_0\in\Lambda(V)\) and perturb \(\ell\) to meet the [[differential-geometry/maslov-cycle|Maslov cycle]] \(\Sigma(L_0)\) transversely; then \(\mu(\ell)\) is the signed crossing count. The normalization used here assigns \(+1\) to the loop of lines \(e^{\pi it}\mathbb R\subset\mathbb C\). For a path whose endpoints are transverse to \(L_0\), the same signed-intersection rule defines an integer invariant under homotopies that preserve endpoint transversality.

## Crossing-form formula

For a smooth path \(\ell:[a,b]\to\Lambda(V)\), a crossing time satisfies \(\ell(t)\cap L_0\neq0\). Its crossing form is the quadratic form on that intersection obtained by differentiating the moving plane. If all crossings are regular and the endpoints are transverse, then
\[
\mu(\ell,L_0)=\sum_{a<t<b}\operatorname{sign}\Gamma(\ell,L_0,t).
\]
This formula explains both the sign and the multiplicity of a crossing [Robbin–Salamon, §2].

## Endpoint-inclusive extension

Robbin and Salamon extend the index to paths with arbitrary endpoints. Under their convention, regular endpoint crossings contribute half their signatures:
\[
\mu_{\mathrm{RS}}(\ell,L_0)
=\tfrac12\operatorname{sign}\Gamma(a)
+\sum_{a<t<b}\operatorname{sign}\Gamma(t)
+\tfrac12\operatorname{sign}\Gamma(b).
\]
The result can be a half-integer. It is homotopy invariant with fixed endpoints, additive under concatenation, and agrees with the integer crossing count when both endpoints are transverse [Robbin–Salamon, Theorem 2.3].

## Basic properties

The loop index is additive under concatenation and under direct sum of Lagrangian paths, invariant under symplectic changes of coordinates, and changes sign when the path orientation is reversed. It depends only on the homotopy class of a loop. For an open path, by contrast, the reference Lagrangian and endpoint convention are part of the data; suppressing them can conceal a change by an endpoint correction.

## Example

In \(\mathbb R^2\cong\mathbb C\), let \(\ell(t)=e^{\pi it}\mathbb R\) for \(0\leq t\leq1\). Because lines are unoriented, the endpoints agree and \(\ell\) is a loop in \(\mathbb RP^1\). It crosses a fixed horizontal reference at the identified endpoint with positive rotation, giving index \(1\). Rotating through \(2\pi\) traverses this loop twice and has index \(2\).

## References

1. V. I. Arnol'd, “On a characteristic class entering into conditions of quantization,” *Functional Analysis and Its Applications* 1 (1967), 1–14. [DOI record](https://doi.org/10.1007/BF01079201). Relevant: the loop index as intersection with the Maslov cycle.
2. Joel Robbin and Dietmar Salamon, “The Maslov index for paths,” *Topology* 32 (1993), 827–844. [DOI record](https://doi.org/10.1016/0040-9383%2893%2990052-W). Relevant: §2, especially Theorem 2.3 and Remark 2.6.
