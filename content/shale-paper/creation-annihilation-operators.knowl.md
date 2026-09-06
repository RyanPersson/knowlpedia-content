+++
id = "shale-paper/creation-annihilation-operators"
title = "Creation and Annihilation Operators"
kind = "knowl"
summary = "Operators adding/removing one symmetric tensor factor in bosonic Fock space"
aliases = ["creation-annihilation-operators", "Creation and Annihilation Operators"]
domains = ["shale-paper"]
legacy_source_path = "shale-paper/creation-annihilation-operators.md"
prerequisites = ["shale-paper/symmetric-fock-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

For \(z\in H\), the **creation operator** on the algebraic finite-particle subspace of [[shale-paper/symmetric-fock-space|symmetric Fock space]] \(S(H)\) is defined by
\[
C(z)(x_1\otimes\cdots\otimes x_n)_s
=\sqrt{n+1}\,(z\otimes x_1\otimes\cdots\otimes x_n)_s.
\]
Its Hilbert-space adjoint \(C(z)^*\), on its natural domain, is the **annihilation operator**. These operators are generally unbounded.

## Field operator

In the paper's notation, the associated field operator is the closure
\[
R(z)=\frac1{\sqrt2}\bigl(C(z)+C(z)^*\bigr)^{\sim}.
\]

In particular, \(C(z)e_0=z\in\operatorname{Sym}^1(H)\), where \(e_0\) is the vacuum vector.
