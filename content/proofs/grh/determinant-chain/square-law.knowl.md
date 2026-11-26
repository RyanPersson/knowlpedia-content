+++
id = "proofs/grh/determinant-chain/square-law"
title = "Square law over a finite ring"
kind = "definition"
summary = "A pair of functions on rectangular matrices over a finite ring that transform by a character of the determinant and have proportional sums against all matched functions."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Exchange.SquareLaw"]
lean_files = ["src/New/Determinant/Chain/SquareLaw.lean"]
+++

Let \(R\) be a finite [[?c:Commutative ring|commutative ring]], let \(\chi\colon R\to\mathbb{C}\) be a [[?c:Multiplicative character of a finite ring|multiplicative character]] of \(R\) (multiplicative on \(R\), zero on non-units), let \(a,b,n\) be finite index sets with a bijection \(\sigma\colon b\sqcup a\to n\), and let \(c\in\mathbb{C}\). Write \(M_{a\times n}(R)\) for the matrices with rows indexed by \(a\) and columns by \(n\).

A pair of functions \(L\colon M_{a\times n}(R)\to\mathbb{C}\) and \(L'\colon M_{n\times b}(R)\to\mathbb{C}\) satisfies the **square law with constant \(c\)** (for \(\chi\) and \(\sigma\)) if

1. \(L(kx)=\chi(\det k)\,L(x)\) for all \(k\in \mathrm{GL}_a(R)\) and all \(x\);
2. \(L'(yk)=\chi(\det k)\,L'(y)\) for all \(k\in \mathrm{GL}_b(R)\) and all \(y\);
3. for every pair \((\Phi,\Psi)\) of [[?lean:New.AreMatched|matched functions]] for \(\chi\) and \(\sigma\) over the whole ring \(R\),
\[
\sum_{y\in M_{n\times b}(R)}\Psi(y)\,L'(y)\;=\;c\sum_{x\in M_{a\times n}(R)}\Phi(x)\,L(x).
\]

Here \(\Phi\colon M_{a\times n}(R)\to\mathbb{C}\) and \(\Psi\colon M_{n\times b}(R)\to\mathbb{C}\) are *matched* if \(\Phi\) vanishes off the matrices \(x_\gamma\) formed by the rows \(\sigma(a)\) of \(\gamma^{-1}\), \(\Psi\) vanishes off the matrices \(y_\gamma\) formed by the columns \(\sigma(b)\) of \(\gamma\), for \(\gamma\in\mathrm{GL}_n(R)\), and \(\Phi(x_\gamma)=\chi(\det\gamma)\,\Psi(y_\gamma)\) for all \(\gamma\in \mathrm{GL}_n(R)\).

## Remarks

In the application \(L(x)\) and \(L'(y)\) are the values of the two composites of theta lifts around a commuting square, as functions of the finite parts of the theta data; the square law is what [[?lean:New.Exchange.one_square_identity_of_isEdgeFamily|the one-square identity]] provides.

## References

1. Lean: `New.Exchange.SquareLaw` in `src/New/Determinant/Chain/SquareLaw.lean`.
