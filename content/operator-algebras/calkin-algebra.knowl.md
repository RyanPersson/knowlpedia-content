+++
id = "operator-algebras/calkin-algebra"
title = "Calkin algebra"
kind = "definition"
summary = "The quotient of the bounded operators on an infinite-dimensional Hilbert space by its compact operators."
aliases = ["Calkin algebra", "B(H)/K(H)"]
domains = ["operator-algebras", "functional-analysis"]
section_mode = "progressive"
prerequisites = ["linear-algebra/hilbert-space", "operator-algebras/bounded-operator-cstar-algebra", "operator-algebras/compact-operator-cstar-algebra", "operator-algebras/quotient-cstar-algebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(H\) be an infinite-dimensional complex [[linear-algebra/hilbert-space|Hilbert space]]. The **Calkin algebra** is the [[operator-algebras/quotient-cstar-algebra|quotient]]
\[
\mathcal Q(H):=\mathcal B(H)/\mathcal K(H),
\]
where \(\mathcal B(H)\) is the [[operator-algebras/bounded-operator-cstar-algebra|bounded-operator algebra]] and \(\mathcal K(H)\) is its [[operator-algebras/compact-operator-cstar-algebra|compact-operator ideal]].

## Essential operator information

Two bounded operators define the same element of \(\mathcal Q(H)\) exactly when their difference is compact.

The quotient map \(q:\mathcal B(H)\to\mathcal Q(H)\) forgets compact perturbations. An operator \(T\) is Fredholm exactly when \(q(T)\) is invertible; this is the Calkin-algebra form of Atkinson's theorem. Thus the Calkin algebra records the operator's essential behavior and discards finite-dimensional errors.

## Scope and conventions

The quotient is a \(C^*\)-algebra because \(\mathcal K(H)\) is a closed two-sided ideal. The infinite-dimensional hypothesis matters: if \(H\) is finite-dimensional, every operator is compact and the quotient is the zero algebra. The notation \(\mathcal Q(H)\) depends on \(H\), although Calkin algebras of Hilbert spaces with the same infinite dimension are canonically isomorphic up to the chosen Hilbert-space identification.

## References

1. John B. Conway, *A Course in Functional Analysis*, 2nd ed., Springer, 1990. [Springer DOI record](https://doi.org/10.1007/978-1-4757-4383-8). Relevant: Chapter XII, Fredholm operators and the Calkin algebra.
2. R. G. Douglas, *Banach Algebra Techniques in Operator Theory*, 2nd ed., Springer, 1998. [Springer DOI record](https://doi.org/10.1007/978-1-4757-4384-5). Relevant: Chapter 3, Fredholm operators and the Calkin algebra.
