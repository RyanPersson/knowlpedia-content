+++
id = "proofs/grh/derivatives-vacuum/bound-for-the-partner-minimum-sum"
title = "A bound for the partner minimum sum"
kind = "lemma"
summary = "If a near pair with start tau can occur only at one exponent and its term is at most c + 1, then R_tau is at most c + 1 + l0 a/x1 + 2b/(kp)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.partnerMinSum_le", "New.Data.partnerMinTerm_le_of_not_isNearPair", "New.Data.tsum_partnerMinTerm_add_le"]
lean_files = ["src/New/Derivatives/Sharpness/NearPairs.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/derivatives-vacuum/partner-minimum-sum|the partner minimum sum]].

**Lemma.** Let \(p\) be a prime, \(\tau\in\Phi\), \(e_0\in\mathbb{N}\) and \(c\ge0\). Suppose that every [[proofs/grh/derivatives-vacuum/near-pair|near pair]] \((\tau,e)\) has \(e=e_0\) and \(\kappa(\tau)/p^e\le c+1\). Then
\[ R_\tau\le c+1+l_0\,\frac{a}{x_1}+\frac{2b}{kp}. \]

## Proof

Let \(n=\lceil l_0/2\rceil\) and split the series at \(n\).

*Terms with \(e<n\)* (so \(2e<l_0\), as \(l_0\) is odd). If \((\tau,e)\) is a near pair, then \(e=e_0\) and the term is \(\le\kappa(\tau)/p^e\le c+1\); this happens for at most one \(e\). Otherwise the term is \(\le a/x_1\): if \(\tau\notin\Phi_b\) it is \(\le\kappa(\tau)=a/x_1\); if \(\tau\in\Phi_b\) and \(e\in I_p\), the partner is not a \(b\)-place (else the pair would be near), so the minimum is \(\le\kappa([-p^e]\tau)=a/x_1\). There are \(n\le l_0\) such terms.

*Terms with \(e\ge n\).* The term at \(e+n\) is \(\le b/(2^ep^n)\), so the tail is \(\le2b/p^n\). Since \(2n\ge l_0>2s\) we have \(n\ge s+1\), and \(k\le2^s\le p^{n-1}\) (the first inequality is a scale inequality of the data, Lean `D.le_of_hasLogBound`). Hence the tail is \(\le2b/(kp)\).

## References

1. Lean: `New.Data.partnerMinSum_le`, `New.Data.partnerMinTerm_le_of_not_isNearPair`, `New.Data.tsum_partnerMinTerm_add_le` in `src/New/Derivatives/Sharpness/NearPairs.lean`.
