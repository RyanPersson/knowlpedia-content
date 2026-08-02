+++
id = "differential-geometry/principal-symbol"
title = "Principal symbol of a differential operator"
kind = "definition"
summary = "The homogeneous bundle map on the cotangent bundle obtained from the highest-order part of a differential operator."
aliases = ["symbol of a differential operator", "leading symbol"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(D:\Gamma^\infty(E)\to\Gamma^\infty(F)\) be a [[differential-geometry/differential-operator-vector-bundles|differential operator between vector bundles]] of order \(m\). Its **principal symbol** is the [[fiber-bundles/bundle-map|bundle map]]
\[
\sigma_m(D):\pi^*E\longrightarrow\pi^*F
\]
over the [[fiber-bundles/cotangent-bundle|cotangent bundle]] \(T^*M\), homogeneous of degree \(m\) in each covector. In local coordinates and frames, if
\[
D=\sum_{|\alpha|\leq m}a_\alpha(x)\partial^\alpha,
\]
then
\[
\sigma_m(D)(x,\xi)=\sum_{|\alpha|=m}a_\alpha(x)\xi^\alpha:E_x\to F_x.
\]
Although this formula uses coordinates, its highest-order transformation law makes \(\sigma_m(D)\) intrinsic.

## Commutator characterization

The principal symbol can be recovered without coordinates. Repeated commutators of \(D\) with multiplication operators are order zero, and their value at \(x\) depends only on the differentials of the functions there. Polarizing this symmetric \(m\)-linear expression yields \(\sigma_m(D)(x,\xi)\). Consequently, adding an operator of order at most \(m-1\) does not change the principal symbol.

## Algebraic properties and ellipticity

For operators of orders \(m\) and \(n\),
\[
\sigma_{m+n}(D_2D_1)=\sigma_n(D_2)\sigma_m(D_1).
\]
Thus leading symbols turn composition of differential operators into pointwise composition of homogeneous bundle maps. An operator is [[differential-geometry/elliptic-differential-operator|elliptic]] precisely when this symbol is invertible at every nonzero covector.

## Conventions and scope

**Warning.** Some analytic texts define \(\sigma_m(D)\) using \(D_x=-i\partial_x\), introducing a factor \(i^m\). The convention here uses \(\partial_x\) and no factor of \(i\). Invertibility, characteristic covectors, and ellipticity are unchanged by this convention.

## References

1. H. B. Lawson Jr. and M.-L. Michelsohn, *Spin Geometry*, Princeton University Press, 1989. [Publisher record](https://doi.org/10.1515/9781400883912). Relevant: chapter III, §1, symbols and ellipticity.
2. N. Berline, E. Getzler, and M. Vergne, *Heat Kernels and Dirac Operators*, Springer, 1992. [Publisher record](https://doi.org/10.1007/978-3-642-58088-8). Relevant: chapter 2, differential operators and symbols.
