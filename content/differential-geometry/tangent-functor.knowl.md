+++
id = "differential-geometry/tangent-functor"
title = "Tangent functor"
kind = "definition"
summary = "The covariant endofunctor on smooth manifolds that assigns tangent bundles to manifolds and differentials to smooth maps."
aliases = ["tangent bundle functor"]
domains = ["differential-geometry", "category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/functor", "differential-geometry/category-of-smooth-manifolds", "fiber-bundles/tangent-bundle", "fiber-bundles/smooth-manifold", "fiber-bundles/smooth-map", "fiber-bundles/differential-of-a-smooth-map", "real-analysis/chain-rule"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

The **tangent functor** is the covariant [[algebra-category-theory/functor|functor]]
\[
T:\mathbf{Man}\longrightarrow\mathbf{Man}
\]
on the [[differential-geometry/category-of-smooth-manifolds|category of smooth manifolds]]. It sends a manifold \(M\) to its [[fiber-bundles/tangent-bundle|tangent bundle]] \(TM\), regarded as a [[fiber-bundles/smooth-manifold|smooth manifold]], and a [[fiber-bundles/smooth-map|smooth map]] \(f:M\to N\) to the smooth map
\[
Tf:TM\longrightarrow TN,\qquad v_p\longmapsto df_p(v_p),
\]
induced by the [[fiber-bundles/differential-of-a-smooth-map|differential of \(f\)]]. The [[real-analysis/chain-rule|chain rule]] gives \(T(g\circ f)=Tg\circ Tf\), while \(T(\operatorname{id}_M)=\operatorname{id}_{TM}\); these are precisely the identity and composition axioms required of a functor.

## Bundle structure and natural maps

For each \(f:M\to N\), the map \(Tf\) is a [[fiber-bundles/bundle-map|bundle map]] over \(f\):
\[
\pi_N\circ Tf=f\circ\pi_M.
\]
Consequently, the bundle projections \(\pi_M:TM\to M\) assemble into a [[algebra-category-theory/natural-transformation|natural transformation]] \(T\Rightarrow\operatorname{Id}_{\mathbf{Man}}\). The [[fiber-bundles/zero-section|zero sections]] \(0_M:M\to TM\) similarly assemble into a natural transformation \(\operatorname{Id}_{\mathbf{Man}}\Rightarrow T\).

## Products and isomorphisms

There is a canonical diffeomorphism \(T(M\times N)\cong TM\times TN\), under which \(T(f\times g)=Tf\times Tg\). If \(f\) is a [[fiber-bundles/diffeomorphism|diffeomorphism]], then \(Tf\) is a diffeomorphism with inverse \(T(f^{-1})\). Thus [[differential-geometry/tangent-space|tangent spaces]] and differentials form one coherent construction, rather than unrelated pointwise assignments.

## Conventions and scope

This knowl concerns the ordinary first tangent functor on finite-dimensional smooth manifolds. [[differential-geometry/iterated-tangent-bundle|Iterated tangent bundles]] \(T^kM\), higher-order tangent functors, tangent functors on manifolds with corners, and tangent constructions in synthetic or infinite-dimensional differential geometry require additional conventions.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 3, tangent vectors, tangent bundles, and differentials.
2. Ivan Kolář, Peter W. Michor, and Jan Slovák, *Natural Operations in Differential Geometry*, Springer, 1993. [DOI record](https://doi.org/10.1007/978-3-662-02950-3). Relevant: Chapter VI, tangent functors and natural transformations.
