+++
id = "langlands/semistable-galois-representation"
title = "Semistable Galois representation"
kind = "definition"
summary = "A p-adic Galois representation whose semistable period module has full dimension."
aliases = ["semistable p-adic representation", "potentially semistable representation", "semistable representation in p-adic Hodge theory"]
domains = ["langlands", "algebra-fields-galois", "algebraic-geometry-foundations"]
section_mode = "progressive"
+++

Let \(K/\mathbb Q_p\) be finite, let \(K_0\) be its maximal unramified
subfield, and let \(V\) be a finite-dimensional \(\mathbb Q_p\)-representation
of the
[[langlands-letter/knowls/galois-extension-and-group|absolute Galois group]]
\(G_K=\operatorname{Gal}(\overline K/K)\). Using the
[[langlands/fontaine-period-rings|Fontaine period ring]]
\(B_{\mathrm{st}}\), set

\[
D_{\mathrm{st}}(V)=
(B_{\mathrm{st}}\otimes_{\mathbb Q_p}V)^{G_K}.
\]

The representation \(V\) is **semistable** when

\[
\dim_{K_0}D_{\mathrm{st}}(V)=\dim_{\mathbb Q_p}V.
\]

The resulting module carries Frobenius \(\varphi\), a nilpotent monodromy
operator \(N\) satisfying \(N\varphi=p\varphi N\), and a filtration after
extension to \(K\).  It is therefore a filtered \((\varphi,N)\)-module.

## Potential semistability

The representation is **potentially semistable** if its restriction to
\(G_L\) is semistable for some finite extension \(L/K\).  The \(p\)-adic
monodromy theorem says that this is equivalent to being
[[langlands/de-rham-galois-representation|de Rham]].

A semistable representation is
[[langlands/crystalline-galois-representation|crystalline]] exactly when its
monodromy operator vanishes.  Geometrically, semistable reduction can produce
nonzero monodromy, while good reduction produces the crystalline case.

## Weil–Deligne representation

Fontaine's construction associates a
[[langlands/weil-deligne-representation|Weil–Deligne representation]] to a
potentially semistable representation.  This is the object compared with the
[[langlands/local-l-parameter|local Langlands parameter]] at a place above
\(p\) in precise formulations of
[[langlands/local-global-compatibility|local–global compatibility]].

## References

1. Jean-Marc Fontaine, “Représentations \(p\)-adiques semi-stables,”
   *Astérisque* 223 (1994), 113–184.
   [Numdam](https://www.numdam.org/item/AST_1994__223__113_0/).
2. Laurent Berger, “Représentations \(p\)-adiques et équations
   différentielles,” *Inventiones Mathematicae* 148 (2002), 219–284.
   [arXiv](https://arxiv.org/abs/math/0102179).
