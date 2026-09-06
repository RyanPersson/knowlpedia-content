+++
id = "harmonic-analysis/fourier-inversion-lca"
title = "Fourier inversion theorem for locally compact abelian groups"
kind = "theorem"
summary = "The Fourier inversion theorem reconstructs a function on a locally compact abelian group from an integrable Fourier transform."
aliases = ["LCA Fourier inversion", "group Fourier inversion"]
domains = ["harmonic-analysis"]
prerequisites = ["algebra-groups/abelian-group", "topology/locally-compact-group", "harmonic-analysis/haar-measure", "harmonic-analysis/pontryagin-dual", "harmonic-analysis/dual-haar-measure", "harmonic-analysis/fourier-transform-lca", "measure-theory/almost-everywhere"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(G\) be an [[algebra-groups/abelian-group|abelian]] [[topology/locally-compact-group|locally compact group]] with [[harmonic-analysis/haar-measure|Haar measure]] \(\mu\), and give its [[harmonic-analysis/pontryagin-dual|Pontryagin dual]] \(\widehat G\) the [[harmonic-analysis/dual-haar-measure|dual Haar measure]] \(\widehat\mu\). The **Fourier inversion theorem** states that if \(f\in L^1(G,\mu)\) and its [[harmonic-analysis/fourier-transform-lca|Fourier transform]] \(\widehat f\) belongs to \(L^1(\widehat G,\widehat\mu)\), then
\[
f_0(x)=\int_{\widehat G}\widehat f(\gamma)\gamma(x)\,d\widehat\mu(\gamma)
\]
defines a continuous function vanishing at infinity, and \(f_0=f\) [[measure-theory/almost-everywhere|almost everywhere]]. The inverse integral converges absolutely for every \(x\) and uses the fixed dual normalization. Hence \(f_0(x)=f(x)\) at every point when \(f\) itself is continuous.

## Why the hypotheses matter

The two \(L^1\) assumptions make both transforms ordinary absolutely convergent integrals. Without integrability of \(\widehat f\), inversion may still hold in \(L^2\), by summability, or in the sense of distributions, but the displayed integral need not converge pointwise.

## Relation to duality

Applying Fourier transformation on \(\widehat G\) and using the evaluation isomorphism \(G\cong\widehat{\widehat G}\) from the [[harmonic-analysis/pontryagin-duality-theorem|Pontryagin duality theorem]] gives
\[
\widehat{\widehat f}(x)=f(-x)
\]
in additive notation under the convention \(\widehat f(\gamma)=\int_Gf(x)\overline{\gamma(x)}\,d\mu(x)\). The reflection changes when the transform convention changes.

## Standard examples

For \(G=\mathbb R^n\), the theorem is Euclidean Fourier inversion with the constants determined by the exponential convention. For \(G=\mathbb Z\), it reconstructs an absolutely summable sequence from its Fourier transform on the circle. On a compact abelian group, the dual is discrete and the inverse integral becomes a sum over characters.

**Warning.** An \(L^1\)-function is an [[shared-foundations/equivalence-class|equivalence class]], so the theorem canonically reconstructs a continuous representative, not arbitrary values assigned on a [[measure-theory/null-set|null set]].

## References

1. Walter Rudin, *Fourier Analysis on Groups*, Wiley-Interscience, 1962. [Wiley DOI record](https://doi.org/10.1002/9781118165621). Relevant: Chapter 1, inversion and duality.
2. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: Chapter 4, Fourier inversion on locally compact abelian groups.
