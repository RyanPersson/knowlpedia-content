+++
id = "mathematical-physics/standard-model-exterior-algebra-representation"
title = "Standard Model exterior-algebra representation"
kind = "construction"
summary = "The 32-dimensional restriction of the SU(5) exterior-algebra representation to the Standard Model group."
aliases = ["Lambda C5 Standard Model representation", "SU(5) exterior algebra fermion representation"]
domains = ["mathematical-physics", "lie-groups", "algebra-modules"]
section_mode = "progressive"
+++

Let \(E=\mathbb C^2\) and \(C=\mathbb C^3\), and let
\[
\Phi(z,A,B)=\operatorname{diag}(z^3A,z^{-2}B)\in SU(E\oplus C)\cong SU(5).
\]
The **Standard Model exterior-algebra representation** is the restriction along \(\Phi\) of the natural \(SU(5)\)-action on
\[
\bigwedge(E\oplus C)=\bigoplus_{k=0}^{5}\bigwedge^k\mathbb C^5.
\]
It has complex dimension \(2^5=32\) and is isomorphic to the internal-symmetry representation on one [[mathematical-physics/standard-model-fermion-generation|fermion generation]] together with its antiparticles, when a gauge-singlet [[mathematical-physics/right-handed-neutrino-gauge-singlet|right-handed neutrino]] is included. Lorentz-spin degrees of freedom are not part of this identification.

## Decomposition into Standard Model multiplets

Write \((d_2,d_3)_Y\) for an \(SU(2)\times SU(3)\) multiplet with [[mathematical-physics/hypercharge|weak hypercharge]] \(Y\), using \(Q=T_3+Y/2\). Since
\[
E=(2,1)_1,\qquad C=(1,3)_{-2/3},
\]
the exterior degrees decompose as
\[
\begin{aligned}
\Lambda^0 &: (1,1)_0,\\
\Lambda^1 &: (2,1)_1\oplus(1,3)_{-2/3},\\
\Lambda^2 &: (1,1)_2\oplus(2,3)_{1/3}\oplus(1,\bar 3)_{-4/3},\\
\Lambda^3 &: (1,1)_{-2}\oplus(2,\bar 3)_{-1/3}\oplus(1,3)_{4/3},\\
\Lambda^4 &: (2,1)_{-1}\oplus(1,\bar 3)_{2/3},\\
\Lambda^5 &: (1,1)_0.
\end{aligned}
\]
The summands in complementary degrees are dual, as follows from the \(SU(5)\)-invariant volume form.

## Role of the two trivial summands

The degree-zero and degree-five lines are trivial representations. They are identified with a right-handed neutrino and its antiparticle, in one order or the other. Omitting a right-handed neutrino removes these two lines and leaves a \(30\)-dimensional particle-plus-antiparticle representation.

## Scope and relation to \(E_7\)

This is an isomorphism of complex representations. It neither makes wedge multiplication a physical product of particles nor includes their Lorentz-spin degrees. In the \(E_7\) construction, three \(32\)-dimensional subspaces each restrict to this same \(\mathfrak g_{\mathrm{SM}}\)-representation. Each arises as \(\Lambda^{\mathrm{even}}\mathbb C^6\) for an intermediate \(\mathfrak{sl}_6\), then restricts along \(\mathbb C^6=\mathbb C^5\oplus\mathbb C\) to \(\Lambda\mathbb C^5\).

## References

1. John C. Baez and John Huerta, “The Algebra of Grand Unified Theories,” *Bulletin of the American Mathematical Society* 47 (2010), 483–552. [arXiv record](https://arxiv.org/abs/0904.1556). Relevant: §3.1 and Table 4.
2. John C. Baez, “Three Generations in \(E_7\),” 2026. [arXiv record](https://arxiv.org/abs/2608.06271). Relevant: §§9–10, especially Theorem 12.
