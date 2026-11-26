+++
id = "proofs/grh/derivatives-vacuum/valuation-bound-on-twelve-copies"
title = "The valuation bound on twelve copies at every prime"
kind = "theorem"
summary = "For a tight frame of length M containing a vector with a unit linear form at p, and every degree l near the weights, v(l!) + val_12(l) <= S_p + 2 sum over the places of v(B_tau), for every prime p."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.leastValLE_twelve"]
lean_files = ["src/New/Derivatives/Sharpness/Cases.lean"]
proof_status = "full"
+++

Let \(D\) be [[?lean:New.Data|admissible data]], \(p\) a prime with a \(p\)-adic place \(\iota_p\), \((w_i)_{i\in J}\) with multiplicities \((c_i)\) a [[?lean:New.IsTightFrame|tight frame]] of length \(M\), \(\mu\) its [[proofs/grh/derivatives-vacuum/resolution-forms-of-a-frame|resolution forms]], and \(\operatorname{val}_n\) the [[proofs/grh/derivatives-vacuum/least-valuation-relation|least valuation]] for the CM curve, \(\mu\) and \(c\).

**Theorem.** Suppose \(\lvert\mu_{i_0,\tau}\rvert_p=1\) for some \(i_0\in J\) and all \(\tau\in\Phi\) (that is, \(w_{i_0}\) [[proofs/grh/derivatives-vacuum/unit-linear-form|has a unit linear form]] at \(\iota_p\)), and let \(l\) be a degree [[proofs/grh/derivatives-vacuum/degree-near-the-weights|near the weights]]. Then
\[ \operatorname{val}_{12}(l)\le S_p+2\sum_{\tau\in\Phi}v_p\bigl(B(l_\tau)\bigr)-\sum_{\tau\in\Phi}v_p(l_\tau!), \]
where \(S_p\) is the [[?lean:New.Data.localPrimeSumTotal|predicted valuation]] and \(B\) the [[proofs/grh/derivatives-vacuum/loss-product|loss product]]. Explicitly: there are twelve integral series \(H_c\) in the parameters \(y(\mu_iz)\) and degrees \(\alpha_c\) with \(\sum_c\alpha_c=l\) such that the product of the coefficients of \(z^{\alpha_c}\) in \(H_c\Theta\) has valuation at most the right-hand side.

## Proof

Three cases, using that \(v_p(B)\ge0\).

* \(p\) splits: [[proofs/grh/derivatives-vacuum/valuation-bound-at-split-primes|the split case]].
* \(p\) does not split and \(p>k\): then \(p>k\ge d\) (the inequality \(d\le k\) is a scale inequality of the data), so \(p\ne d\) and \(p\) is inert; [[proofs/grh/derivatives-vacuum/valuation-bound-at-large-inert-primes|the case of large inert primes]].
* \(p\) does not split and \(p\le k\): [[proofs/grh/derivatives-vacuum/valuation-bound-at-small-non-split-primes|the case of small non-split primes]].

## References

1. Lean: `New.Data.leastValLE_twelve` in `src/New/Derivatives/Sharpness/Cases.lean`.
