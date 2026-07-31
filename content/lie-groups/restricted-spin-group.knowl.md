+++
id = "lie-groups/restricted-spin-group"
title = "Restricted spin group"
kind = "construction"
summary = "The full preimage Spin⁺(p,q) of the identity component SO⁺(p,q) under the indefinite spin covering."
aliases = ["Spin+(p,q)", "proper orthochronous spin group"]
domains = ["lie-groups", "differential-geometry", "mathematical-physics"]
section_mode = "progressive"
+++

Let
\[
\rho:\operatorname{Spin}(p,q)\longrightarrow SO(p,q)
\]
be the covering from the
[[lie-groups/indefinite-spin-group|indefinite spin group]]. In this
collection, the **restricted spin group** is the full preimage
\[
\operatorname{Spin}^+(p,q)
:=
\rho^{-1}\bigl(SO^+(p,q)\bigr)
\]
of the identity component of the special orthogonal group.

Its restricted homomorphism
\[
\rho:\operatorname{Spin}^+(p,q)\longrightarrow SO^+(p,q)
\]
is a two-sheeted covering with kernel \(\{\pm1\}\).

## Components

In the standard mixed signatures of total dimension at least \(3\), this full
preimage is connected and is the identity component of
\(\operatorname{Spin}(p,q)\). Signature \((1,1)\) is exceptional: the full
preimage has two components, while restricting further to the identity
component makes the map to \(SO^+(1,1)\) one-to-one.

Thus some authors use \(\operatorname{Spin}_0(p,q)\) for a group that can
differ in low dimension from the full preimage denoted
\(\operatorname{Spin}^+(p,q)\) here.

## Lorentzian four-space

For the \((-+++)\) convention in four dimensions,
\[
\operatorname{Spin}^+(1,3)
\cong
SL(2,\mathbb C)_{\mathbb R},
\]
and the covering becomes the
[[lie-groups/sl2c-spin-cover-of-lorentz-group|
\(SL(2,\mathbb C)\) spin cover]]
of \(SO^+(1,3)\).

## References

1. H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry*, Princeton University Press, 1989, Chapter I, §§2–4. [Publisher record](https://doi.org/10.1515/9781400883912).
2. Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge University Press, 1995, Chapters 13–15. [Publisher record](https://doi.org/10.1017/CBO9780511470912).
