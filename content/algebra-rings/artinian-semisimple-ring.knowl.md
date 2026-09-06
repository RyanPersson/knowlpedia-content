+++
id = "algebra-rings/artinian-semisimple-ring"
title = "Artinian semisimple ring"
kind = "knowl"
summary = "A semisimple ring that satisfies the descending chain condition on ideals; equivalently a finite product of matrix algebras over division rings."
aliases = ["artinian-semisimple-ring", "Artinian semisimple ring"]
domains = ["algebra-rings"]
prerequisites = ["algebra-rings/semisimple-ring"]
dependency_review_count = 1
legacy_source_path = "algebra-rings/artinian-semisimple-ring.md"
+++

An **Artinian semisimple ring** is a ring \(R\) that is [[algebra-rings/semisimple-ring|semisimple]] and left Artinian, meaning that every descending chain of left ideals stabilizes.

## Remarks

By the [[algebra-rings/artin-wedderburn-theorem|Artin–Wedderburn theorem]], such rings are precisely finite direct products of [[algebra-rings/matrix-ring|matrix rings]] over [[algebra-rings/division-ring|division rings]], and these rings are the basic building blocks for finite-length module categories.

## Examples

- \(M_n(k)\) is Artinian semisimple for any field \(k\).
- A finite product of fields, e.g. \(\mathbb{Q}\times \mathbb{Q}\times \mathbb{F}_5\), is Artinian semisimple.
- An infinite product \(\prod_{i\in \mathbb{N}}k\) (with \(k\) a field) is not Artinian, hence not Artinian semisimple.
