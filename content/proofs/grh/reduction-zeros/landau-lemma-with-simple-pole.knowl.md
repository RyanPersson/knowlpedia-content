+++
id = "proofs/grh/reduction-zeros/landau-lemma-with-simple-pole"
title = "Landau's lemma at a simple pole with residue of non-positive real part"
kind = "proposition"
summary = "If the continuation of a Laplace transform of a nonnegative measure has at most a simple pole at the real endpoint, with residue of real part at most 0, the transform converges further to the left."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.exists_Ioi_subset_integrableExpSet"]
lean_files = ["src/Lib/Analytic/Landau.lean"]
proof_status = "full"
+++

**Proposition.** Let \(\mu\), \(X\le0\), \(S\) and \(M\) be as in [[proofs/grh/reduction-zeros/landau-lemma|Landau's lemma]], and let \((a,\infty)\) lie in the interior of \(S\). Let \(\Psi\) be [[complex-analysis/meromorphic-function|meromorphic]] at \(a\), let \(\Psi=M\) on a punctured neighbourhood of every real \(x>a\), and let
\[
\lim_{z\to a,\ z\ne a}(z-a)\Psi(z)=c\quad\text{with }\operatorname{Re}c\le0 .
\]
Then there is \(b<a\) with \((b,\infty)\subseteq S\).

## Proof

*\(\Psi=M\) near real points.* Since \(\Psi\) is meromorphic at \(a\), it is holomorphic on a punctured neighbourhood of \(a\). For real \(x>a\) close to \(a\), both \(\Psi\) and \(M\) are holomorphic at \(x\) and agree on a punctured neighbourhood of \(x\); hence they agree on a neighbourhood of \(x\). In particular \(\Psi(x)=M(x)=\int e^{xX}\,d\mu\ge0\).

*The residue vanishes.* For such \(x\), \((x-a)\Psi(x)\) is a nonnegative real number. Letting \(x\downarrow a\) gives \(c\in[0,\infty)\). With \(\operatorname{Re}c\le0\) this forces \(c=0\).

*Removing the singularity.* The function \(G(z)=(z-a)\Psi(z)\) is meromorphic at \(a\) and tends to \(0\) there, so it extends holomorphically with \(G(a)=0\). Then \(g(z)=G(z)/(z-a)\) (with \(g(a)=G'(a)\)) is holomorphic at \(a\) and equals \(\Psi\) for \(z\ne a\). So for real \(x>a\) near \(a\), \(g=\Psi=M\) near \(x\), and Landau's lemma applied to \(g\) gives \(b\). \(\blacksquare\)

## References

1. Lean: `New.exists_Ioi_subset_integrableExpSet` in `src/Lib/Analytic/Landau.lean`.
