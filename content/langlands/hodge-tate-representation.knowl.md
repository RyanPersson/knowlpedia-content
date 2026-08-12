+++
id = "langlands/hodge-tate-representation"
title = "Hodge–Tate representation"
kind = "definition"
summary = "A p-adic Galois representation that splits over C_p into integral Tate twists."
aliases = ["Hodge-Tate representation", "Hodge–Tate weights", "Hodge-Tate weights"]
domains = ["langlands", "algebra-fields-galois", "algebraic-geometry-foundations"]
section_mode = "progressive"
+++

Let \(K/\mathbb Q_p\) be a finite extension, let \(G_K\) be its
[[langlands-letter/knowls/galois-extension-and-group|absolute Galois group]],
and let \(V\) be a finite-dimensional \(\mathbb Q_p\)-representation of \(G_K\).
It is **Hodge–Tate** if there is a \(G_K\)-equivariant decomposition

\[
\mathbb C_p\otimes_{\mathbb Q_p}V
\simeq\bigoplus_{i\in\mathbb Z}
\mathbb C_p(-i)^{m_i}.
\]

The integers \(i\), repeated with multiplicity \(m_i\), are the Hodge–Tate
weights in the convention used here.  Some authors attach weight \(-i\) to
\(\mathbb Q_p(i)\), so signs must be checked when comparing sources.

## Period-ring criterion

With the
[[langlands/fontaine-period-rings|Fontaine period ring]]
\(B_{\mathrm{HT}}=\bigoplus_{i\in\mathbb Z}\mathbb C_p(i)\), set

\[
D_{\mathrm{HT}}(V)=
(B_{\mathrm{HT}}\otimes_{\mathbb Q_p}V)^{G_K}.
\]

Then \(V\) is Hodge–Tate exactly when the total \(K\)-dimension of this graded
space equals \(\dim_{\mathbb Q_p}V\).  The grading records the weights.

Every [[langlands/de-rham-galois-representation|de Rham representation]] is
Hodge–Tate, but not conversely.  Hodge–Tate weights are the local \(p\)-adic
Hodge invariants that appear in the algebraicity conditions on automorphic
Galois representations.

## References

1. Olivier Brinon and Brian Conrad, *CMI Summer School Notes on \(p\)-adic
   Hodge Theory*, 2009, §§2.3–2.4.
   [Author notes](https://math.stanford.edu/~conrad/papers/notes.pdf).
2. Jean-Marc Fontaine, “Représentations \(p\)-adiques des corps locaux. I,” in
   *The Grothendieck Festschrift II*, Progress in Mathematics 87, 1990.
