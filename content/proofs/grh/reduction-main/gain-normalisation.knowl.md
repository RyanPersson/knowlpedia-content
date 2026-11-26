+++
id = "proofs/grh/reduction-main/gain-normalisation"
title = "Divisibility errors, gain exponents and the factor c_B"
kind = "definition"
summary = "A choice of the errors err_l in the divisibility of the composite lift, the integers g_l = floor(gain_l - err_l), and the rational number c_B, the product of l^(-g_l) over the non-split primes below x1 and N."
aliases = ["divisibilityError", "gainExponent", "invGainFactor", "c_B"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.divisibilityError", "New.Data.divisibilityError_nonneg", "New.Data.divisibilityError_eq_zero", "New.Data.sum_divisibilityError_mul_log_le", "New.Data.exists_colengthDvd_gaugeLe_divisibilityError", "New.Data.gainExponent", "New.Data.invGainFactor", "New.Data.prime_of_mem_smallNonsplitPrimes_union", "New.Data.invGainFactor_pos", "New.Data.sum_log_smallNonsplitPrimes_union_le", "New.Data.log_invGainFactor_le", "New.Data.norm_invGainFactor"]
lean_files = ["src/New/Reduction/ShortAndEnough.lean"]
+++

Let \(D\) be [[proofs/grh/reduction-main/data|data]]. Let \(\operatorname{gain}_\ell\ge0\) be the [[?lean:New.Data.gain|gain]], the divisibility asked of the chain of lifts at \(\ell\); it vanishes if \(\chi_K(\ell)=1\) or \(\ell\ge x_1\) ([[?lean:New.Data.gain_eq_zero|vanishing of the gain]]). Let \(\mathcal P\) be the set of primes \(\ell<x_1\) with \(\chi_K(\ell)\ne1\) ([[?lean:New.Data.smallNonsplitPrimes|small non-split primes]]).

- **Errors.** By the theorem on the [[?lean:New.Data.exists_err_gaugeLe_compositeLift|divisibility of the composite lift]] there are real numbers \(\operatorname{err}_\ell\), \(\ell\in\mathbb N\), with: (a) \(\operatorname{err}_\ell\ge0\); (b) \(\operatorname{err}_\ell=0\) if \(\ell\ne N\) and (\(\chi_K(\ell)=1\) or \(\ell\ge x_1\)); (c) \(\sum_{\ell\in U}\operatorname{err}_\ell\log\ell\le f\,a\log^3b\) for every finite \(U\subset\mathbb N\); (d) for every prime \(\ell\) and every \(\iota\mid\ell\) there are an integer \(0\le j\le\operatorname{err}_\ell\cdot D_X\) (\(D_X\) the dimension of the space of all source forms) and an \(\mathcal O_\iota\)-module \(S\) of source forms such that [[proofs/grh/reduction-main/colength-divides|\(\operatorname{colen}(I_\iota,S)\mid\ell^{\,j}\)]], where \(I_\iota\) is the \(\mathcal O_\iota\)-module of ramified source forms integral at \(\iota\), and such that for every \(\varphi\in S\), every twist \(\vartheta\) with \(\gcd(\ell,\mathrm{Nm}Q(\vartheta))=1\) and every chain datum \(\Psi\) of \(\vartheta\), the [[?lean:New.Data.compositeLift|composite lift]] \(B_{\vartheta,\Psi}\varphi\) has all values of \(\ell\)-adic gauge at most \(\ell^{\operatorname{err}_\ell-\operatorname{gain}_\ell}\). **One such family \((\operatorname{err}_\ell)\) is fixed once and for all** (by choice).
- **Gain exponent.** \(g_\ell:=\lfloor\operatorname{gain}_\ell-\operatorname{err}_\ell\rfloor\in\mathbb Z\).
- **The factor.** \(c_B:=\prod_{\ell\in\mathcal P\cup\{N\}}\ell^{-g_\ell}\), a positive rational number.

## Properties

1. \(g_\ell=0\) for primes \(\ell\notin\mathcal P\cup\{N\}\); hence \(\lvert c_B\rvert_\ell=\ell^{\,g_\ell}\) for every prime \(\ell\).
2. \(\sum_{\ell\in\mathcal P\cup\{N\}}\log\ell\le b\).
3. \(\log c_B\le-\sum_{\ell\in\mathcal P}\operatorname{gain}_\ell\log\ell+f\,a\log^3b+b\).

*Proof.* (1) A prime \(\ell\notin\mathcal P\), \(\ell\ne N\), has \(\chi_K(\ell)=1\) or \(\ell\ge x_1\), so gain and error vanish. In the product, the factors at primes \(p\ne\ell\) are \(\ell\)-adic units. (2) There are fewer than \(x_1\) primes in \(\mathcal P\), each with \(\log\ell\le x_1\); and \(x_1^2+\log N\le x_1^2+30m\log b\le b\) by the [[proofs/grh/reduction-main/data-sizes|sizes of the data]]. (3) \(-g_\ell<-\operatorname{gain}_\ell+\operatorname{err}_\ell+1\), so \(\log c_B\le\sum_{\mathcal P\cup\{N\}}(-\operatorname{gain}_\ell+\operatorname{err}_\ell+1)\log\ell\); now \(\operatorname{gain}_N=0\) because \(N\ge x_1\), and use (c) and (2). \(\square\)

## References

1. Lean: the declarations in the front matter, in `src/New/Reduction/ShortAndEnough.lean`.
