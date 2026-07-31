+++
id = "differential-geometry/sheaf-of-smooth-functions"
title = "Sheaf of smooth functions"
kind = "definition"
summary = "The sheaf assigning to each open subset of a smooth manifold its algebra of smooth real-valued functions."
aliases = ["smooth structure sheaf", "C-infinity sheaf", "C∞_M"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(M\) be a [[fiber-bundles/smooth-manifold|smooth manifold]]. Its **sheaf of smooth functions**, denoted \(C^\infty_M\), assigns to every open set \(U\subseteq M\) the commutative unital real algebra
\[
C^\infty_M(U)=\{f:U\to\mathbb R\mid f\text{ is smooth}\},
\]
with restriction maps given by restricting functions. Smooth functions that agree on overlaps glue uniquely, and smoothness can be checked locally in charts, so \(C^\infty_M\) is a [[algebraic-geometry-foundations/sheaf|sheaf]] of \(\mathbb R\)-algebras. The pair \((M,C^\infty_M)\) is the smooth manifold regarded as a [[algebraic-geometry-foundations/locally-ringed-space|locally ringed space]].

Each \(C^\infty_M(U)\) also has its canonical
[[differential-geometry/c-infinity-ring|\(C^\infty\)-ring]] operations,
defined by pointwise smooth functional calculus, and restriction preserves
all these operations. Thus \(C^\infty_M\) is a sheaf of \(C^\infty\)-rings,
and \((M,C^\infty_M)\) is naturally a
[[differential-geometry/locally-c-infinity-ringed-space|locally
\(C^\infty\)-ringed space]]. Forgetting the extra operations recovers the
ordinary locally ringed space above.

## Stalks and local structure

The [[algebraic-geometry-foundations/stalk|stalk]] \(C^\infty_{M,p}\) consists of germs of smooth real-valued functions near \(p\). It is a [[algebra-commutative/local-ring|local ring]]: its unique [[algebra-rings/maximal-ideal|maximal ideal]] contains exactly the germs that vanish at \(p\), and evaluation at \(p\) identifies the [[algebra-commutative/residue-field|residue field]] with \(\mathbb R\). Unlike the holomorphic case, a smooth germ is not determined by its Taylor series; nonzero flat germs have every derivative equal to zero at the base point.

## Pullback and geometric meaning

Every [[fiber-bundles/smooth-map|smooth map]] \(F:M\to N\) pulls functions back by composition and therefore induces local homomorphisms
\[
C^\infty_{N,F(p)}\longrightarrow C^\infty_{M,p}.
\]
These are local \(C^\infty\)-ring homomorphisms, not merely homomorphisms of
the underlying real algebras.
The sheaf records the smooth structure algebraically: [[fiber-bundles/vector-field|vector fields]] act as local derivations of it, differential forms can be organized as modules over it, and [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|partitions of unity]] let local smooth constructions be patched globally.

## Conventions and scope

**Warning.** Here the coefficient field is \(\mathbb R\). Complex-valued smooth functions form the complexification \(C^\infty_M\otimes_{\mathbb R}\mathbb C\), not the [[differential-geometry/sheaf-of-holomorphic-functions|sheaf of holomorphic functions]]. The notation \(C^\infty(M)\) denotes global sections, while \(C^\infty_M\) denotes the entire sheaf. “Smooth [[algebraic-geometry-foundations/structure-sheaf|structure sheaf]]” should not be confused with a single algebra of functions unless the open set is specified.

## References

1. Jet Nestruev, *Smooth Manifolds and Observables*, 2nd ed., Graduate Texts in Mathematics 220, Springer, 2020. [Publisher record](https://doi.org/10.1007/978-3-030-45650-4). Relevant: Chapters 1–5, smooth functions and the algebraic description of manifolds.
2. Ieke Moerdijk and Janez Mrčun, *Introduction to Foliations and Lie Groupoids*, Cambridge Studies in Advanced Mathematics 91, Cambridge University Press, 2003. [Publisher record](https://doi.org/10.1017/CBO9780511615450). Relevant: prerequisites and Appendix A, smooth manifolds, sheaves, and partitions of unity.
3. Dominic Joyce, “Algebraic Geometry over \(C^\infty\)-rings,” *Memoirs of the AMS* 260 (2019). [arXiv version](https://arxiv.org/abs/1001.0023). Relevant: \(C^\infty\)-rings and \(C^\infty\)-ringed spaces.
