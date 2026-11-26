+++
id = "proofs/grh/derivatives-divisibility/integral-above-p"
title = "Elements of a number field integral above a prime"
kind = "definition"
summary = "An element of a number field is integral above p if it is integral at every prime ideal above p; it is then an algebraic integer divided by a natural number prime to p."
aliases = ["integral above p", "integral at all places above p"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsIntegralAbove", "New.IsIntegralAbove.exists_mul_eq", "New.IsIntegralAbove.norm_le_one", "New.IsIntegralAbove.norm_conj_le_one"]
lean_files = ["src/New/Derivatives/FormalGroup/Resolution.lean"]
+++

**Definition.** Let \(E\) be a [[algebra-fields-galois/number-field|number field]] with [[algebra-fields-galois/ring-of-integers|ring of integers]] \(\mathcal{O}_E\), and \(p\) a prime number. An element \(y\in E\) is **integral above \(p\)** if \(v_w(y)\ge0\) for the valuation \(v_w\) of every nonzero prime ideal \(w\) of \(\mathcal{O}_E\) that contains \(p\).

## Properties

1. If \(y\) is integral above \(p\), there are a natural number \(N\) prime to \(p\) and \(\alpha\in\mathcal{O}_E\) with \(Ny=\alpha\).
2. If \(y\) is integral above \(p\), then \(\lvert\sigma(y)\rvert\le1\) for every ring homomorphism \(\sigma\colon E\to\mathbb{C}_p\). In particular \(\lvert\iota_p(\overline{\tau(y)})\rvert\le1\) for every embedding \(\tau\colon E\to\mathbb{C}\) and every \(p\)-adic place \(\iota_p\) of \(\mathbb{C}\).

## Proof

1. Some positive integer \(D\) has \(Dy\in\mathcal{O}_E\); write \(D=p^kN\) with \(p\nmid N\). At a prime \(w\ni p\), \(v_w(Ny)\ge v_w(y)\ge0\). At a prime \(w\not\ni p\), \(p\) is a unit, so \(v_w(Ny)=v_w(p^kNy)\ge0\). An element of \(E\) with nonnegative valuation at all primes lies in \(\mathcal{O}_E\), since \(\mathcal O_E\) is a [[algebra-commutative/dedekind-domain|Dedekind domain]].

2. The set \(\{a\in\mathcal{O}_E:\lvert\sigma(a)\rvert<1\}\) is a prime ideal \(w\) containing \(p\), and \(\lvert\sigma(\cdot)\rvert\) is an absolute value on \(E\) equivalent to the \(w\)-adic one; so \(v_w(y)\ge0\) gives \(\lvert\sigma(y)\rvert\le 1\). For the last claim take \(\sigma=\iota_p\circ(\text{complex conjugation})\circ\tau\). \(\blacksquare\)

## References

1. Lean: `New.IsIntegralAbove`, `New.IsIntegralAbove.exists_mul_eq`, `New.IsIntegralAbove.norm_le_one`, `New.IsIntegralAbove.norm_conj_le_one` in `src/New/Derivatives/FormalGroup/Resolution.lean`; the place of an embedding into \(\mathbb{C}_p\) is `New.placeOfEmb` (`src/Lib/ClassField/Places/ValuationSubrings.lean`).
