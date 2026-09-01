+++
id = "langlands/geometric-langlands-correspondence"
title = "Categorical geometric Langlands theorem"
kind = "theorem"
summary = "In characteristic zero, the automorphic category of half-twisted D-modules on Bun_G is equivalent to the spectral category IndCoh_N on dual-group local systems."
aliases = ["geometric Langlands conjecture", "categorical geometric Langlands"]
domains = ["langlands", "algebraic-geometry-foundations"]
prerequisites = ["algebraic-geometry-foundations/smooth-projective-curve", "algebraic-geometry-foundations/reductive-algebraic-group", "langlands-letter/knowls/langlands-dual-group", "algebraic-geometry-foundations/d-module", "algebraic-geometry-foundations/moduli-stack-of-g-bundles-on-a-curve", "langlands/ind-coherent-sheaves-with-nilpotent-singular-support", "langlands/moduli-stack-of-g-local-systems", "langlands/global-nilpotent-cone"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(X\) be a [[algebraic-geometry-foundations/smooth-projective-curve|smooth
projective connected curve]] over an algebraically closed
field of characteristic \(0\), let \(G\) be a connected [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]], and
let \(\widehat G\) be its
[[langlands-letter/knowls/langlands-dual-group|Langlands dual group]]. The
modern de Rham **categorical geometric Langlands theorem** gives an
equivalence
\[
D\text{-}\operatorname{mod}_{1/2}\bigl(\operatorname{Bun}_G(X)\bigr)
\simeq
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
systems]]. Here \(\mathcal N\) is the
[[langlands/global-nilpotent-cone|global nilpotent cone]].

## Pointwise consequence

At a sufficiently regular spectral point \(E\), the correspondence predicts
an automorphic [[langlands/hecke-eigensheaf|Hecke eigensheaf]]
\(\mathcal F_E\). For every representation \(V\) of \(\widehat G\),
\[
H_V(\mathcal F_E)\simeq \mathcal F_E\boxtimes E_V.
\]
This is a sheaf-theoretic analogue of simultaneous Hecke eigenfunctions.

## Scope and status

The characteristic-zero de Rham theorem and an equivalent Betti form have
been established. Earlier work proved the torus case and numerous special
cases and constructed important families of eigensheaves.

Étale, positive-characteristic, quantum, and
[[langlands/ramified-geometric-langlands|ramified]] versions require their
own hypotheses and are not all consequences of this theorem. Thus
“geometric Langlands” also continues to name a broader program.

## Necessary spectral enlargement

Replacing the spectral category by
\(\operatorname{QCoh}(\operatorname{LocSys}_{\widehat G})\) works in the
abelian case but is generally too small. Likewise, the correspondence is not
a bijection between individual bundles and individual local systems: both
sides are categories on moduli stacks.

## Half twisting

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
4. Dennis Gaitsgory and Sam Raskin, “Proof of the geometric
   Langlands conjecture V: the multiplicity one theorem,” 2024.
   [arXiv](https://arxiv.org/abs/2409.09856).
