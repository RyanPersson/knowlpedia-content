+++
id = "proofs/grh/derivatives-vacuum/least-valuation-with-a-unit-form"
title = "Least valuation over six copies when one form has unit coefficients"
kind = "theorem"
summary = "If one of the linear forms has all coefficients of absolute value one, the least valuation over six copies in degree nu is at most gamma_p times the degree of nu minus the valuation of nu factorial."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.CMLattice.leastValLE_of_unit_coefficients"]
lean_files = ["src/New/Derivatives/Sharpness/LeastValuation.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/derivatives-vacuum/least-valuation-relation|the least valuation relation]]; \(d\) is a prime \(\equiv7\bmod8\), \(\gamma_p\) the [[?lean:New.gammaPrime|rate]] (\(0\), \(p/(p^2-1)\), \(1/(2p-2)\) for \(p\) split, inert, ramified in \(K\)).

**Theorem.** Suppose \(\lvert\mu_{i_0,x}\rvert_p=1\) for some \(i_0\in J\) and all \(x\in X\). Then for every exponent \(\nu\)
\[ \operatorname{val}_6(\nu)\le\gamma_p\lvert\nu\rvert-v_p(\nu!),\qquad\nu!=\prod_x\nu_x! . \]

## Proof

By [[proofs/grh/derivatives-vacuum/katz-divisibility-limit|the limit of Katz divisibility]] there is \(g\in\mathcal{O}[\![y]\!]\) with \(\lvert\lvert\nu\rvert!\,[z^{\lvert\nu\rvert}]g\rvert_p\ge p^{-\gamma_p\lvert\nu\rvert}\). Put \(G=g(\mu_{i_0}z)\in\mathcal{O}[\![y(\mu z)]\!]\). By [[proofs/grh/derivatives-vacuum/six-scaled-copies-are-a-unit|the theorem on six scaled copies]] choose \(\delta\in\mathbb{Z}_p^6\) with \(\delta_1=1\) and an inverse \(V\) of \(\Theta_\delta\) in \(\mathcal{O}[\![y(\mu z)]\!]\). Take \(H_1=GV\) and \(H_c=1\) for \(c\ge2\). Then
\[ \prod_{c=1}^6(H_c\Theta)(\delta_cz)=G(z)V(z)\,\Theta_\delta(z)=G(z). \]
The coefficient of \(z^\nu\) in \(G=g(\sum_x\mu_{i_0,x}z_x)\) is \(\frac{\lvert\nu\rvert!}{\nu!}\prod_x\mu_{i_0,x}^{\nu_x}\,[z^{\lvert\nu\rvert}]g\), of absolute value \(\lvert\lvert\nu\rvert!\,[z^{\lvert\nu\rvert}]g\rvert_p\cdot p^{v_p(\nu!)}\ge p^{-(\gamma_p\lvert\nu\rvert-v_p(\nu!))}\). Conclude by rule 3 of [[proofs/grh/derivatives-vacuum/least-valuation-rules|the rules]] (the \(\delta_c\) are integral).

## References

1. Lean: `New.CMLattice.leastValLE_of_unit_coefficients` in `src/New/Derivatives/Sharpness/LeastValuation.lean`.
