+++
id = "proofs/grh/upper-seesaw/top-of-the-chain"
title = "The top of the chain: restriction to the definite space Y_m"
kind = "lemma"
summary = "On the definite space Y_m, the integral of a matrix coefficient of a form on X_m against a form on Y_m is a constant times the inner product with the restricted form."
aliases = ["restriction to Y_m"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.restrictToFormY", "New.Data.lowerChain_eq_of_lowerChainUpTo_eq", "New.Data.exists_integral_eq_mul_inner_restrictToFormY"]
lean_files = ["src/New/UpperBound/Seesaw/SeesawIdentity.lean"]
proof_status = "outline"
+++

Let \(D\) be the [[?lean:New.Data|data]] with \(m\) lifts. The space \(Y_m\) is definite, with
Gram matrix \(1\); the [[proofs/grh/upper-seesaw/tower-gradings-and-evaluated-data|last grading]]
identifies it with the standard definite space on the \(n_m-1\) basis vectors of \(X_m\) other than
the last, so that \(U(Y_m)\hookrightarrow U(X_m)\), \(k\mapsto\operatorname{diag}(k,1)\). Let
\(\operatorname{res}\) be the [[?lean:New.Data.restrictToY|restriction]] from forms on \(X_m\) to
forms on \(Y_m\), read on [[langlands/automorphic-form|automorphic]] forms.

**Lemma.** For every linear form \(t\) on the values of forms on \(X_m\) there is a constant
\(C_t\in\mathbb{C}\) such that for every form \(x\) on \(Y_m\), every form \(\psi\) on \(X_m\) and
every function \(F\) on \(U(Y_m)(\mathbb{A})\) with
\(F(k)=t\bigl(\psi(\operatorname{diag}(k,1))\bigr)\) for all adelic points \(k\) of \(U(Y_m)\) — where, for \(h=\operatorname{diag}(k,1)=(h_\infty,h_f)\), the symbol \(t(\psi(h))\) denotes the adelic coefficient \(t\bigl(\rho(h_\infty)^{-1}\psi(h_f)\bigr)\) of the algebraic form \(\psi\) (a vector-valued function on finite points; \(\rho\) the conjugate Weyl representation):
\[
\int_{[U(Y_m)]}F(g)\,\overline{x(g)}\,dg=C_t\,\langle x,\operatorname{res}\psi\rangle .
\]
The map \(t\mapsto C_t\) is whatever the construction gives; only its existence for each \(t\) is
used. Moreover, if the composite of the \(m\) lifts of the lower chain applied to \(f\) equals
\(\operatorname{res}\psi\) as automorphic forms, the same holds for the corresponding algebraic
forms.

## Proof

(Outline; the structure is that of the Lean proof, and two library statements are asserted.)

*Reduction.* The space \(Y_m\) is standard (its point is \(1\), its signs are \(+\)), and the last
grading has an empty string; so its Bessel subgroup is the whole group, the quotient
\(R(F)\backslash G_m\) is \([U(Y_m)]\), and the hypothesis describes \(F\) at every point:
\(F(g)=t\bigl(\psi(\operatorname{diag}(g,1))\bigr)\), in the sense of coefficients of algebraic
forms.

*Both sides as a mean over finite points.* Let \(x^{\mathrm{alg}}\) be the algebraic form of \(x\),
so that \(\overline{x(a,g)}=\langle x^{\mathrm{alg}}(g),\rho(a)v_{\mathrm{hw}}\rangle\) with
\(v_{\mathrm{hw}}\) the highest weight vector, and let \(\mathrm{br}\) be the
[[?lean:New.Data.branching|branching map]] from the representation of \(U(n_m)\) to that of
\(U(n_m-1)\). Put
\[
\mathrm{avg}=\text{the class integral over the finite points } h \text{ (level } K_m) \text{ of }\bigl\langle x^{\mathrm{alg}}(h),\ \mathrm{br}\,\psi(\operatorname{diag}(h,1))\bigr\rangle .
\]
(a) There is a constant \(C\), depending on \(t\) only, with
\(\int_{[U(Y_m)]}F\bar x=C\cdot\mathrm{avg}\): the archimedean integral of the matrix coefficient
\(t(\psi(\operatorname{diag}(\cdot,1)))\) against the translates of \(v_{\mathrm{hw}}\) factors
through the branching map (asserted; Lean `integral_algFormCoeff_blockEmb`, using that the
branching map spans the relevant intertwiners).
(b) \(\langle x,\operatorname{res}\psi\rangle=d^{-1}c^{-1}\,\mathrm{avg}\), where \(d\) is the
dimension of the archimedean representation of \(Y_m\) and
\(c=\prod_\tau\tau(\bar\pi_N)^{e_\tau}\ne0\) is the normalising product of powers of the conjugates
of \(\bar\pi_N\) in the definition of the restriction, \(\operatorname{res}=c^{-1}\mathrm{br}\)
(the inner product of two forms is the class integral of the pairing of their algebraic forms
divided by \(d\): asserted; Lean `integral_mul_eq_classIntegral`).

Hence the lemma holds with \(C_t=C\cdot d\cdot c\).

The last assertion is the bijection between automorphic forms of the given type and algebraic
forms. \(\blacksquare\)

## References

1. Lean: `New.Data.exists_integral_eq_mul_inner_restrictToFormY`, `New.Data.restrictToFormY`, `New.Data.lowerChain_eq_of_lowerChainUpTo_eq` in `src/New/UpperBound/Seesaw/SeesawIdentity.lean`.
