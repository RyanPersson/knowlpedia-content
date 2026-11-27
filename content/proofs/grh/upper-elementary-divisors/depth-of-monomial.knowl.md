+++
id = "proofs/grh/upper-elementary-divisors/depth-of-monomial"
title = "Depth of a monomial"
kind = "definition"
summary = "The degree of a monomial in the deep variables: those with even letter and index at least r, or odd letter and index below r."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.deepIndicator", "New.FrobeniusCycle.depth", "New.FrobeniusCycle.diagonal_pow_depth"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/TwistingData.lean"]
+++

Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] for \((N,W,R)\), and let \(k,r\ge 0\). A variable \(x_{b,s}\) is **deep for \(r\)** if \(s\) is even and \(b\ge r\), or \(s\) is odd and \(b<r\); let \(\delta_r(b,s)\in\{0,1\}\) be the indicator of this. The **depth** (for \(r\)) of an exponent \(\beta\in\mathcal{E}(N,k,n)\) is the degree of \(x^{\beta}\) in the deep variables:
\[
\operatorname{depth}_r(\beta)=\sum_{s\in\mathbb{Z}/N}\sum_{b=0}^{k-1}\beta_s(b)\,\delta_r(b,s).
\]

## Properties

For \(t\in R\) the diagonal matrix \(\operatorname{diag}\bigl(t^{\operatorname{depth}_r(\beta)}\bigr)_{\beta}\) equals \(\bigotimes_s\operatorname{Sym}^n\bigl(\operatorname{diag}(t^{\delta_r(b,s)})_b\bigr)\): the diagonal substitution \(x_{b,s}\mapsto t^{\delta_r(b,s)}x_{b,s}\) multiplies \(x^{\beta}\) by \(t^{\operatorname{depth}_r(\beta)}\). Thus scaling by \(t^{\text{depth}}\) is the tensor product over the letters of the symmetric powers of the letterwise diagonal matrices in the display, which scale the last \(k-r\) coordinates on even letters and the first \(r\) coordinates on odd letters. It has the same shape as the [[proofs/grh/upper-elementary-divisors/twisted-action|twisted representation]] but is in general not a value of it (for instance \(t\) need not be invertible).

## References

1. Lean: `New.FrobeniusCycle.deepIndicator`, `New.FrobeniusCycle.depth`, `New.FrobeniusCycle.diagonal_pow_depth` in `src/New/UpperBound/ElementaryDivisors/TwistingData.lean`.
