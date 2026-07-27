+++
id = "measure-theory/convergence-in-lp"
title = "Convergence in \\(L^p\\)"
kind = "knowl"
summary = "Norm convergence in an Lp space."
aliases = ["convergence-in-lp", "Convergence in \\(L^p\\)"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/convergence-in-lp.md"
+++

A [[shared-foundations/sequence|sequence]] \((f_n)\) in a [[measure-theory/lp-space|\(L^p\) space]] \(L^p(X,\mathcal A,\mu)\) **converges in \(L^p\)** to \(f\in L^p(X,\mathcal A,\mu)\) if
\[
\|f_n-f\|_p \to 0 \quad \text{as } n\to\infty,
\]
where \((X,\mathcal A,\mu)\) is a [[measure-theory/measure-space|measure space]]. For \(p=\infty\), the norm is the [[measure-theory/essential-supremum|essential supremum]] norm.

## Relation to convergence in measure

For \(1\le p<\infty\) and \(\varepsilon>0\), Markov's inequality gives
\[
\mu(\{|f_n-f|>\varepsilon\}) \le \varepsilon^{-p}\|f_n-f\|_p^p
\]
for every \(n\). Consequently, convergence in \(L^p\) implies [[measure-theory/convergence-in-measure|convergence in measure]].

## Examples

- On \(([0,1],\mathcal{B},\lambda)\), the functions \(f_n(x)=x^n\) satisfy \(f_n\to 0\) in \(L^p\) for every \(1\le p<\infty\), since
  \[
  \|f_n\|_p^p=\int_0^1 x^{np}\,dx=\frac{1}{np+1}\to 0.
  \]
- On the same space, for fixed \(1\le p<\infty\), the functions \(g_n=n^{1/p}\mathbf{1}_{[0,1/n]}\) converge to \(0\) in measure but not in \(L^p\), because
  \[
  \|g_n\|_p^p = \int_0^{1/n} n\,dx = 1
  \]
  for every \(n\).
