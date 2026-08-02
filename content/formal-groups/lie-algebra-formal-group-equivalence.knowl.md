+++
id = "formal-groups/lie-algebra-formal-group-equivalence"
title = "Equivalence between Lie algebras and formal groups"
kind = "theorem"
summary = "Over a characteristic-zero field, finite-dimensional Lie algebras are equivalent to formally smooth formal groups on finite formal discs."
aliases = ["formal Lie correspondence", "Lie algebra–formal group equivalence", "finite-dimensional formal Lie theory", "Lie algebras and formal group laws"]
domains = ["formal-groups", "lie-groups"]
section_mode = "progressive"
+++

Let \(k\) be a field of characteristic \(0\). Let
\(\mathbf{LieAlg}^{\mathrm{fd}}_k\) be the category of finite-dimensional
[[lie-groups/lie-algebra|Lie algebras]] over \(k\), and let
\(\mathbf{FGrp}^{\mathrm{disc}}_k\) be the category of [[formal-groups/formal-group|formal groups]] over \(k\)
whose pointed underlying formal scheme is isomorphic to a finite-dimensional
[[formal-groups/formal-affine-space|formal disc]] \(\operatorname{Spf}k[[X_1,\ldots,X_n]]\). Then the
[[formal-groups/tangent-lie-algebra|tangent functor]]
\[
\operatorname{Lie}:
\mathbf{FGrp}^{\mathrm{disc}}_k
\longrightarrow
\mathbf{LieAlg}^{\mathrm{fd}}_k
\]
is an [[algebra-category-theory/equivalence-of-categories|equivalence of categories]].

Equivalently, every finite-dimensional Lie algebra integrates to a formal
group, every homomorphism of such Lie algebras integrates uniquely to a formal
group homomorphism, and the isomorphism class of every formal group in this
category is determined by its tangent Lie algebra. The isomorphism between two
integrations need not be unique unless an isomorphism of their tangent Lie
algebras has been specified; that specified map has a unique integrated
isomorphism.

## The BCH quasi-inverse

Given \(\mathfrak g\in\mathbf{LieAlg}^{\mathrm{fd}}_k\), take the formal
completion of its underlying [[algebraic-geometry-foundations/affine-n-space|affine space]] at \(0\). On formal points define
\[
X*Y:=\operatorname{BCH}_{\mathfrak g}(X,Y),
\]
where
[[lie-groups/baker-campbell-hausdorff-formula|\(\operatorname{BCH}\)]] is the
universal completed Lie series. Characteristic zero allows all its rational
coefficients. The formal BCH identity gives associativity, \(0\) is the
identity, and \(-X\) is the inverse.

A [[lie-groups/lie-algebra-homomorphism|Lie algebra homomorphism]] preserves every iterated bracket, hence every
homogeneous BCH term, so it gives a formal group homomorphism. This constructs
a functor
\[
\operatorname{BCH}:
\mathbf{LieAlg}^{\mathrm{fd}}_k
\longrightarrow
\mathbf{FGrp}^{\mathrm{disc}}_k
\]
quasi-inverse to \(\operatorname{Lie}\).

## Coordinate formal-group-law corollary

After choosing coordinates on each formal disc,
[[formal-groups/formal-group-laws-as-coordinates|formal groups become formal
group laws]]. Therefore the category of finite-dimensional, possibly
noncommutative [[formal-groups/formal-group-law|formal group laws]] over \(k\), with formal-group-law morphisms,
is also equivalent to \(\mathbf{LieAlg}^{\mathrm{fd}}_k\). Its tangent functor
takes
\[
F(X,Y)=X+Y+B(X,Y)+O(3)
\]
to the bracket
\([u,v]=B(u,v)-B(v,u)\).

The coordinate formulation involves a choice of basis for an abstract tangent
space; the intrinsic formal-group equivalence does not.

## Commutative one-dimensional case

A one-dimensional Lie algebra is abelian. Consequently every
[[formal-groups/one-dimensional-formal-group-law|one-dimensional formal group law]] over a characteristic-zero field is
isomorphic to the additive law, and every
[[formal-groups/one-dimensional-formal-group-law|commutative one-dimensional
law]] has its more explicit [[formal-groups/formal-group-logarithm|formal
logarithm]]. Integral and positive-characteristic forms are much richer
because that logarithm may require unavailable denominators.

## What the theorem does not say

- It is not an equivalence between Lie algebras and global Lie groups.
  [[topology/fundamental-group|Fundamental groups]], disconnected components, lattices, and other global
  data disappear upon formal completion.
- It does not classify arbitrary formal schemes carrying group structures;
  the underlying pointed object must be a finite-dimensional formally smooth
  formal disc.
- It fails in characteristic \(p>0\): tangent brackets do not see height,
  Frobenius, or the full \(p\)-series.
- Pronilpotent and [[lie-groups/complete-filtered-lie-algebra|complete filtered Lie algebras]] admit broader BCH
  correspondences, but they require their own completeness hypotheses and are
  not part of this finite-dimensional statement.

## References

1. A. Fröhlich, *Formal Groups*, Lecture Notes in Mathematics 74, Springer, 1968. [Publisher record](https://link.springer.com/book/10.1007/BFb0074373). Relevant: Chapter 2, Lie theory.
2. Nicolas Bourbaki, *Lie Groups and Lie Algebras: Chapters 1–3*, Springer, 1989. [Publisher record](https://link.springer.com/book/9783540642428). Relevant: Chapter 2, formal exponential, logarithmic, and Hausdorff series.
3. Michiel Hazewinkel, *Formal Groups and Applications*, AMS Chelsea Publishing, 2012. [AMS book record](https://bookstore.ams.org/chel-375-h). Relevant: Chapter 2 and the Lie-theory portion of the text.
