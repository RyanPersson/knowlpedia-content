+++
id = "catalog/finite-groups/lie-type/ree-f4-8"
title = "²F₄(8)"
kind = "definition"
summary = "Fixed points of the exceptional F4 endomorphism composed with Frobenius in characteristic 2."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["catalog/finite-groups/lie-type/steinberg-fixed-point-group", "algebraic-geometry-foundations/algebraic-group"]
dependency_heuristic = "finite-lie-type-core-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

For \(q=8=2^{2m+1}\), where \(m=1\), \({}^2F_4(8)\) is the [[catalog/finite-groups/lie-type/steinberg-fixed-point-group|Steinberg fixed-point group]]
\[
 {}^2F_4(8)=\mathbf G_{F_4,\mathrm{sc}}^F,\qquad F=\tau F_{2^m},\qquad \tau^2=F_2.
\]
Here \(\mathbf G_{F_4,\mathrm{sc}}\) is the split simply connected [[algebraic-geometry-foundations/algebraic-group|algebraic group]] of type \(F_4\) over \(\overline{\mathbb F}_2\), and \(\tau\) is its exceptional endomorphism interchanging the long and short root data. It commutes with Frobenius. Thus \(F^2=F_q\); the group consists of all \(g\) with \(F(g)=g\), under inherited multiplication. Its center is trivial.

## Order and simplicity

Its order is
\[ |{}^2F_4(8)|=264905352699586176614400. \]

It is a nonabelian [[algebra-groups/simple-group|simple group]] for every admitted parameter. The exact order is 264,905,352,699,586,176,614,400.

## Parameter convention

The absolute root-system rank is \(4\), and the exponent of \(2\) in \(q\) must be odd. The notation does not define this family over arbitrary prime powers.

## The prime-field boundary

At \(m=0\), the group \({}^2F_4(2)\) has order 35,942,400. Its [[algebra-groups/commutator-subgroup|commutator subgroup]] has index two and is the [[catalog/finite-groups/lie-type/tits|Tits group]], of order 17,971,200. The Tits group is displayed separately, and is not a 27th sporadic group.

## References

1. [Robert A. Wilson, On the simple groups of Suzuki and Ree (24 April 2010)](https://webspace.maths.qmul.ac.uk/r.a.wilson/pubs_files/SuzRee0.pdf), Introduction; §5.1 orders, §5.2 simplicity, and §5.3 the groups over the prime fields, pp. 24–30.
2. [Robert Steinberg, Lectures on Chevalley Groups (Yale, 1967)](https://www.math.utah.edu/~ptrapa/math-library/steinberg/steinberg-yale-notes.pdf), §11, especially Theorems 34–35, PDF pp. 193–196; notation for field and twisting parameters differs.
3. [B. Akbari, ODs-characterization of some low-dimensional finite classical groups](https://www.ieja.net/files/papers/volume-24/8-V24-2018.pdf), Table 2, p. 85: order column only; its additional Restrictions concern a separate invariant.
