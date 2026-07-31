+++
id = "langlands-letter/knowls/langlands-dual-group"
title = "Langlands Dual Group"
kind = "knowl"
summary = "The connected complex reductive group whose root datum is dual to that of a split reductive group."
aliases = ["langlands-dual-group", "Langlands Dual Group"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/langlands-dual-group.md"
+++

Let \(G\) be a split connected reductive group with maximal torus \(T\) and root datum
\[
\bigl(X^*(T),\Phi,X_*(T),\Phi^\vee\bigr).
\]
The **Langlands dual group** \(\widehat G\) is the connected complex reductive group with dual root datum
\[
\bigl(X_*(T),\Phi^\vee,X^*(T),\Phi\bigr).
\]

Here \(X^*(T)\) and \(X_*(T)\) exchange roles, as do roots and coroots. The source letter writes \(\widehat G\) as \(cG\) and uses \(cL\) for dual lattices.

## Remarks

**Key property (for Satake):**
- Unramified Hecke eigencharacters correspond to semisimple conjugacy classes in \(\widehat G\), more precisely in the [[langlands-letter/knowls/l-group-satake-parameter|\(L\)-group]].

## Examples

- \(\widehat{\operatorname{GL}_n}=\operatorname{GL}_n(\mathbb C)\), and \(\widehat{\operatorname{SL}_n}=\operatorname{PGL}_n(\mathbb C)\).
- In type \(A_1\),
  \[
  \widehat{SL_2}=PGL_2(\mathbb C),
  \qquad
  \widehat{PGL_2}=SL_2(\mathbb C).
  \]
  Duality exchanges the simply connected and adjoint isogeny forms.

## Rank-one scope warning

Over \(\mathbb C\), \(PGL_2\) is also the automorphism group of the projective
line. That geometric action does not define Langlands duality: the dual group
is determined by exchanging the root and coroot data. The same \(PGL_2\)
therefore appears in two mathematically distinct roles in
[[langlands/ramified-geometric-langlands|ramified projective-line examples]].

## References

1. Robert P. Langlands, “Problems in the theory of automorphic forms,” in
   *Lectures in Modern Analysis and Applications III*, Lecture Notes in
   Mathematics 170, Springer, 1970, 18–61.
   [DOI](https://doi.org/10.1007/BFb0079065).
