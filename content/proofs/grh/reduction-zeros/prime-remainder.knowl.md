+++
id = "proofs/grh/reduction-zeros/prime-remainder"
title = "The remainder R_q of the weighted prime sum"
kind = "definition"
summary = "The smoothed sum of the weight over n up to x with factor 1/n - 1/x, less log x / phi(q) and less a constant."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.primeRemainder", "New.lambdaKSum", "New.primeRemainder_eq_sum_posPart", "New.primeRemainder_eq_sum"]
lean_files = ["src/New/Reduction/Zeros/PrimeError.lean"]
+++

Let \(d\) be a prime, \(q\ge1\), \(\lambda\) the [[proofs/grh/reduction-zeros/weight-lambda-k|weight]] \(\Lambda(n)(1-(n/d))\) on \(n\equiv1\pmod q\), and \(G_q\) the [[proofs/grh/reduction-zeros/log-deriv-mean|mean of logarithmic derivatives]]. For a real \(x>0\) the **remainder** is
\[
R_q(x)=\sum_{1\le n\le x}\lambda(n)\Bigl(\frac1n-\frac1x\Bigr)-\frac{\log x}{\varphi(q)}-c_q,\qquad c_q=\operatorname{Re}G_q(1).
\]
Equivalently \(R_q(x)=S_0(x)-S_1(x)-\log x/\varphi(q)-c_q\), where for an integer \(r\ge0\)
\[
S_r(y)=y^{-r}\sum_{1\le n\le y}\lambda(n)\,n^{r-1}.
\]

## Equivalent forms

For \(x>0\) and an integer \(A\ge\lfloor x\rfloor\),
\[
\sum_{1\le n\le x}\lambda(n)\Bigl(\frac1n-\frac1x\Bigr)=\sum_{n=1}^{A}\lambda(n)\Bigl(\frac1n-\frac1x\Bigr)_{+},
\]
where \(t_+=\max(t,0)\): the positive part vanishes for \(n>x\). If moreover \(A\ge x\), the sum equals \(A^{-1}\sum_{n=1}^{A}\lambda(n)\,(A/n-A/x)_+\).

## Remarks

* For odd \(d\) prime to \(q\) the number \(G_q(1)\) is [[proofs/grh/reduction-zeros/g-q-at-one-is-real|real]], and \(c_q\) is the unique constant for which \(R_q(x)\to0\); see [[proofs/grh/reduction-zeros/pnt-for-prime-remainder|the prime number theorem for \(R_q\)]].
* For \(q=1\), \(c_1=-1-\gamma+\operatorname{Re}\frac{L'}{L}(1,\chi_K)\) for odd \(d\); see [[proofs/grh/reduction-zeros/g-one-and-chowla-selberg-constant|the value of \(c_1\)]].

## References

1. Lean: `New.primeRemainder`, `New.lambdaKSum`, `New.primeRemainder_eq_sum_posPart`, `New.primeRemainder_eq_sum` in `src/New/Reduction/Zeros/PrimeError.lean`.
