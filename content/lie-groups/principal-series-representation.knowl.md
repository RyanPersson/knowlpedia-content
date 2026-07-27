+++
id = "lie-groups/principal-series-representation"
title = "Principal series representation"
kind = "definition"
summary = "A representation of a real reductive group obtained by normalized induction from a minimal parabolic subgroup."
aliases = ["principal series", "minimal principal series"]
domains = ["lie-groups", "harmonic-analysis"]
section_mode = "progressive"
+++

Let \(G\) be a [[lie-groups/real-reductive-lie-group|real reductive Lie group]] and let
\(P_0=MAN\) be a [[lie-groups/minimal-parabolic-subgroup|minimal parabolic subgroup]]. Given an [[lie-groups/irreducible-unitary-representation|irreducible unitary representation]] \(\sigma\) of \(M\)
and a parameter \(\lambda\in\mathfrak a_{\mathbb C}^*\), extend
\(\sigma\otimes e^\lambda\), where
\(e^\lambda(a)=e^{\lambda(\log a)}\), to \(P_0\) by making \(N\) act
trivially. The
**principal series representation** with parameters \((\sigma,\lambda)\) is
\[
I(\sigma,\lambda)
=i_{P_0}^G(\sigma\otimes e^\lambda),
\]
where \(i_{P_0}^G\) denotes
[[lie-groups/normalized-parabolic-induction|normalized parabolic induction]].
If \(\lambda\in i\mathfrak a^*\), the inducing character is unitary and
\(I(\sigma,\lambda)\) is a unitary representation.

## Compact picture

Choose a [[lie-groups/maximal-compact-subgroup-real-reductive-group|maximal compact subgroup]] \(K\) with \(G=KP_0\). Restriction to \(K\)
realizes every \(I(\sigma,\lambda)\) on the same space of functions
\(f:K\to V_\sigma\) satisfying the appropriate \(M\cap K\)-equivariance.
Only the \(G\)-action depends on \(\lambda\). This fixed-space realization
makes the analytic dependence on the parameter visible and is the standard
compact picture of the principal series
[Knapp, Chapter VII](https://www.math.stonybrook.edu/~aknapp/books/repthy1.html).

## Spherical and unitary cases

When \(\sigma\) is trivial, the family is the **spherical principal series**;
it contains a nonzero \(K\)-fixed vector. Parameters on the imaginary axis
give the unitary principal series. At exceptional parameters the induced
representation can be reducible, and [[lie-groups/complementary-series-representation|complementary series]] may remain
unitarizable for certain nonimaginary parameters. Thus “principal series”
does not by itself mean irreducible or unitary.

## Role in noncompact representation theory

Principal series supply continuous families of representations and are the
starting point for harmonic analysis on many noncompact groups. Their
irreducible subquotients include important tempered and nontempered
representations. Induction from arbitrary parabolics, rather than only
minimal ones, produces generalized principal series and the standard modules
appearing in the Langlands classification.

## Example

For \(G=\operatorname{SL}(2,\mathbb R)\), a minimal parabolic is the subgroup
of upper triangular matrices. Its compact \(M\)-factor has two characters,
and its one-dimensional split factor \(A\) contributes a complex parameter.
The resulting even and odd principal-series families are unitary on the
imaginary parameter axis and become reducible at a discrete set of
parameters.

## Conventions and scope

**Warning.** Some authors call induction from a nonminimal parabolic a
“principal series” as well; here that is called generalized principal series.
The normalized and unnormalized parameters differ by the half-sum
\(\rho\) of positive restricted roots, so reducibility points quoted in two
sources may appear shifted unless their induction conventions agree.

## References

1. Anthony W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton University Press, 1986. [Author-maintained record](https://www.math.stonybrook.edu/~aknapp/books/repthy1.html). Relevant: Chapter VII on minimal principal series, compact pictures, and intertwining operators.
2. Nolan R. Wallach, *Real Reductive Groups I*, Pure and Applied Mathematics 132, Academic Press, 1988. [Publisher record](https://shop.elsevier.com/books/real-reductive-groups-i/wallach/978-0-12-732960-4). Relevant: chapters on real reductive groups, principal series, and the Langlands classification.
