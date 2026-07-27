+++
id = "fiber-bundles/existence-of-partitions-of-unity-on-paracompact-manifolds"
title = "Existence of partitions of unity on paracompact manifolds"
kind = "knowl"
summary = "On a paracompact smooth manifold, every open cover admits a smooth partition of unity subordinate to it."
aliases = ["existence-of-partitions-of-unity-on-paracompact-manifolds", "Existence of partitions of unity on paracompact manifolds"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/existence-of-partitions-of-unity-on-paracompact-manifolds.md"
+++

Let \(M\) be a paracompact [[fiber-bundles/smooth-manifold|smooth manifold]] and let \(\{U_i\}_{i\in I}\) be an open cover of \(M\). Then there is a family of smooth functions \(\{\rho_i:M\to[0,1]\}_{i\in I}\) such that:

1. the supports \(\operatorname{supp}(\rho_i)\) form a locally finite family;
2. \(\operatorname{supp}(\rho_i)\subseteq U_i\) for every \(i\); and
3. \(\sum_{i\in I}\rho_i(x)=1\) for every \(x\in M\).

Such a family is a smooth partition of unity subordinate to the cover.

## Use

Local finiteness makes weighted sums locally finite, allowing compatible local constructions to be assembled globally. This is a standard tool for constructing metrics and [[fiber-bundles/connection-on-a-vector-bundle|connections on vector bundles]].
