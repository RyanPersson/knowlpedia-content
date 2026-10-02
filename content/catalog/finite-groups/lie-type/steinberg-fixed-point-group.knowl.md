+++
id = "catalog/finite-groups/lie-type/steinberg-fixed-point-group"
title = "Steinberg fixed-point group"
kind = "definition"
summary = "A finite group obtained as fixed points of a specified algebraic-group endomorphism, modulo the finite center."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["algebraic-geometry-foundations/simply-connected-semisimple-group", "algebra-fields-galois/frobenius-endomorphism", "algebra-groups/center-of-group", "algebra-groups/finite-group"]
dependency_heuristic = "finite-lie-type-core-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(\mathbf G\) be a connected [[algebraic-geometry-foundations/simply-connected-semisimple-group|simply connected semisimple algebraic group]] over \(\overline{\mathbb F}_p\). For an algebraic-group endomorphism \(F\) such that \(F^a=F_{p^b}\) for some positive integers \(a,b\), the **Steinberg fixed-point group** and its central quotient are
\[
 \mathbf G^F=\{g\in\mathbf G(\overline{\mathbb F}_p):F(g)=g\},
 \qquad \mathbf G^F/Z(\mathbf G^F).
\]
Here \(F_{p^b}\) is the [[algebra-fields-galois/frobenius-endomorphism|Frobenius endomorphism]] of a chosen split model and \(Z\) is the [[algebra-groups/center-of-group|finite center]]. The fixed points form a [[algebra-groups/finite-group|finite group]] under inherited multiplication. A specific twisted family includes the choice of \(\mathbf G\) and \(F\) as part of its definition.

## Graph and exceptional twists

For a pinned Dynkin-diagram automorphism \(\gamma\) of order \(a\) commuting with \(F_q\), the choice \(F=\gamma F_q\) has \(F^a=F_{q^a}\). An exceptional endomorphism \(\tau\) in the Suzuki–Ree cases instead satisfies \(\tau^2=F_p\). With \(F=\tau F_{p^m}\), one has \(F^2=F_{p^{2m+1}}\).

These two constructions use different field conventions. Here \({}^2A_{n-1}(q)\) uses matrices over \(\mathbb F_{q^2}\), while \({}^3D_4(q)\) and \({}^2E_6(q)\) use the indicated graph–Frobenius parameter \(q\). Some sources put \(q^2\) or \(q^3\) in those names instead.

## References

1. [Robert Steinberg, Lectures on Chevalley Groups (Yale, 1967)](https://www.math.utah.edu/~ptrapa/math-library/steinberg/steinberg-yale-notes.pdf), §11, especially Theorems 34–35, PDF pp. 193–196; notation for field and twisting parameters differs.
2. [Robert A. Wilson, On the simple groups of Suzuki and Ree (24 April 2010)](https://webspace.maths.qmul.ac.uk/r.a.wilson/pubs_files/SuzRee0.pdf), Introduction; §5.1 orders, §5.2 simplicity, and §5.3 the groups over the prime fields, pp. 24–30.
