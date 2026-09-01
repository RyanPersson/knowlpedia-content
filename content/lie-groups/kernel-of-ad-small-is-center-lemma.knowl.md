+++
id = "lie-groups/kernel-of-ad-small-is-center-lemma"
title = "Kernel of the Lie-algebra adjoint representation"
kind = "knowl"
summary = "The kernel of the adjoint representation ad is the center of the Lie algebra."
aliases = ["kernel-of-ad-small-is-center-lemma", "Kernel of the Lie-algebra adjoint representation"]
domains = ["lie-groups"]
prerequisites = ["lie-groups/lie-algebra", "lie-groups/adjoint-representation-of-a-lie-algebra", "lie-groups/center-of-a-lie-algebra"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "lie-groups/kernel-of-ad-small-is-center-lemma.md"
+++

Let \(\mathfrak g\) be a [[lie-groups/lie-algebra|Lie algebra]]. Its [[lie-groups/adjoint-representation-of-a-lie-algebra|adjoint representation]] is
\[
\mathrm{ad}:\mathfrak g\to \mathfrak{gl}(\mathfrak g),\qquad \mathrm{ad}_x(y)=[x,y].
\]

**Lemma.**
\[
\ker(\mathrm{ad}) \;=\; Z(\mathfrak g),
\]
where \(Z(\mathfrak g)\) is the [[lie-groups/center-of-a-lie-algebra|center]] of \(\mathfrak g\).

## Remarks

**Proof.** By definition, \(x\in\ker(\operatorname{ad})\) if and only if \([x,y]=0\) for every \(y\in\mathfrak g\), which is precisely the condition \(x\in Z(\mathfrak g)\).

Thus \(\operatorname{ad}_x\) depends only on the class of \(x\) modulo the center.
