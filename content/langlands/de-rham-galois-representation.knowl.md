+++
id = "langlands/de-rham-galois-representation"
title = "De Rham Galois representation"
kind = "definition"
summary = "A p-adic Galois representation with the full expected space of de Rham periods."
aliases = ["de Rham representation", "de Rham p-adic representation"]
domains = ["langlands", "algebra-fields-galois", "algebraic-geometry-foundations"]
prerequisites = ["langlands-letter/knowls/galois-extension-and-group", "langlands/fontaine-period-rings", "langlands/hodge-tate-representation"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(K/\mathbb Q_p\) be finite, let
\(G_K=\operatorname{Gal}(\overline K/K)\) be its
[[langlands-letter/knowls/galois-extension-and-group|absolute Galois group]],
and let \(V\) be a finite-dimensional \(\mathbb Q_p\)-representation of
\(G_K\). Its space of **de Rham periods**, defined using the
[[langlands/fontaine-period-rings|Fontaine period ring]]
\(B_{\mathrm{dR}}\), is

\[
D_{\mathrm{dR}}(V)=
(B_{\mathrm{dR}}\otimes_{\mathbb Q_p}V)^{G_K},
\]

a filtered \(K\)-vector space.  The representation \(V\) is **de Rham** when

\[
\dim_KD_{\mathrm{dR}}(V)=\dim_{\mathbb Q_p}V.
\]

The decreasing filtration inherited from \(B_{\mathrm{dR}}\) encodes the
Hodge filtration.  Its jumps recover the
[[langlands/hodge-tate-representation|Hodge–Tate weights]], up to the stated
sign convention.

## Place in p-adic Hodge theory

There are implications

\[
\text{crystalline}\Longrightarrow\text{semistable}
\Longrightarrow\text{de Rham}\Longrightarrow\text{Hodge–Tate}.
\]

The \(p\)-adic monodromy theorem strengthens the middle relation: a
representation is de Rham if and only if it becomes
[[langlands/semistable-galois-representation|semistable]] after a finite
extension of \(K\).  Thus “de Rham at places above \(p\)” is a robust local
condition in automorphic constructions of Galois representations.

## Geometric origin

If \(X/K\) is smooth and proper, its \(p\)-adic étale cohomology is de Rham;
the comparison isomorphism identifies \(D_{\mathrm{dR}}\) with algebraic de
Rham cohomology. Smooth proper varieties with good reduction give
representations satisfying the stronger
[[langlands/crystalline-galois-representation|crystalline condition]].

## References

1. Olivier Brinon and Brian Conrad, *CMI Summer School Notes on \(p\)-adic
   Hodge Theory*, 2009, Chapters 4–6.
   [Author notes](https://math.stanford.edu/~conrad/papers/notes.pdf).
2. Laurent Berger, “Représentations \(p\)-adiques et équations
   différentielles,” *Inventiones Mathematicae* 148 (2002), 219–284.
   [arXiv](https://arxiv.org/abs/math/0102179).
