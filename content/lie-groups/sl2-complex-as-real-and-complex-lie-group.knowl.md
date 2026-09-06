+++
id = "lie-groups/sl2-complex-as-real-and-complex-lie-group"
title = "SL(2,C) as a real and complex Lie group"
kind = "example"
summary = "The determinant-one complex matrix group has complex dimension three and underlying real dimension six."
aliases = ["realification of SL(2,C)", "SL2C as a real Lie group"]
domains = ["lie-groups"]
prerequisites = ["lie-groups/complex-lie-group", "lie-groups/underlying-real-lie-group", "topology/topological-group"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

The matrix group
\[
SL(2,\mathbb C)=
\left\{\begin{pmatrix}a&b\\c&d\end{pmatrix}:ad-bc=1\right\}
\]
is a [[lie-groups/complex-lie-group|complex Lie group]] of complex dimension \(3\). Its [[lie-groups/underlying-real-lie-group|underlying real Lie group]] \(SL(2,\mathbb C)_{\mathbb R}\) is the same [[topology/topological-group|topological group]] with the same multiplication, but has real dimension \(6\).

## Lie algebras and dimensions

Its complex [[lie-groups/lie-algebra|Lie algebra]] is
\[
\mathfrak{sl}_2(\mathbb C)
=\left\{\begin{pmatrix}z&w\\u&-z\end{pmatrix}:z,w,u\in\mathbb C\right\},
\qquad \dim_{\mathbb C}=3.
\]
The real Lie algebra of \(SL(2,\mathbb C)_{\mathbb R}\) is \(\mathfrak{sl}_2(\mathbb C)_{\mathbb R}\), which has real dimension \(6\). The bracket is unchanged, but only real scalar multiplication remains. In particular this is not the \(3\)-dimensional real Lie algebra \(\mathfrak{sl}_2(\mathbb R)\).

## Global relationships

The center is \(\{\pm I\}\), and quotienting by it gives [[lie-groups/psl2-complex|\(PSL(2,\mathbb C)\)]]. As a real Lie group, \(SL(2,\mathbb C)_{\mathbb R}\) is isomorphic to \(\operatorname{Spin}^+(1,3)\) and double-covers [[lie-groups/proper-orthochronous-lorentz-group|\(SO^+(1,3)\)]]. It is also [[topology/simply-connected-space|simply connected]]; the quotient by its center is not.

## References

1. Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., Springer, 2015, §§2.1–2.2. [Publisher record](https://doi.org/10.1007/978-3-319-13467-3).
2. Frank W. Warner, *Foundations of Differentiable Manifolds and Lie Groups*, Springer, 1983, Chapter 3. [Publisher record](https://doi.org/10.1007/978-1-4757-1799-0).
