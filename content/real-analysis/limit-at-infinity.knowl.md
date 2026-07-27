+++
id = "real-analysis/limit-at-infinity"
title = "Limit at infinity"
kind = "knowl"
summary = "The epsilon-M definition of the limit of a function as x goes to plus or minus infinity."
aliases = ["limit-at-infinity", "Limit at infinity"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/limit-at-infinity.md"
+++

Let \(D\subseteq\mathbb R\) be unbounded above and let \(f:D\to\mathbb R\). The statement
\[
\lim_{x\to+\infty}f(x)=L
\]
means that for every \(\varepsilon>0\) there exists \(M\in\mathbb R\) such that
\[
x\in D,\ x>M\quad\Longrightarrow\quad |f(x)-L|<\varepsilon.
\]

If \(D\) is unbounded below, then \(\lim_{x\to-\infty}f(x)=L\) means that for every \(\varepsilon>0\) there exists \(M\in\mathbb R\) such that \(x\in D\) and \(x<M\) imply \(|f(x)-L|<\varepsilon\).


## Examples

- \(\lim_{x\to\infty}\tfrac1x=0\).
- \(\lim_{x\to\infty}\tfrac{2x+1}{x}=2\).

## Remarks

This is the [[real-analysis/limit-at-a-point|limit]] definition with closeness to a finite point replaced by movement arbitrarily far along one end of the real line.
