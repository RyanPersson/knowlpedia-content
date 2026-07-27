+++
id = "operator-algebras/entire-analytic-element-one-parameter-automorphism"
title = "Entire analytic element for a one-parameter automorphism group"
kind = "definition"
summary = "An element whose orbit under a one-parameter automorphism group extends to an entire algebra-valued function."
aliases = ["entire analytic element", "analytic element for an automorphism group"]
domains = ["operator-algebras", "functional-analysis", "dynamical-systems"]
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]] and
\(\alpha:\mathbb R\to\operatorname{Aut}(A)\) a point-norm continuous
one-parameter group of
[[operator-algebras/star-automorphism|\(*\)-automorphisms]]. An element
\(a\in A\) is **entire analytic for \(\alpha\)** if the orbit map
\[
t\longmapsto\alpha_t(a)
\]
extends to an entire \(A\)-valued function on \(\mathbb C\). The extension is
unique and its value at \(z\in\mathbb C\) is denoted \(\alpha_z(a)\). Thus an
expression such as \(\alpha_{-i}(a)\) is defined only for analytic \(a\), not
by extending the [[algebra-groups/automorphism-group|automorphism group]] to all complex times.

## Algebraic properties

Entire analytic elements form a dense \(*\)-subalgebra \(A_{\mathrm{an}}\)
that is invariant under every \(\alpha_z\). For \(a,b\in A_{\mathrm{an}}\),
\[
\alpha_z(ab)=\alpha_z(a)\alpha_z(b),\qquad
\alpha_z(a^*)=\alpha_{\overline z}(a)^*.
\]
The maps \(\alpha_z\) on \(A_{\mathrm{an}}\) generally are not bounded for
nonreal \(z\), which is why they need not extend to all of \(A\).

## Gaussian analytic approximation

For \(a\in A\) and \(n>0\), the norm-convergent Bochner integral
\[
a_n=\sqrt{\frac n\pi}\int_{\mathbb R}e^{-nt^2}\alpha_t(a)\,dt
\]
is entire analytic, and \(a_n\to a\) in norm as \(n\to\infty\). This Gaussian
smoothing proves density and gives the extension by replacing
\(e^{-nt^2}\) with \(e^{-n(t-z)^2}\)
[Bratteli–Robinson, §2.5.3](https://doi.org/10.1007/978-3-662-02520-8).

## Modular-theory use and conventions

There is a parallel \(W^*\)-algebra convention. If
\(\sigma:\mathbb R\to\operatorname{Aut}(M)\) is only point-ultraweakly
continuous, an element \(a\in M\) is entire analytic when its orbit has an
entire extension \(z\mapsto\sigma_z(a)\) in the ultraweak sense: for every
[[operator-algebras/normal-functional|normal functional]] \(\omega\in M_*\), the scalar function
\(z\mapsto\omega(\sigma_z(a))\) is entire. This is not a norm-entire
extension on all of \(M\).

For a [[operator-algebras/modular-automorphism-group|modular automorphism
group]] \(\sigma^\varphi\), it is this \(W^*\)-analytic convention that makes
the imaginary-time term \(\sigma^\varphi_{-i}(a)\) in the
[[operator-algebras/modular-kms-condition|modular KMS condition]]
meaningful. Some sources reserve “analytic element” for extension to a strip
or neighborhood of zero; “entire analytic” here always means extension to
all of \(\mathbb C\), in the topology appropriate to the stated action.

## References

1. Ola Bratteli and Derek W. Robinson, *Operator Algebras and Quantum Statistical Mechanics 1*, 2nd ed., Springer, 1987. [Publisher DOI record](https://doi.org/10.1007/978-3-662-02520-8). Relevant: §2.5.3 on analytic elements for one-parameter groups.
2. Masamichi Takesaki, *Theory of Operator Algebras II*, Springer, 2003. [Publisher DOI record](https://doi.org/10.1007/978-3-662-10451-4). Relevant: Chapter VIII, §1 on analytic elements and modular automorphism groups.
