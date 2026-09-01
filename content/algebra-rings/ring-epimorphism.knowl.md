+++
id = "algebra-rings/ring-epimorphism"
title = "Ring epimorphism"
kind = "knowl"
summary = "A ring homomorphism that is right-cancellative among ring homomorphisms."
aliases = ["ring-epimorphism", "Ring epimorphism"]
domains = ["algebra-rings"]
prerequisites = ["algebra-rings/ring-homomorphism"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "algebra-rings/ring-epimorphism.md"
+++

A **ring epimorphism** is a [[algebra-rings/ring-homomorphism|ring homomorphism]] \(\varphi:R\to S\) such that for every ring \(T\) and homomorphisms \(g,h:S\to T\),
\[
g\circ\varphi=h\circ\varphi\quad\Longrightarrow\quad g=h.
\]
Thus \(\varphi\) is an epimorphism in the category of rings.

## Remarks

Every surjective ring homomorphism is an epimorphism, but the converse fails. In the category of commutative unital rings, for example, the localization map \(\mathbb Z\to\mathbb Q\) is an epimorphism but is not surjective.

## Examples

- The quotient map \(R\to R/I\), \(r\mapsto r+I\), is a ring epimorphism.
- The evaluation map \(k[x]\to k\), \(f\mapsto f(c)\), is a surjective ring epimorphism for every \(c\in k\).
- The localization \(\mathbb Z\to\mathbb Q\) is a nonsurjective ring epimorphism.
