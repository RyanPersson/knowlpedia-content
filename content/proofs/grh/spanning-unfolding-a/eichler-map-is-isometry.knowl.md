+++
id = "proofs/grh/spanning-unfolding-a/eichler-map-is-isometry"
title = "Eichler maps are isometries"
kind = "lemma"
summary = "For isotropic, mutually orthogonal columns x orthogonal to u, the matrix 1 + g(x u* J - (u + x(tau u* J u - s)) x* J) preserves the hermitian matrix J."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.conjTranspose_eichler_mul_mul"]
lean_files = ["src/New/Spanning/Unfolding/ReducedPoints.lean"]
proof_status = "full"
+++

**Lemma (Eichler's formula).** Let \(E\) be a commutative ring with an involution \(a\mapsto\bar a\); for a matrix \(A\) write \(A^{*}\) for its [[?c:Conjugate transpose|conjugate transpose]]. Let \(J\) be an \(n\times n\) matrix with \(J^{*}=J\), let \(x,u\) be \(n\times m\) matrices and \(s\) an \(m\times m\) matrix over \(E\), and let \(g,\tau\in E\). Assume

\[
x^{*}Ju=0,\qquad x^{*}Jx=0,\qquad s^{*}=-s,\qquad \bar g=g,\qquad \tau+\bar\tau=g .
\]

Put \(W=\tau\,u^{*}Ju-s\) and \(A=x\,u^{*}J-(u+xW)\,x^{*}J\). Then
\[
(1+gA)^{*}\,J\,(1+gA)=J .
\]

## Proof

Since \(J^{*}=J\), taking conjugate transposes in \(x^{*}Ju=0\) gives \(u^{*}Jx=0\), and \((JA)^{*}=A^{*}J\). Because \(\bar g=g\), the claim is \(g\bigl(JA+(JA)^{*}\bigr)+g^{2}A^{*}JA=0\).

*Linear term.* We have \(JA=Jxu^{*}J-Jux^{*}J-JxWx^{*}J\) and \((JA)^{*}=Jux^{*}J-Jxu^{*}J-JxW^{*}x^{*}J\), so
\[
JA+(JA)^{*}=-Jx\,(W+W^{*})\,x^{*}J .
\]
As \(u^{*}Ju\) is hermitian and \(s\) is skew-hermitian, \(W+W^{*}=(\tau+\bar\tau)\,u^{*}Ju=g\,u^{*}Ju\). Hence \(JA+(JA)^{*}=-g\,Jx\,u^{*}Ju\,x^{*}J\).

*Quadratic term.* \(A^{*}=Jux^{*}-Jx(u+xW)^{*}\). In the product \(A^{*}JA\) every term containing one of \(x^{*}Jx\), \(x^{*}Ju\), \(u^{*}Jx\) vanishes; the only surviving term is
\[
A^{*}JA=Jx\,(u+xW)^{*}J(u+xW)\,x^{*}J=Jx\,u^{*}Ju\,x^{*}J .
\]

Therefore \(g(JA+(JA)^{*})+g^{2}A^{*}JA=-g^{2}Jxu^{*}Jux^{*}J+g^{2}Jxu^{*}Jux^{*}J=0\).

## References

1. Lean: `New.Filling.conjTranspose_eichler_mul_mul` in `src/New/Spanning/Unfolding/ReducedPoints.lean`.
