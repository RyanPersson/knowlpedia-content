+++
id = "harmonic-analysis/plancherel-theorem-unimodular-type-i-groups"
title = "Plancherel theorem for unimodular type I groups"
kind = "theorem"
summary = "The nonabelian Fourier transform is an L2 isometry onto a direct integral of Hilbert–Schmidt operator spaces."
aliases = ["nonabelian Plancherel theorem", "abstract Plancherel formula"]
domains = ["harmonic-analysis", "lie-groups", "functional-analysis"]
section_mode = "progressive"
+++

Let \(G\) be a second-countable
[[harmonic-analysis/unimodular-group|unimodular]]
[[lie-groups/type-i-locally-compact-group|type I locally compact group]] with fixed left
[[harmonic-analysis/haar-measure|Haar measure]]. There is a unique
[[harmonic-analysis/plancherel-measure-nonabelian|Plancherel measure]]
\(\mu_{\mathrm{Pl}}\) on \(\widehat G\) such that, for
\(f\in L^1(G)\cap L^2(G)\),
\[
\lVert f\rVert_2^2
=\int_{\widehat G}\lVert\widehat f(\pi)\rVert_{\mathrm{HS}}^2\,
d\mu_{\mathrm{Pl}}(\pi).
\]
The [[harmonic-analysis/group-fourier-transform-nonabelian|nonabelian Fourier transform]] extends uniquely to a unitary map from \(L^2(G)\) onto the direct
integral of the [[linear-algebra/hilbert-space|Hilbert spaces]] of
[[functional-analysis/hilbert-schmidt-operator|Hilbert–Schmidt operators]] on the
representation spaces \(\mathcal H_\pi\). The target [[linear-algebra/inner-product|inner product]] is
obtained by integrating the Hilbert–Schmidt inner products against
\(\mu_{\mathrm{Pl}}\).

## Why the hypotheses appear

Second countability supplies the standard measurable framework, and the type
I condition makes irreducible direct-integral decomposition essentially
unique. Unimodularity removes the Duflo–Moore operators required in the
general nonunimodular formula. Thus the theorem is not merely an \(L^2\)
estimate: its clean operator-valued target depends on all three hypotheses.

## Regular-representation disintegration

Under the Plancherel transform, the
[[harmonic-analysis/regular-representations-locally-compact-group|left regular representation]] becomes fiberwise left multiplication:
\[
\widehat{\lambda_G(x)f}(\pi)=\pi(x)\widehat f(\pi).
\]
This is the
[[harmonic-analysis/direct-integral-unitary-representations|direct-integral decomposition]] of \(\lambda_G\). Its measure class is supported on the
[[harmonic-analysis/tempered-dual|tempered dual]], which explains why
Plancherel theory sees only irreducibles weakly contained in \(\lambda_G\).

## Standard special cases

For an [[algebra-groups/abelian-group|abelian group]], the fibers are
one-dimensional and the statement is the
ordinary LCA Plancherel theorem. For a compact group with Haar probability
measure, the integral becomes a sum over the discrete
[[harmonic-analysis/unitary-dual|unitary dual]] with weight
\(\dim\pi\), yielding the Peter–Weyl Parseval formula. These examples expose
the same theorem with scalar and finite-dimensional operator fibers,
respectively.

## References

1. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: Theorem 7.50 and the preceding construction of Plancherel measure.
2. Jacques Dixmier, *\(C^*\)-Algebras*, North-Holland Mathematical Library 15, North-Holland, 1977. [Publisher record](https://www.sciencedirect.com/bookseries/north-holland-mathematical-library/vol/15/suppl/C). Relevant: §18.8 on the regular representation, reduced dual, and Plancherel decomposition.
