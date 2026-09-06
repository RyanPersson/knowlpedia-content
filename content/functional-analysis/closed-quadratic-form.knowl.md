+++
id = "functional-analysis/closed-quadratic-form"
title = "Closed quadratic form"
kind = "definition"
summary = "A lower-semibounded symmetric form whose domain is complete in its shifted form norm."
aliases = ["closed semibounded form", "closed symmetric form"]
domains = ["functional-analysis"]
prerequisites = ["linear-algebra/hilbert-space", "shared-foundations/lower-bound", "functional-analysis/closed-linear-operator"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(H\) be a [[linear-algebra/hilbert-space|Hilbert space]] and let
\(\mathfrak a\) be a densely defined symmetric sesquilinear form, linear in
the second variable, with domain \(D(\mathfrak a)\subseteq H\). Suppose
\(\mathfrak a[u,u]\geq m\|u\|^2\) for some \(m\in\mathbb R\). The associated
quadratic form is \(q[u]=\mathfrak a[u,u]\). It is **closed** if
\(D(\mathfrak a)\) is complete for the form norm
\[
\|u\|_{\mathfrak a}=
\bigl(\mathfrak a[u,u]+(1-m)\|u\|^2\bigr)^{1/2}.
\]
Replacing \(m\) by another [[shared-foundations/lower-bound|lower bound]] gives an equivalent norm. Unlike a
[[functional-analysis/closed-linear-operator|closed operator]], a closed form
is not defined by closure of the graph of the scalar-valued function \(q\).

## Representation by an operator

The first representation theorem associates to every densely defined closed
lower-semibounded form \(\mathfrak a\) a unique self-adjoint operator \(A\)
with \(A\geq m\). For any \(\lambda<m\),
\[
D(\mathfrak a)=D\bigl((A-\lambda)^{1/2}\bigr)
\]
\[
\mathfrak a[u,v]
=\langle(A-\lambda)^{1/2}u,(A-\lambda)^{1/2}v\rangle
+\lambda\langle u,v\rangle.
\]
Thus form domains can be larger than operator domains while still determining
the operator uniquely.

## Closability and completion

A lower-semibounded form is **closable** when it has a closed extension; its
smallest closed extension is its closure. Equivalently, if
\(u_n\to0\) in \(H\) and \((u_n)\) is Cauchy in the form norm, then
\(\mathfrak a[u_n,u_n]\to0\) after shifting to a nonnegative form. This is a
form criterion and is distinct from
[[functional-analysis/closable-operator|closability of an operator]], even
though the two theories interact through associated operators.

## Examples and conventions

Every bounded symmetric form on all of \(H\) is closed. On
\(L^2(\Omega)\), the Dirichlet energy
\(\mathfrak a[u,v]=\int_\Omega\nabla u\cdot\overline{\nabla v}\) with domain
\(H_0^1(\Omega)\) is closed; its restriction to \(C_c^\infty(\Omega)\) is
typically closable but not closed. More general literature defines closed
sectorial forms using the real part of a shifted form. Without symmetry or a
sectoriality hypothesis, “closed quadratic form” requires an explicit
convention and cannot be inferred from the norm above.

## References

1. Tosio Kato, Perturbation Theory for Linear Operators, 2nd ed., corrected reprint, Springer, 1995. [DOI record](https://doi.org/10.1007/978-3-642-66282-9). Relevant: Chapter VI, §§1–2 on closed sectorial forms and representation theorems.
2. Michael Reed and Barry Simon, Methods of Modern Mathematical Physics I: Functional Analysis, Academic Press, 1972. [Publisher record](https://doi.org/10.1016/B978-0-12-585001-8.X5001-6). Relevant: Chapter VIII on closed semibounded quadratic forms and associated self-adjoint operators.
