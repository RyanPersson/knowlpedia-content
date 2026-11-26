+++
id = "proofs/grh/upper-elementary-divisors/large-degree-conditions"
title = "Size conditions of large degree"
kind = "definition"
summary = "The numerical hypotheses of the theorem on elementary divisors relating the rank k, the degree n, the block size r, the proportion theta, and the sizes P and q."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.IsLargeDegree", "New.FrobeniusCycle.congruencePrecision", "New.FrobeniusCycle.two_le_card_letters", "New.FrobeniusCycle.card_isEven_add_self"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean"]
+++

Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] with \(N\ge1\) letters, and let \(k,n,r\in\mathbb{N}\), \(\theta\in\mathbb{R}\). The degree is **large** for \((k,n,r,\theta)\) if

1. \(0<r\) and \(2r\le k\);
2. \(0<\theta\le1\);
3. \(n^{4}\le q\);
4. \(\bigl(N\,k\,\log q/\theta\bigr)^{5}\,P^{3r}\le n\) (natural logarithm).

The **congruence precision** is \(c=5Nc_0\), with \(c_0=k^{2}fN\) (\(P=p^{f}\)).

## Remarks

Exactly half of the letters are even (shifting by one exchanges even and odd letters), so \(N=2\ell\) is even and \(N\ge2\). The numerical consequences used in the proofs are collected in [[proofs/grh/upper-elementary-divisors/consequences-of-large-degree|consequences of large degree]].

## References

1. Lean: `New.FrobeniusCycle.IsLargeDegree`, `New.FrobeniusCycle.congruencePrecision`, `New.FrobeniusCycle.two_le_card_letters`, `New.FrobeniusCycle.card_isEven_add_self` in `src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean`.
