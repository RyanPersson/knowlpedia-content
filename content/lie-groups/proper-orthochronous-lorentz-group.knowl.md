+++
id = "lie-groups/proper-orthochronous-lorentz-group"
title = "Proper orthochronous Lorentz group"
kind = "definition"
summary = "The identity component SO⁺(1,3) of the four-dimensional Lorentz group."
aliases = ["SO+(1,3)", "restricted Lorentz group", "identity component of the Lorentz group"]
domains = ["lie-groups", "mathematical-physics"]
section_mode = "progressive"
+++

For \(\eta=\operatorname{diag}(-1,1,1,1)\), the **proper orthochronous Lorentz group** is
\[
SO^+(1,3)
=\{\Lambda\in GL_4(\mathbb R):
\Lambda^{\mathsf T}\eta\Lambda=\eta,\ 
\det\Lambda=1,\ 
\Lambda^0{}_0>0\}.
\]
It is the identity component of the [[lie-groups/lorentz-group|Lorentz group]] \(O(1,3)\). “Proper” means determinant \(+1\), and “orthochronous” means preserving the [[differential-geometry/time-orientation|future cone]].

## Structure

The group is connected, noncompact, and has real dimension \(6\). Its Lie algebra is
\[
\mathfrak{so}(1,3)
=\{X\in M_4(\mathbb R):X^{\mathsf T}\eta+\eta X=0\}.
\]
There is a double covering
\[
SL(2,\mathbb C)_{\mathbb R}\longrightarrow SO^+(1,3)
\]
with kernel \(\{\pm I\}\), and hence a real-Lie-group isomorphism
\[
PSL(2,\mathbb C)_{\mathbb R}\cong SO^+(1,3).
\]
The subscript \(\mathbb R\) is essential: the target is a real Lie group, not a complex Lie group.

## References

1. Gregory L. Naber, *The Geometry of Minkowski Spacetime*, 2nd ed., Springer, 2012, Chapters 1–2. [Publisher record](https://doi.org/10.1007/978-1-4419-7838-7).
2. Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1, Cambridge University Press, 1984, §1.2. [Publisher record](https://doi.org/10.1017/CBO9780511564048).
