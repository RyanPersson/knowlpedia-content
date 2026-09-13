+++
id = "real-analysis/right-derivative-left-derivative"
title = "Right derivative and left derivative"
kind = "knowl"
summary = "One-sided derivatives defined by one-sided limits of the difference quotient."
aliases = ["right-derivative-left-derivative", "Right derivative and left derivative"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/right-derivative-left-derivative.md"
prerequisites = ["real-analysis/limit-of-a-function-at-a-point", "real-analysis/difference-quotient", "topology/limit-point"]
dependency_heuristic = "component-dependency-review-v1"
dependency_review_count = 2
+++

Let \(f:E\to\mathbb{R}\) (or \(\mathbb{C}\)) with \(E\subseteq\mathbb{R}\), and let \(a\in E\). If \(a\) is a [[topology/limit-point|limit point]] of \(E\cap(a,\infty)\), the **right derivative** of \(f\) at \(a\) is
\[f'_+(a):=\lim_{h\downarrow 0}\frac{f(a+h)-f(a)}{h},\]
provided the limit exists as a finite number; the limit is taken only over increments with \(a+h\in E\). If \(a\) is a limit point of \(E\cap(-\infty,a)\), the **left derivative** is
\[f'_-(a):=\lim_{h\uparrow 0}\frac{f(a+h)-f(a)}{h},\]
provided the limit exists as a finite number; the limit is taken only over increments with \(a+h\in E\).

## Relation to differentiability

If both one-sided derivatives exist and are equal, then \(f\) is differentiable at \(a\) and \(f'(a)=f'_+(a)=f'_-(a)\).

## Examples

- For \(f(x)=|x|\), one has \(f'_+(0)=1\) and \(f'_-(0)=-1\), so \(f'(0)\) does not exist.
- For \(f(x)=x^2\), \(f'_+(a)=f'_-(a)=2a\) for all \(a\).
- For the [[real-analysis/step-function|step function]] \(\mathbf{1}_{[0,\infty)}\), the right derivative at \(0\) is \(0\). From the left, the [[real-analysis/difference-quotient|difference quotient]] is \(1/h\to-\infty\), so no finite left derivative exists.
