+++
id = "real-analysis/implicit-function-theorem"
title = "Implicit function theorem"
kind = "knowl"
summary = "Solves an equation F(x,y)=0 locally for y as a function of x under a nondegeneracy condition."
aliases = ["implicit-function-theorem", "Implicit function theorem"]
domains = ["real-analysis"]
prerequisites = ["topology/open-set", "real-analysis/jacobian-matrix"]
dependency_review_count = 1
legacy_source_path = "real-analysis/implicit-function-theorem.md"
+++

**Implicit function theorem.** Let \(U\subseteq\mathbb R^{n+m}\) be [[topology/open-set|open]], and let \(F:U\to\mathbb R^m\) be continuously differentiable. Write points as \((x,y)\), where \(x\in\mathbb R^n\) and \(y\in\mathbb R^m\). Suppose \((a,b)\in U\), \(F(a,b)=0\), and the [[real-analysis/jacobian-matrix|partial Jacobian]] \(D_yF(a,b)\) is invertible. Then there are neighborhoods \(A\) of \(a\) and \(B\) of \(b\), with \(A\times B\subseteq U\), and a unique continuously differentiable map \(g:A\to B\) such that \(g(a)=b\) and
\[
F(x,y)=0\quad\Longleftrightarrow\quad y=g(x)
\]
for all \((x,y)\in A\times B\).

Moreover, for each \(x\in A\),
\[
Dg(x)=-(D_yF(x,g(x)))^{-1}D_xF(x,g(x)).
\]

## Remarks

This theorem produces an [[real-analysis/implicitly-defined-function|implicitly defined function]] from an equation, and it is tightly connected to the [[real-analysis/inverse-function-theorem-rk|inverse function theorem]] (which can be recovered as a special case).
