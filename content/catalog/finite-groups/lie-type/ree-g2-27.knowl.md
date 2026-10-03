+++
id = "catalog/finite-groups/lie-type/ree-g2-27"
title = "²G₂(27)"
kind = "definition"
summary = "Fixed points of the exceptional G2 endomorphism composed with Frobenius in characteristic 3."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["catalog/finite-groups/lie-type/steinberg-fixed-point-group", "algebraic-geometry-foundations/algebraic-group"]
dependency_heuristic = "finite-lie-type-core-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

For \(q=27=3^{2m+1}\), where \(m=1\), \({}^2G_2(27)\) is the [[catalog/finite-groups/lie-type/steinberg-fixed-point-group|Steinberg fixed-point group]]
\[
 {}^2G_2(27)=\mathbf G_{G_2,\mathrm{sc}}^F,\qquad F=\tau F_{3^m},\qquad \tau^2=F_3.
\]
Here \(\mathbf G_{G_2,\mathrm{sc}}\) is the split simply connected [[algebraic-geometry-foundations/algebraic-group|algebraic group]] of type \(G_2\) over \(\overline{\mathbb F}_3\), and \(\tau\) is its exceptional endomorphism interchanging the long and short root data. It commutes with Frobenius. Thus \(F^2=F_q\); the group consists of all \(g\) with \(F(g)=g\), under inherited multiplication. Its center is trivial.

## Order and simplicity

Its order is
\[ |{}^2G_2(27)|=10073444472. \]

It is a nonabelian [[algebra-groups/simple-group|simple group]] for every admitted parameter. The exact order is 10,073,444,472.

## Parameter convention

The absolute root-system rank is \(2\), and the exponent of \(3\) in \(q\) must be odd. The notation does not define this family over arbitrary prime powers.

## The prime-field boundary

At \(m=0\), the group \({}^2G_2(3)\) has order 1,512. Its [[algebra-groups/commutator-subgroup|commutator subgroup]] has index three and is isomorphic to \(\operatorname{PSL}_2(8)\), of order 504. The full group at this parameter is excluded from the simple-family tile.

## References

1. [Robert A. Wilson, On the simple groups of Suzuki and Ree (24 April 2010)](https://webspace.maths.qmul.ac.uk/r.a.wilson/pubs_files/SuzRee0.pdf), Introduction; §5.1 orders, §5.2 simplicity, and §5.3 the groups over the prime fields, pp. 24–30.
2. [Robert Steinberg, Lectures on Chevalley Groups (Yale, 1967)](https://www.math.utah.edu/~ptrapa/math-library/steinberg/steinberg-yale-notes.pdf), §11, especially Theorems 34–35, PDF pp. 193–196; notation for field and twisting parameters differs.
3. [B. Akbari, ODs-characterization of some low-dimensional finite classical groups](https://www.ieja.net/files/papers/volume-24/8-V24-2018.pdf), Table 2, p. 85: order column only; its additional Restrictions concern a separate invariant.
4. [ATLAS of Finite Group Representations: ²G₂(27)](https://brauer.maths.qmul.ac.uk/Atlas/v3/exc/R27/), Group heading: exact order 10073444472.
