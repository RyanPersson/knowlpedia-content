+++
id = "shared-foundations/lattice"
title = "Lattice"
kind = "definition"
summary = "A partially ordered set in which every pair has a join and a meet."
aliases = ["order lattice", "lattice in order theory"]
domains = ["shared-foundations", "order-theory", "algebra-groups"]
section_mode = "progressive"
prerequisites = ["shared-foundations/partial-order", "shared-foundations/upper-bound", "shared-foundations/lower-bound"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A **lattice** is a [[shared-foundations/partial-order|partially ordered set]]
\((L,\leq)\) in which every pair \(a,b\in L\) has both a least [[shared-foundations/upper-bound|upper bound]],
called its **join** \(a\vee b\), and a greatest [[shared-foundations/lower-bound|lower bound]], called its
**meet** \(a\wedge b\).

## Algebraic laws

Join and meet are commutative, associative, and idempotent, and they satisfy
the absorption laws
\[
a\vee(a\wedge b)=a,\qquad a\wedge(a\vee b)=a.
\]
Conversely, two binary operations satisfying these laws determine a partial
order by
\[
a\leq b\quad\Longleftrightarrow\quad a\vee b=b
\quad\Longleftrightarrow\quad a\wedge b=a.
\]
Thus order-theoretic and algebraic definitions of a lattice are equivalent.

## Examples and scope

The subsets of a set form a lattice under inclusion, with union as join and
intersection as meet. Every [[shared-foundations/total-order|total order]] is a lattice, with maximum as join
and minimum as meet, but a lattice need not be totally ordered.

A **lattice homomorphism** preserves binary joins and binary meets. A bounded
lattice additionally has a least and a greatest element; a homomorphism of
bounded lattices is normally also required to preserve those bounds.
Boundedness is not part of the definition here.

## References

1. Garrett Birkhoff, *Lattice Theory*, 3rd ed., American Mathematical Society, 1967. [AMS record](https://bookstore.ams.org/coll-25-s). Relevant: Chapter I.
