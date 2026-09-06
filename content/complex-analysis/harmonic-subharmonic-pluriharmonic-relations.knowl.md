+++
id = "complex-analysis/harmonic-subharmonic-pluriharmonic-relations"
title = "Relations among harmonic and plurisubharmonic functions"
kind = "theorem"
summary = "The inclusion and intersection relations among H, SH, PSH, and PH on a complex domain."
aliases = ["H SH PSH PH relations", "harmonic plurisubharmonic Venn diagram"]
domains = ["complex-analysis", "several-complex-variables", "potential-theory"]
prerequisites = ["complex-analysis/harmonic-function", "complex-analysis/subharmonic-function", "complex-analysis/plurisubharmonic-function", "complex-analysis/pluriharmonic-function", "linear-algebra/hermitian-matrix"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

On a domain \(U\subseteq\mathbb C^d\), let \(H\), \(SH\), \(PSH\), and
\(PH\) denote the [[complex-analysis/harmonic-function|harmonic]],
[[complex-analysis/subharmonic-function|subharmonic]],
[[complex-analysis/plurisubharmonic-function|plurisubharmonic]], and
[[complex-analysis/pluriharmonic-function|pluriharmonic]] functions,
respectively. Then
\[
PH=H\cap PSH,\qquad H\subseteq SH,\qquad PSH\subseteq SH.
\]
Equivalently, inside \(SH\), the classes \(H\) and \(PSH\) overlap exactly in
\(PH\). When \(d=1\), \(PSH=SH\) and \(PH=H\).

## Diagram

The set-theoretic picture for \(d>1\) is
\[
\begin{array}{c}
SH\\[2pt]
\supset\; H\ \cup\ PSH,\\[2pt]
H\cap PSH=PH.
\end{array}
\]
Neither \(H\subseteq PSH\) nor \(PSH\subseteq H\) holds in general.

## Why the intersection is pluriharmonic

For a smooth function, \(PSH\) means that the Levi matrix is positive
semidefinite, while harmonicity says that its trace is zero because
\[
\Delta u=4\sum_{j=1}^d
\frac{\partial^2u}{\partial z_j\partial\bar z_j}.
\]
A positive-semidefinite [[linear-algebra/hermitian-matrix|Hermitian matrix]]
with zero trace is zero. Hence a harmonic PSH function has vanishing
[[complex-analysis/levi-form|Levi form]] and is pluriharmonic. The same
conclusion holds without smoothness by distributional regularity.

## Separating examples

On \(\mathbb C^d\), the function \(u(z)=|z_1|^2\) is PSH but not harmonic.
For \(d\ge2\), the function
\(v(z)=|z_1|^2-|z_2|^2\) is harmonic but not PSH. These examples expose the
distinction: subharmonicity controls the trace of the
[[complex-analysis/levi-form|complex Hessian]], whereas
plurisubharmonicity controls the whole Hermitian matrix.

## References

1. Lars Hörmander, *Notions of Convexity*, Birkhäuser, 2007. [DOI record](https://doi.org/10.1007/978-0-8176-4585-4). Relevant: Chapter 2.
2. Marek Klimek, *Pluripotential Theory*, Oxford University Press, 1991. [Publisher record](https://global.oup.com/academic/product/pluripotential-theory-9780198535683).
