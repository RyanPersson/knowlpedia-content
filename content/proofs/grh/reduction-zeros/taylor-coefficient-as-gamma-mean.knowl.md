+++
id = "proofs/grh/reduction-zeros/taylor-coefficient-as-gamma-mean"
title = "A Taylor coefficient of a Laplace transform as a Gamma mean"
kind = "lemma"
summary = "A normalised k-th derivative of the transform at 1 + H is the mean of the function against a Gamma density, hence close to its value at the mean for a Lipschitz function."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.iteratedDeriv_transform", "New.integrableOn_and_integral_pow_mul_exp_neg_mul", "New.integrableOn_and_integral_gamma_mul_quadratic", "New.norm_taylorCoeff_transform_sub_le", "New.norm_taylorCoeff_transform_sub_le_of_lipschitz", "New.abs_sub_le_of_unit_steps"]
lean_files = ["src/Lib/Analytic/PrimeNumberTheorem/Tauberian.lean"]
proof_status = "full"
+++

**Lemma.** Let \(R\colon\mathbb{R}\to\mathbb{R}\) be [[measure-theory/measurable-function|measurable]] with \(\lvert R(v)\rvert\le Ce^{v}\) for \(v\ge0\), and let \(\Phi\) be a function with \(\Phi(s)=\int_0^\infty R(v)e^{(1-s)v}dv\) for \(\operatorname{Re}s>2\). For \(H>1\) and an integer \(k\ge0\) put
\[
T_k(H)=\frac{(-H)^{k}H}{k!}\,\Phi^{(k)}(1+H).
\]

1. \(\Phi^{(k)}(s)=\int_0^\infty(-v)^{k}R(v)e^{(1-s)v}dv\) for \(\operatorname{Re}s>2\), with absolute convergence. Hence
\[
T_k(H)=\int_0^\infty R(v)\,\frac{H^{k+1}v^{k}e^{-Hv}}{k!}\,dv ,
\]
the mean of \(R\) for the [[?c:Gamma distribution|Gamma density]] of mean \((k+1)/H\) and variance \((k+1)/H^{2}\).
2. If \(\lvert R(v)-c\rvert\le a+b\,(v-(k+1)/H)^{2}\) for all \(v>0\), then \(\lvert T_k(H)-c\rvert\le a+b\,(k+1)/H^{2}\).
3. If \(\lvert R(y)-R(x)\rvert\le L\lvert y-x\rvert\) for all \(x,y\ge0\), and \(u>0\), \(\delta>0\), \(H=(k+1)/u>1\), then
\[
\lvert T_k(H)-R(u)\rvert\le L\Bigl(\delta+\frac{u^{2}}{(k+1)\,\delta}\Bigr).
\]
4. If \(\lvert R(v)-R(u)\rvert\le L(v-u)\) whenever \(0\le u\le v\le u+1\), then \(\lvert R(y)-R(x)\rvert\le L\lvert y-x\rvert\) for all \(x,y\ge0\).

## Proof

1. By induction on \(k\), differentiating under the integral sign ([[measure-theory/dominated-convergence-theorem|dominated convergence]]): for \(\operatorname{Re}z>2+2\varepsilon\) the derivative in \(z\) of \((-v)^kR(v)e^{(1-z)v}\) is bounded by \(\varepsilon^{-1}v^{k}\lvert R(v)\rvert e^{(1-(2+\varepsilon))v}\), because \(\varepsilon v\le e^{\varepsilon v}\), and this is integrable by the induction hypothesis at \(2+\varepsilon\). At \(s=1+H\) the factor is \(e^{-Hv}\), and \((-H)^{k}(-1)^{k}=H^{k}\).

2. The moments \(\int_0^\infty v^{j}e^{-Hv}dv=j!/H^{j+1}\) show that the density has total mass \(1\), mean \((k+1)/H\) and second moment \((k+1)(k+2)/H^2\), so variance \((k+1)/H^2\). Then \(T_k(H)-c\) is the mean of \(R-c\), bounded by the mean of \(a+b(v-(k+1)/H)^2\).

3. For \(v>0\): \(\lvert R(v)-R(u)\rvert\le L\lvert v-u\rvert\le L\bigl(\delta+(v-u)^2/\delta\bigr)\), since \(t\le\delta+t^{2}/\delta\) for \(t\ge0\). Also \(\lvert R(v)\rvert\le(\lvert R(0)\rvert+L)e^{v}\). Apply 2 with \(c=R(u)\), \(a=L\delta\), \(b=L/\delta\), and \((k+1)/H=u\), \((k+1)/H^{2}=u^{2}/(k+1)\).

4. For \(x\le y\) cut \([x,y]\) into \(n>y-x\) equal steps of length \(\le1\) and add the bounds. \(\blacksquare\)

## References

1. Lean: `New.iteratedDeriv_transform`, `New.norm_taylorCoeff_transform_sub_le`, `New.norm_taylorCoeff_transform_sub_le_of_lipschitz`, `New.abs_sub_le_of_unit_steps` in `src/Lib/Analytic/PrimeNumberTheorem/Tauberian.lean`.
