+++
id = "lie-groups/generation-plane"
title = "Generation plane in e7"
kind = "definition"
summary = "The real two-plane spanned by the A2 roots of the generation sl3 after choosing a compatible Cartan subalgebra."
aliases = ["generation plane", "E7 generation plane"]
domains = ["lie-groups", "mathematical-physics"]
section_mode = "progressive"
+++

Fix a [[lie-groups/good-standard-model-embedding-in-e7|good]] \(\mathfrak g_{\mathrm{SM}}\subset\mathfrak e_7\), its [[lie-groups/generation-sl3-in-e7|generation algebra]] \(\mathfrak{sl}_3^{\mathrm{gen}}\), and [[lie-groups/compatible-cartan-subalgebras|compatible Cartan subalgebras]]. If \(A\) is the resulting \(A_2\) [[lie-groups/root-system|root system]] of \(\mathfrak{sl}_3^{\mathrm{gen}}\) inside the real span \(V\) of the \(E_7\) roots, the **generation plane** is
\[
P:=\operatorname{span}_{\mathbb R}(A)\subset V.
\]
It is a two-dimensional Euclidean subspace. Its complexification \(\mathbb C\otimes_{\mathbb R}P\) is the [[lie-groups/cartan-subalgebra|Cartan subalgebra]] of \(\mathfrak{sl}_3^{\mathrm{gen}}\).

## Geometry of the A2 roots

Let \(w_1,w_2,w_3\in P\) be the [[lie-groups/weights-of-the-defining-sl3-representation|weights of the defining \(\mathfrak{sl}_3\)-module]], normalized so that the roots have squared length \(2\). Then
\[
w_1+w_2+w_3=0,
\qquad \lVert w_i\rVert^2=\frac23,
\qquad \langle w_i,w_j\rangle=-\frac13\quad(i\ne j),
\]
and
\[
A=\{w_i-w_j:i\ne j\}.
\]
The six roots form three unoriented lines in \(P\), one for each [[lie-groups/generation-sl2-subalgebras|generation \(\mathfrak{sl}_2\)]].

## What is canonical

The subalgebra \(\mathfrak{sl}_3^{\mathrm{gen}}\) is determined by the embedded \(\mathfrak g_{\mathrm{SM}}\), but \(P\) as a plane in a chosen real root space uses a compatible Cartan subalgebra and the Killing-form identification of Cartan and dual Cartan. Permuting the weights relabels the three generations; replacing a root by its negative changes an orientation convention but not its root line.

## Role in decompositions

[[linear-algebra/orthogonal-projection|Orthogonal projection]] \(\pi:V\to P\) partitions the \(E_7\) roots through the [[lie-groups/e7-root-projection-trichotomy|root-projection trichotomy]]. The Cartan summand \(\mathbb C\otimes P\), rather than all of \(\mathfrak{sl}_3^{\mathrm{gen}}\), appears in the [[lie-groups/three-generation-decomposition-of-e7|three-generation vector-space decomposition]].

## References

1. John C. Baez, “Three Generations in E7,” 2026, §§3–5. [arXiv:2608.06271](https://arxiv.org/abs/2608.06271).
