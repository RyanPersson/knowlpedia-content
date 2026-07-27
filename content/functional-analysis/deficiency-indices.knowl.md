+++
id = "functional-analysis/deficiency-indices"
title = "Deficiency indices"
kind = "definition"
summary = "The dimensions of the two nonreal eigenspaces of the adjoint of a symmetric operator."
aliases = ["defect indices", "deficiency numbers"]
domains = ["functional-analysis"]
section_mode = "progressive"
+++

Let \(A\) be a densely defined closed
[[functional-analysis/symmetric-operator|symmetric operator]] on a complex
[[linear-algebra/hilbert-space|Hilbert space]]. Its **deficiency subspaces** are
\[
\mathcal N_+=\ker(A^*-iI),\qquad
\mathcal N_-=\ker(A^*+iI),
\]
where \(A^*\) is the
[[functional-analysis/adjoint-unbounded-operator|adjoint of \(A\)]]. The
**deficiency indices** are the cardinal dimensions
\[
n_+(A)=\dim\mathcal N_+,\qquad n_-(A)=\dim\mathcal N_-.
\]
They may be finite or infinite. More generally, \(\dim\ker(A^*-zI)\) is
constant as \(z\) ranges over either open half-plane; \(n_+\) uses the upper
half-plane and \(n_-\) the lower half-plane under the convention above.

## Self-adjointness and extensions

The operator \(A\) is
[[functional-analysis/self-adjoint-unbounded-operator|self-adjoint]] exactly
when \(n_+(A)=n_-(A)=0\). It has a
[[functional-analysis/self-adjoint-extension|self-adjoint extension]] on the
same Hilbert space exactly when \(n_+(A)=n_-(A)\); when these common dimensions
are nonzero, unitary maps from \(\mathcal N_+\) to \(\mathcal N_-\) parametrize
the extensions. This is von Neumann’s extension theorem
[Schmüdgen, Chapter 13](https://doi.org/10.1007/978-94-007-4753-1).

## Closure and geometric meaning

If a symmetric operator is not closed, its deficiency indices are defined to
be those of its [[functional-analysis/closure-of-operator|closure]]. For a
closed symmetric \(A\), the domain of \(A^*\) decomposes into the domain of
\(A\) together with the two deficiency subspaces. The latter measure the
independent boundary data missing from \(A\); equality of their dimensions is
precisely what permits those data to be paired to form a self-adjoint domain.

## Examples and sign convention

The minimal momentum operator \(-i\,d/dx\) on a bounded interval, obtained by
closing the operator on [[functional-analysis/test-function-space|compactly supported smooth functions]], has deficiency
indices \((1,1)\) and admits a circle of self-adjoint boundary conditions. On
the whole real line the corresponding minimal operator has indices \((0,0)\)
and is essentially self-adjoint. Interchanging \(i\) and \(-i\), or changing
the sign of the operator, swaps the [[shared-foundations/ordered-pair|ordered pair]]; a source’s convention should
therefore be checked before comparing formulas.

## References

1. Konrad Schmüdgen, *Unbounded Self-adjoint Operators on Hilbert Space*, Graduate Texts in Mathematics 265, Springer, 2012. [DOI record](https://doi.org/10.1007/978-94-007-4753-1). Relevant: Chapter 13 on deficiency indices and self-adjoint extensions.
2. Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics II: Fourier Analysis, Self-Adjointness*, Academic Press, 1975. [Bibliographic record](https://catalogue.bnf.fr/ark:/12148/cb37359774j). Relevant: Chapter X on self-adjoint extensions.
