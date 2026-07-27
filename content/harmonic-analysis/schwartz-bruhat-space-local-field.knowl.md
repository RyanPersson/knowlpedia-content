+++
id = "harmonic-analysis/schwartz-bruhat-space-local-field"
title = "Schwartz–Bruhat space over a local field"
kind = "definition"
summary = "The test-function space on a local field, given by Schwartz functions at archimedean places and locally constant compactly supported functions otherwise."
aliases = ["Schwartz-Bruhat functions", "Bruhat-Schwartz functions on a local field"]
domains = ["harmonic-analysis", "number-theory"]
section_mode = "progressive"
+++

Let \(K\) be a locally compact nondiscrete field. The **Schwartz–Bruhat space** \(\mathcal S(K)\) is defined according to the type of \(K\). If \(K\cong\mathbb R\) or \(\mathbb C\), then \(\mathcal S(K)\) is the usual [[functional-analysis/schwartz-space|Schwartz space]]: its smooth functions and all their derivatives decay faster than every polynomial. If \(K\) is nonarchimedean, then
\[
\mathcal S(K)=C_c^\infty(K),
\]
the complex-valued, locally constant, compactly supported functions on the additive group of \(K\). Equivalently, each such function is constant on cosets of some open fractional ideal and vanishes outside a compact set. This is the local-field specialization of the [[harmonic-analysis/schwartz-bruhat-space-lca|Schwartz–Bruhat space on a locally compact abelian group]].

## Fourier stability

Choose a nontrivial continuous additive character \(\psi:K\to\mathbb T\) and a [[harmonic-analysis/haar-measure|Haar measure]] on the additive group of \(K\). The Fourier transform
\[
\widehat f(y)=\int_K f(x)\overline{\psi(xy)}\,dx
\]
maps \(\mathcal S(K)\) onto itself. With the self-dual normalization of Haar measure it satisfies the usual Fourier inversion formula. This common formalism lets archimedean and nonarchimedean local factors be treated in parallel [Weil, “Lattices and duality over local fields”](https://doi.org/10.1007/978-3-642-61945-8).

## Basic nonarchimedean examples

If \(\mathcal O_K\) is the valuation ring, then its indicator \(1_{\mathcal O_K}\) lies in \(\mathcal S(K)\): the ring is compact and open, so its indicator is both compactly supported and locally constant. A continuous compactly supported function need not belong to \(\mathcal S(K)\); local constancy is a defining requirement.

## Conventions and scope

The notation \(C_c^\infty(K)\) in the nonarchimedean case does not refer to derivatives. “Smooth” there means locally constant, equivalently smooth for the action of the totally disconnected additive group. For \(K=\mathbb C\), rapid decay is measured on the underlying real vector space \(\mathbb R^2\).

## References

1. André Weil, *Basic Number Theory*, 3rd ed., Springer, 1974. [DOI record](https://doi.org/10.1007/978-3-642-61945-8). Relevant: “Lattices and duality over local fields,” pp. 24–42.
2. François Bruhat, “Distributions sur un groupe localement compact et applications à l’étude des représentations des groupes \(p\)-adiques,” *Bulletin de la Société Mathématique de France* 89 (1961), 43–75. [DOI record](https://doi.org/10.24033/bsmf.1559). Relevant: pp. 60–61 on the general Schwartz–Bruhat construction.
