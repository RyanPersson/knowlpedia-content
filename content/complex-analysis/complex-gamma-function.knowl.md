+++
id = "complex-analysis/complex-gamma-function"
title = "Complex gamma function"
kind = "definition"
summary = "The meromorphic continuation of Euler's integral to complex arguments."
domains = ["complex-analysis"]
section_mode = "progressive"
prerequisites = ["complex-analysis/meromorphic-function","real-analysis/gamma-function","measure-theory/dominated-convergence-theorem"]
+++

The **complex gamma function** \(\Gamma\) is the [[complex-analysis/meromorphic-function|meromorphic]] continuation of
\[
\Gamma(z)=\int_0^\infty e^{-t}t^{z-1}\,dt,\qquad \Re z>0,
\]
where \(t^{z-1}=\exp((z-1)\log t)\) for \(t>0\). It restricts to [[real-analysis/gamma-function|Euler's gamma integral]] on the positive real axis. Integration by parts gives \(\Gamma(z+1)=z\Gamma(z)\), which extends the function successively to the left.

## Zeros and poles

For \(\Re z>0\), repeated integration by parts gives
\[
\int_0^1 t^{z-1}(1-t)^N\,dt=\frac{N!}{z(z+1)\cdots(z+N)} .
\]
Multiply by \(N^z\) and substitute \(u=Nt\). The integrand on \(0<u<N\) is bounded in absolute value by \(u^{\Re z-1}e^{-u}\) and converges to \(u^{z-1}e^{-u}\). [[measure-theory/dominated-convergence-theorem|Dominated convergence]] gives \(\Gamma(z)\) as the limit.

The reciprocals of these approximants equal
\[
 z\exp\!\left(z\Big(\sum_{k=1}^N k^{-1}-\log N\Big)\right)
 \prod_{k=1}^N (1+z/k)e^{-z/k}.
\]
The expression in parentheses converges by integral comparison of \(1/x\) with its values at the integers. The product converges to a nonzero number since none of its factors is zero and the logarithms of the tail are \(O_z(k^{-2})\). Thus \(\Gamma(z)\ne0\) in this half-plane. The recurrence and \(\Gamma(1)=1\) show that the continuation has no zeros and has simple poles exactly at \(0,-1,-2,\ldots\).

## References

- [NIST DLMF, Euler's integral and meromorphic continuation](https://dlmf.nist.gov/5.2#i).
- [NIST DLMF, Euler limit and reciprocal gamma product](https://dlmf.nist.gov/5.8).
