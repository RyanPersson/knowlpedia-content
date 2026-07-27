+++
id = "harmonic-analysis/spherical-function"
title = "Spherical function on a Gelfand pair"
kind = "definition"
summary = "A normalized bi-invariant function whose averaging product formula makes it a character of a Gelfand pair's convolution algebra."
aliases = ["zonal spherical function", "spherical function", "K-bi-invariant spherical function", "elementary spherical function"]
domains = ["harmonic-analysis", "lie-groups", "functional-analysis"]
section_mode = "progressive"
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact group]] and
\(K\leq G\) a compact subgroup such that the algebra of compactly supported
continuous \(K\)-bi-invariant functions is commutative under
[[harmonic-analysis/convolution-on-locally-compact-group|convolution]]; then
\((G,K)\) is a [[lie-groups/gelfand-pair|Gelfand pair]]. A **spherical
function** is a nonzero continuous
\(K\)-bi-invariant function \(\varphi:G\to\mathbb C\), normalized by
\(\varphi(e)=1\), that satisfies
\[
\int_K\varphi(xky)\,dk=\varphi(x)\varphi(y)
\qquad(x,y\in G),
\]
where \(dk\) is normalized [[harmonic-analysis/haar-measure|Haar measure]] on
\(K\). Equivalently,
integration against \(\varphi\) defines a nonzero multiplicative functional
on this test-function convolution algebra. The normalization excludes
nontrivial scalar rescalings and makes the product formula canonical.

## Representation-theoretic realization

If \(\pi\) is an irreducible
[[lie-groups/spherical-representation|spherical representation]] and \(v\) is
a unit \(K\)-fixed vector, then
\[
\varphi_\pi(g)=\langle\pi(g)v,v\rangle
\]
is a positive-definite spherical function. Conversely, every
[[harmonic-analysis/positive-definite-function|positive-definite]] spherical
function arises this way, up to unitary equivalence. This identifies the
positive-definite spherical spectrum with the \(K\)-spherical part of the
[[harmonic-analysis/unitary-dual|unitary dual]]
[Helgason, Chapter IV, §§2–3](https://doi.org/10.1090/surv/039).

## Convolution eigenfunctions

For every integrable \(K\)-bi-invariant \(f\), convolution by \(f\) acts on a
spherical function by a scalar determined by the
[[harmonic-analysis/spherical-transform|spherical transform]]. This
simultaneous diagonalization is the commutative harmonic analysis of the
[[lie-groups/homogeneous-space|homogeneous space]] \(G/K\); the product
formula in the core is precisely what
makes all invariant convolution operators share these eigenfunctions.

## Conventions and scope

Some sources build positive definiteness into “zonal spherical function,”
while others call every normalized convolution-algebra character
“elementary spherical.” The core adopts the broader algebraic convention, so
a spherical function need not be unitary or positive-definite. The compact
subgroup \(K\) and its normalized Haar measure are part of the setting.

## References

1. Sigurdur Helgason, *Groups and Geometric Analysis: Integral Geometry, Invariant Differential Operators, and Spherical Functions*, American Mathematical Society, 2000. [AMS record](https://doi.org/10.1090/surv/039). Relevant: Chapter IV, §§2–3 on spherical functions and class-one representations.
2. Roger Godement, “A Theory of Spherical Functions. I,” *Transactions of the American Mathematical Society* 73 (1952), 496–556. [DOI record](https://doi.org/10.1090/S0002-9947-1952-0052444-2). Relevant: the abstract theory of spherical functions and Gelfand pairs.
