+++
id = "catalog/finite-groups/lie-type/sz-q"
title = "Sz(q)"
kind = "definition"
summary = "Fixed points of the exceptional B2 endomorphism composed with Frobenius in characteristic 2."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["catalog/finite-groups/lie-type/steinberg-fixed-point-group", "algebraic-geometry-foundations/algebraic-group"]
dependency_heuristic = "finite-lie-type-core-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

For \(q=2^{2m+1}\), where \(m\geq1\) is an integer, \({}^2B_2(q)\) is the [[catalog/finite-groups/lie-type/steinberg-fixed-point-group|Steinberg fixed-point group]]
\[
 {}^2B_2(q)=\mathbf G_{B_2,\mathrm{sc}}^F,\qquad F=\tau F_{2^m},\qquad \tau^2=F_2.
\]
Here \(\mathbf G_{B_2,\mathrm{sc}}\) is the split simply connected [[algebraic-geometry-foundations/algebraic-group|algebraic group]] of type \(B_2\) over \(\overline{\mathbb F}_2\), and \(\tau\) is its exceptional endomorphism interchanging the long and short root data. It commutes with Frobenius. Thus \(F^2=F_q\); the group consists of all \(g\) with \(F(g)=g\), under inherited multiplication. Its center is trivial.

## Order and simplicity

Its order is
\[ |{}^2B_2(q)|=q^2(q^2+1)(q-1). \]

It is a nonabelian [[algebra-groups/simple-group|simple group]] for every admitted parameter.

## Parameter convention

The absolute root-system rank is \(2\), and the exponent of \(2\) in \(q\) must be odd. The notation does not define this family over arbitrary prime powers. The traditional notation \(\operatorname{Sz}(q)\) is another name for \({}^2B_2(q)\).

## The prime-field boundary

The same fixed-point construction at \(m=0\) gives \(\operatorname{Sz}(2)\), of order 20, isomorphic to \(C_5\rtimes C_4\) with [[algebra-groups/faithful-action|faithful action]] of \(C_4=\operatorname{Aut}(C_5)\). It is excluded from the simple-family tile.

## References

1. [Robert A. Wilson, On the simple groups of Suzuki and Ree (24 April 2010)](https://webspace.maths.qmul.ac.uk/r.a.wilson/pubs_files/SuzRee0.pdf), Introduction; §5.1 orders, §5.2 simplicity, and §5.3 the groups over the prime fields, pp. 24–30.
2. [Robert Steinberg, Lectures on Chevalley Groups (Yale, 1967)](https://www.math.utah.edu/~ptrapa/math-library/steinberg/steinberg-yale-notes.pdf), §11, especially Theorems 34–35, PDF pp. 193–196; notation for field and twisting parameters differs.
3. [B. Akbari, ODs-characterization of some low-dimensional finite classical groups](https://www.ieja.net/files/papers/volume-24/8-V24-2018.pdf), Table 2, p. 85: order column only; its additional Restrictions concern a separate invariant.
