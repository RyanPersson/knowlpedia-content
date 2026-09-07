+++
id = "shared-foundations/integers"
title = "Integers"
kind = "knowl"
summary = "The set of whole numbers, positive, negative, and zero."
aliases = ["integers"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/integers.md"
prerequisites = ["shared-foundations/natural-numbers", "shared-foundations/cartesian-product", "shared-foundations/quotient-set"]
dependency_heuristic = "axiomatic-dependency-review-v1"
dependency_review_count = 2
+++

The **integers** are the [[shared-foundations/quotient-set|quotient set]]
\[
\mathbb Z=(\mathbb N\times\mathbb N)/{\sim},
\qquad (a,b)\sim(c,d)\ \Longleftrightarrow\ a+d=b+c,
\]
where \(\mathbb N\) denotes the [[shared-foundations/natural-numbers|natural numbers]]. The class \([a,b]\) represents the formal difference \(a-b\).

## Arithmetic and notation

Addition and multiplication are defined by
\[
[a,b]+[c,d]=[a+c,b+d],\qquad
[a,b][c,d]=[ac+bd,ad+bc].
\]
The zero and unit are \([0,0]\) and \([1,0]\), and \(-[a,b]=[b,a]\). These operations are independent of the representatives. Identifying \(n\in\mathbb N\) with \([n,0]\) gives the usual notation \(\mathbb Z=\{\ldots,-2,-1,0,1,2,\ldots\}\).

## Remarks

The integers extend the [[shared-foundations/natural-numbers|natural numbers]] by including additive inverses, and they sit inside the [[shared-foundations/rational-numbers|rational numbers]] via the identification \(n = n/1\). With the usual \(\le\), they form a [[shared-foundations/total-order|totally ordered]] set.

## Examples

- \(-3\), \(0\), and \(14\) are integers.
- The equation \(x+3=0\) has the integer solution \(x=-3\).
