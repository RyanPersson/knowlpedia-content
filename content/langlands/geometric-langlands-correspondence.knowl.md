+++
id = "langlands/geometric-langlands-correspondence"
title = "Geometric Langlands correspondence"
kind = "context"
summary = "A program relating automorphic sheaves on Bun_G to spectral sheaves on the moduli of dual-group local systems."
aliases = ["geometric Langlands conjecture", "categorical geometric Langlands"]
domains = ["langlands", "algebraic-geometry-foundations"]
section_mode = "progressive"
+++

Let \(X\) be a smooth projective curve over a field of characteristic \(0\),
let \(G\) be a connected reductive group, and let \(\widehat G\) be its
[[langlands-letter/knowls/langlands-dual-group|Langlands dual group]]. The
**geometric Langlands correspondence** is the program whose modern de Rham
categorical form relates
\[
D\text{-}\operatorname{mod}_{1/2}\bigl(\operatorname{Bun}_G(X)\bigr)
\quad\text{and}\quad
\operatorname{IndCoh}_{\mathcal N}
\bigl(\operatorname{LocSys}_{\widehat G}(X)\bigr).
\]
The left side is the derived category of half-twisted
[[algebraic-geometry-foundations/d-module|\(D\)-modules]] on the
[[algebraic-geometry-foundations/moduli-stack-of-g-bundles-on-a-curve|stack
of \(G\)-bundles]]. The right side is the category of
[[langlands/ind-coherent-sheaves-with-nilpotent-singular-support|ind-coherent
sheaves with nilpotent singular support]] on the
[[langlands/moduli-stack-of-g-local-systems|stack of \(\widehat G\)-local
systems]].

## Eigensheaf form

At a sufficiently regular spectral point \(E\), the correspondence predicts
an automorphic [[langlands/hecke-eigensheaf|Hecke eigensheaf]]
\(\mathcal F_E\). For every representation \(V\) of \(\widehat G\),
\[
H_V(\mathcal F_E)\simeq \mathcal F_E\boxtimes E_V.
\]
This is a sheaf-theoretic analogue of simultaneous Hecke eigenfunctions.

## Status

“Geometric Langlands” names a family of related de Rham, Betti, étale, and
ramified statements, not one formulation with a single status.

- For tori, the correspondence reduces to a geometric Fourier transform and
  is established.
- Beilinson and Drinfeld constructed important families of eigensheaves,
  including those arising from opers.
- Many ramified and low-rank cases are theorems, including the rank-one
  pair-of-pants case.
- A five-paper 2024 preprint series led by Gaitsgory and Raskin gives a proof
  of the characteristic-zero de Rham and Betti categorical conjecture in its
  modern derived form.

Other coefficient systems, positive-characteristic forms, quantum versions,
and ramification regimes have their own statements and are not all implied by
that theorem. It remains accurate to call geometric Langlands a program and
to label historical or variant formulations as conjectural.

## Why the naive slogan is insufficient

Replacing the spectral category by
\(\operatorname{QCoh}(\operatorname{LocSys}_{\widehat G})\) works in the
abelian case but is generally too small. Likewise, the correspondence is not
a bijection between individual bundles and individual local systems: both
sides are categories on moduli stacks.

## Normalizations hidden by the slogan

The subscript \(1/2\) denotes the standard half-density, or square-root of the
canonical, twisting on the automorphic side. Precise theorem statements also
specify derived and renormalized categories, sheaf theories, coefficient
fields, and duality data. Writing an untwisted
\(D\text{-}\operatorname{mod}(\operatorname{Bun}_G)\) is a useful first
approximation, but it suppresses a real normalization rather than a cosmetic
choice.

## References

1. Alexander Beilinson and Vladimir Drinfeld, *Quantization of Hitchin’s
   Integrable System and Hecke Eigensheaves*, preprint.
   [author manuscript](https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf).
2. Dima Arinkin and Dennis Gaitsgory, “Singular support of coherent sheaves,
   and the geometric Langlands conjecture,” *Selecta Mathematica* 21 (2015),
   1–199. [arXiv](https://arxiv.org/abs/1201.6343).
3. Dennis Gaitsgory and Sam Raskin, “Proof of the geometric Langlands
   conjecture I: construction of the functor,” 2024.
   [arXiv](https://arxiv.org/abs/2405.03599).
4. Dennis Gaitsgory, Sam Raskin, and collaborators, “Proof of the geometric
   Langlands conjecture V: the multiplicity one theorem,” 2024.
   [arXiv](https://arxiv.org/abs/2409.09856).
