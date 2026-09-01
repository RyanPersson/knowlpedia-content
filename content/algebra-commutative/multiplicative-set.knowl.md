+++
id = "algebra-commutative/multiplicative-set"
title = "Multiplicative set"
kind = "knowl"
summary = "A subset of a ring closed under multiplication and containing 1, used to form localizations."
aliases = ["multiplicative-set", "Multiplicative set"]
domains = ["algebra-commutative"]
prerequisites = ["algebra-rings/commutative-ring", "algebra-commutative/localization-ring", "algebra-commutative/localization-at-prime"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "algebra-commutative/multiplicative-set.md"
+++

Let \(R\) be a [[algebra-rings/commutative-ring|commutative ring]]. A subset \(S\subseteq R\) is a **multiplicative set** if

1. \(1\in S\), and
2. \(s,t\in S\) implies \(st\in S\).

The definition permits \(0\in S\). In that case the [[algebra-commutative/localization-ring|localization]] \(S^{-1}R\) is the zero ring.

A key source of multiplicative sets is complements of primes: if \(\mathfrak p\subset R\) is prime, then \(R\setminus \mathfrak p\) is multiplicative, and this choice produces the [[algebra-commutative/localization-at-prime|localization at a prime]].

## Examples

1. **Powers of an element.** For \(f\in R\), the set
   \[
   S=\{1,f,f^2,f^3,\dots\}
   \]
   is multiplicative. (If \(f\) is nilpotent, then \(0\in S\) and the corresponding localization collapses to the zero ring.)

2. **Complement of a prime ideal.** If \(\mathfrak p\) is a prime ideal of \(R\), then
   \[
   S=R\setminus \mathfrak p
   \]
   is multiplicative (primality ensures \(st\notin\mathfrak p\) whenever \(s,t\notin\mathfrak p\)). Localizing at this \(S\) gives \(R_{\mathfrak p}\).

3. **Inverting a prime number in \(\mathbb Z\).** In \(R=\mathbb Z\), the subset \(S=\{1,p,p^2,\dots\}\) (for a prime \(p\)) is multiplicative. The localization \(S^{-1}\mathbb Z\) is the subring of \(\mathbb Q\) consisting of fractions whose denominator is a power of \(p\).
