+++
id = "functional-analysis/continuous-antidual"
title = "Continuous anti-dual"
kind = "definition"
summary = "The continuous conjugate-linear functionals, used to embed Hilbert vectors linearly as generalized vectors."
aliases = ["antidual", "continuous conjugate-linear dual", "strong anti-dual"]
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["functional-analysis/locally-convex-space", "functional-analysis/strong-dual", "linear-algebra/inner-product"]
+++

For a complex [[functional-analysis/locally-convex-space|locally convex space]] \(E\), its **continuous anti-dual** is
\[
E^\times=\{\lambda:E\to\mathbb C:\lambda\text{ is continuous and conjugate-linear}\}.
\]
Conjugate-linearity means \(\lambda(av+bw)=\overline a\lambda(v)+\overline b\lambda(w)\). Pointwise addition and scalar multiplication make \(E^\times\) a complex vector space. Its **strong anti-dual topology** is uniform convergence on bounded subsets, with seminorms
\[
q_B(\lambda)=\sup_{w\in B}|\lambda(w)|.
\]
This is the anti-linear version of the [[functional-analysis/strong-dual|strong dual topology]].

## Hilbert-space embedding

Use an [[linear-algebra/inner-product|inner product]] linear in its first argument. If \(E\hookrightarrow H\) is continuous and dense, then
\[
j:H\longrightarrow E^\times,\qquad j(v)(w)=\langle v,w\rangle_H
\]
is a continuous linear injection. Indeed,
\(q_B(j(v))\leq\|v\|\sup_{w\in B}\|w\|\), and density proves injectivity.

## Relation to the linear dual

The map \(\lambda\mapsto\overline\lambda\), with \(\overline\lambda(w)=\overline{\lambda(w)}\), identifies the anti-dual conjugate-linearly with the [[functional-analysis/topological-dual|continuous linear dual]]. Thus linear and anti-linear distribution conventions differ by complex conjugation. The anti-dual convention makes \(j\) linear without choosing a conjugation on \(H\).
