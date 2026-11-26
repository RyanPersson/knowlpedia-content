+++
id = "proofs/grh/upper-divisibility/scaled-hecke-operator"
title = "Scaled Hecke operator at a marked prime"
kind = "definition"
summary = "The operator p^(A_l) T_(l,r) on source forms, for a marked prime l and r the base-p logarithm of m rounded up."
aliases = ["scaled Hecke operator"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.IsMarked.scaledHeckeOperator"]
lean_files = ["src/New/UpperBound/Divisibility/MarkedPrimes.lean"]
+++

Let \(\Lambda\) be a [[proofs/grh/upper-divisibility/marked-set-of-primes|marked set]] of primes of \(E\) above \(p\), \(\mathfrak l\in\Lambda\), and \(\mathfrak r=\mathfrak r(p)\) the least natural number with \(m\le p^{\mathfrak r}\). Since \(\mathfrak l\ne\bar{\mathfrak l}\), the unitary group of \(X_0\) at the pair \(\{\mathfrak l,\bar{\mathfrak l}\}\) is a general linear group over \(E_{\mathfrak l}\), and \(T_{\mathfrak l,\mathfrak r}\) denotes the [[?lean:New.heckeSplit|Hecke operator at the split prime \(\mathfrak l\) of index \(\mathfrak r\)]] acting on algebraic forms of the weight of \(X_0\). It preserves the space \(\mathcal S\) of [[?lean:New.Data.SourceForm|source forms]], because these are spherical at \(\mathfrak l\) ([[proofs/grh/upper-divisibility/properties-of-marked-sets|properties of marked sets]], (4)) and the Hecke operator at \(\mathfrak l\) commutes with the level away from \(\mathfrak l\). The **scaled Hecke operator** at \(\mathfrak l\) is the endomorphism
\[
\widetilde T_{\mathfrak l}\;=\;p^{A_{\mathfrak l}}\cdot T_{\mathfrak l,\mathfrak r}\ \colon\ \mathcal S\to\mathcal S,
\]
where \(A_{\mathfrak l}=a\cdot\lvert\{\tau\in\Phi_a:w_\tau=\mathfrak l\}\rvert\) is the Hecke scaling exponent. It is regarded as linear over the valuation ring \(\{z\in\mathbb{C}:\lvert\iota z\rvert_p\le1\}\).

## Remarks

The scaling by \(p^{A_{\mathfrak l}}\) makes the operator preserve the integral source forms and gives its cokernel on them a controlled length; see [[proofs/grh/upper-divisibility/mark-operator|the mark operator]].

## References

1. Lean: `New.Data.IsMarked.scaledHeckeOperator` in `src/New/UpperBound/Divisibility/MarkedPrimes.lean`; `New.heckeSplit` is defined in another file.
