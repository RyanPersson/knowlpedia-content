+++
id = "complex-analysis/modular-form"
title = "Holomorphic modular form"
kind = "definition"
summary = "A holomorphic function on the upper half-plane satisfying a weight transformation law and regularity at every cusp."
aliases = ["modular form", "classical modular form", "holomorphic modular forms"]
domains = ["complex-analysis"]
section_mode = "progressive"
prerequisites = ["differential-geometry/holomorphic-map", "algebra-groups/special-linear-group-over-ring"]
dependency_heuristic = "transcript-connections-semantic-v1"
dependency_review_count = 1
+++
Let \(\Gamma\) be a finite-index subgroup of [[algebra-groups/special-linear-group-over-ring|\(\operatorname{SL}_2(\mathbb Z)\)]] and \(k\ge0\) an integer. A **holomorphic modular form of weight \(k\) for \(\Gamma\)**, with trivial character, is a [[differential-geometry/holomorphic-map|holomorphic]] function \(f\) on \(\mathcal H=\{z\in\mathbb C:\operatorname{Im}z>0\}\) such that
\[
f\!\left(\frac{az+b}{cz+d}\right)=(cz+d)^kf(z)
\quad\left(\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\Gamma\right),
\]
and \(f\) is holomorphic at every cusp. Explicitly, for every \(\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\operatorname{SL}_2(\mathbb Z)\),
\[
(f|_k\gamma)(z)=(cz+d)^{-k}f(\gamma z)
\]
has a convergent expansion \(\sum_{n\ge0}a_n e^{2\pi inz/h}\) near infinity, for some positive integer period \(h\). This is the cusp condition at \(\gamma\infty\).

## Notation

The space is \(M_k(\Gamma)\). Requiring zero constant coefficient at every cusp defines the subspace of [[complex-analysis/cusp-form|cusp forms]]. A common group is
\[
\Gamma_0(N)=\left\{\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\operatorname{SL}_2(\mathbb Z):N\mid c\right\}.
\]
If \(-I\in\Gamma\) and \(k\) is odd, the transformation law forces \(f=0\).

## References

1. Andrew V. Sutherland, *18.786 Number Theory II*, Spring 2024, [Lecture 6](https://math.mit.edu/classes/18.786/2024/LectureNotes6.pdf), Definitions 6.1–6.5 and the cusp expansions on pp. 1–2.
