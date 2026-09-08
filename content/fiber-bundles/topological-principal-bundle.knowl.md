+++
id = "fiber-bundles/topological-principal-bundle"
title = "Topological principal bundle"
kind = "definition"
summary = "A locally trivial bundle with a continuous right group action modeled equivariantly on a product."
aliases = []
domains = ["fiber-bundles", "topology"]
section_mode = "progressive"
prerequisites = ["topology/topological-group", "topology/continuous-map", "topology/homeomorphism", "topology/product-topology", "topology/open-cover"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a [[topology/topological-group|topological group]] and \(X\) a topological space. A **topological principal \(G\)-bundle** over \(X\) consists of a topological space \(P\), a continuous surjection \(\pi:P\to X\), and a continuous right action \(P\times G\to P\), \((p,g)\mapsto pg\), such that:

1. \(pe=p\), \((pg)h=p(gh)\), and \(\pi(pg)=\pi(p)\).
2. There is an [[topology/open-cover|open cover]] \(\{U_i\}\) of \(X\) and [[topology/homeomorphism|homeomorphisms]] \(\varphi_i:\pi^{-1}(U_i)\to U_i\times G\) over \(U_i\) satisfying \(\varphi_i(pg)=(x,hg)\) whenever \(\varphi_i(p)=(x,h)\).

The action is therefore free and transitive on each fiber. The topology on the local product is the [[topology/product-topology|product topology]]. A bundle isomorphism is a \(G\)-equivariant homeomorphism over the base.

## Pullback

For a continuous map \(f:Y\to X\), define \(f^*P=\{(y,p):f(y)=\pi(p)\}\) with the subspace topology from \(Y\times P\), projection \((y,p)\mapsto y\), and right action \((y,p)g=(y,pg)\). Pulling back the local trivializations gives a topological principal \(G\)-bundle over \(Y\).

## Smooth bundles and universal bundles

A [[fiber-bundles/principal-g-bundle|smooth principal bundle]] has an underlying topological principal bundle. The topological definition also applies when the base or total space is not a finite-dimensional manifold, as happens for universal bundles.
