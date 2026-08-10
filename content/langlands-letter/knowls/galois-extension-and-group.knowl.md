+++
id = "langlands-letter/knowls/galois-extension-and-group"
title = "Galois extension and Galois group"
kind = "knowl"
summary = "A normal separable field extension and its group of base-field automorphisms."
aliases = ["galois-extension-and-group", "Galois Extension and Galois Group"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/galois-extension-and-group.md"
section_mode = "progressive"
+++

A finite field extension \(K/k\) is **Galois** if it is normal and
separable. Its **Galois group** is

\[
\operatorname{Gal}(K/k)=\operatorname{Aut}_k(K),
\]

and the [[algebra-fields-galois/fixed-field|fixed field]] of the whole group is \(k\).

Normality means that every \(k\)-embedding \(K\hookrightarrow\overline k\)
has image \(K\). Separability means that every element has a separable
[[linear-algebra/minimal-polynomial|minimal polynomial]] over \(k\).

## Infinite extensions

An [[algebra-fields-galois/algebraic-extension|algebraic extension]] can be Galois without being finite. Its [[algebra-fields-galois/galois-group|Galois group]]
has the Krull topology

\[
\operatorname{Gal}(K/k)
\simeq
\varprojlim_{L/k\ \mathrm{finite\ Galois}}
\operatorname{Gal}(L/k),
\]

and is profinite. The **absolute Galois group** is
\(\Gamma_k=\operatorname{Gal}(k_s/k)\).

Continuous finite quotients of \(\Gamma_k\) correspond to finite Galois
extensions. Continuous \(\ell\)-adic representations can have infinite
image and therefore do not generally factor through one finite extension.

## Langlands role

Finite Galois groups act on split root data in descent constructions. Weil
groups and absolute Galois groups supply the parameter side of local and
global Langlands. The [[langlands/l-group|\(L\)-group]] usually uses a Weil
group whose action on the pinned dual group factors through a finite Galois
quotient.

## References

1. Jean-Pierre Serre, *Galois Cohomology*, Springer, 1997.
