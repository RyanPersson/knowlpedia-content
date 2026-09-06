+++
id = "complex-analysis/monodromy-theorem"
title = "Monodromy theorem"
kind = "theorem"
summary = "Analytic continuation along all paths in a simply connected domain produces a single-valued holomorphic function."
aliases = ["monodromy theorem for analytic continuation"]
domains = ["complex-analysis", "topology"]
section_mode = "progressive"
prerequisites = ["topology/simply-connected-space", "complex-analysis/holomorphic-germ", "complex-analysis/analytic-continuation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(D\subseteq\mathbb C\) be a [[topology/simply-connected-space|simply connected]] domain, let \(a\in D\), and let \(f_a\) be a [[complex-analysis/holomorphic-germ|holomorphic germ]] at \(a\). If \(f_a\) can be analytically continued along every path in \(D\) starting at \(a\), then all continuations fit together to a single holomorphic function \(F:D\to\mathbb C\) whose germ at \(a\) is \(f_a\).

## Homotopy form

More generally, [[complex-analysis/analytic-continuation|analytic continuations]] along two paths with the same endpoints give the same terminal germ when the paths are homotopic relative to their endpoints and continuation exists throughout the homotopy. Simple connectivity makes every two such paths homotopic, which yields the core statement.

The homotopy assertion follows by subdividing the homotopy square into small rectangles on which continuation is represented by one convergent power series. Uniqueness of a power-series germ makes the terminal germ unchanged across adjacent rectangles. Thus it depends only on the homotopy class; simple connectivity makes all paths with fixed endpoints equivalent, so the local germs glue to \(F\).

## Why the hypotheses matter

The square-root germ near \(1\) can be continued along every path in \(\mathbb C\setminus\{0\}\), but continuation around a loop encircling \(0\) changes its sign. The punctured plane is not simply connected, so the theorem does not force a single-valued square root there.

## Scope

The theorem concerns monodromy of analytic continuation. It should not be confused with monodromy representations of covering spaces or differential equations, although those constructions encode the same path-dependence mechanism.

## References

1. Otto Forster, *Lectures on Riemann Surfaces*, Springer, 1981. [Publisher record](https://doi.org/10.1007/978-1-4612-5961-9). Relevant: Chapter 1, §§6–7.
