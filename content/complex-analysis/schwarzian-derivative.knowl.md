+++
id = "complex-analysis/schwarzian-derivative"
title = "Schwarzian derivative"
kind = "definition"
summary = "A third-order differential invariant of a locally univalent holomorphic function."
aliases = ["Schwarzian", "Schwarz derivative"]
domains = ["complex-analysis", "differential-geometry"]
section_mode = "progressive"
+++

Let \(f\) be holomorphic and locally univalent on a plane domain, so \(f'\ne0\). Its **Schwarzian derivative** is
\[
S(f)
=\frac{f'''}{f'}-\frac32\left(\frac{f''}{f'}\right)^2.
\]
It is a holomorphic function in the chosen coordinate.

## Logarithmic-derivative form

Writing \(u=f''/f'\), one has
\[
S(f)=u'-\frac12u^2.
\]
This form displays the nonlinear correction that makes the Schwarzian obey its special [[complex-analysis/schwarzian-chain-rule-and-mobius-characterization|composition law]].

## Geometric role

The Schwarzian measures the failure of a locally univalent map to be projective-linear. Under changes of source coordinate it transforms as a [[complex-analysis/projective-connection|projective connection]] rather than as an ordinary function. It also relates ratios of solutions of second-order linear differential equations to complex projective structures.

## Scope

At a critical point \(f'=0\), the displayed expression is not holomorphic and may have a pole. One can treat the Schwarzian meromorphically in broader settings, but local univalence is the clean hypothesis for this definition.

## References

1. Zeev Nehari, *Conformal Mapping*, Dover, 1975. Relevant: Chapter VI.
2. R. C. Gunning, *Lectures on Riemann Surfaces*, Princeton University Press, 1966. Relevant: projective connections and the Schwarzian.
