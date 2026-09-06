+++
id = "algebra-rings/matrix-ring"
title = "Matrix ring"
kind = "knowl"
summary = "The ring of square matrices over a ring, with entrywise addition and matrix multiplication."
aliases = ["matrix-ring", "Matrix ring"]
domains = ["algebra-rings"]
prerequisites = ["algebra-rings/ring"]
dependency_review_count = 1
legacy_source_path = "algebra-rings/matrix-ring.md"
+++

Let \(R\) be a [[algebra-rings/ring|ring]] and \(n\ge 1\). The **matrix ring** \(M_n(R)\) consists of the \(n\times n\) matrices over \(R\), with entrywise addition and multiplication
\[
(AB)_{ij}=\sum_{k=1}^n A_{ik}B_{kj}.
\]

## Remarks

If \(R\) is [[algebra-rings/unital-ring|unital]], then \(M_n(R)\) is unital with identity matrix \(I_n\). Even when \(R\) is commutative, \(M_n(R)\) is generally noncommutative for \(n>1\). If \(D\) is a division ring, then \(M_n(D)\) is [[algebra-rings/simple-ring|simple]], and its [[algebra-rings/center-of-ring|center]] consists of scalar matrices with entries in \(Z(D)\).

## Examples

- \(M_2(\mathbb Z)\) is a noncommutative ring with identity.
- For a prime \(p\), the ring \(M_3(\mathbb F_p)\) has \(p^9\) elements.
- The ring \(M_1(R)\) is canonically isomorphic to \(R\).
