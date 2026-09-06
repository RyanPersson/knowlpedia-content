+++
id = "nonassociative-algebra/spin9-stabilizer-of-an-octonionic-spin-factor"
title = "Spin(9) stabilizer of an octonionic spin factor"
kind = "theorem"
summary = "The stabilizer in compact F_4 of an H_2(O) corner of the Albert algebra is Spin(9)."
aliases = ["Spin(9) subgroup of F4", "octonionic spin-factor stabilizer", "Cayley-plane isotropy"]
domains = ["nonassociative-algebra", "lie-groups"]
prerequisites = ["nonassociative-algebra/jordan-subalgebra"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(J=H_3(\mathbb O)\), let \(F_4=\operatorname{Aut}(J)\), and let
\(A\subset J\) be a [[nonassociative-algebra/jordan-subalgebra|Jordan subalgebra]] isomorphic to \(H_2(\mathbb O)\). Then
its setwise stabilizer is connected and
\[
\operatorname{Stab}_{F_4}(A)\cong\mathrm{Spin}(9).
\]

## Reduction to a primitive idempotent

There is a unique trace-two idempotent \(\ell\) with
\(A=J_1(\ell)\). Its complement \(p=1-\ell\) is a primitive idempotent, and
an automorphism preserves \(A\) if and only if it preserves \(p\). Thus this
stabilizer is the isotropy group of a point of the octonionic projective plane,
and the transitive orbit description is
\[
\mathbb O P^2\cong F_4/\mathrm{Spin}(9).
\]
Here \(F_4\) and \(\mathrm{Spin}(9)\) denote their compact real forms.

The connectedness is unlike the stabilizer of a complex-qutrit subalgebra,
whose full stabilizer has more than one [[topology/connected-component|connected component]].

## References

1. Ichirô Yokota, *Exceptional Lie Groups*, 2009, Chapter 2. [arXiv:0902.0431](https://arxiv.org/abs/0902.0431).
2. Tonny A. Springer and Ferdinand D. Veldkamp, *Octonions, Jordan Algebras and Exceptional Groups*, Springer, 2000, Chapters 7 and 8. [Publisher record](https://doi.org/10.1007/978-3-662-12622-6).
3. John C. Baez and Paul Schwahn, “The Standard Model Gauge Group from the Exceptional Jordan Algebra,” 2026, §§3 and 5. [arXiv:2606.15235](https://arxiv.org/abs/2606.15235).
