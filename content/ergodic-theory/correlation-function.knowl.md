+++
id = "ergodic-theory/correlation-function"
title = "Correlation of dynamical observables"
kind = "definition"
summary = "Inner products between an evolved observable and a fixed observable."
aliases = ["autocorrelation of an observable", "dynamical correlation"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/koopman-operator", "measure-theory/l2-hilbert-space", "harmonic-analysis/coefficient-function"]
+++

For a [[ergodic-theory/measure-preserving-transformation|probability-preserving transformation]] \(T\) and \(f,h\in L^2\), their **correlation** at time \(n\geq0\) is
\[
c_n(f,h)=\langle U_T^nf,h\rangle
=\int_X f(T^nx)\overline{h(x)}\,d\mu(x).
\]
For invertible \(T\), negative times are also defined. The **centered correlation** subtracts \((\int f\,d\mu)\overline{\int h\,d\mu}\); the **autocorrelation** takes \(h=f\).

## Events and representations

For \(f=1_A,h=1_B\), correlation equals \(\mu(T^{-n}A\cap B)\). It is a [[harmonic-analysis/coefficient-function|matrix coefficient]] of the Koopman representation, with the sign of \(n\) adjusted for the inverse-pullback convention.
