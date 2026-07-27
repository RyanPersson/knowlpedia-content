+++
id = "harmonic-analysis/plancherel-theorem-lca"
title = "Plancherel theorem for locally compact abelian groups"
kind = "theorem"
summary = "The Plancherel theorem extends Fourier transformation to a unitary operator between the L2 spaces of a locally compact abelian group and its dual."
aliases = ["L2 Fourier transform", "Parseval-Plancherel theorem"]
domains = ["harmonic-analysis", "functional-analysis"]
section_mode = "progressive"
+++

Let \(G\) be an [[algebra-groups/abelian-group|abelian]] [[topology/locally-compact-group|locally compact group]] with [[harmonic-analysis/haar-measure|Haar measure]] \(\mu\), and equip its [[harmonic-analysis/pontryagin-dual|Pontryagin dual]] \(\widehat G\) with the [[harmonic-analysis/dual-haar-measure|dual Haar measure]] \(\widehat\mu\). The **Plancherel theorem** states that the [[harmonic-analysis/fourier-transform-lca|Fourier transform]], initially defined on \(L^1(G,\mu)\cap L^2(G,\mu)\), extends uniquely to a [[functional-analysis/unitary-operator|unitary operator]] between complex [[linear-algebra/hilbert-space|Hilbert spaces]],
\[
\mathcal F_2:L^2(G,\mu)\longrightarrow L^2(\widehat G,\widehat\mu).
\]
Thus \(\|\mathcal F_2f\|_2=\|f\|_2\), and the inverse unitary is the \(L^2\)-extension of inverse Fourier transformation. In particular, the extension preserves Hilbert-space [[linear-algebra/inner-product|inner products]] as well as norms.

## Meaning of the extension

An arbitrary \(L^2\)-function need not be integrable, so its Fourier transform need not be given by a pointwise convergent integral. Choose \(f_n\in L^1(G)\cap L^2(G)\) with \(f_n\to f\) in \(L^2(G)\); then \(\widehat f_n\) converges in \(L^2(\widehat G)\), and its limit is \(\mathcal F_2f\). Unitarity makes the limit independent of the approximating sequence. The density and extension argument is part of the standard LCA Plancherel theorem [Folland, Chapter 4](https://doi.org/10.1201/B19172).

## Parseval identity and normalization

For \(f,g\in L^2(G)\), unitarity yields
\[
\langle f,g\rangle_{L^2(G)}
=
\langle \mathcal F_2f,\mathcal F_2g\rangle_{L^2(\widehat G)}.
\]
This Parseval identity includes the norm equality as the case \(g=f\). The theorem also fixes the normalization of \(\widehat\mu\): multiplying \(\mu\) by \(c>0\) requires multiplying \(\widehat\mu\) by \(c^{-1}\).

## Standard examples

For \(G=\mathbb R^n\) with characters \(x\mapsto e^{2\pi i x\cdot\xi}\), both Haar measures are [[measure-theory/lebesgue-measure|Lebesgue measure]] and \(\mathcal F_2\) is the usual unitary Euclidean Fourier transform. For \(G=\mathbb Z\) with counting measure, the theorem identifies \(\ell^2(\mathbb Z)\) unitarily with \(L^2(\mathbb T)\) for normalized Haar measure on the circle.

**Warning.** The theorem gives an \(L^2\)-equivalence class, not pointwise values. Pointwise recovery requires additional hypotheses supplied by Fourier inversion.

## References

1. Walter Rudin, *Fourier Analysis on Groups*, Wiley-Interscience, 1962. [Wiley DOI record](https://doi.org/10.1002/9781118165621). Relevant: Chapter 1, Fourier transformation and the Plancherel theorem.
2. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: Chapter 4, Fourier analysis on locally compact abelian groups.
