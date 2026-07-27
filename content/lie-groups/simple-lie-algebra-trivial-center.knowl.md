+++
id = "lie-groups/simple-lie-algebra-trivial-center"
title = "Center of a simple Lie algebra is trivial"
kind = "knowl"
summary = "A simple Lie algebra has zero center, since the center is always an ideal."
aliases = ["simple-lie-algebra-trivial-center", "Center of a simple Lie algebra is trivial"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/simple-lie-algebra-trivial-center.md"
+++

**Proposition.** Let \(\mathfrak g\) be a [[lie-groups/simple-lie-algebra|simple Lie algebra]]. Then
\[
Z(\mathfrak g)=\{0\},
\]
where \(Z(\mathfrak g)\) is the [[lie-groups/center-of-a-lie-algebra|center]] of \(\mathfrak g\).

## Proof

The center is an ideal, so simplicity implies that it is either \(0\) or all of \(\mathfrak g\). The second possibility would make \(\mathfrak g\) abelian, contrary to the definition of a simple Lie algebra. Equivalently, this follows from [[lie-groups/kernel-of-ad-small-is-center-lemma|the identity \(\ker(\operatorname{ad})=Z(\mathfrak g)\)]].
