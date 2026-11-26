+++
id = "grh-lean/primitive-zeros"
title = "Zeros for primitive Dirichlet characters"
kind = "theorem"
summary = "The primitive-character conclusion follows by specializing the all-character statement."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["grh-lean/strip-zeros", "analytic-number-theory/dirichlet-character"]
+++

If \(\chi\) is a [[analytic-number-theory/primitive-dirichlet-character|primitive Dirichlet character]] and \(L(s,\chi)=0\) with \(0<\Re s<1\), then \(\Re s=1/2\).

## Proof

Apply the [[grh-lean/strip-zeros|theorem for every Dirichlet character]] to the given modulus, character and zero. It already quantifies over the [[analytic-number-theory/primitive-dirichlet-character|primitive characters]].

## References

- [Main.lean, LFunction_eq_zero_re_of_isPrimitive](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Main.lean#L21)
