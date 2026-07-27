+++
id = "topology/cup-product-and-cohomology-ring"
title = "Cup product and cohomology ring"
kind = "definition"
summary = "The natural graded multiplication on singular cohomology induced by multiplying cochains."
aliases = ["cup product", "cohomology ring", "graded cohomology ring"]
domains = ["topology"]
section_mode = "progressive"
+++

Let \(X\) be a [[topology/topological-space|topological space]] and \(R\) a [[algebra-rings/commutative-ring|commutative ring with identity]]. The **cup product** is the natural bilinear operation
\[
\smile:H^p(X;R)\times H^q(X;R)\longrightarrow H^{p+q}(X;R)
\]
on [[topology/singular-cohomology-group|singular cohomology]]. It is induced by multiplying cochains after restricting a singular \((p+q)\)-simplex to its front \(p\)-face and back \(q\)-face. With this multiplication and the class \(1\in H^0(X;R)\), the [[algebra-modules/graded-module|graded module]]
\[
H^*(X;R)=\bigoplus_{n\geq 0}H^n(X;R)
\]
is the **cohomology ring** of \(X\).

## Cochain construction

For \(\alpha\in C^p(X;R)\), \(\beta\in C^q(X;R)\), and a singular simplex \(\sigma:\Delta^{p+q}\to X\), the Alexander–Whitney convention gives
\[
(\alpha\smile\beta)(\sigma)
=
\alpha(\sigma|[v_0,\ldots,v_p])\,
\beta(\sigma|[v_p,\ldots,v_{p+q}]).
\]
The identity
\[
\delta(\alpha\smile\beta)
=
\delta\alpha\smile\beta+(-1)^p\alpha\smile\delta\beta
\]
shows that the product descends to cohomology. Different standard cochain models induce the same product on cohomology; see [Hatcher, §3.2](https://pi.math.cornell.edu/~hatcher/AT/ATchapters.html).

## Algebraic properties

The cup product is associative, unital, natural under pullback, and graded-commutative:
\[
a\smile b=(-1)^{pq}b\smile a
\]
for \(a\in H^p(X;R)\) and \(b\in H^q(X;R)\). Consequently \(H^*(X;R)\) is a graded-commutative [[algebra-modules/graded-ring|graded ring]]. The ring structure can distinguish spaces whose cohomology groups are additively isomorphic.

## Examples and scope

If \(x\in H^2(\mathbb{CP}^n;\mathbb Z)\) is the standard generator, then
\[
H^*(\mathbb{CP}^n;\mathbb Z)\cong\mathbb Z[x]/(x^{n+1}).
\]
By contrast, all positive-degree products vanish in the reduced cohomology ring of a suspension.

**Warning.** The coefficient ring is part of the structure: signs, torsion, and even whether odd-degree squares vanish can change with \(R\).

## References

1. Allen Hatcher, *Algebraic Topology*, Cambridge University Press, 2002. [Author-hosted book record](https://pi.math.cornell.edu/~hatcher/AT/ATpage.html). Relevant: §3.2, cup product and the cohomology ring.
