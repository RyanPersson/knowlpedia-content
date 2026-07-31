+++
id = "harmonic-analysis/hausdorff-young-inequality-lca"
title = "Hausdorff–Young inequality on a locally compact abelian group"
kind = "theorem"
summary = "The Fourier transform maps Lp of a locally compact abelian group boundedly into Lq of its dual when 1 is at most p and p is at most 2."
aliases = ["Hausdorff-Young inequality", "Lp Fourier estimate"]
domains = ["harmonic-analysis", "measure-theory", "functional-analysis"]
section_mode = "progressive"
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact group]] that
is [[algebra-groups/abelian-group|abelian]], choose
[[harmonic-analysis/haar-measure|Haar measures]] on \(G\) and its dual
\(\widehat G\) in Plancherel duality, and let
\(1\leq p\leq2\). If \(q\) is the conjugate exponent, so
\(p^{-1}+q^{-1}=1\), then the
[[harmonic-analysis/fourier-transform-lca|Fourier transform]] extends
uniquely to a bounded map
\[
L^p(G)\longrightarrow L^q(\widehat G)
\]
satisfying
\[
\lVert\widehat f\rVert_q\leq\lVert f\rVert_p.
\]
At \(p=1\), interpret \(q=\infty\). At \(p=2\), the extension is the unitary
Plancherel transform. The statement concerns [[shared-foundations/equivalence-class|equivalence classes]] in the
corresponding [[measure-theory/lp-space|\(L^p\) spaces]]. On the dense
intersection \(L^1(G)\cap L^p(G)\), the extension agrees with the defining
Fourier integral.

## Proof mechanism

The \(p=1\) estimate follows directly from the defining integral:
\(\lvert\widehat f(\gamma)\rvert\leq\lVert f\rVert_1\). The \(p=2\) estimate
is equality by Plancherel's theorem. Complex interpolation between these
endpoint operators gives the intermediate exponents
[Folland, Chapter 4]. The constant \(1\) is
the interpolation bound for the paired Haar normalization, not necessarily
the sharp interior constant in every concrete model.

## Examples and boundary cases

For \(G=\mathbb R^n\) with the standard dual normalization, this is the
classical \(L^p(\mathbb R^n)\)-to-\(L^q(\mathbb R^n)\) Hausdorff–Young
inequality. For a compact group such as the circle, it bounds Fourier
coefficients in \(\ell^q\). The direction generally cannot be extended to
\(p>2\): an arbitrary \(L^p\) function then need not have an \(L^q\) Fourier
transform.

## Normalization and scope

Rescaling the Haar measure on \(G\) requires the reciprocal Plancherel
normalization on \(\widehat G\), and the numerical bound changes if unrelated
normalizations are chosen. The scalar theorem stated here uses commutativity.
For nonabelian groups, Hausdorff–Young inequalities require operator-valued
targets and Schatten norms rather than the displayed scalar \(L^q\) space.

## References

1. Walter Rudin, *Fourier Analysis on Groups*, Wiley-Interscience, 1962. [Wiley DOI record](https://doi.org/10.1002/9781118165621). Relevant: Chapter 1 on Fourier transformation and the Hausdorff–Young inequality.
2. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: Chapter 4 on Fourier analysis on locally compact abelian groups.
