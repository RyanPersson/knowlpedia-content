+++
id = "operator-algebras/fell-bundle"
title = "Fell bundle"
kind = "definition"
summary = "A bundle over a group whose fibers multiply and take adjoints like the homogeneous pieces of a C*-algebra."
aliases = ["C*-algebraic bundle", "Banach *-algebraic bundle"]
domains = ["operator-algebras", "harmonic-analysis"]
section_mode = "progressive"
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact group]]. A
**Fell bundle** \(\mathcal B=(B_s)_{s\in G}\) is a Banach bundle over \(G\)
with continuous operations
\[
B_s\times B_t\longrightarrow B_{st},\qquad
B_s\longrightarrow B_{s^{-1}},\quad b\longmapsto b^*,
\]
that are associative and involutive, satisfy
\(\lVert bc\rVert\leq\lVert b\rVert\lVert c\rVert\),
\(\lVert b^*b\rVert=\lVert b\rVert^2\), and make \(b^*b\) positive in the
[[operator-algebras/cstar-algebra|\(C^*\)-algebra]] \(B_e\). The bundle
axioms also require the usual fiberwise linearity and continuity. Thus each
\(B_s\) behaves as a homogeneous component, while \(B_e\) is the unit fiber.
Multiplication and involution link different fibers without identifying them,
so the total space need not itself be a \(C^*\)-algebra.

## Cross-sectional algebras

Compactly supported continuous sections form a convolution \(*\)-algebra.
After choosing a left [[harmonic-analysis/haar-measure|Haar measure]], its
operations are
\[
(f*g)(s)=\int_G f(t)g(t^{-1}s)\,dt,\qquad
f^*(s)=\Delta(s^{-1})f(s^{-1})^*,
\]
where \(\Delta\) is the modular function. Completing this algebra in the
universal norm gives the full cross-sectional algebra \(C^*(\mathcal B)\);
the [[algebra-representation-theory/regular-representation|regular representation]] gives \(C_r^*(\mathcal B)\). These constructions
extend full and [[operator-algebras/reduced-crossed-product|reduced crossed products]]
[Exel, Chapters 16–17](https://bookstore.ams.org/surv-224/).

## Examples and saturation

For a [[operator-algebras/cstar-dynamical-system|\(C^*\)-dynamical system]]
\((A,G,\alpha)\), take \(B_s=A\) as [[linear-algebra/banach-space|Banach spaces]] and define
\[
(a,s)(b,t)=(a\alpha_s(b),st),\qquad
(a,s)^*=(\alpha_{s^{-1}}(a^*),s^{-1}).
\]
Its cross-sectional algebras are the ordinary crossed products of the
action. Fell bundles also encode partial actions and graded
\(C^*\)-algebras.

A Fell bundle is **saturated** when
\(\overline{\operatorname{span}}(B_sB_t)=B_{st}\) for every \(s,t\).
Saturation is an additional property in the convention used here. Some
older sources build it into “\(C^*\)-algebraic bundle,” so hypotheses should
be compared before importing a theorem.

## References

1. Ruy Exel, *Partial Dynamical Systems, Fell Bundles and Applications*, Mathematical Surveys and Monographs 224, American Mathematical Society, 2017. [AMS record](https://bookstore.ams.org/surv-224/). Relevant: Chapters 16–20 on Fell bundles and their cross-sectional algebras.
2. J. M. G. Fell and Robert S. Doran, *Representations of *-Algebras, Locally Compact Groups, and Banach *-Algebraic Bundles*, Volumes 1–2, Academic Press, 1988. [Volume 1 publisher record](https://shop.elsevier.com/books/representations-of-algebras-locally-compact-groups-and-banach-algebraic-bundles/fell/978-0-12-252721-0). Relevant: the axioms and representation theory of Banach \(*\)-algebraic bundles.
