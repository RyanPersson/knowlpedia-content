+++
id = "analytic-number-theory/character-projection"
title = "Projection onto a character by weighting"
kind = "construction"
summary = "An average weighted by the conjugate character extracts its Fourier coefficient."
aliases = ["choice of weights", "character isolation"]
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/finite-fourier-inversion"]
+++

Suppose \(f(g)=\sum_{\chi}a_\chi\chi(g)\) on a finite [[algebra-groups/abelian-group|abelian group]] \(G\). To **isolate a character** \(\eta\), give \(f(g)\) weight \(\overline{\eta(g)}/|G|\) and sum over \(g\). By [[analytic-number-theory/finite-fourier-inversion|finite Fourier orthogonality]] the result is \(a_\eta\).

## Two weights by hand

On the two-element group \(\{1,c\}\), the nontrivial character sends \(c\) to \(-1\). If \(f(1)=a+b\) and \(f(c)=a-b\), their average extracts the trivial coefficient \(a\). Half their difference extracts \(b\). For example, the values \(7\) and \(3\) give the constant coefficient \(5\) and the nontrivial coefficient \(2\).
