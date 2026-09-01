+++
id = "harmonic-analysis/higher-dimensional-line-porous-fup"
title = "Higher-dimensional line-porous fractal uncertainty principle"
kind = "theorem"
summary = "Ball porosity in physical space and line porosity in Fourier space imply an L2 power-saving uncertainty estimate in every dimension."
aliases = ["Cohen higher-dimensional FUP", "line-porous FUP"]
domains = ["harmonic-analysis", "mathematical-physics", "quantum-chaos"]
prerequisites = ["analysis/porosity-on-balls", "analysis/porosity-on-lines"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(d\ge1\), \(0<\nu\le1/3\), and \(0<h<1/100\). Suppose
\(X\subseteq[-1,1]^d\) is \(\nu\)-[[analysis/porosity-on-balls|porous on balls]]
from scales \(h\) to \(1\), and
\(Y\subseteq[-h^{-1},h^{-1}]^d\) is
\(\nu\)-[[analysis/porosity-on-lines|porous on lines]] from scales \(1\) to
\(h^{-1}\). Then constants \(C,\beta>0\), depending only on \(\nu\) and \(d\),
satisfy
\[
\operatorname{supp}\widehat f\subseteq Y
\quad\Longrightarrow\quad
\|f\mathbf1_X\|_2\le Ch^\beta\|f\|_2
\]
for every \(f\in L^2(\mathbb R^d)\).

## Proof architecture

[[harmonic-analysis/line-porosity-damping-function-theorem|Line porosity
produces damping functions]] after all dilations, bounded thickenings, and
translations needed by the Han–Schlag iteration. The
[[harmonic-analysis/damping-function-fup-theorem|damping-function FUP theorem]]
then converts their fast decay into a single-scale observability estimate and
iterates that estimate through the holes of \(X\).

## Necessity of directional control

For \(d\ge2\), two orthogonal [[convex-analysis/linear-subspace|linear subspaces]] can be ball porous while Fourier
duality maps the natural measure on one to the natural measure on the other.
Line porosity excludes this model obstruction.

## References

1. Alex Cohen, “Fractal uncertainty in higher dimensions,” 2024. [arXiv record](https://arxiv.org/abs/2305.05022). Relevant: Theorem 1.1.
