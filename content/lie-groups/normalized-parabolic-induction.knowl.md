+++
id = "lie-groups/normalized-parabolic-induction"
title = "Normalized parabolic induction"
kind = "definition"
summary = "Parabolic induction with a half-modular correction that preserves unitarity on the unitary parameter axis."
aliases = ["unitary parabolic induction", "normalized induction"]
domains = ["lie-groups", "harmonic-analysis"]
section_mode = "progressive"
+++

Let \(G\) be a [[lie-groups/real-reductive-lie-group|real reductive Lie group]], let
\(P=MAN\) be a
[[lie-groups/parabolic-subgroup-real-reductive-group|parabolic subgroup]] in
[[lie-groups/langlands-decomposition-of-a-parabolic|Langlands form]], and let
\(\tau\) be a representation of \(MA\), extended trivially across \(N\).
**Normalized parabolic induction** is the representation \(i_P^G(\tau)\)
realized with the half-modular normalization. In the right-equivariant
function convention its vectors satisfy
\[
f(gp)=\delta_P(p)^{-1/2}\tau(p)^{-1}f(g),
\]
where \(\delta_P\) is the positive
[[harmonic-analysis/modular-function|reciprocal modular function]], or
**parabolic modulus**,
\[
\delta_P(p)=\Delta_P(p)^{-1}
=\left|\det\!\left(\operatorname{Ad}(p)|_{\mathfrak n}\right)\right|.
\]
The factor \(\delta_P^{-1/2}\) is what distinguishes normalized from
unnormalized parabolic induction.

## Compact picture and unitarity

Choose a [[lie-groups/maximal-compact-subgroup-real-reductive-group|maximal compact subgroup]] \(K\) with \(G=KP\). Restriction to \(K\)
realizes the induced space using functions on \(K\) with their \(K\cap M\)
equivariance; the Hilbert norm is then independent of the continuous
induction parameter. If \(\tau\) is unitary, [[lie-groups/left-translation|left translation]] gives a unitary
representation. Equivalently, the half-modular factor in the equivariant
function model packages the Radon–Nikodym correction in
[[harmonic-analysis/unitary-induced-representation|unitary induction]]
[Knapp, Chapter VII].

## Root-theoretic form

For \(P=MAN\), let \(\rho_P\in\mathfrak a^*\) be half the sum of the positive
restricted roots occurring in \(\mathfrak n\), counted with multiplicity.
Then
\[
\delta_P(a)^{1/2}=e^{\rho_P(\log a)}
\qquad (a\in A).
\]
Thus, with the corpus convention
\(\int_P f(xp)\,dx=\Delta_P(p)^{-1}\int_P f(x)\,dx\), one has
\(\Delta_P(a)=e^{-2\rho_P(\log a)}\) and
\(\delta_P(a)=\Delta_P(a)^{-1}\).
Thus the half-modular normalization is often written as a shift by
\(\rho_P\). This shift makes [[lie-groups/knapp-stein-intertwining-operator|standard intertwining operators]] and induction in
stages take their customary symmetric forms.

## Relationship to principal series

When \(P\) is minimal and
\(\tau=\sigma\otimes e^\lambda\) on \(MA\), normalized parabolic induction
produces a [[lie-groups/principal-series-representation|principal series representation]]. Induction from larger parabolics gives generalized
principal series and the standard modules used in the Langlands
classification.

## Convention warning

**Warning.** Some authors write \(\operatorname{Ind}\) for an already
normalized functor; others reserve it for unnormalized induction and insert
\(\delta_P^{1/2}\) into the inducing representation. Reversing left and right
equivariance replaces \(\delta_P\) by its inverse. A formula is meaningful
only after these conventions are fixed; the invariant content is the
half-density correction and its preservation of the unitary axis.

## References

1. Anthony W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton University Press, 1986. [Author-maintained record](https://www.math.stonybrook.edu/~aknapp/books/repthy1.html). Relevant: Chapter VII on induced representations and the compact picture.
2. Nolan R. Wallach, *Real Reductive Groups I*, Pure and Applied Mathematics 132, Academic Press, 1988. [Publisher record](https://shop.elsevier.com/books/real-reductive-groups-i/wallach/978-0-12-732960-4). Relevant: chapters on real reductive groups, principal series, and normalized induction.
