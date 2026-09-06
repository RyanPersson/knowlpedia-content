+++
id = "fiber-bundles/anti-self-dual-moduli-space"
title = "Anti-self-dual moduli space"
kind = "definition"
summary = "The gauge-equivalence classes of anti-self-dual connections on a fixed principal bundle over an oriented Riemannian four-manifold."
aliases = ["instanton moduli space", "ASD connection moduli"]
domains = ["fiber-bundles", "differential-geometry"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/principal-g-bundle", "differential-geometry/riemannian-manifold", "fiber-bundles/gauge-group", "fiber-bundles/instanton"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(P\to X\) be a [[fiber-bundles/principal-g-bundle|principal bundle]] with compact structure group over an oriented [[differential-geometry/riemannian-manifold|Riemannian]] four-manifold. Write \(\mathcal A(P)\) for its connections and \(\mathcal G(P)\) for its [[fiber-bundles/gauge-group|gauge group]]. The **anti-self-dual moduli space** is
\[
\mathcal M_{\mathrm{ASD}}(P)
=\{A\in\mathcal A(P):F_A^+=0\}/\mathcal G(P),
\]
where \(F_A^+\) is the self-dual component of the curvature. Thus its points are gauge-equivalence classes of anti-self-dual connections, or [[fiber-bundles/instanton|instantons]] in the common orientation convention. Analytic constructions use compatible Sobolev completions of \(\mathcal A(P)\) and \(\mathcal G(P)\), while retaining the same smooth solutions by elliptic regularity.

## Local deformation theory

At an [[fiber-bundles/self-dual-and-anti-self-dual-connection|ASD connection]] \(A\), the [[fiber-bundles/asd-deformation-complex|ASD deformation complex]] has cohomology \(H_A^0,H_A^1,H_A^2\). Infinitesimal stabilizers form \(H_A^0\), infinitesimal deformations modulo gauge form \(H_A^1\), and \(H_A^2\) contains the obstructions. If \(A\) is irreducible and regular, a neighborhood of \([A]\) is a [[fiber-bundles/smooth-manifold|smooth manifold]] with [[differential-geometry/tangent-space|tangent space]] \(H_A^1\) and dimension equal to the index of the deformation complex.

## Singularities and compactification

[[fiber-bundles/irreducible-connection|Irreducibility]] and regularity are independent conditions. [[fiber-bundles/reducible-connection|Reducible connections]] create stabilizer singularities, while nonregular irreducible connections can have obstruction singularities. Even a smooth ASD moduli space need not be compact: sequences can concentrate curvature at finitely many points. [[fiber-bundles/uhlenbeck-compactness-theorem|Uhlenbeck compactness]] enlarges it by ideal instantons with lower [[fiber-bundles/instanton-number|instanton number]] plus bubbling points.

## Orientation convention

Reversing the orientation of \(X\) exchanges self-dual and anti-self-dual two-forms and hence exchanges the ASD and self-dual moduli spaces. Some authors use “instanton moduli space” for \(F_A^+=0\), others for \(F_A^-=0\). The displayed equation removes this ambiguity.

The ASD moduli space is a distinguished subspace of the full [[fiber-bundles/yang-mills-moduli-space|Yang–Mills moduli space]], because every ASD connection is Yang–Mills but not every [[fiber-bundles/yangmills-connection|Yang–Mills connection]] is ASD.

## References

1. Simon K. Donaldson and Peter B. Kronheimer, *The Geometry of Four-Manifolds*, Oxford University Press, 1990. [DOI record](https://doi.org/10.1093/oso/9780198535539.001.0001). Relevant: Chapter 4, ASD moduli spaces, deformation theory, and compactification.
2. Daniel S. Freed and Karen K. Uhlenbeck, *Instantons and Four-Manifolds*, 2nd ed., Springer, 1991. [DOI record](https://doi.org/10.1007/978-1-4613-9703-8). Relevant: Chapter 3, gauge quotients and local instanton moduli.
