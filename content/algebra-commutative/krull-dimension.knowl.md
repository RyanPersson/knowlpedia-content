+++
id = "algebra-commutative/krull-dimension"
title = "Krull dimension"
kind = "knowl"
summary = "The supremum of lengths of chains of prime ideals in a ring (equivalently, the dimension of its prime spectrum)."
aliases = ["krull-dimension", "Krull dimension"]
domains = ["algebra-commutative"]
prerequisites = ["algebra-rings/commutative-ring"]
dependency_review_count = 1
legacy_source_path = "algebra-commutative/krull-dimension.md"
+++

Let \(R\) be a nonzero [[algebra-rings/commutative-ring|commutative ring]]. The **Krull dimension** of \(R\), denoted \(\dim R\), is the supremum of the integers \(n\ge 0\) for which there exists a strictly increasing chain of prime ideals
\[
\mathfrak p_0 \subsetneq \mathfrak p_1 \subsetneq \cdots \subsetneq \mathfrak p_n
\]
in \(R\). If these lengths are unbounded, then \(\dim R=\infty\).

## Equivalent characterizations

Equivalently, \(\dim R\) is the Krull dimension of the topological space [[algebra-commutative/prime-spectrum|\(\operatorname{Spec}(R)\)]] with its [[algebra-commutative/zariski-topology|Zariski topology]].

## Remarks

The Krull dimension can also be expressed in terms of heights: for each prime \(\mathfrak p\), its [[algebra-commutative/height-of-prime|height]] \(\operatorname{ht}(\mathfrak p)\) is the supremum of lengths of prime chains ending at \(\mathfrak p\), and
\[
\dim R = \sup_{\mathfrak p\in \operatorname{Spec}(R)} \operatorname{ht}(\mathfrak p).
\]
Moreover, \(\operatorname{ht}(\mathfrak p)\) is the dimension of the [[algebra-commutative/localization-at-prime|localization \(R_{\mathfrak p}\)]].

## Examples

1. **Fields and nonzero Artinian rings have dimension \(0\).**
   If \(k\) is a [[algebra-rings/field|field]], its only prime ideal is \((0)\), so \(\dim k=0\). More generally, every prime ideal in a nonzero commutative [[algebra-commutative/artinian-ring|Artinian ring]] is maximal, so no strict chain of prime ideals has positive length.

2. **Dimension \(1\): \(\mathbb Z\) and \(k[x]\).**
   In \(\mathbb Z\) there are chains \((0)\subsetneq(p)\), but no longer chains, so \(\dim\mathbb Z=1\). Similarly, for a field \(k\), the ring \(k[x]\) has chains \((0)\subsetneq(f)\), with \(f\) irreducible, but no longer ones.

3. **Polynomial rings.**
   For a field \(k\), the polynomial ring \(k[x_1,\dots,x_n]\) has Krull dimension \(n\). For instance, in \(k[x,y]\),
   \[
   (0)\subsetneq (x)\subsetneq (x,y),
   \]
   has length \(2\), and no longer prime chain exists.
