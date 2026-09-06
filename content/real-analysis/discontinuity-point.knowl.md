+++
id = "real-analysis/discontinuity-point"
title = "Discontinuity point"
kind = "knowl"
summary = "A point where a function fails to be continuous"
aliases = ["discontinuity-point", "Discontinuity point"]
domains = ["real-analysis"]
prerequisites = ["topology/continuous-map"]
dependency_review_count = 1
legacy_source_path = "real-analysis/discontinuity-point.md"
+++

Let \(U\subseteq\mathbb R^n\), let \(f:U\to\mathbb R^m\), and let \(a\in U\). The point \(a\) is a **discontinuity point** of \(f\) if \(f\) is not [[topology/continuous-map|continuous]] at \(a\). Equivalently, there exists \(\varepsilon>0\) such that for every \(\delta>0\) there is \(x\in U\) with
\[
\lVert x-a\rVert<\delta
\quad\text{and}\quad
\lVert f(x)-f(a)\rVert\ge\varepsilon.
\]

## Remarks

In many common situations, discontinuity at \(a\) can be detected by limits: if \(\lim_{x\to a}f(x)\) exists in the sense of a [[real-analysis/limit-at-a-point|limit at a point]] and is not equal to \(f(a)\), then \(a\) is a discontinuity point. The collection of all such points is the [[real-analysis/set-of-discontinuities|set of discontinuities]].

## Examples

- The sign function defined by \(f(x)=1\) for \(x>0\), \(f(x)=-1\) for \(x<0\), and \(f(0)=0\) is discontinuous at \(0\).
- The function \(f:\mathbb R\to\mathbb R\) defined by \(f(x)=1\) for rational \(x\) and \(f(x)=0\) for irrational \(x\) is discontinuous at every real number.
