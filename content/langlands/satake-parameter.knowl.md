+++
id = "langlands/satake-parameter"
title = "Satake parameter"
kind = "definition"
summary = "The semisimple dual-group conjugacy class classifying an unramified representation."
aliases = ["unramified Langlands parameter", "Hecke parameter", "Satake conjugacy class"]
domains = ["langlands", "harmonic-analysis"]
section_mode = "progressive"
+++

Let \(G\) be an unramified connected [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]] over a nonarchimedean
local field \(F\), choose a hyperspecial subgroup \(K\leq G(F)\), and let
\(\pi\) be an irreducible
[[harmonic-analysis/unramified-representation-p-adic-group|unramified
representation]]. Its **Satake parameter** is the semisimple
\(\widehat G\)-conjugacy class

\[
s(\pi)=[g\rtimes\operatorname{Fr}_F]
\subset \widehat G\rtimes\operatorname{Fr}_F
\subset{}^LG
\]

corresponding, under the normalized Satake isomorphism, to the character by
which the [[harmonic-analysis/hecke-algebra-locally-compact-group-pair|spherical Hecke algebra]] acts on the line \(\pi^K\). If \(G\) is
split, this is commonly recorded simply as a semisimple [[algebra-groups/conjugacy-class|conjugacy class]]
\([g]\) in \(\widehat G\).

## As a local parameter

The associated [[langlands/local-l-parameter|local \(L\)-parameter]] is
trivial on inertia and on the Deligne \(\mathrm{SL}_2\), and sends geometric
Frobenius to \(s(\pi)\). Thus Satake parameters are precisely the unramified
part of the [[langlands/local-langlands-correspondence|local Langlands correspondence]].

## Normalization warning

The unnormalized Satake isomorphism differs from the normalized one by a
\(q_F^\rho\)-shift. Arithmetic instead of geometric Frobenius also inverts the
Frobenius convention. A local-factor formula must use the same normalization
as its Satake parameter.

## Local factors

For an algebraic representation \(r:{}^LG\to\operatorname{GL}(V)\), the
unramified local factor is

\[
L(s,\pi,r)=
\det\!\left(1-r(s(\pi))q_F^{-s}\mid V\right)^{-1}.
\]

## References

1. Armand Borel, “Automorphic \(L\)-functions,” in *Automorphic Forms,
   Representations and \(L\)-Functions*, Proceedings of Symposia in Pure
   Mathematics 33, part 2, 1979, §§3–4.
2. Jayce R. Getz, *An Introduction to Automorphic Representations*, §§9–10.
   [Author notes](https://sites.math.duke.edu/~jgetz/aut_reps.pdf).
