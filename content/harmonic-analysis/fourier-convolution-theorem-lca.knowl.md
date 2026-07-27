+++
id = "harmonic-analysis/fourier-convolution-theorem-lca"
title = "Fourier convolution theorem on a locally compact abelian group"
kind = "theorem"
summary = "On a locally compact abelian group, the Fourier transform changes convolution into pointwise multiplication on the Pontryagin dual."
aliases = ["convolution theorem", "Fourier transform of convolution", "Fourier convolution theorem on an abelian group"]
domains = ["harmonic-analysis", "functional-analysis", "algebra-groups"]
section_mode = "progressive"
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact group]] that is [[algebra-groups/abelian-group|abelian]], with a fixed [[harmonic-analysis/haar-measure|Haar measure]]. For \(f,g\in L^1(G)\), define their [[harmonic-analysis/convolution-on-locally-compact-group|convolution]] using that measure. The **Fourier convolution theorem** states that
\[
\widehat{f*g}(\gamma)=\widehat f(\gamma)\widehat g(\gamma)
\qquad(\gamma\in\widehat G),
\]
where hats denote the [[harmonic-analysis/fourier-transform-lca|Fourier transform]] on \(G\) and \(\widehat G\) is the [[harmonic-analysis/pontryagin-dual|Pontryagin dual]]. Thus the Fourier transform is an [[algebra-modules/algebra-homomorphism|algebra homomorphism]] from the convolution algebra \(L^1(G)\) to continuous functions on \(\widehat G\) with pointwise multiplication.

## Proof mechanism

Expanding the definitions gives
\[
\widehat{f*g}(\gamma)
=\int_G\int_G f(y)g(y^{-1}x)\overline{\gamma(x)}\,dy\,dx.
\]
Absolute integrability permits [[measure-theory/fubinis-theorem|Fubini's theorem]]. The substitution \(x=yz\), left invariance of Haar measure, and \(\gamma(yz)=\gamma(y)\gamma(z)\) split the double integral into \(\widehat f(\gamma)\widehat g(\gamma)\). This calculation also explains exactly where commutativity enters: it makes scalar characters sufficient to diagonalize convolution [Folland, Chapter 4](https://doi.org/10.1201/B19172).

## Analytic consequences

Convolution operators become multiplication operators after Fourier transformation. With the [[harmonic-analysis/dual-haar-measure|dual Haar measure]], the [[harmonic-analysis/plancherel-theorem-lca|Plancherel theorem]] therefore converts suitable translation-invariant operators on \(L^2(G)\) into multiplication by Fourier multipliers. The identity also shows that zeros of Fourier transforms control invertibility and ideal structure in the commutative [[harmonic-analysis/l1-group-algebra|\(L^1\) group algebra]].

## Examples and conventions

For \(G=\mathbb R^n\), this is the classical identity \(\mathcal F(f*g)=(\mathcal Ff)(\mathcal Fg)\). For \(G=\mathbb Z\), convolution of sequences becomes multiplication of Fourier series on the circle. Changing the sign or \(2\pi\) convention in both transforms leaves the product identity unchanged.

**Warning.** The companion assertion that the Fourier transform of a pointwise product is a convolution requires additional integrability hypotheses and depends on the normalization of dual Haar measure.

## References

1. W. Rudin, *Fourier Analysis on Groups*, Wiley-Interscience, 1962. [DOI record](https://doi.org/10.1002/9781118165621). Relevant: Fourier transforms and convolution on locally compact abelian groups.
2. G. B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: Chapter 4, Fourier analysis on locally compact abelian groups.
