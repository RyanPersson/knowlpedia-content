+++
id = "functional-analysis/seminorm-quotient-completion"
title = "Banach completion of a seminorm quotient"
kind = "definition"
summary = "The Banach space obtained by completing a seminorm quotient of a vector space."
aliases = ["seminorm quotient completion", "completion associated to a seminorm"]
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["linear-algebra/vector-space", "convex-analysis/seminorm", "convex-analysis/quotient-vector-space-codimension", "linear-algebra/banach-space"]
+++

Let \(E\) be a [[linear-algebra/vector-space|vector space]] and \(p\) a
[[convex-analysis/seminorm|seminorm]] on \(E\). Its kernel
\(\ker p=\{x:p(x)=0\}\) is a linear subspace, and \(p\) induces a norm on the
[[convex-analysis/quotient-vector-space-codimension|quotient vector space]]
\(E/\ker p\) by
\[
\lVert [x]\rVert_p=p(x).
\]
The **Banach completion of the seminorm quotient**, denoted \(E_p\), is the
completion of this normed space. Thus \(E_p\) is a
[[linear-algebra/banach-space|Banach space]], and the quotient map gives a
canonical linear map \(E\to E_p\) whose induced map from \(E/\ker p\) is
isometric and whose image is dense. Equivalently, \(E_p\) is the complete
normed space obtained by adjoining limits of all Cauchy sequences in
\(E/\ker p\).

When \(q\geq p\) are seminorms, the identity on \(E\) induces a contraction
\(E_q\to E_p\). These canonical linking maps are the ones used in the
definition of a [[functional-analysis/nuclear-space|nuclear space]].

## Reference

See Sections 2–3 of [Kazhdan's notes on nuclear spaces](https://math.huji.ac.il/~kazhdan/QFT/nuclear.pdf)
for the seminorm-completion construction and the nuclear linking-map
criterion.
