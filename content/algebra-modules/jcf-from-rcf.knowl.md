+++
id = "algebra-modules/jcf-from-rcf"
title = "Jordan canonical form from rational canonical form"
kind = "knowl"
summary = "When the relevant polynomials split, rational canonical form refines to Jordan form."
aliases = ["jcf-from-rcf", "Jordan canonical form from rational canonical form"]
domains = ["algebra-modules"]
prerequisites = ["algebra-modules/rcf-from-structure-theorem", "algebra-modules/jordan-canonical-form-theorem", "linear-algebra/characteristic-polynomial", "linear-algebra/linear-map", "linear-algebra/vector-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "algebra-modules/jcf-from-rcf.md"
+++

**Jordan canonical form from rational canonical form**: Let \(V\) be a finite-dimensional vector space over a field \(F\), and let \(T:V\to V\) be linear. Assume the characteristic polynomial of \(T\) splits over \(F\). Then there exists a basis of \(V\) for which the matrix of \(T\) is in Jordan canonical form.

This follows by refining the invariant-factor decomposition in [[algebra-modules/rcf-from-structure-theorem|rational canonical form from the structure theorem]] into primary factors, yielding the [[algebra-modules/jordan-canonical-form-theorem|Jordan canonical form theorem]]; the Jordan blocks are organized by the roots of the [[linear-algebra/characteristic-polynomial|characteristic polynomial]].

## Examples

If \(F\) is algebraically closed, every characteristic polynomial over \(F\) splits, so the splitting hypothesis is automatic.
