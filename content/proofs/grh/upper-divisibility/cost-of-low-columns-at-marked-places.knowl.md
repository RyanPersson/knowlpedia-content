+++
id = "proofs/grh/upper-divisibility/cost-of-low-columns-at-marked-places"
title = "Cost of the transfer and of the low columns at marked places"
kind = "lemma"
summary = "For a marked set, the transfer exponents and r times the low columns at the places inducing it are within loss/m plus a/x_1 per marked a-place."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.IsMarked.card_mul_transferExponent_add_sum_lowColumns_le"]
lean_files = ["src/New/UpperBound/Divisibility/MarkedPrimes.lean"]
proof_status = "outline"
+++

**Lemma.** Let \(D\) be [[?lean:New.Data|admissible data]], \(j<m\), and \(\Lambda\) a [[proofs/grh/upper-divisibility/marked-set-of-primes|marked set]] at a prime \(p\). With \(\mathfrak r=\mathfrak r(p)\), \(\nu_p=\mathfrak rf(n_m+\mathfrak r)\) the [[proofs/grh/upper-divisibility/classes-of-primes|transfer exponent]] and \(c_j(\sigma)\) the number of [[proofs/grh/upper-divisibility/divisibility-bound|low columns]] at \(\sigma\),
\[
\lvert\Lambda\rvert\,\nu_p+\mathfrak r\sum_{\sigma\in\Phi_\Lambda}c_j(\sigma)\;\le\;\frac{\operatorname{loss}(p)}{m}+\lvert\Phi_a\cap\Phi_\Lambda\rvert\cdot\frac a{x_1}.
\]

## Proof

Let \(\sigma\in\Phi_\Lambda\). By the [[proofs/grh/upper-divisibility/properties-of-marked-sets|properties of marked sets]] \(w(\sigma)=a/x_1\), so \(c_j(\sigma)\le a/x_1+x^{60}\) ([[proofs/grh/upper-divisibility/only-collisions-lose|Step 0 there]]). We claim
\[
\mathfrak r\,c_j(\sigma)\le\frac a{pm}+[\sigma\in\Phi_a]\frac a{x_1}.
\]
If \(p\le m\): \(\mathfrak r(a/x_1+x^{60})\le a/m^2\le a/(pm)\) is a size comparison (quoted; \(\mathfrak r\le s\) is of size \(\log x\)). If \(p>m\): then \(\mathfrak r=1\), so the odd number \(o_0\le\mathfrak r\) is \(1\), that is \(-p\equiv1\bmod q_0\); the a-place inducing \(w_\sigma\) differs from \(\sigma\) by a power of \(u(-p)\), which has class \(1\) modulo \(q_0\), so \(\sigma\) is itself an a-place, and \(c_j(\sigma)\le a/x_1+x^{60}\le a/x_1+a/(pm)\) (quoted comparison, using \(p<x_1\)).

Summing over \(\sigma\in\Phi_\Lambda\), using \(\lvert\Lambda\rvert\le f\), \(\operatorname{loss}(p)\ge f(\log b)^2a/p\), it remains to check
\[
f\cdot\mathfrak rf(n_m+\mathfrak r)+\lvert\Phi_\Lambda\rvert\frac{a}{pm}\le\frac{f(\log b)^2a}{pm},
\]
which, after multiplying by \(p\), is the size comparison \(f^2\mathfrak r(n_m+\mathfrak r)p+\lvert\Phi_\Lambda\rvert a/m\le fa(\log b)^2/m\) proved in Lean by [[?lean:New.Data.le_of_hasLogBound|`le_of_hasLogBound`]] (quoted). \(\blacksquare\)

## References

1. Lean: `New.Data.IsMarked.card_mul_transferExponent_add_sum_lowColumns_le` in `src/New/UpperBound/Divisibility/MarkedPrimes.lean`.
