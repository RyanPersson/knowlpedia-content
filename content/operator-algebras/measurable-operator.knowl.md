+++
id = "operator-algebras/measurable-operator"
title = "Measurable operator affiliated with a von Neumann algebra"
kind = "definition"
summary = "An affiliated closed operator whose domain contains an increasing family of almost-full projections with finite complements."
aliases = ["Segal measurable operator", "measurable affiliated operator"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(M\subseteq B(H)\) be a [[operator-algebras/semifinite-von-neumann-algebra|semifinite von Neumann algebra]]. A closed densely defined
[[operator-algebras/affiliated-operator|operator affiliated with \(M\)]] is
**measurable with respect to \(M\)** if its domain is strongly dense: there are
projections \(p_n\in M\) such that \(p_n\uparrow1\) strongly,
\(p_nH\subseteq\operatorname{dom}(T)\), and each complementary projection
\(1-p_n\) is [[operator-algebras/finite-projection|finite]] in \(M\). This
condition uses Murray–von Neumann finiteness, not a numerical trace. It permits
unbounded operators while ensuring that \(T\) is bounded on successively
larger corners whose omitted parts are finite.

## Spectral characterization

Write \(E^{|T|}\) for the spectral measure of the positive operator \(|T|\).
Measurability is equivalent to the existence of \(s\geq0\) for which the
spectral tail \(E^{|T|}((s,\infty))\) is a finite projection. Once one such
tail is finite, every higher tail is finite and the projections
\(E^{|T|}([0,n])\) supply a strongly dense domain. This formulation makes the
definition independent of a chosen approximating sequence
[Nelson, pp. 103–106](https://doi.org/10.1016/0022-1236%2874%2990014-7).

## Algebra and examples

The measurable operators form a unital involutive algebra \(S(M)\) when sums,
products, and adjoints are taken with their natural closed extensions. This is
the noncommutative analogue of the algebra of almost-everywhere finite
measurable functions
[Segal, pp. 401–457](https://doi.org/10.2307/1969729).

If \(M\) is finite, every closed densely defined affiliated operator is
measurable. At the other extreme, for \(M=B(H)\) on an infinite-dimensional
Hilbert space, finite projections have finite-dimensional range and
\(S(M)=B(H)\); the definition admits no genuinely unbounded operators there
[Nelson, pp. 103–106](https://doi.org/10.1016/0022-1236%2874%2990014-7).

## Conventions and scope

**Warning.** An \(M\)-measurable operator, a
[[operator-algebras/tau-measurable-operator|\(\tau\)-measurable operator]], and
a locally measurable operator are different notions. The first uses finite
projections intrinsic to \(M\); the second uses the numerical size assigned by
a specified faithful normal semifinite trace. Some authors reserve
“measurable operator” for the trace-relative notion, so the ambient convention
must be stated.

## References

1. Irving E. Segal, “A Non-Commutative Extension of Abstract Integration,” Annals of Mathematics 57 (1953), 401–457. [DOI record](https://doi.org/10.2307/1969729). Relevant: the strongly dense domain and measurable-operator algebra.
2. Edward Nelson, “Notes on Non-Commutative Integration,” Journal of Functional Analysis 15 (1974), 103–116. [DOI record](https://doi.org/10.1016/0022-1236%2874%2990014-7). Relevant: pp. 103–106 on affiliated measurable operators and the measure topology.
