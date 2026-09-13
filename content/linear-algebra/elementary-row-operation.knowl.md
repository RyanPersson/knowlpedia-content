+++
id = "linear-algebra/elementary-row-operation"
title = "Elementary row operation"
kind = "definition"
summary = "Swapping rows, rescaling one row by a nonzero scalar, or adding a multiple of another row."
aliases = ["row operation", "row reduction operation"]
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/matrix", "algebra-rings/field", "linear-algebra/matrix-inverse"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

An **elementary row operation** on a [[linear-algebra/matrix|matrix]] over a [[algebra-rings/field|field]] is one of three reversible operations: interchange two rows; multiply one row by a nonzero scalar; or add a scalar multiple of one row to a different row. Each is multiplication on the left by an invertible elementary matrix.

## Linear systems

Applying the same row operation to both sides of \(Ax=b\) preserves its solution set because it replaces the equation by \(EAx=Eb\) with \(E\) invertible. Applying an operation to \(A\) without also changing \(b\) generally changes the system. Row operations preserve rank but can change eigenvalues, since left multiplication need not be a change of basis by conjugation.
