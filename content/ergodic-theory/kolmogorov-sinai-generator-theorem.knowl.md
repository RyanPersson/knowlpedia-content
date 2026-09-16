+++
id = "ergodic-theory/kolmogorov-sinai-generator-theorem"
title = "Kolmogorov–Sinai generator theorem"
kind = "theorem"
summary = "A finite generating partition computes the entire measure-theoretic entropy."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/generating-partition", "ergodic-theory/kolmogorov-sinai-entropy"]
+++

If \(\mathcal P\) is a [[ergodic-theory/generating-partition|finite generating partition]] of an invertible probability-preserving system, then
\[
h_\mu(T)=h_\mu(T,\mathcal P).
\]
The analogous statement holds for a finite one-sided generator of a noninvertible system. This is the **Kolmogorov–Sinai generator theorem**.

## Why it helps

The entropy definition takes a supremum over all finite partitions. A generator contains all measurable information through its iterates, so one partition suffices. For Bernoulli shifts this reduces entropy to the Shannon entropy of one coordinate; for circle doubling, the two half-circle cells give entropy \(\log2\).

## References

1. Karma Dajani, [*Introduction to Ergodic Theory and its Applications to Number Theory*](https://www.staff.science.uu.nl/~kraai101/LectureNotesMM-2.pdf), 2014, Theorem 5.3.1 and Exercise 5.3.2(c).
