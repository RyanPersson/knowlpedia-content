+++
id = "functional-analysis/essentially-self-adjoint-operator"
title = "Essentially self-adjoint operator"
kind = "definition"
summary = "A densely defined symmetric operator whose closure is self-adjoint."
aliases = ["essential self-adjointness"]
domains = ["functional-analysis"]
prerequisites = ["functional-analysis/symmetric-operator", "linear-algebra/hilbert-space", "functional-analysis/closure-of-operator", "functional-analysis/self-adjoint-unbounded-operator", "functional-analysis/self-adjoint-extension"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(T\) be a densely defined
[[functional-analysis/symmetric-operator|symmetric operator]] on a complex
[[linear-algebra/hilbert-space|Hilbert space]]. It is **essentially self-adjoint** if its
[[functional-analysis/closure-of-operator|closure]] \(\overline T\) is a
[[functional-analysis/self-adjoint-unbounded-operator|self-adjoint operator]].
Equivalently, \(T\) has exactly one [[functional-analysis/self-adjoint-extension|self-adjoint extension]], namely
\(\overline T\). The definition refers to the operator together with its
specified dense domain: the same differential expression on different initial
domains can be essentially self-adjoint, admit many self-adjoint extensions,
or admit none. Symmetry alone does not imply essential self-adjointness because
the domains of \(\overline T\) and \(T^*\) may differ.

## Deficiency-space criteria

Essential self-adjointness is equivalent to vanishing of both deficiency
spaces:
\[
\ker(T^*-i)=\{0\},\qquad \ker(T^*+i)=\{0\}.
\]
Equivalently, each of the ranges \(\operatorname{Ran}(T+i)\) and
\(\operatorname{Ran}(T-i)\) is dense in \(H\). Surjectivity of these ranges is
a criterion for an already closed self-adjoint operator; density is the
correct criterion for the unclosed operator \(T\). These are the
deficiency-space criteria for essential self-adjointness.

## Cores and closure

If \(A\) is self-adjoint and \(D\subseteq\mathcal D(A)\) is dense in
\(\mathcal D(A)\) for the [[functional-analysis/graph-norm|graph norm]], then \(D\) is a
[[functional-analysis/core-of-closed-operator|core]] for \(A\), and the
restriction \(A|_D\) is essentially self-adjoint with closure \(A\).
This is the standard way differential and geometric operators initially
defined on test sections recover a canonical self-adjoint operator. Ordinary
Hilbert-space density of \(D\) is not enough; graph-norm density is required.

## Examples and domain sensitivity

On \(L^2(\mathbb R)\), the momentum operator
\(-i\,d/dx\) with initial domain \(C_c^\infty(\mathbb R)\) is essentially
self-adjoint. On \(L^2(0,1)\), the same expression on
\(C_c^\infty(0,1)\) is symmetric but not essentially self-adjoint; different
boundary conditions produce distinct self-adjoint extensions. This contrast
shows why a formal adjoint calculation does not settle essential
self-adjointness.

## References

1. Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis*, Academic Press, 1972. [Publisher record](https://doi.org/10.1016/B978-0-12-585001-8.X5001-6). Relevant: Chapter VIII on symmetric operators, deficiency indices, and essential self-adjointness.
2. Konrad Schmüdgen, *Unbounded Self-adjoint Operators on Hilbert Space*, Springer, 2012. [DOI record](https://doi.org/10.1007/978-94-007-4753-1). Relevant: Chapters 1, 3, and 13 on closed operators, self-adjointness criteria, and extension theory.
