+++
id = "algebra-commutative/going-down-theorem"
title = "Going-down theorem"
kind = "knowl"
summary = "For an integral extension of domains with integrally closed base, prime chains descend inside a prescribed prime upstairs."
aliases = ["going-down-theorem", "Going-down theorem"]
domains = ["algebra-commutative"]
prerequisites = ["algebra-commutative/integral-extension", "algebra-commutative/integrally-closed-domain"]
dependency_review_count = 1
legacy_source_path = "algebra-commutative/going-down-theorem.md"
+++

**Theorem (Going down).**
Let \(A\subseteq B\) be an [[algebra-commutative/integral-extension|integral extension]] of integral domains, and assume that \(A\) is [[algebra-commutative/integrally-closed-domain|integrally closed]]. Let \(\mathfrak p\subseteq \mathfrak p'\) be prime ideals of \(A\), and let \(\mathfrak q'\in \operatorname{Spec}(B)\) satisfy \(\mathfrak q'\cap A=\mathfrak p'\). Then there exists a prime ideal \(\mathfrak q\) of \(B\) such that
\[
\mathfrak q\subseteq \mathfrak q'
\qquad\text{and}\qquad
\mathfrak q\cap A=\mathfrak p.
\]

Thus, after fixing a prime upstairs over the larger prime downstairs, one can descend along the inclusion of primes.

## Equivalent characterizations

Equivalently, any finite chain of primes in \(A\) can be realized as the contraction of a chain in \(\operatorname{Spec}(B)\) ending at a prescribed prime over the top member.

## Remarks

The integrally closed hypothesis is essential: for general integral extensions, going-down can fail, even though [[algebra-commutative/lying-over-theorem|lying over]] and [[algebra-commutative/going-up-theorem|going up]] always hold.

### Examples
1. **A Dedekind-domain example.**
   The domain \(\mathbb Z\) is [[algebra-commutative/integrally-closed-domain|integrally closed]], and \(\mathbb Z\subset\mathbb Z[i]\) is integral. Take the chain \((0)\subset (5)\) in \(\mathbb Z\) and the prime \(\mathfrak q'=(2+i)\subset \mathbb Z[i]\) lying over \((5)\). Going-down provides a prime \(\mathfrak q\subset (2+i)\) with \(\mathfrak q\cap\mathbb Z=(0)\); necessarily \(\mathfrak q=(0)\).

2. **From \(k[t^2]\) to \(k[t]\).**
   Let \(A=k[t^2]\) and \(B=k[t]\) for a [[algebra-rings/field|field]] \(k\). Since \(A\cong k[s]\) is a PID, it is [[algebra-commutative/integrally-closed-domain|integrally closed]], and \(A\subset B\) is integral. For the chain \((0)\subset (t^2)\) in \(A\) and the prime \((t)\subset B\) lying over \((t^2)\), going-down yields \((0)\subset (t)\) inside \(B\).

3. **A quadratic integral extension of a PID.**
   Let \(A=k[x]\) and \(B=k[x,y]/(y^2-x)\). The ring \(A\) is a PID, hence [[algebra-commutative/integrally-closed-domain|integrally closed]], and \(B\) is integral over \(A\). For the chain \((0)\subset (x)\) in \(A\) and the prime \((x,y)\subset B\) lying over \((x)\), going-down produces a prime inside \((x,y)\) contracting to \((0)\); again this is \((0)\).
