+++
id = "langlands/crystalline-galois-representation"
title = "Crystalline Galois representation"
kind = "definition"
summary = "A p-adic Galois representation with the full expected space of crystalline periods."
aliases = ["crystalline representation", "crystalline p-adic representation"]
domains = ["langlands", "algebra-fields-galois", "algebraic-geometry-foundations"]
prerequisites = ["langlands-letter/knowls/galois-extension-and-group", "langlands/fontaine-period-rings"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(K/\mathbb Q_p\) be finite, let \(K_0\) be the maximal unramified
subfield of \(K\), and let \(V\) be a finite-dimensional
\(\mathbb Q_p\)-representation of the
[[langlands-letter/knowls/galois-extension-and-group|absolute Galois group]]
\(G_K=\operatorname{Gal}(\overline K/K)\). Using the
[[langlands/fontaine-period-rings|Fontaine period ring]]
\(B_{\mathrm{cris}}\), set

\[
D_{\mathrm{cris}}(V)=
(B_{\mathrm{cris}}\otimes_{\mathbb Q_p}V)^{G_K}.
\]

The representation \(V\) is **crystalline** when

\[
\dim_{K_0}D_{\mathrm{cris}}(V)=\dim_{\mathbb Q_p}V.
\]

The period module has a semilinear Frobenius, and after extension from \(K_0\)
to \(K\) it has the filtration inherited from \(B_{\mathrm{dR}}\).  These data
form a filtered Frobenius module.

## Relation to reduction and monodromy

Crystalline representations are
[[langlands/semistable-galois-representation|semistable]] with monodromy
operator \(N=0\), hence are
[[langlands/de-rham-galois-representation|de Rham]].  The word “crystalline”
is not synonymous with “unramified”: a crystalline representation can have
nontrivial [[algebra-fields-galois/inertia-subgroup|inertia action]],
although its ramification is tightly constrained.

For a smooth proper variety with good reduction over \(K\), \(p\)-adic étale
cohomology is crystalline and compares with crystalline cohomology of the
special fiber.  This good-reduction paradigm motivates the terminology.

## References

1. Jean-Marc Fontaine, “Le corps des périodes \(p\)-adiques,” *Astérisque*
   223 (1994), 59–111. [Numdam](https://www.numdam.org/item/AST_1994__223__59_0/).
2. Olivier Brinon and Brian Conrad, *CMI Summer School Notes on \(p\)-adic
   Hodge Theory*, 2009, Chapters 9–10.
   [Author notes](https://math.stanford.edu/~conrad/papers/notes.pdf).
