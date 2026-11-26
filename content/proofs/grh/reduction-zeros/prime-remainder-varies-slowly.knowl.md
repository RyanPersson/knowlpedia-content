+++
id = "proofs/grh/reduction-zeros/prime-remainder-varies-slowly"
title = "The remainder varies slowly"
kind = "lemma"
summary = "R_q changes by at most 13(z-y)/y between y and z, and is Lipschitz with constant 26 in the variable log y on steps of length at most 1."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.abs_primeRemainder_sub_le", "New.abs_primeRemainder_exp_sub_le"]
lean_files = ["src/New/Reduction/Zeros/PrimeNumberTheorem.lean"]
proof_status = "full"
+++

**Lemma.** Let \(d\) be a prime, \(q\ge1\) and \(R_q\) the [[proofs/grh/reduction-zeros/prime-remainder|remainder]].

1. For \(1\le y\le z\): \(\lvert R_q(z)-R_q(y)\rvert\le13\,\dfrac{z-y}{y}\).
2. For \(0\le u\le v\le u+1\): \(\lvert R_q(e^{v})-R_q(e^{u})\rvert\le26\,(v-u)\).

## Proof

1. By the [[proofs/grh/reduction-zeros/prime-remainder-as-integral|integral formula]], \(R_q(z)-R_q(y)=\int_y^{z}\mathcal{E}_q(t)t^{-2}dt\), and \(\lvert\mathcal{E}_q(t)\rvert t^{-2}\le13/t\le13/y\) on \([y,z]\).

2. By 1 with \(y=e^{u}\), \(z=e^{v}\): the difference is at most \(13(e^{v-u}-1)\), and \(e^{x}-1\le2x\) for \(0\le x\le1\). \(\blacksquare\)

## References

1. Lean: `New.abs_primeRemainder_sub_le`, `New.abs_primeRemainder_exp_sub_le` in `src/New/Reduction/Zeros/PrimeNumberTheorem.lean`.
