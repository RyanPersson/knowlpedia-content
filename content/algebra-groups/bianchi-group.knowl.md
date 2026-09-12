+++
id = "algebra-groups/bianchi-group"
title = "Bianchi group"
kind = "definition"
summary = "The projective determinant-one matrix group over an imaginary quadratic ring of integers."
aliases = ["Bianchi groups", "PSL2 of imaginary quadratic integers"]
domains = ["algebra-groups"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/imaginary-quadratic-field", "algebra-fields-galois/ring-of-integers", "algebra-groups/projective-special-linear-group-over-ring"]
+++

For \(K=\mathbb Q(\sqrt{-d})\), \(d>0\) square-free, the **Bianchi group** is
\[
\Gamma_d=\operatorname{PSL}_2(\mathcal O_K)
=\operatorname{SL}_2(\mathcal O_K)/\{\pm I\},
\]
where \(\mathcal O_K\) is the [[algebra-fields-galois/ring-of-integers|ring of integers]] of the [[algebra-fields-galois/imaginary-quadratic-field|imaginary quadratic field]]. We use the [[algebra-groups/projective-special-linear-group-over-ring|ring-valued projective convention]] and the inclusion \(K\subseteq\mathbb C\) to regard \(\Gamma_d\) as a subgroup of \(\operatorname{PSL}_2(\mathbb C)\).

## Concrete matrices

Its elements are determinant-one matrices \(\begin{pmatrix}a&b\\c&e\end{pmatrix}\) with entries in \(\mathcal O_K\), where a matrix and its negative represent the same element. On the boundary sphere the action is \(z\mapsto(az+b)/(cz+e)\).

For \(d=1\), the entries are Gaussian integers \(a+bi\), \(a,b\in\mathbb Z\). The matrix \(\begin{pmatrix}1&i\\0&1\end{pmatrix}\) acts on the boundary by \(z\mapsto z+i\).

## Geometry and conventions

The [[lie-groups/psl2c-action-on-hyperbolic-three-space|hyperbolic action]] gives the [[differential-geometry/bianchi-orbifold|Bianchi orbifold]]. Some sources call the unprojectivized SL group a Bianchi group; its central kernel acts trivially on hyperbolic space. Replacing PSL by PGL can change the effective group and the quotient volume.

## References

1. T. Church, B. Farb, and A. Putman, *Integrality in the Steinberg module and the top-dimensional cohomology of SL_n O_K*, Example 5.6, p. 31 of the linked version. [Author-hosted paper](https://math.uchicago.edu/~farb/papers/Steinberg2.pdf)
