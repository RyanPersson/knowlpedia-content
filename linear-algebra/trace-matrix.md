---
title: "Trace of a matrix"
description: "The sum of the diagonal entries of a square matrix."
---

The **trace** of an \(n \times n\) {{< knowl id="matrix" text="matrix" >}} \(A\) is the sum of its diagonal entries:
$$
\operatorname{tr}(A) = \sum_{i=1}^n a_{ii}.
$$

## Properties
For square matrices \(A, B\) and scalar \(c\):

- **Linearity**: \(\operatorname{tr}(A + B) = \operatorname{tr}(A) + \operatorname{tr}(B)\) and \(\operatorname{tr}(cA) = c \operatorname{tr}(A)\).
- **Cyclic property**: \(\operatorname{tr}(AB) = \operatorname{tr}(BA)\).
- **Similarity invariance**: If \(B = P^{-1}AP\), then \(\operatorname{tr}(B) = \operatorname{tr}(A)\).
- **Transpose**: \(\operatorname{tr}(A^T) = \operatorname{tr}(A)\).

## Relation to eigenvalues
The trace equals the sum of {{< knowl id="eigenvalue" text="eigenvalues" >}} (counted with algebraic multiplicity):
$$
\operatorname{tr}(A) = \sum_{i=1}^n \lambda_i.
$$

## Examples
- \(\operatorname{tr}(I_n) = n\).
- For a projection \(P\) onto a \(k\)-dimensional subspace, \(\operatorname{tr}(P) = k\).
