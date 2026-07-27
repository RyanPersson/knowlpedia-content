+++
id = "langlands-letter/knowls/automorphic-form-hecke-eigen"
title = "Automorphic Form and Hecke Eigenvalues"
kind = "knowl"
summary = "An adelic automorphic form that is an eigenvector for unramified spherical Hecke operators."
aliases = ["automorphic-form-hecke-eigen", "Automorphic Form and Hecke Eigenvalues"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/automorphic-form-hecke-eigen.md"
+++

Let \(F\) be a number field, \(\mathbb A_F\) its adele ring, and \(G\) a reductive group over \(F\).

In the setting of the letter, an **automorphic form** \(\phi\) is a function on \(G(F)\backslash G(\mathbb A_F)\), subject to the usual regularity and finiteness conditions. At an unramified finite place \(v\), it is a **spherical Hecke eigenform** if its \(K_v\)-fixed component is a simultaneous eigenvector for the spherical Hecke algebra \(\mathcal H(G(F_v),K_v)\).

Equivalently, there is a character
\[
\chi_v:\mathcal H(G(F_v),K_v)\to\mathbb C
\]
such that \(T\phi=\chi_v(T)\phi\) for every \(T\) in the spherical Hecke algebra.

## Remarks

Via the [[langlands-letter/knowls/spherical-hecke-algebra-satake|Satake isomorphism]], \(\chi_v\) determines the semisimple conjugacy class used in the corresponding unramified Euler factor.

## Examples

- Classical modular forms give automorphic forms on \(\mathrm{GL}_2\).
