+++
id = "langlands/fontaine-period-rings"
title = "Fontaine period rings"
kind = "definition"
summary = "Galois-equivariant p-adic coefficient rings whose invariant periods define Hodge–Tate, de Rham, crystalline, and semistable representations."
aliases = ["p-adic period rings", "Fontaine's period rings", "B_HT B_dR B_cris B_st"]
domains = ["langlands", "algebra-fields-galois", "algebraic-geometry-foundations"]
section_mode = "progressive"
+++

Let \(K/\mathbb Q_p\) be a
[[langlands-letter/knowls/p-adic-field|\(p\)-adic field]], let
\(G_K=\operatorname{Gal}(\overline K/K)\) be its
[[langlands-letter/knowls/galois-extension-and-group|absolute Galois group]],
and let \(K_0\) be the maximal unramified subfield of \(K\).
**Fontaine's period rings** are topological \(\mathbb Q_p\)-algebras with
continuous \(G_K\)-actions and additional structures. The four basic rings
are

\[
B_{\mathrm{HT}},\qquad
B_{\mathrm{dR}},\qquad
B_{\mathrm{cris}},\qquad
B_{\mathrm{st}}.
\]

For a finite-dimensional \(p\)-adic representation \(V\), taking invariants
in \(B\otimes_{\mathbb Q_p}V\) produces its \(B\)-period module. Having the
largest dimension allowed by \(V\) is the corresponding admissibility
condition.

## Structures carried by the rings

- \(B_{\mathrm{HT}}=\bigoplus_{i\in\mathbb Z}\mathbb C_p(i)\) is graded and
  detects [[langlands/hodge-tate-representation|Hodge–Tate weights]].
- \(B_{\mathrm{dR}}\) is a complete filtered field; its invariants form the
  filtered \(K\)-vector space of
  [[langlands/de-rham-galois-representation|de Rham periods]].
- \(B_{\mathrm{cris}}\subset B_{\mathrm{dR}}\) carries Frobenius. Its
  invariants form a filtered Frobenius module and define
  [[langlands/crystalline-galois-representation|crystalline
  representations]].
- \(B_{\mathrm{st}}\) contains \(B_{\mathrm{cris}}\) and carries Frobenius
  together with a nilpotent monodromy operator \(N\). It defines
  [[langlands/semistable-galois-representation|semistable
  representations]].

The inclusions and extra structures explain the implication

\[
\text{crystalline}\Longrightarrow\text{semistable}
\Longrightarrow\text{de Rham}\Longrightarrow\text{Hodge–Tate}.
\]

## Ring versus period module

The rings are universal coefficient objects; they do not depend on a
particular \(V\). By contrast,

\[
D_B(V)=(B\otimes_{\mathbb Q_p}V)^{G_K}
\]

is a linear-algebraic invariant of \(V\). For \(B_{\mathrm{dR}}\) it is a
filtered \(K\)-vector space, while for \(B_{\mathrm{cris}}\) and
\(B_{\mathrm{st}}\) it is initially a \(K_0\)-vector space with Frobenius
and, in the semistable case, monodromy. Confusing \(B\) with \(D_B(V)\)
suppresses both the Galois-invariant operation and the base field of the
result.

## References

1. Olivier Brinon and Brian Conrad, *CMI Summer School Notes on \(p\)-adic
   Hodge Theory*, 2009, Chapters 2, 4, and 9.
   [Author notes](https://math.stanford.edu/~conrad/papers/notes.pdf).
2. Jean-Marc Fontaine, “Le corps des périodes \(p\)-adiques,”
   *Astérisque* 223 (1994), 59–111.
   [Numdam](https://www.numdam.org/item/AST_1994__223__59_0/).
