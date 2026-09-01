+++
id = "lie-groups/lie-functor-commutes-with-realification"
title = "Lie functor commutes with realification"
kind = "theorem"
summary = "For a complex Lie group, taking the Lie algebra and forgetting complex scalars commute."
aliases = ["Lie algebra of an underlying real Lie group"]
domains = ["lie-groups"]
prerequisites = ["lie-groups/complex-lie-group", "algebra-category-theory/natural-isomorphism", "lie-groups/underlying-real-lie-group", "lie-groups/underlying-real-lie-algebra"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

For every [[lie-groups/complex-lie-group|complex Lie group]] \(G\), there is a [[algebra-category-theory/natural-isomorphism|natural isomorphism]] of real Lie algebras
\[
\operatorname{Lie}_{\mathbb R}(G_{\mathbb R})
\cong
\bigl(\operatorname{Lie}_{\mathbb C}G\bigr)_{\mathbb R}.
\]
Here \(G_{\mathbb R}\) is the [[lie-groups/underlying-real-lie-group|underlying real Lie group]] and the expression on the right is the [[lie-groups/underlying-real-lie-algebra|underlying real Lie algebra]].

## Why the identification holds

Both sides have the same real [[differential-geometry/tangent-space|tangent space]] \(T_eG\). Their brackets are obtained from the same [[lie-groups/left-invariant-vector-field|left-invariant vector fields]] and therefore agree. Naturality means that for a holomorphic homomorphism \(f:G\to H\), this identification intertwines the real differential of \(f_{\mathbb R}\) with the scalar restriction of the complex differential of \(f\).

Consequently, if \(G\) has complex dimension \(n\), its complex Lie algebra has complex dimension \(n\), while the Lie algebra of \(G_{\mathbb R}\) has real dimension \(2n\).

## References

1. Anthony W. Knapp, *Lie Groups Beyond an Introduction*, 2nd ed., Birkhäuser, 2002, §I.3. [Publisher record](https://doi.org/10.1007/978-1-4757-2453-0).
2. Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., Springer, 2015, Chapters 2–3. [Publisher record](https://doi.org/10.1007/978-3-319-13467-3).
