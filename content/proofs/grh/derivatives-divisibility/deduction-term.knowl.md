+++
id = "proofs/grh/derivatives-divisibility/deduction-term"
title = "Deduction term and exempt pairs of heights"
kind = "definition"
summary = "The real number charged, in units of v(pi), for making the pairings between a place and a partner divisible by pi; and the pairs of heights that are exempt because of a marked place."
aliases = ["deduction term", "exempt pair", "marked place"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.deductionTerm", "New.IsExemptPair"]
lean_files = ["src/New/Derivatives/Divisibility/NullFrames.lean"]
+++

**Definition (deduction term).** Let \(p\) be a prime, \(\Phi\) a set of *places*, \(\kappa\colon\Phi\times\mathbb{N}\to\mathbb{N}\) (the number \(\kappa(\tau,h)\) is the number of columns of height \(h\) of a diagram at \(\tau\)), \(N\ge0\) an integer, and \(\mathrm{ev}\subseteq\Phi\) a finite set of **marked places**. For \(\sigma\in\Phi\) put
\[
t(\sigma)=\begin{cases}\kappa(\sigma,1)&\text{if } 1<N \text{ and } \sigma\notin\mathrm{ev},\\ 0&\text{otherwise,}\end{cases}\qquad
r(\sigma)=\sum_{\substack{h<N\\ h\ne1}}\kappa(\sigma,h),\qquad
B(\sigma)=\sum_{\substack{h<N\\ h\neq 1}}h\,\kappa(\sigma,h):
\]
the number of columns of height one (not counted at marked places), the number of the other columns of height below \(N\), and the number of boxes in the latter. For places \(\sigma,\sigma'\) and an exponent \(e\ge 0\) the **deduction term** is the real number
\[
D_{\mathrm{ev}}(\sigma,\sigma',e)=\min\Bigl(\frac{t(\sigma)}{p^e},\,r(\sigma')+t(\sigma')\Bigr)+\frac{r(\sigma)}{p^e}+\min\Bigl(\frac{B(\sigma)}{p^e},\,B(\sigma')\Bigr).
\]

**Definition (exempt pair).** A pair of heights \((h,h')\), \(h\) at \(\sigma\) and \(h'\) at \(\sigma'\), is **exempt** for \(\mathrm{ev}\) if \(h=1\) and either \(\sigma\in\mathrm{ev}\), or \(h'=1\) and \(\sigma'\in\mathrm{ev}\).

## Remarks

Columns of height \(0\), if \(\kappa(\sigma,0)\ne0\), are counted in \(r(\sigma)\); a diagram has none. The term is the cost of one specific choice of congruences that covers all non-exempt pairs, constructed in the [[proofs/grh/derivatives-divisibility/change-of-directions|change of directions]]; it is an upper bound for the loss in determinants, not claimed to be the minimal cost (cheaper covering choices can exist). Summed over the places and the exponents and multiplied by \(v(\pi_p)\) it is the deduction in [[proofs/grh/derivatives-divisibility/count-with-charges|the count]].

## References

1. Lean: `New.deductionTerm`, `New.IsExemptPair` in `src/New/Derivatives/Divisibility/NullFrames.lean`.
