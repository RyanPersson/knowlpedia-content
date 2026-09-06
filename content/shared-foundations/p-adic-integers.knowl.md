+++
id = "shared-foundations/p-adic-integers"
title = "p-adic integers"
kind = "knowl"
summary = "The compact ring obtained as the inverse limit of the residue rings modulo powers of a prime."
aliases = ["p-adic integers", "ring of p-adic integers"]
domains = ["shared-foundations", "algebra-fields-galois", "topology"]
prerequisites = ["shared-foundations/integers", "shared-foundations/sequence", "shared-foundations/p-adic-valuation", "topology/locally-compact-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Fix a prime \(p\). The ring of **\(p\)-adic [[shared-foundations/integers|integers]]** is the inverse limit
\[
\mathbb Z_p=\varprojlim_n \mathbb Z/p^n\mathbb Z.
\]
An element is a compatible [[shared-foundations/sequence|sequence]] \((a_n)\), where \(a_n\) is a residue class modulo \(p^n\) and \(a_{n+1}\equiv a_n\pmod{p^n}\). Addition and multiplication are coordinatewise.

Equivalently, \(\mathbb Z_p\) is the completion of \(\mathbb Z\) for the norm defined by the [[shared-foundations/p-adic-valuation|\(p\)-adic valuation]]. Its natural topology is compact, Hausdorff, and totally disconnected. Under addition it is therefore a [[topology/locally-compact-group|locally compact group]].
