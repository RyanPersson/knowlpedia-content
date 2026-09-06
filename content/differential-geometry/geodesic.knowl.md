+++
id = "differential-geometry/geodesic"
title = "Geodesic"
kind = "definition"
summary = "A constant-speed curve whose covariant acceleration vanishes on a Riemannian manifold."
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/riemannian-manifold", "fiber-bundles/levicivita-connection-connection", "fiber-bundles/covariant-derivative-of-a-section"]
dependency_heuristic = "semantic-spotcheck-review-v1"
dependency_review_count = 2
+++

Let \((M,g)\) be a [[differential-geometry/riemannian-manifold|Riemannian manifold]] with [[fiber-bundles/levicivita-connection-connection|Levi–Civita connection]] \(\nabla\). A smooth curve \(\gamma:I\to M\) is a **geodesic** if \(\nabla_{\dot\gamma}\dot\gamma=0\) along \(I\).

## Existence and speed

Its speed \(\|\dot\gamma(t)\|_g\) is constant. Given \((x,v)\in TM\), there is a unique geodesic with \(\gamma(0)=x\) and \(\dot\gamma(0)=v\) on its maximal interval of existence. If \(\|v\|_g=1\), it is unit speed.

## Reference

[George Wilkens, Math 439 Course Notes, geodesic equations](https://math.hawaii.edu/~grw/Classes/2009-2010/2009Fall/Math442_1/439notes.pdf).
