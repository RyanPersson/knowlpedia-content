+++
id = "proofs/grh/reduction-zeros/tauberian-theorem"
title = "A Tauberian theorem with a power of the logarithm"
kind = "theorem"
summary = "A Lipschitz function whose Laplace-type transform is (F(s) - F(1))/(s - 1), with F holomorphic and polynomially bounded in l on regions reaching l^(-A) to the left of Re s = 1, decays faster than every power."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.eventually_abs_le_inv_pow_of_transform", "New.eventually_log_pow_le_and_pow_le_exp_sqrt"]
lean_files = ["src/Lib/Analytic/PrimeNumberTheorem/Tauberian.lean"]
proof_status = "full"
+++

**Theorem.** Let \(R\colon\mathbb{R}\to\mathbb{R}\) be [[measure-theory/measurable-function|measurable]], \(L\) a real number, \(F\colon\mathbb{C}\to\mathbb{C}\) a function and \(A\ge0\) an integer such that

* \(\lvert R(v)-R(u)\rvert\le L\,(v-u)\) whenever \(0\le u\le v\le u+1\);
* \(\displaystyle\frac{F(s)-F(1)}{s-1}=\int_0^\infty R(v)\,e^{(1-s)v}\,dv\) for all \(s\) with \(\operatorname{Re}s>2\);
* there is \(l_0\) such that for all \(l\ge l_0\) and all \(s\) with \(\operatorname{Re}s\ge1-l^{-A}\) and \(\lvert s\rvert\le e^{l}\), \(F\) is complex differentiable at \(s\) and \(\lvert F(s)\rvert\le l^{A}\).

Then for every integer \(B\ge0\) there is \(u_0\) with \(\lvert R(u)\rvert\le u^{-B}\) for all \(u\ge u_0\).

## Proof

By the [[proofs/grh/reduction-zeros/taylor-coefficient-as-gamma-mean|lemma on Gamma means]] (part 4), \(R\) is Lipschitz on \([0,\infty)\) with constant \(L\ge0\). Let \(g\) be the slope of \(F\) at \(1\) as in the [[proofs/grh/reduction-zeros/cauchy-estimate-for-slope|Cauchy estimate for a slope]]; for \(\operatorname{Re}s>2\), \(g(s)\) is the transform of \(R\).

Fix \(B\) and let \(u\) be large (how large is specified along the way). Put
\[
l=(2B+5)\log u,\qquad k=\lfloor u^{2B+4}\rfloor,\qquad H=\frac{k+1}{u},\qquad\eta=l^{-A},\qquad\delta=u^{-(B+1)},
\]
and \(T=\dfrac{(-H)^{k}H}{k!}g^{(k)}(1+H)\). For large \(u\): \(l\ge\max(1,l_0)\), \(u\ge2L+8\), \(l^{2A}\le u\) and \(u^{3B+7}\le e^{\sqrt u/2}\). Since \(u^{2B+4}\le k+1\le u^{2B+4}+1\), we have \(1<H\le2u^{2B+4}\), and \(\eta\le1<H\).

*\(T\) is close to \(R(u)\).* By part 3 of the lemma on Gamma means (applied to \(\Phi=g\)),
\[
\lvert T-R(u)\rvert\le L\Bigl(u^{-(B+1)}+\frac{u^{2}}{k+1}\,u^{B+1}\Bigr)\le L\bigl(u^{-(B+1)}+u^{2-(2B+4)+(B+1)}\bigr)=2L\,u^{-(B+1)}.
\]

*\(T\) is small.* Every \(s\) in the closed disc of radius \(H+\eta\) about \(1+H\) has \(\operatorname{Re}s\ge1-\eta=1-l^{-A}\) and \(\lvert s\rvert\le2H+\eta+1\le4u^{2B+4}+2\le u^{2B+5}=e^{l}\) (as \(u\ge8\)). So \(F\) is holomorphic there with \(\lvert F\rvert\le M=l^{A}\), and the Cauchy estimate for a slope gives
\[
\lvert T\rvert\le4\,l^{A}\,H\,l^{A}\exp\Bigl(-\frac{(k+1)\,l^{-A}}{2H}\Bigr)=l^{2A}\cdot4H\cdot\exp\Bigl(-\frac{u}{2\,l^{A}}\Bigr).
\]
Now \(l^{2A}\le u\) gives \(l^{A}\le\sqrt u\), hence \(\exp(-u/(2l^{A}))\le e^{-\sqrt u/2}\le u^{-(3B+7)}\); and \(4H\le8u^{2B+4}\le u^{2B+5}\). Therefore \(\lvert T\rvert\le u\cdot u^{2B+5}\cdot u^{-(3B+7)}=u^{-(B+1)}\).

*Conclusion.* \(\lvert R(u)\rvert\le\lvert T\rvert+\lvert T-R(u)\rvert\le(1+2L)\,u^{-(B+1)}\le u^{-B}\), since \(1+2L\le u\). \(\blacksquare\)

## Remarks

The theorem replaces the contour integration usual in proofs of the prime number theorem: one Taylor coefficient of the transform at the far point \(1+H\) is read once as a mean of \(R\) concentrated near \(u\), and once through Cauchy's estimate on a disc that crosses the line \(\operatorname{Re}s=1\).

## References

1. Lean: `New.eventually_abs_le_inv_pow_of_transform` in `src/Lib/Analytic/PrimeNumberTheorem/Tauberian.lean`.
2. H. L. Montgomery, R. C. Vaughan, *Multiplicative Number Theory I*, 2007, Section 6.2 (cited in the head of the Lean file for the result, proved there by a contour integral).
