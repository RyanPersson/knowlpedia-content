+++
id = "real-analysis/right-derivative-left-derivative"
title = "Right derivative and left derivative"
kind = "knowl"
summary = "One-sided derivatives defined by one-sided limits of the difference quotient."
aliases = ["right-derivative-left-derivative", "Right derivative and left derivative"]
domains = ["real-analysis"]
prerequisites = []
dependency_review_count = 1
legacy_source_path = "real-analysis/right-derivative-left-derivative.md"
+++

Let \(f:E\to\mathbb{R}\) (or \(\mathbb{C}\)) with \(E\subseteq\mathbb{R}\), and let \(a\in E\). If \(a\) is a limit point of \(E\cap(a,\infty)\), the **right derivative** of \(f\) at \(a\) is
\[f'_+(a):=\lim_{h\downarrow 0}\frac{f(a+h)-f(a)}{h},\]
provided the limit exists. If \(a\) is a limit point of \(E\cap(-\infty,a)\), the **left derivative** is
\[f'_-(a):=\lim_{h\uparrow 0}\frac{f(a+h)-f(a)}{h},\]
provided the limit exists.

If both one-sided derivatives exist and are equal, then \(f\) is differentiable at \(a\) and \(f'(a)=f'_+(a)=f'_-(a)\).

## Examples

- For \(f(x)=|x|\), one has \(f'_+(0)=1\) and \(f'_-(0)=-1\), so \(f'(0)\) does not exist.
- For \(f(x)=x^2\), \(f'_+(a)=f'_-(a)=2a\) for all \(a\).
- For the step function \(\mathbf{1}_{[0,\infty)}\), the one-sided derivatives at \(0\) do not exist (difference quotient blows up).
