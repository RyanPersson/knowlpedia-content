+++
id = "complex-analysis/logarithmic-derivative"
title = "Logarithmic derivative"
kind = "definition"
summary = "The meromorphic function f prime over f, whose residues record zeros and poles."
aliases = ["log derivative"]
domains = ["complex-analysis"]
section_mode = "progressive"
+++

Let \(f\) be a nonzero [[complex-analysis/meromorphic-function|meromorphic function]]. Its **logarithmic derivative** is
\[
\frac{f'}{f}.
\]
Where a local branch of \(\log f\) exists, this is literally \((\log f)'\), but the quotient is globally defined even when no single-valued logarithm exists.

## Zeros, poles, and residues

If
\[
f(z)=(z-a)^m u(z),\qquad u(a)\ne0,
\]
then
\[
\frac{f'(z)}{f(z)}=\frac{m}{z-a}+\frac{u'(z)}{u(z)}.
\]
Thus \(f'/f\) has a simple pole at each zero or pole of \(f\), with [[complex-analysis/residue|residue]] \(m=\operatorname{ord}_a(f)\).

## Argument principle

Integrating around a contour gives
\[
\frac{1}{2\pi i}\int_\gamma\frac{f'}f\,dz
=\sum_a\operatorname{Ind}(\gamma,a)\operatorname{ord}_a(f).
\]
This is the [[complex-analysis/argument-principle|argument principle]]: the logarithmic derivative converts multiplicative zero-and-pole data into an additive [[complex-analysis/complex-contour-integral|contour integral]].

## Product behavior

The familiar rules
\[
\frac{(fg)'}{fg}=\frac{f'}f+\frac{g'}g,
\qquad
\frac{(f/g)'}{f/g}=\frac{f'}f-\frac{g'}g
\]
mirror additivity of orders under products and quotients.

## References

1. Lars V. Ahlfors, *Complex Analysis*, 3rd ed., McGraw–Hill, 1979. Relevant: Chapter 5, §2.
