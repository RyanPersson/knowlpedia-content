+++
id = "operator-algebras/cauchy-schwarz-positive-functional"
title = "Cauchy–Schwarz inequality for a positive functional"
kind = "definition"
summary = "A positive functional on a C*-algebra induces a positive semidefinite form satisfying the scalar Cauchy–Schwarz inequality."
aliases = ["Schwarz inequality for positive functionals", "C*-Cauchy–Schwarz"]
domains = ["operator-algebras", "functional-analysis"]
section_mode = "progressive"
prerequisites = ["operator-algebras/cstar-algebra", "operator-algebras/positive-linear-functional", "linear-algebra/cauchy-schwarz-inequality"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]] and let
\(\varphi:A\to\mathbb C\) be a
[[operator-algebras/positive-linear-functional|positive linear functional]].
The **Cauchy–Schwarz inequality for \(\varphi\)** is
\[
\left|\varphi(b^*a)\right|^2
\leq \varphi(a^*a)\,\varphi(b^*b)
\qquad(a,b\in A).
\]
It is the ordinary
[[linear-algebra/cauchy-schwarz-inequality|Cauchy–Schwarz inequality]] for
the positive semidefinite sesquilinear form
\[
\langle a,b\rangle_\varphi=\varphi(b^*a).
\]
No faithfulness, unitality, or normalization of \(\varphi\) is required.
When either factor on the right vanishes, the mixed term necessarily
vanishes as well.

## Derivation and equality

Positivity gives
\[
0\leq \varphi\bigl((a+\lambda b)^*(a+\lambda b)\bigr)
\qquad(\lambda\in\mathbb C).
\]
If \(\varphi(b^*b)>0\), choosing
\(\lambda=-\varphi(b^*a)/\varphi(b^*b)\) yields the displayed inequality.
If \(\varphi(b^*b)=0\), applying positivity first to
\(a+\lambda b\) shows directly that \(\varphi(b^*a)=0\).

After quotienting by the zero-length vectors, equality holds precisely when
the classes of \(a\) and \(b\) are linearly dependent. This is the usual
equality criterion in the resulting pre-Hilbert space; it need not mean that
\(a\) and \(b\) are linearly dependent inside \(A\).

## Structure and consequences

The null space
\[
N_\varphi=\{a\in A:\varphi(a^*a)=0\}
\]
is a left ideal. Indeed, Cauchy–Schwarz and
\(a^*c^*ca\leq\lVert c\rVert^2a^*a\) show that \(ca\in N_\varphi\) whenever
\(a\in N_\varphi\). Consequently the form descends to \(A/N_\varphi\);
its Hilbert-space completion is the space used in the
[[operator-algebras/gns-construction|GNS construction]].

For a state on \(M_n(\mathbb C)\) of the form
\(\varphi(x)=\langle x\xi,\xi\rangle\), the inequality becomes the usual
Cauchy–Schwarz inequality for the vectors \(a\xi\) and \(b\xi\). Positivity
is decisive: an arbitrary bounded linear functional need not make
\(\varphi(b^*a)\) into a positive semidefinite form and need not satisfy this
inequality.

## References

1. Gerard J. Murphy, *C*-Algebras and Operator Theory*, Academic Press, 1990. [Elsevier DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §3.3 on positive linear functionals and their Cauchy–Schwarz inequality.
