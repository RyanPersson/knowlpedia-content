+++
id = "langlands/weil-deligne-representation"
title = "Weil–Deligne representation"
kind = "definition"
summary = "A Weil-group representation together with a compatible nilpotent monodromy operator."
aliases = ["Weil-Deligne representation", "WD representation", "Frobenius-semisimple Weil–Deligne representation"]
domains = ["langlands", "algebra-fields-galois"]
section_mode = "progressive"
+++

Let \(F\) be a nonarchimedean local field. A **Weil–Deligne
representation** on a finite-dimensional complex [[linear-algebra/vector-space|vector space]] \(V\) is a pair
\((r,N)\), where

\[
r:W_F\longrightarrow\operatorname{GL}(V)
\]

is continuous with open kernel on inertia, \(N\in\operatorname{End}(V)\) is
nilpotent, and

\[
r(w)Nr(w)^{-1}=|w|_F N
\qquad(w\in W_F).
\]

Morphisms intertwine both \(r\) and \(N\). This is the representation-theoretic
form of a representation of the [[langlands/weil-deligne-group|Weil–Deligne
group]].

## Frobenius semisimplification

The pair is **Frobenius-semisimple** if \(r(\operatorname{Fr}_F)\) is
semisimple. Replacing the Frobenius action by its semisimple part gives the
Frobenius semisimplification. Local Langlands for
\(\operatorname{GL}_n\) is normally stated using isomorphism classes of
Frobenius-semisimple Weil–Deligne representations.

## Local factor

With geometric Frobenius and inertia \(I_F\), the standard local factor is

\[
L(s,r,N)=
\det\!\left(
1-q_F^{-s}r(\operatorname{Fr}_F)
\mid(\ker N)^{I_F}
\right)^{-1}.
\]

Changing to arithmetic Frobenius changes the displayed convention, not the
underlying representation.

## Monodromy-free case

The condition \(N=0\) gives an ordinary Weil-group representation. If inertia
also acts trivially, the representation is unramified and is determined by the
semisimple [[algebra-groups/conjugacy-class|conjugacy class]] of Frobenius.

## References

1. Pierre Deligne, “Les constantes des équations fonctionnelles des fonctions
   \(L\),” in *Modular Functions of One Variable II*, Lecture Notes in
   Mathematics 349, 1973. [DOI](https://doi.org/10.1007/BFb0067048).
2. Michael Harris, “On the local Langlands correspondence,” 2003, §2.
   [arXiv](https://arxiv.org/abs/math/0304324).
