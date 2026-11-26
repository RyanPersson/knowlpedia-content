+++
id = "proofs/grh/reduction-zeros/polar-function"
title = "Polar function"
kind = "definition"
summary = "A real function of exponential growth whose Laplace-type transform continues meromorphically with at most simple poles of prescribed residues in the right half-plane."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsPolar", "New.integrableOn_laplace_of_abs_le"]
lean_files = ["src/Lib/Analytic/EntireLFunction.lean"]
+++

Let \(E\colon\mathbb{R}\to\mathbb{R}\) and \(r\colon\mathbb{C}\to\mathbb{C}\) be functions. The function \(E\) is **polar with residues \(r\)** if \(E\) is [[measure-theory/measurable-function|measurable]] and there exist a real number \(C\) and a [[complex-analysis/meromorphic-function|meromorphic function]] \(\Phi\) on \(\mathbb{C}\) such that

1. (growth) \(\lvert E(v)\rvert\le C e^{v}\) for all \(v\ge0\);
2. (transform) \(\displaystyle\Phi(s)=\int_0^\infty E(v)\,e^{(1-s)v}\,dv\) for all \(s\) with \(\operatorname{Re}s>2\);
3. (poles) for every \(\rho\in\mathbb{C}\) with \(\operatorname{Re}\rho>0\), \(\displaystyle\lim_{z\to\rho,\ z\ne\rho}(z-\rho)\,\Phi(z)=r(\rho)\).

## Remarks

* By 1 the integral in 2 converges absolutely for \(\operatorname{Re}s>2\): the integrand is at most \(Ce^{(2-\operatorname{Re}s)v}\) in absolute value.
* Condition 3 says that the poles of \(\Phi\) in \(\operatorname{Re}s>0\) are at most simple, that \(r(\rho)\) is the [[complex-analysis/residue|residue]] at \(\rho\), and that \(r(\rho)=0\) where \(\Phi\) is holomorphic. Nothing is required of \(r\) on \(\operatorname{Re}\rho\le0\).
* If \(E(v)=R(e^{v})\), the transform is \(\int_1^\infty R(y)\,y^{-s}\,dy\).

## References

1. Lean: `New.IsPolar` in `src/Lib/Analytic/EntireLFunction.lean`.
