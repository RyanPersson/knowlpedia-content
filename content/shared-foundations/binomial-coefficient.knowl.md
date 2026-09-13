+++
id = "shared-foundations/binomial-coefficient"
title = "Binomial coefficient"
kind = "definition"
summary = "The number of k-element subsets of an n-element set and its factorial formula."
aliases = ["binomial coefficients", "n choose k"]
domains = ["shared-foundations"]
section_mode = "progressive"
prerequisites = ["shared-foundations/finite-set", "shared-foundations/factorial", "shared-foundations/rational-numbers"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For integers \(0\le k\le n\), the **binomial coefficient** is
\[
\binom nk=\frac{n!}{k!(n-k)!}.
\]
It counts the \(k\)-element [[shared-foundations/subset|subsets]] of an \(n\)-element set. We set \(\binom nk=0\) when \(k<0\) or \(k>n\), and \(\binom n0=\binom nn=1\).

## Counting argument

There are \(n(n-1)\cdots(n-k+1)\) ordered selections of \(k\) distinct elements. Each subset is represented by exactly \(k!\) orders, giving the factorial formula. Splitting subsets according to whether they contain one distinguished element gives Pascal's identity
\[
\binom{n+1}{k}=\binom n{k-1}+\binom nk.
\]

## A product bound

For \(0\le k\le a\) and \(0\le l\le b\), choosing \(k\) elements from a first block and \(l\) from a second gives only some of the \((k+l)\)-element subsets of the union. Consequently
\[
\binom ak\binom bl\le\binom{a+b}{k+l}.
\]
This bound often controls coefficients in repeated product differentiation.

## References

- [Jonathan Pila, Set Theory, Sections 2–9 and 15](https://www.maths.ox.ac.uk/system/files/attachments/SetTheoryHT18.pdf).
