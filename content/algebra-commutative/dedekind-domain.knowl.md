+++
id = "algebra-commutative/dedekind-domain"
title = "Dedekind domain"
kind = "knowl"
summary = "A Noetherian, integrally closed domain of Krull dimension one; equivalently, a nonfield domain with unique factorization of nonzero proper ideals into primes."
aliases = ["dedekind-domain", "Dedekind domain"]
domains = ["algebra-commutative"]
legacy_source_path = "algebra-commutative/dedekind-domain.md"
prerequisites = ["algebra-rings/integral-domain", "algebra-commutative/noetherian-ring", "algebra-commutative/integrally-closed-domain", "algebra-commutative/krull-dimension", "algebra-rings/prime-ideal"]
dependency_heuristic = "semantic-transcript-review-v1"
dependency_review_count = 2
+++

An [[algebra-rings/integral-domain|integral domain]] \(R\) is a **Dedekind domain** if:

1. \(R\) is a [[algebra-commutative/noetherian-ring|Noetherian ring]];
2. \(R\) is an [[algebra-commutative/integrally-closed-domain|integrally closed domain]];
3. \(R\) has [[algebra-commutative/krull-dimension|Krull dimension]] \(1\) (equivalently, \(R\) is not a field and every nonzero [[algebra-rings/prime-ideal|prime ideal]] is maximal).

We use the convention excluding fields. With this convention, every nonzero prime has [[algebra-commutative/height-of-prime|height]] one; some authors allow fields by requiring dimension at most one instead.

## Equivalent and characteristic properties
For a domain \(R\) that is not a field, each of the following characterizes a Dedekind domain:

- Every nonzero proper [[algebra-rings/ideal|ideal]] factors as a product of [[algebra-rings/prime-ideal|prime ideals]], and this factorization is unique up to ordering.
- The ring is Noetherian, and for every nonzero prime ideal \(\mathfrak p\), the localization \(R_\mathfrak p\) (see [[algebra-commutative/localization-at-prime|localization at a prime]]) is a [[algebra-commutative/dvr|discrete valuation ring]]. The Noetherian hypothesis is required in this characterization.
- Every nonzero [[algebra-commutative/fractional-ideal|fractional ideal]] is [[algebra-commutative/invertible-fractional-ideal|invertible]].

## Examples
1. **The integers.**
   \(\mathbb{Z}\) is a Dedekind domain: it is Noetherian, integrally closed in \(\mathbb{Q}\), and has dimension \(1\). (More generally, any PID that is not a field is Dedekind; for instance, any [[algebra-rings/euclidean-domain|Euclidean domain]] that is not a field is a PID by [[algebra-rings/euclidean-implies-pid|Euclidean ⇒ PID]] and hence Dedekind.)

2. **A principal ideal domain of dimension one.**
   For a field \(k\), the [[algebra-rings/polynomial-ring|polynomial ring]] \(k[t]\) is a PID, hence Dedekind.

3. **Rings of integers in number fields.**
   If \(K/\mathbb{Q}\) is a [[algebra-fields-galois/number-field|number field]] and \(\mathcal O_K\) is its [[algebra-fields-galois/ring-of-integers|ring of integers]], then \(\mathcal O_K\) is a Dedekind domain (a key reason prime ideal factorization replaces unique factorization of elements).

## Non-example
- \(k[x,y]\) (two variables over a field \(k\)) is Noetherian and integrally closed, but it has Krull dimension \(2\), so it is not Dedekind.

## References

1. J. S. Milne, *Algebraic Number Theory*, [author’s text](https://www.jmilne.org/math/CourseNotes/ANTc.pdf), §3, Definition 3.3, Proposition 3.6, Theorem 3.7, and Theorem 3.20. The discussion after Proposition 3.6 explains the field convention and why the Noetherian hypothesis cannot be omitted.
