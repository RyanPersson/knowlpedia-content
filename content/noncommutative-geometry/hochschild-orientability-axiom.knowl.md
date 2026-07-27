+++
id = "noncommutative-geometry/hochschild-orientability-axiom"
title = "Hochschild orientability axiom for a spectral triple"
kind = "definition"
summary = "The requirement that a Hochschild cycle be represented by the grading in even parity or the identity in odd parity."
aliases = ["orientability cycle", "Hochschild orientation", "chirality Hochschild cycle"]
domains = ["noncommutative-geometry", "algebra-homological"]
section_mode = "progressive"
+++

An \(n\)-dimensional [[noncommutative-geometry/real-spectral-triple|real spectral triple]] \((\mathcal A,H,D,J)\) satisfies the **Hochschild orientability axiom** if there is a [[noncommutative-geometry/hochschild-cycle|Hochschild \(n\)-cycle]]
\[
c=\sum_j(a_j^0\otimes (b_j^0)^{\mathrm{op}})\otimes a_j^1\otimes\cdots\otimes a_j^n
\]
with coefficients in \(\mathcal A\otimes\mathcal A^{\mathrm{op}}\) such that
\[
\pi_D(c)=\sum_j a_j^0J(b_j^0)^*J^{-1}[D,a_j^1]\cdots[D,a_j^n]
\]
equals the grading \(\Gamma\) for an [[noncommutative-geometry/even-spectral-triple|even spectral triple]] and the identity operator in odd parity. Thus an algebraic orientation cycle reproduces the analytic chirality operator. In formulations without a real structure, one instead uses an ordinary Hochschild cycle and omits the opposite-algebra factor.

## Geometric model

For the canonical spectral triple of a closed oriented spin manifold, the antisymmetrized Hochschild cycle corresponding to the volume form is sent by \(\pi_D\) to Clifford multiplication by that volume form. After the standard normalization, this is chirality in even dimension and the identity in odd dimension. This is the model for the abstract axiom [Connes, chapter VI](https://www.alainconnes.org/docs/book94bigpdf.pdf).

## Role and limitations

Orientability is one of several independent geometric hypotheses in spectral reconstruction. Regularity, finiteness, absolute continuity, first order, and Poincaré duality are not consequences of the existence of \(c\). In the commutative reconstruction theorem, orientability helps produce local coordinate data, but the manifold conclusion uses the full axiom system [Rennie and Várilly, §3.1](https://arxiv.org/abs/math/0610418).

**Warning.** Twisted spectral triples, nonunital algebras, and manifolds with boundary may require twisted, local, or relative versions of Hochschild homology. The formula above is the standard unital real convention.

## References

1. A. Connes, *Noncommutative Geometry*, Academic Press, 1994. [Author-maintained text](https://www.alainconnes.org/docs/book94bigpdf.pdf). Relevant: chapter VI on the orientability cycle and its representation.
2. A. Connes, “Gravity Coupled with Matter and the Foundation of Non-Commutative Geometry,” *Communications in Mathematical Physics* 182 (1996), 155–176. [DOI record](https://doi.org/10.1007/BF02506388). Relevant: the real spectral-geometric axioms and represented Hochschild cycles.
3. A. Rennie and J. C. Várilly, “Reconstruction of Manifolds in Noncommutative Geometry,” 2007. [Stable preprint](https://arxiv.org/abs/math/0610418). Relevant: §3.1 on orientability among the reconstruction hypotheses.
