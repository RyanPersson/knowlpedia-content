+++
id = "analytic-number-theory/dirichlet-zero-reflection"
title = "Reflection of a Dirichlet L-function zero in the critical strip"
kind = "theorem"
summary = "A zero for a character gives a reflected zero for its inverse, including at imprimitive levels."
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/dirichlet-character", "analytic-number-theory/critical-strip", "analytic-number-theory/dirichlet-l-function", "analytic-number-theory/primitive-dirichlet-character", "analytic-number-theory/induced-dirichlet-character", "analytic-number-theory/euler-factors-under-induction", "analytic-number-theory/completed-dirichlet-l-function", "analytic-number-theory/dirichlet-functional-equation", "analytic-number-theory/dirichlet-root-number"]
+++

Let \(\chi\) be a [[analytic-number-theory/dirichlet-character|Dirichlet character]] of any positive modulus. If \(s\) lies in the [[analytic-number-theory/critical-strip|open critical strip]] and its [[analytic-number-theory/dirichlet-l-function|\(L\)-function]] vanishes there, then \(L(1-s,\bar\chi)=0\). Here \(\bar\chi\) is the inverse character on units, extended by zero.

## Proof

Choose the [[analytic-number-theory/primitive-dirichlet-character|primitive]] character \(\psi\) that [[analytic-number-theory/induced-dirichlet-character|induces]] \(\chi\). The [[analytic-number-theory/euler-factors-under-induction|change-of-modulus formula]] shows \(L(s,\psi)=0\), since all extra factors are nonzero when \(\Re s>0\).

On the strip, the factor relating \(L(s,\psi)\) to its [[analytic-number-theory/completed-dirichlet-l-function|completed function]] is finite and nonzero. Thus \(\Lambda(s,\psi)=0\). The [[analytic-number-theory/dirichlet-functional-equation|primitive functional equation]], whose [[analytic-number-theory/dirichlet-root-number|root number]] is nonzero, gives \(\Lambda(1-s,\bar\psi)=0\). The conjugate of a primitive character is primitive, since an inducing character for \(\bar\psi\) could be conjugated to induce \(\psi\). As \(\Re(1-s)>0\), division by the completion factor gives \(L(1-s,\bar\psi)=0\). Applying the change-of-modulus formula to \(\bar\chi\) now gives \(L(1-s,\bar\chi)=0\).

## References

- [Reflection for a character of arbitrary level](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/ZeroSymmetry.lean#L61)
