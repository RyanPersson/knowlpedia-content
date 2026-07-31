+++
id = "noncommutative-geometry/noncommutative-integral"
title = "Noncommutative integral of a spectral triple"
kind = "definition"
summary = "The Dixmier-trace functional that integrates represented algebra elements against a critical power of the inverse Dirac operator."
aliases = ["Connes integral", "Dixmier-trace integral"]
domains = ["noncommutative-geometry", "operator-algebras"]
section_mode = "progressive"
+++

Let \((\mathcal A,H,D)\) be a
[[noncommutative-geometry/spectral-triple|spectral triple]] of positive
[[noncommutative-geometry/metric-dimension|metric dimension]] \(p\), assume
\(|D|^{-p}\in\mathcal L^{1,\infty}(H)\) after setting it to zero on
\(\ker D\), and choose a [[operator-algebras/dixmier-trace|Dixmier trace]]
\(\operatorname{Tr}_{\omega}\). The associated **noncommutative integral** is
\[
\int_D a=\operatorname{Tr}_{\omega}\!\left(a|D|^{-p}\right),
\qquad a\in\mathcal A,
\]
with \(a\) represented on \(H\). This is a
[[operator-algebras/positive-linear-functional|positive linear functional]] on the
represented algebra. It is tracial only under additional hypotheses ensuring
that commutators with \(|D|^{-p}\) have zero Dixmier trace. If every
\(a|D|^{-p}\) is measurable, its value is independent of \(\omega\); without
measurability, the chosen generalized limit is part of the definition.

## Why the critical power is used

Powers \(|D|^{-q}\) with \(q>p\) are ordinarily trace class, and every Dixmier
trace vanishes on them. Powers with \(q<p\) need not lie in the Dixmier ideal.
The critical power \(|D|^{-p}\) has the borderline \(1/n\)-type singular-value
decay detected by a logarithmic trace. The construction therefore extracts a
volume coefficient invisible to the ordinary trace.

When the zeta function has a simple pole and appropriate Tauberian or
measurability hypotheses hold, the same functional can be recovered from a
residue:
\[
\operatorname{Tr}_{\omega}(a|D|^{-p})
=\frac{1}{p}\operatorname*{Res}_{s=p}
\operatorname{Tr}(a|D|^{-s}),
\]
subject to the normalization conventions of the trace and zeta variable
[Connes, Chapter IV, §2].

## Classical geometric meaning

For the [[noncommutative-geometry/canonical-spin-spectral-triple|canonical Dirac spectral triple]]
of a closed \(p\)-dimensional
Riemannian spin manifold, Connes's trace theorem identifies the Dixmier trace
of a classical pseudodifferential operator of order \(-p\) with a normalized
Wodzicki residue. Consequently
\[
\operatorname{Tr}_{\omega}(f|\not D|^{-p})
=c_p\int_M f\,d\operatorname{vol}_g
\]
for an explicit constant \(c_p\) determined by dimension, spinor rank, and
normalization. This is the model for interpreting the functional as
integration [Connes, Theorem 1].

## Conventions and scope

The symbol \(\int_D\) is not standardized. Authors may write
\(f\,a|D|^{-p}\), absorb the geometric constant \(c_p^{-1}\), or define the
integral by a zeta residue. These normalizations agree only after the
constants are stated.

**Warning.** Metric dimension by itself does not imply
\(|D|^{-p}\in\mathcal L^{1,\infty}\), nor does weak-ideal membership imply
Dixmier measurability. In nonregular triples the zeta-residue formula may be
unavailable even when the Dixmier-trace functional exists. The term
“noncommutative integral” is also used for faithful
[[operator-algebras/semifinite-weight|semifinite weights]] on von
Neumann algebras; that broader usage is not the construction defined here.

## References

1. A. Connes, *Noncommutative Geometry*, Academic Press, 1994. [Author-hosted text](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf). Relevant: Chapter IV, §2 on infinitesimals, Dixmier trace, and the noncommutative integral.
2. A. Connes, “The Action Functional in Non-Commutative Geometry,” *Communications in Mathematical Physics* 117 (1988), 673–683. [DOI record](https://doi.org/10.1007/BF01218391). Relevant: Theorem 1, identifying the Dixmier trace with the noncommutative residue on critical-order pseudodifferential operators.
