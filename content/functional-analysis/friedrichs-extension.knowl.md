+++
id = "functional-analysis/friedrichs-extension"
title = "Friedrichs extension"
kind = "definition"
summary = "The canonical self-adjoint extension obtained by closing the quadratic form of a semibounded symmetric operator."
aliases = ["Friedrichs self-adjoint extension"]
domains = ["functional-analysis"]
section_mode = "progressive"
+++

Let \(A\) be a densely defined
[[functional-analysis/symmetric-operator|symmetric operator]] on a complex
[[linear-algebra/hilbert-space|Hilbert space]] with
\(\langle Ax,x\rangle\geq m\lVert x\rVert^2\) for some real \(m\). The
form
\[
\mathfrak a[x,y]=\langle Ax,y\rangle,\qquad x,y\in\mathcal D(A),
\]
is closable. The **Friedrichs extension** \(A_F\) is the unique self-adjoint
operator associated by the representation theorem to the resulting
[[functional-analysis/closed-quadratic-form|closed quadratic form]]. It is a
[[functional-analysis/self-adjoint-extension|self-adjoint extension]] of
\(A\) and satisfies \(A_F\geq mI\). Thus it preserves the original lower
bound while replacing the initial operator domain by the domain determined by
the closed form.

## Construction from the form norm

Choose \(c>1-m\) and complete \(\mathcal D(A)\) in the norm
\[
\lVert x\rVert_{\mathfrak a,c}^2
=\langle Ax,x\rangle+c\lVert x\rVert^2.
\]
The closure of \(\mathfrak a\) has this completion as its form domain. The
first representation theorem then produces \(A_F\), characterized by
\[
\overline{\mathfrak a}[x,y]=\langle A_Fx,y\rangle
\]
for \(x\in\mathcal D(A_F)\) and every \(y\) in the form domain. Different
admissible values of \(c\) give equivalent form norms and the same extension
[Kato, Chapter VI, §2](https://doi.org/10.1007/978-3-642-66282-9).

## Canonical but not generally unique

The Friedrichs construction depends only on the semibounded symmetric
operator and selects an extension with the same [[shared-foundations/lower-bound|lower bound]]. It does not say
that \(A\) has only one self-adjoint extension. Other boundary conditions may
produce other semibounded extensions. Among nonnegative self-adjoint
extensions, the Friedrichs and Kreĭn–von Neumann extensions occupy opposite
extremal positions in the standard form or resolvent order; they coincide
when the original operator is essentially self-adjoint.

## Example

Let \(A=-d^2/dx^2\) on \(L^2(0,1)\) with initial domain
\(C_c^\infty(0,1)\). Its quadratic form is
\[
\mathfrak a[f,g]=\int_0^1 f'(x)\overline{g'(x)}\,dx.
\]
The form closure has domain \(H_0^1(0,1)\), and its associated operator is the
Dirichlet Laplacian with domain
\(H^2(0,1)\cap H_0^1(0,1)\). This is the Friedrichs extension; Neumann and
periodic Laplacians are other self-adjoint realizations but are not selected
by closing this initial form.

## References

1. Tosio Kato, *Perturbation Theory for Linear Operators*, 2nd ed., Springer, 1995. [DOI record](https://doi.org/10.1007/978-3-642-66282-9). Relevant: Chapter VI, §§1–2 on closed forms and representation theorems.
2. Konrad Schmüdgen, *Unbounded Self-adjoint Operators on Hilbert Space*, Graduate Texts in Mathematics 265, Springer, 2012. [DOI record](https://doi.org/10.1007/978-94-007-4753-1). Relevant: Chapter 10 on the Friedrichs extension.
