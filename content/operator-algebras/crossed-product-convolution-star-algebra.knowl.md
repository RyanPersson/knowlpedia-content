+++
id = "operator-algebras/crossed-product-convolution-star-algebra"
title = "Crossed-product convolution *-algebra C_c(G,A)"
kind = "definition"
summary = "The compactly supported A-valued convolution algebra associated with a C*-dynamical system."
aliases = ["covariant convolution algebra", "C_c(G,A)"]
domains = ["operator-algebras", "harmonic-analysis"]
section_mode = "progressive"
+++

Let \((A,G,\alpha)\) be a [[operator-algebras/cstar-dynamical-system|\(C^*\)-dynamical system]], fix a left [[harmonic-analysis/haar-measure|Haar measure]] \(ds\), and let \(\Delta\) be the [[harmonic-analysis/modular-function|modular function]] of \(G\). The **crossed-product convolution \(*\)-algebra** is the [[linear-algebra/vector-space|vector space]] \(C_c(G,A)\) of continuous compactly supported functions \(G\to A\), with
\[
(f*g)(s)=\int_G f(t)\alpha_t\!\left(g(t^{-1}s)\right)\,dt
\]
\[
f^*(s)=\Delta(s^{-1})\alpha_s\!\left(f(s^{-1})^*\right).
\]
The integrals are \(A\)-valued Bochner integrals. These operations make \(C_c(G,A)\) an associative [[operator-algebras/involutive-algebra|involutive algebra]], generally without an identity.

## Algebraic role

The twisting by \(\alpha_t\) in convolution records the interaction between the group and the coefficient algebra. The modular factor in the involution compensates for inversion under a left Haar measure. With these choices, every [[operator-algebras/covariant-representation-cstar-dynamical-system|covariant pair]] has an integrated form that respects both multiplication and involution.

The [[operator-algebras/full-crossed-product|full crossed product]] and [[operator-algebras/reduced-crossed-product|reduced crossed product]] are different \(C^*\)-completions of this same dense algebraic core. Consequently, the notation \(C_c(G,A)\) alone does not select a \(C^*\)-norm.

## Standard cases

If \(A=\mathbb C\) and the action is trivial, the formulas reduce to the ordinary convolution and involution on \(C_c(G)\). If \(G\) is discrete, integration becomes summation, compact support becomes finite support, and
\[
(f*g)(s)=\sum_{t\in G}f(t)\alpha_t\!\left(g(t^{-1}s)\right).
\]
For the trivial action on a general \(A\), the twisting disappears but the coefficients still multiply in \(A\), so the algebra need not be commutative.

## Conventions and scope

The formulas depend on choosing a left rather than right Haar measure and on the convention for \(\Delta\). Equivalent conventions move inverses or modular factors between formulas. The displayed pair is one coherent standard convention; mixing it with a different involution formula can destroy the \(*\)-algebra identities. For noncompact \(G\), \(C_c(G,A)\) is not complete in the crossed-product norms.

## References

1. Dana P. Williams, Crossed Products of \(C^*\)-Algebras, Mathematical Surveys and Monographs 134, American Mathematical Society, 2007. [DOI record](https://doi.org/10.1090/surv/134). Relevant: §2.3, especially equations (2.16)–(2.19) for convolution, involution, and integrated forms.
2. J. M. G. Fell and R. S. Doran, Representations of \(*\)-Algebras, Locally Compact Groups, and Banach \(*\)-Algebraic Bundles, Volume 1, Academic Press, 1988. [DOI record](https://doi.org/10.1016/C2009-0-12051-7). Relevant: the convolution algebra of a group action and its representation theory.
