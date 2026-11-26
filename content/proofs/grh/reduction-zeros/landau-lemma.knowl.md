+++
id = "proofs/grh/reduction-zeros/landau-lemma"
title = "Landau's lemma"
kind = "theorem"
summary = "A Laplace transform of a nonnegative measure that continues analytically to the real endpoint of a half-line of convergence converges on a larger half-line."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.exists_Ioi_subset_integrableExpSet_of_analyticAt", "New.mem_integrableExpSet_of_summable_taylor"]
lean_files = ["src/Lib/Analytic/Landau.lean"]
proof_status = "full"
+++

**Theorem (Landau).** Let \(\mu\) be a [[measure-theory/measure|measure]] on \(\mathbb{R}\) and \(X\colon\mathbb{R}\to\mathbb{R}\) a [[measure-theory/measurable-function|measurable function]] with \(X\le0\). Let \(S=\{\sigma\in\mathbb{R}:\int e^{\sigma X}\,d\mu<\infty\}\) and \(M(s)=\int e^{sX}\,d\mu\) for \(\operatorname{Re}s\in S\). Let \(a\in\mathbb{R}\) be such that \((a,\infty)\) is contained in the interior of \(S\). Suppose that \(g\) is holomorphic in a neighbourhood of \(a\) and that for all real \(x>a\) sufficiently close to \(a\) the functions \(g\) and \(M\) agree in a neighbourhood of \(x\). Then there is \(b<a\) with \((b,\infty)\subseteq S\).

## Proof

Let \(g\) be holomorphic on the disc \(\lvert w-a\rvert<\varepsilon\). Choose a real \(z\) with \(a<z<a+\varepsilon/2\) near which \(g=M\). We show that \(b=z-\varepsilon/2\) works; note \(b<a\). Let \(\sigma>b\). If \(\sigma>a\), then \(\sigma\in S\) by hypothesis. So let \(b<\sigma\le a\).

The disc of radius \(\varepsilon/2\) about \(z\) lies in the disc of radius \(\varepsilon\) about \(a\) and contains \(\sigma\). Hence the [[?c:Taylor series of a holomorphic function|Taylor series]] of \(g\) at \(z\) converges at \(\sigma\):
\[
\sum_{k\ge0}\frac{(\sigma-z)^k}{k!}\,g^{(k)}(z)\quad\text{converges.}
\]
Since \(z\) is interior to \(S\), the [[?c:Laplace transform|transform]] \(M\) is holomorphic near \(z\) with derivatives \(M^{(k)}(z)=\int X^k e^{zX}\,d\mu\) (absolutely convergent), and \(g^{(k)}(z)=M^{(k)}(z)\). So the \(k\)-th term of the series is
\[
\int t_k\,d\mu,\qquad t_k(y)=\frac{\bigl((\sigma-z)X(y)\bigr)^k}{k!}\,e^{zX(y)} .
\]
Because \(\sigma-z\le0\) and \(X\le0\), each \(t_k\) is nonnegative, and \(\sum_k t_k(y)=e^{(\sigma-z)X(y)}e^{zX(y)}=e^{\sigma X(y)}\). By the [[measure-theory/monotone-convergence-theorem|monotone convergence theorem]],
\[
\int e^{\sigma X}\,d\mu=\sum_{k\ge0}\int t_k\,d\mu<\infty ,
\]
a convergent series of nonnegative real numbers. Hence \(\sigma\in S\). \(\blacksquare\)

## Remarks

In the application \(X(v)=-\lvert v\rvert\) and \(\mu\) lives on \((0,\infty)\), so \(M(s)=\int e^{-sv}\,d\mu(v)\) is a Laplace transform; the theorem says it cannot be analytic at its abscissa of convergence.

## References

1. Lean: `New.exists_Ioi_subset_integrableExpSet_of_analyticAt` in `src/Lib/Analytic/Landau.lean`.
2. H. L. Montgomery, R. C. Vaughan, *Multiplicative Number Theory I*, Cambridge University Press, 2007, Lemma 15.1 (as cited in the head of the Lean file).
