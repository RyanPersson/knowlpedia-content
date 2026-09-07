+++
id = "differential-geometry/crossing-form"
title = "Crossing form"
kind = "definition"
summary = "The quadratic form that records the infinitesimal crossing of a path of Lagrangian subspaces through a fixed one."
aliases = ["Maslov crossing form", "Lagrangian crossing form"]
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["differential-geometry/symplectic-vector-space", "differential-geometry/lagrangian-subspace"]
dependency_heuristic = "semantic-full-review-v1"
+++

Let \(V\) be a finite-dimensional real [[differential-geometry/symplectic-vector-space|symplectic vector space]], let \(L_0\) be a fixed [[differential-geometry/lagrangian-subspace|Lagrangian subspace]], and let \(L(t)\) be a smooth path of Lagrangian subspaces. If \(t_0\) is a **crossing**, meaning \(L(t_0)\cap L_0\ne\{0\}\), choose a Lagrangian complement \(L_1\) of \(L(t_0)\) and write nearby \(L(t)\) as the graph of \(A(t):L(t_0)\to L_1\), using \(\omega\) to identify \(L_1\) with \(L(t_0)^*\). Its crossing form is the quadratic form
\[
\Gamma(L,L_0,t_0)(v)=\omega\bigl(v,\dot A(t_0)v\bigr),\qquad v\in L(t_0)\cap L_0.
\]
## Graph formula

This is the Robbin–Salamon convention for the graph chart; the resulting form is independent of the complement after the same symplectic identification is used.

The graph description in the core is local: the derivative \(\dot A(t_0)\) is symmetric under the identification induced by \(\omega\), so its restriction to the crossing subspace is a well-defined quadratic form.

## Regular crossings and index contributions

The crossing is **regular** when \(\Gamma(L,L_0,t_0)\) is nondegenerate. A regular crossing is isolated, and its local signed contribution to the Maslov index is the signature \(\operatorname{sign}\Gamma(L,L_0,t_0)\). Endpoint crossings require an endpoint convention; the Robbin–Salamon convention assigns half the signature at each regular endpoint.

## References

1. Joel Robbin and Dietmar Salamon, “The Maslov index for paths,” *Topology* 32 (1993), 827–844. [DOI record](https://doi.org/10.1016/0040-9383%2893%2990052-W). Relevant: §2, crossing forms and regular crossings.
2. Viktor I. Arnol'd, “On a characteristic class entering into conditions of quantization,” *Functional Analysis and Its Applications* 1 (1967), 1–14. [DOI record](https://doi.org/10.1007/BF01079201). Relevant: the Maslov cycle and its coorientation.
