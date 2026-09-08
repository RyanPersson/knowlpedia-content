+++
id = "algebra-category-theory/tannakian-category"
title = "Tannakian category"
kind = "definition"
summary = "A rigid abelian tensor category reconstructed as representations of an affine group scheme by a fiber functor."
aliases = ["neutral Tannakian category", "Tannaka category", "Tannakian fiber functor", "fiber functor"]
domains = ["algebra-category-theory", "algebra-representation-theory", "langlands"]
section_mode = "progressive"
prerequisites = ["algebra-rings/field", "algebra-category-theory/abelian-category", "algebra-category-theory/symmetric-monoidal-category", "algebra-category-theory/exact-functor", "algebra-category-theory/faithful-functor"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(k\) be a [[algebra-rings/field|field]]. A **neutral Tannakian category
over \(k\)** is an essentially small (isomorphism classes form a set), \(k\)-linear
[[algebra-category-theory/abelian-category|abelian]]
[[algebra-category-theory/symmetric-monoidal-category|rigid
symmetric monoidal category]] \(\mathcal C\) with
\(\operatorname{End}(\mathbf 1)=k\), equipped with an exact faithful
\(k\)-linear strong symmetric monoidal [[algebra-category-theory/exact-functor|functor]]

\[
\omega:\mathcal C\longrightarrow\operatorname{Vect}^{\mathrm{fd}}_k.
\]

The functor \(\omega\) is a **fiber functor**.  “Rigid” means every object has
a tensor dual: maps \(e:X^\vee\otimes X\to\mathbf1\) and \(i:\mathbf1\to X\otimes X^\vee\) satisfy
\[
(\operatorname{id}_X\otimes e)\circ(i\otimes\operatorname{id}_X)=\operatorname{id}_X,
\qquad
(e\otimes\operatorname{id}_{X^\vee})\circ(\operatorname{id}_{X^\vee}\otimes i)=\operatorname{id}_{X^\vee},
\]
with the canonical associators and unitors inserted. Strong symmetric monoidality means specified natural isomorphisms \(\omega(X)\otimes\omega(Y)\cong\omega(X\otimes Y)\) and \(k\cong\omega(\mathbf1)\), compatible with associators, both unitors, and symmetries. The hom-spaces and composition are \(k\)-linear, and tensor product is \(k\)-bilinear on morphisms.

## Tannaka reconstruction

The tensor automorphisms of the fiber functor form an affine
[[algebraic-geometry-foundations/group-scheme|group scheme]]

\[
G=\operatorname{Aut}^{\otimes}(\omega),
\]

and Tannaka duality gives a tensor equivalence

\[
\mathcal C\simeq\operatorname{Rep}_k(G).
\]

Here \(\operatorname{Rep}_k(G)\) denotes finite-dimensional algebraic representations. Thus the group is reconstructed from its category of
[[algebra-representation-theory/group-representation|representations]] together
with the forgetful fiber functor.

If a fiber functor exists only after extending scalars, the category is
Tannakian but not necessarily neutral over \(k\); its fiber functors form a
gerbe rather than selecting one group scheme over \(k\).

## Langlands examples

The [[langlands/geometric-satake-equivalence|geometric Satake category]] is
Tannakian, and its Tannaka group is the
[[langlands/langlands-dual-group|Langlands dual group]].
Categories of [[fiber-bundles/local-system|local systems]] or motives, when equipped
with a suitable fiber functor, similarly produce Galois or motivic groups.

## References

1. Pierre Deligne and James S. Milne, “Tannakian Categories,” in *Hodge
   Cycles, Motives, and Shimura Varieties*, Lecture Notes in Mathematics 900,
   Springer, 1982, 101–228.
   [Milne](https://www.jmilne.org/math/xnotes/tc2018.pdf).
2. James S. Milne, “Tannakian categories: origins and summary,” 2025.
   [arXiv](https://arxiv.org/abs/2502.10945).
