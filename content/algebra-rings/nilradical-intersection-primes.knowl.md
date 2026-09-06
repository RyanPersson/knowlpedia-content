+++
id = "algebra-rings/nilradical-intersection-primes"
title = "Nilradical equals intersection of prime ideals"
kind = "knowl"
summary = "In a commutative ring, the nilradical is the intersection of all prime ideals."
aliases = ["nilradical-intersection-primes", "Nilradical equals intersection of prime ideals"]
domains = ["algebra-rings"]
prerequisites = ["algebra-rings/commutative-ring", "algebra-rings/nilradical", "algebra-rings/nilpotent-element", "algebra-rings/prime-ideal", "algebra-rings/radical-of-ideal"]
dependency_review_count = 1
legacy_source_path = "algebra-rings/nilradical-intersection-primes.md"
+++

**Nilradical theorem.** Let \(R\) be a commutative ring. Then
\[
\mathrm{Nil}(R)=\bigcap_{\mathfrak p\in \mathrm{Spec}(R)} \mathfrak p,
\]
Thus an element is nilpotent if and only if it lies in every prime ideal. Equivalently, \(\mathrm{Nil}(R)=\sqrt{(0)}\).

## Remarks

The [[algebra-rings/nilradical|nilradical]] is the ideal of all [[algebra-rings/nilpotent-element|nilpotent elements]]. Since it is the [[algebra-rings/radical-of-ideal|radical]] of \((0)\), the quotient \(R/\mathrm{Nil}(R)\) is [[algebra-rings/reduced-ring|reduced]].
