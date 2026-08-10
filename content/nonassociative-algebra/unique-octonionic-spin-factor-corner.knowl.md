+++
id = "nonassociative-algebra/unique-octonionic-spin-factor-corner"
title = "Unique octonionic spin-factor corner"
kind = "theorem"
summary = "Every complex-qubit Jordan subalgebra of the Albert algebra lies in a unique octonionic spin-factor corner."
aliases = ["unique H2(O) corner containing H2(C)", "octonionic completion of a complex qubit"]
domains = ["nonassociative-algebra"]
section_mode = "progressive"
+++

Let \(J=H_3(\mathbb O)\) be the compact real
[[nonassociative-algebra/exceptional-jordan-algebra|Albert algebra]]. If
\(X\subset J\) is a [[nonassociative-algebra/jordan-subalgebra|Jordan
subalgebra]] isomorphic to \(H_2(\mathbb C)\), then there is a unique Jordan
subalgebra \(A\subset J\) isomorphic to \(H_2(\mathbb O)\) with
\[
X\subseteq A.
\]
This \(A\) is the unique [[nonassociative-algebra/octonionic-spin-factor|octonionic
spin factor]] containing the given complex qubit algebra.

## Intrinsic construction

Let \(\ell\in J\) be the unit of \(X\), viewed as an element of the ambient
Albert algebra. Then \(\ell\) is an idempotent of trace \(2\), and the required
subalgebra is
\[
A=J_1(\ell)=\{a\in J:\ell\circ a=a\}.
\]
The equation is \(\ell\circ a=a\), not \(\ell\circ a=1\). The
[[nonassociative-algebra/peirce-one-space-jordan-corner|Peirce-one corner
theorem]] gives \(A\cong H_2(\mathbb O)\).

If \(A'=J_1(\ell')\cong H_2(\mathbb O)\) also contains \(X\), then
\(\ell\in X\subset A'\), so \(\ell'\circ\ell=\ell\). Both idempotents have
trace \(2\); the relation says that the support of \(\ell\) is contained in
that of \(\ell'\), and equal rank forces \(\ell=\ell'\). This proves
uniqueness.

## More general form

The same argument works with \(H_3(\mathbb K)\) in place of \(H_3(\mathbb O)\):
an embedded copy of \(H_2(\mathbb L)\) is contained in a unique
\(H_2(\mathbb K)\)-corner whenever such an embedding is given, for normed real
division algebras \(\mathbb K,\mathbb L\).

## References

1. John C. Baez and Paul Schwahn, “The Standard Model Gauge Group from the Exceptional Jordan Algebra,” 2026, Lemma 10. [arXiv:2606.15235](https://arxiv.org/abs/2606.15235).
2. Tonny A. Springer and Ferdinand D. Veldkamp, *Octonions, Jordan Algebras and Exceptional Groups*, Springer, 2000, Chapters 5–7. [Publisher record](https://doi.org/10.1007/978-3-662-12622-6).
