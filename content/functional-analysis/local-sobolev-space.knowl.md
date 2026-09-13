+++
id = "functional-analysis/local-sobolev-space"
title = "Local Sobolev space"
kind = "definition"
summary = "Sobolev regularity on every relatively compact subdomain."
aliases = ["locally Sobolev function", "H1 local"]
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["functional-analysis/sobolev-space", "topology/relatively-compact-set", "topology/open-set"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For an open set \(\Omega\), integer \(k\ge0\), and \(1\le p\le\infty\), a function belongs to **\(W^{k,p}_{\mathrm{loc}}(\Omega)\)** if its restriction belongs to the [[functional-analysis/sobolev-space|Sobolev space]] \(W^{k,p}(U)\) for every open \(U\) whose closure is a compact subset of \(\Omega\). Write \(H^k_{\mathrm{loc}}=W^{k,2}_{\mathrm{loc}}\).

## Scope

Local membership imposes no uniform bound as the subdomains approach the boundary or fill an unbounded domain. For example, a smooth polynomial is in every local integer-order Sobolev space, but a nonzero polynomial is not in \(L^2(\mathbb R^n)\). Multiplying a locally Sobolev function by a test function gives a globally Sobolev function after zero extension.
