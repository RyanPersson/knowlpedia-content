+++
id = "nonassociative-algebra/f4-transitivity-on-complex-qutrit-subalgebras"
title = "F4 transitivity on complex-qutrit subalgebras"
kind = "theorem"
summary = "Compact F_4 acts transitively on the H_3(C) Jordan subalgebras of the Albert algebra."
aliases = ["transitivity on H3(C) subalgebras", "complex qutrit subalgebra orbit in F4"]
domains = ["nonassociative-algebra", "lie-groups"]
prerequisites = ["nonassociative-algebra/exceptional-jordan-algebra", "nonassociative-algebra/jordan-subalgebra"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(J=H_3(\mathbb O)\) be the compact real [[nonassociative-algebra/exceptional-jordan-algebra|Albert algebra]]. Its automorphism
group \(F_4\) acts transitively on the set
\[
\{B\subset J:B\text{ is a Jordan subalgebra and }B\cong H_3(\mathbb C)\}.
\]
Equivalently, every complex-qutrit [[nonassociative-algebra/jordan-subalgebra|Jordan subalgebra]] can be carried to the
standard \(H_3(\mathbb C)\subset H_3(\mathbb O)\) by an automorphism of \(J\).

## Proof mechanism

First use transitivity of \(F_4\) on [[nonassociative-algebra/jordan-frame|Jordan frames]] to arrange that \(B\)
contains the standard frame. The associated
[[nonassociative-algebra/albert-algebra-complex-subalgebra-decomposition|three
octonionic two-planes]] can then be normalized by the pointwise frame
stabilizer \(\mathrm{Spin}(8)\). Its [[lie-groups/defining-representation-of-a-classical-lie-algebra|vector representation]] makes the first
two-plane the standard \(\mathbb C\subset\mathbb O\); the residual
\(\mathrm{Spin}(6)\cong\mathrm{SU}(4)\) acts transitively on the [[linear-algebra/unit-sphere|unit sphere]]
in a [[lie-groups/half-spin-representation|half-spin representation]] and normalizes the remaining parameter. The
resulting subalgebra is the standard one.

## Orbit and stabilizer

For a fixed \(B\), the orbit is the [[lie-groups/homogeneous-space|homogeneous space]]
\[
F_4/\operatorname{Stab}_{F_4}(B).
\]
Its isotropy group is not connected. Only its [[lie-groups/identity-component-of-a-lie-group|identity component]] is
\((\mathrm{SU}(3)\times\mathrm{SU}(3))/\mu_3\), as described in
[[nonassociative-algebra/complex-qutrit-stabilizer-in-f4|the complex-qutrit
stabilizer theorem]].

## References

1. John C. Baez and Paul Schwahn, “The Standard Model Gauge Group from the Exceptional Jordan Algebra,” 2026, Lemma 6. [arXiv:2606.15235](https://arxiv.org/abs/2606.15235).
2. John F. Adams, *Lectures on Exceptional Lie Groups*, University of Chicago Press, 1996, Chapters 1–3. [Publisher record](https://press.uchicago.edu/ucp/books/book/chicago/L/bo3627754.html).
