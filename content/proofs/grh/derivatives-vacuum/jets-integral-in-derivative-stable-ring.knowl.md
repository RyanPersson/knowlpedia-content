+++
id = "proofs/grh/derivatives-vacuum/jets-integral-in-derivative-stable-ring"
title = "Jets are integral on a ring of series stable under derivatives"
kind = "lemma"
summary = "If a subring of power series over C_p is stable under partial derivatives and its elements have integral constant terms, then all jets of its elements along polynomials with integral coefficients are integral."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.norm_jet_le_one_of_pderiv_mem"]
lean_files = ["src/New/Derivatives/Vacuum/JetIntegrality.lean"]
proof_status = "full"
+++

**Lemma.** Let \(p\) be a prime, \(X\) a set of variables and \(S\) a subring of \(\mathbb{C}_p[\![X_x:x\in X]\!]\) such that every \(F\in S\) has \(\lvert F(0)\rvert_p\le1\) and \(\partial_xF\in S\) for all \(x\). Let \(R\) be a commutative ring and \(\varphi\colon R\to\mathbb{C}_p\) a ring homomorphism with \(\lvert\varphi(a)\rvert_p\le1\) for all \(a\). Then for every \(Q\in R[X]\) and \(F\in S\),
\[ \bigl\lvert\bigl(\varphi(Q)(\partial)F\bigr)(0)\bigr\rvert_p\le1. \]

## Proof

Induction on the structure of \(Q\), for all \(F\in S\) simultaneously. For a constant \(Q=a\): the jet is \(\varphi(a)F(0)\). For a sum: the ultrametric inequality. For \(Q=Q'X_x\): the jet of \(F\) along \(Q'X_x\) is the jet of \(\partial_xF\in S\) along \(Q'\).

## References

1. Lean: `New.norm_jet_le_one_of_pderiv_mem` in `src/New/Derivatives/Vacuum/JetIntegrality.lean`.
