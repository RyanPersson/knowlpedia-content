+++
id = "fiber-bundles/numerable-principal-bundle"
title = "Numerable principal bundle"
kind = "definition"
summary = "A principal bundle with a trivializing cover admitting a locally finite continuous partition of unity."
aliases = []
domains = ["fiber-bundles", "topology"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/topological-principal-bundle", "topology/continuous-map", "topology/locally-finite-family", "topology/closure"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A [[fiber-bundles/topological-principal-bundle|topological principal bundle]] \(P\to X\) is **numerable** if it has an open trivializing cover \(\{U_i\}_{i\in I}\) and continuous functions \(\phi_i:X\to[0,1]\) such that:

1. the supports \(\operatorname{supp}\phi_i=\overline{\{x:\phi_i(x)\ne0\}}\) form a [[topology/locally-finite-family|locally finite family]];
2. \(\sum_i\phi_i(x)=1\) for all \(x\in X\);
3. \(\{x:\phi_i(x)>0\}\subseteq U_i\) for each \(i\).

The sum is locally finite, so it defines a continuous function. Numerability is the existence of these data; a particular cover and partition are not part of the bundle's structure.

## Classification setting

Every locally trivial principal bundle over a paracompact Hausdorff base is numerable, by the continuous partition-of-unity theorem. Pullback preserves numerability: pull back the trivializing cover and its functions. Universal bundles classify numerable principal bundles over arbitrary bases; the qualification matters when the base is not paracompact Hausdorff.
