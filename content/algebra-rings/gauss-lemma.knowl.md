+++
id = "algebra-rings/gauss-lemma"
title = "Gauss's lemma"
kind = "knowl"
summary = "Over a UFD, primitive polynomials factor over the fraction field exactly when they factor over the ring."
aliases = ["gauss-lemma", "Gauss's lemma"]
domains = ["algebra-rings"]
prerequisites = ["algebra-rings/ufd", "algebra-rings/fraction-field", "algebra-rings/primitive-polynomial", "algebra-rings/polynomial-ring", "algebra-rings/irreducible-polynomial"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "algebra-rings/gauss-lemma.md"
+++

**Gauss's lemma**: Let \(R\) be a [[algebra-rings/ufd|UFD]] with [[algebra-rings/fraction-field|fraction field]] \(K\). If \(f\in R[x]\) is [[algebra-rings/primitive-polynomial|primitive]], then any factorization \(f=gh\) in the [[algebra-rings/polynomial-ring|polynomial ring]] \(K[x]\) can be written (after multiplying \(g,h\) by nonzero scalars in \(K\)) as a factorization \(f=g'h'\) with \(g',h'\in R[x]\) primitive. In particular, a primitive \(f\in R[x]\) is [[algebra-rings/irreducible-polynomial|irreducible]] in \(R[x]\) if and only if it is irreducible in \(K[x]\).

## Remarks

This rests on the [[algebra-rings/gauss-content-lemma|content multiplicativity lemma]] and is the key bridge between factorization over \(R\) and over its field of fractions.
