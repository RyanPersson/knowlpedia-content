+++
id = "fiber-bundles/unit-tangent-bundle"
title = "Unit tangent bundle"
kind = "definition"
summary = "The bundle of unit tangent vectors of a Riemannian manifold."
domains = ["fiber-bundles", "differential-geometry"]
prerequisites = ["differential-geometry/riemannian-manifold", "fiber-bundles/tangent-bundle"]
dependency_heuristic = "semantic-spotcheck-review-v1"
dependency_review_count = 2
+++

Let \((M,g)\) be a [[differential-geometry/riemannian-manifold|Riemannian manifold]] and \(TM\) its [[fiber-bundles/tangent-bundle|tangent bundle]]. The **unit tangent bundle** consists of the vectors of length one:
\[
SM=\{(x,v)\in TM:g_x(v,v)=1\}.
\]
Equivalently, \(\|v\|_{g_x}=1\). Its projection is \(\pi:SM\to M\), \(\pi(x,v)=x\). Each fiber \(S_xM\) is the unit sphere in the inner-product space \(T_xM\).

## Reference

John M. Lee, *Introduction to Riemannian Manifolds*, Chapters 2–5. [Publisher record](https://doi.org/10.1007/978-3-319-91755-9).
