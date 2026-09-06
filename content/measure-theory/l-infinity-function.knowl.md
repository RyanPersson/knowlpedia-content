+++
id = "measure-theory/l-infinity-function"
title = "L-infinity function"
kind = "knowl"
summary = "A measurable function that is essentially bounded on a measure space."
aliases = ["l-infinity-function", "L-infinity function"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/l-infinity-function.md"
prerequisites = ["measure-theory/measure-space", "measure-theory/measurable-function", "measure-theory/essential-supremum", "measure-theory/ae-equality", "measure-theory/null-set"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A **\(L^\infty\) function** on a [[measure-theory/measure-space|measure space]] \((X,\Sigma,\mu)\) is a [[measure-theory/measurable-function|measurable function]] \(f:X\to\mathbb R\) or \(f:X\to\mathbb C\) such that
\[
\|f\|_\infty := \operatorname*{ess\,sup}_{x\in X} |f(x)| < \infty.
\]
Here \(\operatorname*{ess\,sup}\) denotes the [[measure-theory/essential-supremum|essential supremum]].

If \(f\) and \(g\) are [[measure-theory/ae-equality|equal almost everywhere]], then \(\lVert f\rVert_\infty=\lVert g\rVert_\infty\), so membership in \(L^\infty\) depends only on the equivalence class modulo a [[measure-theory/null-set|null set]]. These equivalence classes form the \(p=\infty\) case of an [[measure-theory/lp-space|\(L^p\) space]].

## Examples

- On \(([0,1],\mathcal B,\lambda)\), the function \(f(x)=x\) is in \(L^\infty\) and satisfies \(\lVert f\rVert_\infty=1\).
- If \(A\) is a [[measure-theory/measurable-set|measurable set]] in \(X\), then the indicator function \(\mathbf 1_A\) is in \(L^\infty\) and \(\lVert\mathbf 1_A\rVert_\infty\le 1\), with equality to \(0\) when \(A\) is a [[measure-theory/null-set|null set]].
