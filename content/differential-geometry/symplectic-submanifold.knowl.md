+++
id = "differential-geometry/symplectic-submanifold"
title = "Symplectic submanifold"
kind = "definition"
summary = "An embedded submanifold on which the ambient symplectic form restricts nondegenerately."
aliases = ["nondegenerate submanifold"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/symplectic-manifold", "fiber-bundles/smooth-embedding", "differential-geometry/symplectic-subspace"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((M,\omega)\) be a [[differential-geometry/symplectic-manifold|symplectic manifold]] and let \(\iota:S\hookrightarrow M\) be a [[fiber-bundles/smooth-embedding|smooth embedding]]. The image, or equivalently \(S\) with this embedding, is a **symplectic submanifold** if the pulled-back form
\[
\omega_S=\iota^*\omega
\]
is nondegenerate. Since \(d\omega_S=\iota^*(d\omega)=0\), this makes \((S,\omega_S)\) a symplectic manifold. Pointwise, the condition is that \(d\iota_p(T_pS)\) be a [[differential-geometry/symplectic-subspace|symplectic subspace]] of \(T_{\iota(p)}M\) for every \(p\in S\). In particular, \(S\) has even dimension.

## Normal splitting

At each point of a symplectic submanifold,
\[
T_{\iota(p)}M=d\iota_p(T_pS)\oplus d\iota_p(T_pS)^\omega.
\]
The [[differential-geometry/symplectic-orthogonal-complement|symplectic orthogonal]] spaces form a smooth [[fiber-bundles/vector-bundle|vector bundle]] over \(S\), called the [[differential-geometry/normal-bundle|symplectic normal bundle]], and the restriction of \(\omega\) to that bundle is nondegenerate. This is the linear splitting behind symplectic neighborhood results.

## Examples and contrasts

Every open symplectic submanifold is symplectic with the restricted form. In the product
\[
(M_1\times M_2,\operatorname{pr}_1^*\omega_1+\operatorname{pr}_2^*\omega_2),
\]
the slice \(M_1\times\{p\}\) is symplectic. A [[differential-geometry/complex-submanifold|complex submanifold]] of a [[differential-geometry/kahler-manifold|Kähler manifold]] is symplectic for the restricted [[differential-geometry/kahler-form|Kähler form]].

An [[differential-geometry/isotropic-submanifold|isotropic submanifold]] instead has zero restricted form. A positive-dimensional [[differential-geometry/lagrangian-submanifold|Lagrangian submanifold]] is therefore never symplectic. A [[differential-geometry/coisotropic-submanifold|coisotropic submanifold]] may have a nonzero kernel; if a submanifold is both symplectic and coisotropic, it is open in the ambient manifold.

## Conventions and scope

Some sources permit symplectic immersions and speak of “immersed symplectic submanifolds.” This knowl uses the embedded convention: the map \(\iota\) is an embedding, and its image carries the [[topology/subspace-topology|subspace topology]]. Nondegeneracy alone implies closedness of the restricted form only because the ambient form \(\omega\) is already closed.

## References

1. Dusa McDuff and Dietmar Salamon, *Introduction to Symplectic Topology*, 3rd ed., Oxford University Press, 2017. [Oxford DOI record](https://doi.org/10.1093/oso/9780198794899.001.0001). Relevant: §3.3, symplectic submanifolds and symplectic normal bundles.
2. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2008. [Springer DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: symplectic submanifolds and local models.
