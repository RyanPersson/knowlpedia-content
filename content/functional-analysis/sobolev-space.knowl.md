+++
id = "functional-analysis/sobolev-space"
title = "Sobolev space"
kind = "definition"
summary = "A function space whose weak derivatives through a specified order are integrable to a fixed power."
aliases = ["W^{k,p} space", "H^k space"]
domains = ["functional-analysis", "partial-differential-equations"]
section_mode = "progressive"
+++

Let \(\Omega\subseteq\mathbb R^n\) be open, let \(k\) be a nonnegative
integer, and let \(1\leq p\leq\infty\). The **Sobolev space**
\(W^{k,p}(\Omega)\) consists of equivalence classes of functions
\(u\in L^p(\Omega)\) whose [[functional-analysis/weak-derivative|weak
derivatives]] \(D^\alpha u\) belong to \(L^p(\Omega)\) for every multi-index
\(\alpha\) with \(|\alpha|\leq k\). For \(p<\infty\), its standard norm is
\[
\lVert u\rVert_{W^{k,p}}
=\left(\sum_{|\alpha|\leq k}\lVert D^\alpha u\rVert_{L^p}^p\right)^{1/p};
\]
for \(p=\infty\), use the maximum of the essential-supremum norms. This norm
makes \(W^{k,p}(\Omega)\) a [[linear-algebra/banach-space|Banach space]].

## Hilbert and fractional cases

When \(p=2\), \(W^{k,2}(\Omega)\) is a
[[linear-algebra/hilbert-space|Hilbert space]] and is commonly denoted
\(H^k(\Omega)\). For noninteger \(s\), the notation \(H^s\) usually denotes
a fractional Sobolev space defined by Fourier multipliers, interpolation, or
local charts. On sufficiently regular domains these constructions agree in
their appropriate ranges, but boundary behavior and quotient-versus-
restriction definitions must be specified
[Adams--Fournier, Chapters 3 and 7](https://www.sciencedirect.com/book/9780120441433/sobolev-spaces).

## Completeness, density, and traces

Weak differentiation is closed under \(L^p\)-convergence, which underlies
completeness. On an arbitrary open set, \(C_c^\infty(\Omega)\) is dense in
\(W^{k,p}_0(\Omega)\) by definition, but it need not be dense in all of
\(W^{k,p}(\Omega)\). On domains with suitable boundary regularity, trace
theorems assign boundary values to Sobolev functions even though pointwise
restriction is not defined for a general \(L^p\)-class.

## Examples and non-examples

The function \(u(x)=|x|\) lies in \(W^{1,\infty}((-1,1))\), with weak
derivative \(\operatorname{sgn}(x)\), although it is not classically
differentiable at zero. A jump discontinuity on an interval lies in
\(L^p\) but not in \(W^{1,p}\) for \(p\geq1\), because its distributional
derivative contains a point mass rather than an \(L^p\)-function.

## Conventions and scope

**Warning.** Sobolev spaces consist of almost-everywhere equivalence classes.
Pointwise values become meaningful only after choosing suitable
representatives under an embedding or trace theorem. On manifolds and vector
bundles, defining a Sobolev norm requires charts, a connection, a metric, or
an equivalent auxiliary construction; equivalence of resulting norms needs
hypotheses such as compactness and bounded geometry.

## References

1. Robert A. Adams and John J. F. Fournier, *Sobolev Spaces*, 2nd ed., Academic Press, 2003. [Publisher record](https://www.sciencedirect.com/book/9780120441433/sobolev-spaces). Relevant: Chapters 3 and 7 on integer-order and fractional Sobolev spaces.
2. Lawrence C. Evans, *Partial Differential Equations*, 2nd ed., American Mathematical Society, 2010. [DOI record](https://doi.org/10.1090/gsm/019). Relevant: Chapter 5 on Sobolev spaces, approximation, extensions, and traces.
