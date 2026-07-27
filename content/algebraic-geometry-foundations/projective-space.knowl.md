+++
id = "algebraic-geometry-foundations/projective-space"
title = "Projective space"
kind = "knowl"
summary = "A scheme obtained by gluing affine spaces so that directions at infinity are included."
aliases = ["projective-space", "Projective space", "projective n-space"]
domains = ["algebraic-geometry-foundations"]
legacy_source_path = "algebraic-geometry-foundations/projective-space.md"
+++

Let $k$ be a field. **Projective $n$-space over $k$** is the [[algebraic-geometry-foundations/scheme|scheme]] obtained from the [[algebraic-geometry-foundations/proj|Proj construction]]
$$
\mathbb P_k^n:=\operatorname{Proj}k[x_0,\ldots,x_n].
$$
Its $k$-valued points may be written in homogeneous coordinates $[a_0:\cdots:a_n]$, where not all $a_i$ vanish and
$$
[a_0:\cdots:a_n]=[\lambda a_0:\cdots:\lambda a_n]
$$
for every nonzero $\lambda\in k$.

For each $i$, the condition $a_i\ne0$ defines a standard open subset $U_i$. Dividing the other coordinates by $a_i$ gives an isomorphism
$$
U_i\cong\mathbb A_k^n.
$$
Consequently, $\mathbb P_k^n=\bigcup_{i=0}^nU_i$ is covered by $n+1$ copies of [[algebraic-geometry-foundations/affine-n-space|affine $n$-space]], proving directly that it is a scheme.

For example, $\mathbb P_k^1$ is the [[algebraic-geometry-foundations/affine-line|affine line]] together with one point at infinity. Unlike affine space, projective space is generally not an [[algebraic-geometry-foundations/affine-scheme|affine scheme]].
