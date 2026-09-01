+++
id = "shale-paper/fredholm-determinant-trace-log"
title = "Determinant on I + Trace-Class"
kind = "knowl"
summary = "The Fredholm determinant on identity-plus-trace-class operators."
aliases = ["fredholm-determinant-trace-log", "Determinant on I + Trace-Class"]
domains = ["shale-paper"]
prerequisites = ["linear-algebra/determinant"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "shale-paper/fredholm-determinant-trace-log.md"
+++

Let \(H\) be a Hilbert space and let \(A\) be a trace-class operator on \(H\). The **Fredholm determinant** of \(I+A\) is
\[
\Delta(I+A)=\det(I+A):=\prod_j(1+\lambda_j(A)),
\]
where the nonzero eigenvalues are counted with algebraic multiplicity. The product converges and extends the finite-dimensional [[linear-algebra/determinant|determinant]].

## Remarks

- On a neighborhood of \(I\) where a logarithm is defined,
  \[
  \Delta(T)=\exp\bigl(\operatorname{tr}(\log T)\bigr).
  \]
- The restriction of \(\Delta\) to the invertible group \(GL(H)_1=\{I+A:A\text{ trace class and }I+A\text{ invertible}\}\) is continuous in the trace norm.

## Examples

- If \(A\) is finite rank, \(\Delta(I+A)\) matches the usual finite-dimensional determinant.
