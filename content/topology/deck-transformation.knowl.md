+++
id = "topology/deck-transformation"
title = "Deck transformation"
kind = "definition"
summary = "A homeomorphism of a covering space that preserves its projection."
aliases = ["deck translation", "covering transformation"]
domains = ["topology"]
section_mode = "progressive"
prerequisites = ["topology/covering-space", "topology/homeomorphism", "shared-foundations/composition-of-functions"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a [[topology/covering-space|covering]] \(p:E\to B\), a **deck transformation** is a homeomorphism \(h:E\to E\) such that \(p\circ h=p\). It moves points within fibers while preserving the covering projection. Deck transformations form a group under composition.

## Torus deck translations

For an [[topology/integer-matrix-torus-cover|integer-matrix covering]] \(p_A\), each translation \([x]\mapsto[x+a]\) with \(Aa\in\mathbb Z^n\) is a deck transformation. These are all the deck transformations: the continuous difference \(h([x])-[x]\) lies in the finite kernel of \(p_A\), and the torus is connected, so that difference is constant. The group is \(A^{-1}\mathbb Z^n/\mathbb Z^n\). A general covering need not have enough deck transformations to act transitively on every fiber.

## References

- [Hatcher, Algebraic Topology, §1.3 (covering spaces and deck transformations)](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf).
