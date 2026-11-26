+++
id = "proofs/grh/upper-divisibility/marked-set-of-primes"
title = "Induced primes, marked sets and full marks"
kind = "definition"
summary = "For an exceptional prime p below x_1 and an embedding of C in C_p: the prime induced by an infinite place, sets of induced primes disjoint from their conjugates, and full marks."
aliases = ["marked set", "full mark", "induced prime", "marked prime", "Hecke scaling exponent"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.inducedPlace", "New.Data.IsMarked", "New.Data.IsFullMark", "New.Data.placesInducing", "New.Data.placesInducingConj", "New.Data.heckeScalingExponent", "New.Data.sum_heckeScalingExponent", "New.Data.integralSourceForms"]
lean_files = ["src/New/UpperBound/Divisibility/MarkedPrimes.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]] with CM field \(E\), let \(p\) be a prime and fix an embedding \(\iota\colon\mathbb{C}\to\mathbb{C}_p\) into the [[?c:Field of p-adic complex numbers|\(p\)-adic complex numbers]]. Each infinite place \(\sigma\in\Phi\) is read as the embedding \(E\to\mathbb{C}\) selected by the CM type.

- The **prime induced by \(\sigma\)** is the prime \(w_\sigma\) of \(E\) above \(p\) defined by \(\iota\circ\sigma\): \(w_\sigma=\{x\in\mathcal O_E:\lvert\iota(\sigma x)\rvert_p<1\}\).
- A finite set \(\Lambda\) of primes of \(E\) is **marked** (at \(\iota\)) if (i) \(\mathfrak l\in\Lambda\Rightarrow\bar{\mathfrak l}\notin\Lambda\); (ii) every \(\mathfrak l\in\Lambda\) is induced by an [[?lean:New.Data.aPlaces|a-place]]; (iii) \(p\) is [[proofs/grh/upper-divisibility/classes-of-primes|exceptional]]; and (iv) \(p<x_1\) and \(\chi_K(p)\ne1\).
- A **full mark** is a marked set \(\Lambda\) such that for every a-place \(\tau\), \(w_\tau\in\Lambda\) or \(\bar w_\tau\in\Lambda\).
- For a set \(\Lambda\), \(\Phi_\Lambda=\{\sigma:w_\sigma\in\Lambda\}\) and \(\Phi_{\bar\Lambda}=\{\sigma:\bar w_\sigma\in\Lambda\}\) are the places inducing a prime of \(\Lambda\), respectively the conjugate of one.
- The **Hecke scaling exponent** of a prime \(\mathfrak l\) is \(A_{\mathfrak l}=a\cdot\lvert\{\tau\in\Phi_a:w_\tau=\mathfrak l\}\rvert\); thus \(\sum_{\mathfrak l\in\Lambda}A_{\mathfrak l}=a\,\lvert\Phi_a\cap\Phi_\Lambda\rvert\).
- The **integral source forms** are the source forms of [[?lean:New.weylGauge|gauge]] at most \(1\) at \(\iota\); they form a module over the valuation ring \(\{z\in\mathbb{C}:\lvert\iota z\rvert_p\le1\}\).

## Remarks

Marked sets exist only for exceptional primes; for these the removal of the long rows at the places inducing a full mark removes all [[proofs/grh/upper-divisibility/collisions|collisions]] ([[proofs/grh/upper-divisibility/full-mark-exists|existence of full marks]]), and the lost divisibility is recovered through the [[proofs/grh/upper-divisibility/scaled-hecke-operator|scaled Hecke operators]] at the primes of \(\Lambda\).

## References

1. Lean: the declarations listed in the front matter, in `src/New/UpperBound/Divisibility/MarkedPrimes.lean`.
