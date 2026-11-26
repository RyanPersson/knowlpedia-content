+++
id = "analytic-number-theory/dirichlet-functional-equation"
title = "Functional equation of a primitive Dirichlet L-function"
kind = "theorem"
summary = "The completed L-function at s equals the conjugate character’s completed L-function at 1−s up to a constant of absolute value one."
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/primitive-dirichlet-character", "analytic-number-theory/dirichlet-conductor", "analytic-number-theory/dirichlet-character-parity", "analytic-number-theory/completed-dirichlet-l-function", "analytic-number-theory/dirichlet-root-number", "analytic-number-theory/dirichlet-gauss-sum", "complex-analysis/meromorphic-function", "harmonic-analysis/dirichlet-theta-series", "complex-analysis/complex-gamma-function", "harmonic-analysis/theta-transformation-dirichlet-character"]
+++

A [[analytic-number-theory/primitive-dirichlet-character|primitive Dirichlet character]] \(\chi\) of [[analytic-number-theory/dirichlet-conductor|conductor]] \(q\) and [[analytic-number-theory/dirichlet-character-parity|parity]] \(a\) satisfies the **functional equation**
\[
\Lambda(s,\chi)=\epsilon_\chi\Lambda(1-s,\bar\chi),\qquad
\epsilon_\chi=\frac{\tau(\chi)}{i^a\sqrt q},\qquad |\epsilon_\chi|=1.
\]
Here \(\Lambda\) is the [[analytic-number-theory/completed-dirichlet-l-function|completed \(L\)-function]] and the [[analytic-number-theory/dirichlet-root-number|root number]] is given by the [[analytic-number-theory/dirichlet-gauss-sum|Gauss sum]] \(\tau(\chi)\). This is an identity of [[complex-analysis/meromorphic-function|meromorphic functions]].

## Proof

Put \(u=(s+a)/2\) and \(\theta_\chi(t)=\sum_{n\ge1}n^a\chi(n)e^{-\pi n^2t/q}\). For \(\Re s>1\), integrate the [[harmonic-analysis/dirichlet-theta-series|theta series]] term by term against \(t^u\,dt/t\). Absolute convergence follows by doing the same integral with \(|\chi(n)|\le1\) and \(\Re u\), giving a constant times \(\sum n^{-\Re s}\). The substitution \(v=\pi n^2t/q\) into the [[complex-analysis/complex-gamma-function|gamma integral]] then gives
\[
 \Lambda(s,\chi)=\int_0^\infty\theta_\chi(t)t^{(s+a)/2}\,\frac{dt}{t}.
\]

Write \(A_\chi(s)\) for this integral over \([1,\infty)\). It is entire because the theta series decreases exponentially at infinity, giving an integrable bound even after multiplying by any fixed power of \(t\) or \(\log t\). For \(q>1\), the [[harmonic-analysis/theta-transformation-dirichlet-character|theta transformation]] and the substitution \(t=1/v\) on \((0,1)\) give
\[
\Lambda(s,\chi)=A_\chi(s)+\epsilon_\chi A_{\bar\chi}(1-s).
\]
This expression continues \(\Lambda\) to all \(s\). Conjugating the Gauss sum and changing \(n\) to \(-n\) yields \(\tau(\bar\chi)=(-1)^a\overline{\tau(\chi)}\). Since \(|\tau(\chi)|^2=q\), it follows that \(\epsilon_\chi\epsilon_{\bar\chi}=1\). The same expression for \(\bar\chi\) at \(1-s\) gives the functional equation.

For \(q=1\), write \(A=A_\chi\). The zero term in the two-sided theta sum gives the extra term \((t^{-1/2}-1)/2\) when solving the [[harmonic-analysis/theta-transformation-dirichlet-character|modulus-one theta identity]] for \(\theta(t)\). Integrating this term on \((0,1)\) gives
\[
\Lambda(s)=A(s)+A(1-s)+\frac{1}{s-1}-\frac{1}{s}.
\]
The right side is invariant under \(s\mapsto1-s\). It has simple poles at zero and one.

## References

- [NIST DLMF §25.15(i), functional equation for a primitive character](https://dlmf.nist.gov/25.15#i).
- [Gaussian theta transformation by residue classes](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/DirichletTheta.lean#L361).
