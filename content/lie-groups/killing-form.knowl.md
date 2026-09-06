+++
id = "lie-groups/killing-form"
title = "Killing form"
kind = "knowl"
summary = "The symmetric invariant bilinear form defined by the trace of the product of adjoint operators."
aliases = ["killing-form", "Killing form"]
domains = ["lie-groups"]
prerequisites = ["lie-groups/lie-algebra", "lie-groups/adjoint-representation-of-a-lie-algebra"]
dependency_review_count = 1
legacy_source_path = "lie-groups/killing-form.md"
+++

Let \(\mathfrak g\) be a finite-dimensional [[lie-groups/lie-algebra|Lie algebra]] over a field \(\Bbbk\). Its **Killing form** is the symmetric bilinear form
\[
B:\mathfrak g\times \mathfrak g\to \Bbbk,\qquad B(x,y)=\mathrm{tr}(\mathrm{ad}_x\circ \mathrm{ad}_y).
\]
Here \(\operatorname{ad}\) is the [[lie-groups/adjoint-representation-of-a-lie-algebra|adjoint representation]]. The form is [[lie-groups/killing-form-ad-invariant-lemma|ad-invariant]].

## Examples

For \(\mathfrak{sl}_2(\mathbb C)\), with basis
\[
H=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
E=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
F=\begin{pmatrix}0&0\\1&0\end{pmatrix},
\]
one computes, using \(\operatorname{ad}_X(Y)=[X,Y]\), that
\[
B(H,H)=8,\qquad B(E,F)=4,\qquad B(H,E)=B(H,F)=B(E,E)=B(F,F)=0.
\]
For \(X,Y\in\mathfrak{sl}_n(\mathbb C)\), the Killing form is
\[
B(X,Y)=2n\,\mathrm{tr}(XY).
\]

## Remarks

Over a field of characteristic \(0\), nondegeneracy of \(B\) characterizes [[lie-groups/semisimple-lie-algebra|semisimplicity]].
