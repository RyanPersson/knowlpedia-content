---
title: "Linear independence"
description: "A set of vectors is linearly independent if no nontrivial linear combination equals zero."
---

A set of vectors \(\{v_1, \ldots, v_n\}\) in a {{< knowl id="module" text="module" >}} or {{< knowl id="vector-space" section="linear-algebra" text="vector space" >}} is **linearly independent** if the only solution to
$$
c_1 v_1 + c_2 v_2 + \cdots + c_n v_n = 0
$$
is \(c_1 = c_2 = \cdots = c_n = 0\).

Otherwise, the set is **linearly dependent**.

## Characterizations
For a finite set \(\{v_1, \ldots, v_n\}\) in a vector space:
- No \(v_i\) is a {{< knowl id="linear-combination" section="convex-analysis" text="linear combination" >}} of the others.
- Removing any vector strictly decreases the span.
- The vectors form a {{< knowl id="basis-module" text="basis" >}} of their span.

## Properties
- Any subset of a linearly independent set is linearly independent.
- In a finite-dimensional space of dimension \(n\), at most \(n\) vectors can be linearly independent.
- The columns of a {{< knowl id="matrix" section="linear-algebra" text="matrix" >}} are linearly independent iff the matrix has full column rank.

## Module warning
Over rings (not fields), linear independence behaves differently. For example, \(\{2, 3\}\) is linearly dependent in \(\mathbb{Z}\) since \(3 \cdot 2 + (-2) \cdot 3 = 0\).
