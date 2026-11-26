+++
id = "proofs/grh/reduction-zeros/g-q-at-one-is-real"
title = "The value G_q(1) is real"
kind = "lemma"
summary = "For odd d prime to q the number G_q(1) is real, hence equal to the constant c_q."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.ofReal_re_logDerivMean_one"]
lean_files = ["src/New/Reduction/Zeros/PrimeError.lean"]
proof_status = "full"
+++

**Lemma.** Let \(d\) be an odd prime and \(q\ge1\) prime to \(d\). Then \(G_q(1)\in\mathbb{R}\), for the [[proofs/grh/reduction-zeros/log-deriv-mean|function \(G_q\)]]. Consequently \(c_q=\operatorname{Re}G_q(1)=G_q(1)\).

## Proof

Let \(F(s)=G_q(s)/s-c_q\). It is holomorphic at every real \(x\ge1\), since \(G_q\) is holomorphic on \(\operatorname{Re}s\ge1\). For real \(x>2\), by the [[proofs/grh/reduction-zeros/laplace-transform-of-prime-remainder|Laplace transform of the remainder]],
\[
F(x)=(x-1)\int_0^\infty R_q(e^{v})\,e^{(1-x)v}\,dv\in\mathbb{R}.
\]
The function \(x\mapsto\operatorname{Im}F(x)\) is real-analytic on \([1,\infty)\) and vanishes on \((2,\infty)\); as \([1,\infty)\) is connected, it vanishes identically. At \(x=1\): \(0=\operatorname{Im}F(1)=\operatorname{Im}G_q(1)\). \(\blacksquare\)

## References

1. Lean: `New.ofReal_re_logDerivMean_one` in `src/New/Reduction/Zeros/PrimeError.lean`.
