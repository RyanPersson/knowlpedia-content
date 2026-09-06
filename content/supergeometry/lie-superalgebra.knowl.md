+++
id = "supergeometry/lie-superalgebra"
title = "Lie superalgebra"
kind = "definition"
summary = "A Z/2-graded vector space with a graded-skew bracket satisfying the super Jacobi identity."
aliases = ["super Lie algebra", "Z/2-graded Lie algebra"]
domains = ["supergeometry", "lie-groups"]
section_mode = "progressive"
prerequisites = ["supergeometry/super-vector-space", "linear-algebra/vector-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(k\) be a field of characteristic \(0\). A **Lie superalgebra** over \(k\)
is a [[supergeometry/super-vector-space|super vector space]]
\(\mathfrak g=\mathfrak g_{\bar0}\oplus\mathfrak g_{\bar1}\) with an even
bilinear bracket such that homogeneous \(x,y,z\) satisfy
\[
[x,y]=-(-1)^{|x||y|}[y,x]
\]
and
\[
(-1)^{|x||z|}[x,[y,z]]
+(-1)^{|y||x|}[y,[z,x]]
+(-1)^{|z||y|}[z,[x,y]]=0.
\]
The first formula is graded skew-symmetry and the second is the **super Jacobi
identity**.

## Even and odd parts

The even part \(\mathfrak g_{\bar0}\) is an ordinary
[[lie-groups/lie-algebra|Lie algebra]]. The odd part
\(\mathfrak g_{\bar1}\) is a representation of \(\mathfrak g_{\bar0}\), and
the bracket on two odd elements is a symmetric [[fiber-bundles/equivariant-map|equivariant map]]
\[
\mathfrak g_{\bar1}\otimes\mathfrak g_{\bar1}
\longrightarrow\mathfrak g_{\bar0}.
\]
It is symmetric because graded skew-symmetry gives
\([x,y]=[y,x]\) when \(x\) and \(y\) are odd.

## Morphisms

A morphism of Lie superalgebras is an even linear map that preserves brackets.
A Lie superalgebra can act on a super vector space through a
[[supergeometry/representation-of-a-lie-superalgebra|representation of a Lie
superalgebra]].

## Associative source of examples

Every associative [[supergeometry/superalgebra|superalgebra]] \(A\) becomes a
Lie superalgebra under its [[supergeometry/supercommutator|supercommutator]].
In particular, endomorphisms of a super vector space form
\(\mathfrak{gl}(V)\).

## Small-characteristic warning

The displayed sign definition is cleanest in characteristic \(0\). In
characteristic \(2\), graded skew-symmetry loses its usual meaning; in
characteristic \(3\), one must take care with the additional behavior of
\([x,[x,x]]\) for odd \(x\). Definitions over those fields therefore include
extra axioms or divided-power data and are not being silently identified with
the characteristic-zero theory here.

## References

1. M. Scheunert, *The Theory of Lie Superalgebras*, Lecture Notes in
   Mathematics 716, Springer, 1979. [DOI
   record](https://doi.org/10.1007/BFb0073442). Relevant: Chapter 1.
2. I. M. Musson, *Lie Superalgebras and Enveloping Algebras*, American
   Mathematical Society, 2012. [DOI
   record](https://doi.org/10.1090/gsm/131). Relevant: Chapters 1–2.
