+++
id = "proofs/grh/reduction-zeros/no-pole-right-of-beta"
title = "No pole to the right of the exponent of a one-sided bound"
kind = "theorem"
summary = "For a polar function bounded above by exp((beta-1)v) whose residues at real points beyond beta have nonnegative real part, all residues in Re s > beta vanish."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsPolar.landau", "New.eventuallyEq_of_eq_far_right"]
lean_files = ["src/Lib/Analytic/Landau.lean"]
proof_status = "full"
+++

**Theorem.** Let \(E\) be a [[proofs/grh/reduction-zeros/polar-function|polar function]] with residues \(r\), and let \(\beta>0\). Assume

* \(\operatorname{Re}r(x)\ge0\) for every real \(x>\beta\);
* \(E(v)\le e^{(\beta-1)v}\) for all sufficiently large real \(v\).

Then \(r(\rho)=0\) for every \(\rho\in\mathbb{C}\) with \(\operatorname{Re}\rho>\beta\).

## Proof

Let \(C\) and \(\Phi\) be as in the definition of a polar function. By the [[proofs/grh/reduction-zeros/measure-for-one-sided-bound|lemma on the attached measure]] there are \(K\in\mathbb{R}\) and a measure \(\mu\) on \((0,\infty)\) such that, with
\[
F(s)=\int e^{-sv}\,d\mu(v),\qquad \Psi(s)=\frac{K}{s-\beta}-\Phi(s),
\]
the integral \(F(s)\) converges and \(F(s)=\Psi(s)\) for \(\operatorname{Re}s>\beta+2\). The function \(\Psi\) is meromorphic on \(\mathbb{C}\).

*Residues of \(\Psi\).* For \(\operatorname{Re}\rho>\beta\) the function \(K/(s-\beta)\) is continuous at \(\rho\), so \(\lim_{z\to\rho}(z-\rho)\Psi(z)=-r(\rho)\) (note \(\operatorname{Re}\rho>0\)).

*The abscissa.* Let \(S=\{\sigma\in\mathbb{R}:\int e^{-\sigma v}d\mu<\infty\}\). Its complement is bounded above by \(\beta+2\). Let \(a=\sup(\{\beta\}\cup(\mathbb{R}\setminus S))\ge\beta\). Then \((a,\infty)\subseteq S\), so \((a,\infty)\) lies in the interior of \(S\), and \(F\) is holomorphic on \(\operatorname{Re}s>a\). Both \(\Psi\) and \(F\) are meromorphic on the connected open set \(\operatorname{Re}s>a\) and agree for \(\operatorname{Re}s>\beta+2\); by the [[complex-analysis/identity-theorem|identity theorem]], \(\Psi=F\) on a punctured neighbourhood of every point of \(\operatorname{Re}s>a\).

*Case \(a=\beta\).* Let \(\operatorname{Re}\rho>\beta\). Near \(\rho\), \(\Psi\) agrees off \(\rho\) with the function \(F\), holomorphic at \(\rho\); so \((z-\rho)\Psi(z)\to0\), and \(-r(\rho)=0\).

*Case \(a>\beta\) is impossible.* The residue of \(\Psi\) at the real point \(a>\beta\) is \(-r(a)\), of real part \(\le0\) by hypothesis. Apply [[proofs/grh/reduction-zeros/landau-lemma-with-simple-pole|Landau's lemma at a simple pole]] with \(X(v)=-\lvert v\rvert\) (so \(\int e^{sX}d\mu=F(s)\)): there is \(b<a\) with \((b,\infty)\subseteq S\). As \(\max(\beta,b)<a\) and \(a\) is a least upper bound, there is \(\sigma\in\{\beta\}\cup(\mathbb{R}\setminus S)\) with \(\max(\beta,b)<\sigma\le a\). Then \(\sigma\ne\beta\), so \(\sigma\notin S\); but \(\sigma>b\) gives \(\sigma\in S\). Contradiction. \(\blacksquare\)

## References

1. Lean: `New.IsPolar.landau` in `src/Lib/Analytic/Landau.lean`.
2. H. L. Montgomery, R. C. Vaughan, *Multiplicative Number Theory I*, Cambridge University Press, 2007, Lemma 15.1 and §15.1 (as cited in the head of the Lean file).
