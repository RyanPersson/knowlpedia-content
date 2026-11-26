+++
id = "proofs/grh/reduction-main/star-inequality"
title = "The main inequality"
kind = "theorem"
summary = "For all data: m · rem <= f a (log b)^5."
aliases = ["main inequality", "star_inequality"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.star_inequality"]
lean_files = ["src/New/Reduction/MainInequality.lean"]
proof_status = "full"
+++

**Theorem (main inequality).** Let \(P\) be [[proofs/grh/reduction-main/parameters|parameters]] and \(D\) [[proofs/grh/reduction-main/data|data]] for \(P\). Then
\[
m\cdot\mathrm{rem}\ \le\ f\,a\,(\log b)^5 ,
\]
where \(m\) is the number of lifts, \(\mathrm{rem}\) the [[proofs/grh/reduction-main/main-amount-and-total-remainder|total remainder]], \(f\) the number of infinite places of \(E\) and \(a=xb\).

## Proof

Complete relative to Theorems A, B, C. Write \(F=fa\log^4b\), \(E=fa\log^3b\), \(h=h_{\mathrm{main}}\), and \(V_0:=h-m\,\mathrm{rem}+F\).

*The family.* By [[proofs/grh/reduction-main/theorem-b-enough-forms|Theorem B]], \(d_T\ge1\) and there is \(t\subseteq\bar G\) with \(\#t\dim\mathcal S\le5d_T\log(1+2b^2)\) and \(\dim\sum_{s\in t}s\mathfrak p(\mathcal S)\ge(1-4/b^2)d_T\). Let \(\mathcal S^{\mathrm{sh}}\) be the set of \(\varphi\in\mathcal S^{\mathrm{int}}\) with \(\lVert\Theta_1s\mathfrak p\varphi\rVert^2_\sigma\le e^{V_0}\) for all \(s\in\bar G\), \(\sigma\); by [[proofs/grh/reduction-main/theorem-a-short-forms|Theorem A (a)]] it spans \(\mathcal S\). Hence the set \(\bigcup_{s\in t}s\mathfrak p(\mathcal S^{\mathrm{sh}})\) spans \(\sum_{s\in t}s\mathfrak p(\mathcal S)\); choose from it a basis \(y_1,\dots,y_n\) of that space. So \(y\) is linearly independent, \((1-4/b^2)d_T\le n\le d_T\), and each \(y_i=s\mathfrak p\varphi\) with \(s\in t\), \(\varphi\in\mathcal S^{\mathrm{sh}}\).

*Covolume.* \(\lVert\Theta_1y_i\rVert_\sigma^2\le e^{V_0}\), so by Hadamard (rule (3) of [[proofs/grh/reduction-main/covolume-calculus|the calculus of covolumes]]) \(y\) has covolume at most \(nV_0\).

*Index.* By [[proofs/grh/reduction-main/theorem-a-index|Theorem A (b)]], \(y\) has index at most \(\#t\dim\mathcal S\cdot2E\le d_T\cdot I\), \(I:=10\log(1+2b^2)E\).

*Comparison.* [[proofs/grh/reduction-main/theorem-c-integral-forms-long|Theorem C]] gives \(d_T(h-3F)\le nV_0+2d_TI\). Since \(h\ge0\) ([[proofs/grh/reduction-main/prime-sum-bounds|bounds]]), \(F>0\) and \(n\le d_T\), we have \(n(h+F)\le d_T(h+F)\). Therefore
\[
n\cdot m\,\mathrm{rem}=n(h+F)-nV_0\le d_T(h+F)-d_T(h-3F)+2d_TI=d_T\,(4F+2I).
\]
The main amount has cancelled.

*Division.* As \(4/b^2\le\tfrac12\), \(n\ge d_T/2>0\). Hence \(n\,m\,\mathrm{rem}\le d_T\lvert4F+2I\rvert\le n\cdot2\lvert4F+2I\rvert\), and
\[
m\,\mathrm{rem}\le8F+40\log(1+2b^2)\,fa\log^3b\le fa\log^5b ,
\]
because \(\log(1+2b^2)\le3\log b\) and \(8+120\le\log b\).

## Remarks

Errors per dimension: size \(F\) (Theorem A (a)); index \(20\log(1+2b^2)E\) (Theorems A (b), B; the index enters doubled); covolume \(3F\) (Theorem C). What cancels: the main amount between the two bounds; the gains \(\sum\operatorname{gain}_\ell\log\ell\) against \(\log c_B\) inside Theorem A (a).

## References

1. Lean: `New.star_inequality` in `src/New/Reduction/MainInequality.lean`.
2. Earlier bounds for sums over primes by size against divisibility named in the Lean file head: I. Pritsker, *The Gelfond–Schnirelman method in prime number theory*, 2005; A. Granville, H. Stark, *ABC implies no "Siegel zeros" for L-functions of characters with negative discriminant*, 2000; E. Bombieri, *Counting points on curves over finite fields*, Sém. Bourbaki 430, 1973; M. van Frankenhuijsen, *The Riemann hypothesis for function fields over a finite field*, 2008.
