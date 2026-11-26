+++
id = "proofs/grh/derivatives-vacuum/katz-divisibility-limit"
title = "The limit of Katz divisibility of derivatives"
kind = "theorem"
summary = "For every n some integral power series in the parameter y of the CM lattice has n-th derivative at 0 of valuation at most gamma_p n."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.CMLattice.katz_divisibility_limit"]
lean_files = ["src/New/Derivatives/Sharpness/OneCurve.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/derivatives-vacuum/derivatives-of-the-formal-parameter|the lemma on the formal parameter]].

**Theorem.** Let \(d\) be a prime \(\equiv7\bmod8\), \(C\) a CM lattice for \(d\), \(p\) a prime and \(\iota_p\) a \(p\)-adic place. For every \(n\in\mathbb{N}\) there is \(f\in\mathcal{O}[\![y]\!]\) with
\[ \lvert f^{(n)}(0)\rvert_p\ge p^{-\gamma_pn},\qquad\gamma_p=\frac1{p-1}-\rho_p . \]

## Proof

Let \(b=p^{-\gamma_p}\); \(0<b\le1\) since \(\gamma_p\ge0\). The sequence \(c_C\) has \(c_C(0)=1\), values in \([0,1]\), and is [[proofs/grh/derivatives-vacuum/greatest-norm-of-derivatives-is-submultiplicative|submultiplicative]]. For every \(M\), \(q=q_p^{M}>M\) and by [[proofs/grh/derivatives-vacuum/derivatives-of-the-formal-parameter|the formal parameter]] \(c_C(q)\ge b^{q-1}\ge b^q\). By [[proofs/grh/derivatives-vacuum/submultiplicative-sequences|the lemma on submultiplicative sequences]], \(b^n\le c_C(n)\) for all \(n\), and \(c_C(n)\) is attained by some \(f\).

## References

1. Lean: `New.CMLattice.katz_divisibility_limit` in `src/New/Derivatives/Sharpness/OneCurve.lean`.
2. The Lean file head: at inert primes the rate is that of N. Katz, Divisibilities, congruences, and Cartier duality (no locator given there).
