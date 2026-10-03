+++
id = "algebra-commutative/conductor-of-order"
title = "Conductor of an order"
kind = "definition"
summary = "The largest ideal of the ring of integers contained in a given number-field order."
aliases = ["conductor of an order", "conductor ideal of an order"]
domains = ["algebra-commutative"]
section_mode = "progressive"
prerequisites = ["algebra-rings/order-in-algebra", "algebra-fields-galois/number-field", "algebra-fields-galois/ring-of-integers", "algebra-rings/ideal"]
dependency_heuristic = "semantic-transcript-review-v1"
dependency_review_count = 1
+++

Let \(\mathcal O\subseteq\mathcal O_K\) be an [[algebra-rings/order-in-algebra|order]] in a [[algebra-fields-galois/number-field|number field]] \(K\), with [[algebra-fields-galois/ring-of-integers|ring of integers]] \(\mathcal O_K\). Its **conductor** is
\[
\mathfrak f=\{x\in\mathcal O_K:x\mathcal O_K\subseteq\mathcal O\}.
\]

It is the largest \(\mathcal O_K\)-[[algebra-rings/ideal|ideal]] contained in \(\mathcal O\), and is also an ideal of \(\mathcal O\). Since \(1\in\mathcal O_K\), every element of \(\mathfrak f\) already belongs to \(\mathcal O\).

## Why it is nonzero

The additive quotient \(\mathcal O_K/\mathcal O\) is finite. If its order is \(m\), then \(m\mathcal O_K\subseteq\mathfrak f\). Thus the conductor records a finite obstruction to the order being maximal; it equals \(\mathcal O_K\) exactly when \(\mathcal O=\mathcal O_K\).

## Quadratic orders

If \(K\) is quadratic and \(\mathcal O=\mathbb Z+f\mathcal O_K\) with \(f\ge1\), then \(\mathfrak f=f\mathcal O_K\). The integer \(f\) is also called the conductor, whereas \(\mathfrak f\) is the conductor ideal.

For \(K=\mathbb Q(\sqrt{-3})\) and \(\mathcal O=\mathbb Z[\sqrt{-3}]\), this gives
\[
\mathfrak f=2\mathcal O_K=(2,1+\sqrt{-3}).
\]
It is the noninvertible ideal from the [[algebra-commutative/invertible-fractional-ideal|invertibility example]].

## Away from the conductor

For an integral ideal \(I\subseteq\mathcal O\), being prime to the conductor means \(I+\mathfrak f=\mathcal O\). Such nonzero ideals are invertible. Localization outside the primes containing \(\mathfrak f\) removes the difference between \(\mathcal O\) and \(\mathcal O_K\).

## References

1. Andrew Sutherland, [MIT 18.785 Lecture 7](https://math.mit.edu/classes/18.785/2015fa/LectureNotes7.pdf), §7.1, Lemma 7.1, Theorem 7.8, and Corollary 7.10.
