+++
id = "catalog/finite-groups/lie-type/twisted-e6-q"
title = "²E₆(q)"
kind = "definition"
summary = "Fixed points of a diagram automorphism of order 2 composed with q-power Frobenius, modulo the finite center."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["catalog/finite-groups/lie-type/steinberg-fixed-point-group", "algebraic-geometry-foundations/algebraic-group"]
dependency_heuristic = "finite-lie-type-core-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

For a prime power \(q\), \({}^2E_6(q)\) is the central quotient of the [[catalog/finite-groups/lie-type/steinberg-fixed-point-group|Steinberg fixed-point group]]
\[
 {}^2E_6(q)=\mathbf G_{E_6,\mathrm{sc}}^F/Z(\mathbf G_{E_6,\mathrm{sc}}^F),\qquad F=\gamma F_q.
\]
The [[algebraic-geometry-foundations/algebraic-group|algebraic group]] is split and simply connected over \(\overline{\mathbb F}_p\), where \(q\) is a power of \(p\). The pinned diagram automorphism \(\gamma\) has order \(2\) and is the nontrivial symmetry of the \(E_6\) diagram. It commutes with coordinatewise Frobenius \(F_q\), so \(F^2=F_{q^2}\). Multiplication is multiplication of cosets of the finite center.

## Order and simplicity

Its order is
\[ |{}^2E_6(q)|=\frac{q^{36}(q^{12}-1)(q^9+1)(q^8-1)(q^6-1)(q^5+1)(q^2-1)}{\gcd(3,q+1)}. \]

It is a nonabelian [[algebra-groups/simple-group|simple group]] for every admitted parameter.

## Field and center convention

Here \(q\) names the graph–Frobenius parameter; some sources write \(q^2\) in the group name instead. The absolute rank is \(6\). The finite center of the simply connected fixed-point group has order \(\gcd(3,q+1)\), which is divided out.

## References

1. [Robert Steinberg, Lectures on Chevalley Groups (Yale, 1967)](https://www.math.utah.edu/~ptrapa/math-library/steinberg/steinberg-yale-notes.pdf), §11, especially Theorems 34–35, PDF pp. 193–196; notation for field and twisting parameters differs.
2. [B. Akbari, ODs-characterization of some low-dimensional finite classical groups](https://www.ieja.net/files/papers/volume-24/8-V24-2018.pdf), Table 2, p. 85: order column only; its additional Restrictions concern a separate invariant.
