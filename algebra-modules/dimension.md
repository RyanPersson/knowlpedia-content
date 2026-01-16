---
title: "Dimension of a vector space"
description: "The cardinality of any basis, measuring the 'size' of a vector space."
---

The **dimension** of a {{< knowl id="vector-space" section="linear-algebra" text="vector space" >}} \(V\) is the cardinality of any {{< knowl id="basis-module" text="basis" >}} of \(V\), denoted \(\dim V\).

## Well-definedness
All bases of a vector space have the same cardinality (this requires proof, using {{< knowl id="linear-independence" text="linear independence" >}}). Thus dimension is well-defined.

## Properties
- \(\dim \{0\} = 0\) (the zero space has the empty basis).
- \(\dim \mathbb{R}^n = n\) (standard basis has \(n\) vectors).
- A vector space is finite-dimensional iff it has a finite spanning set.
- Subspaces satisfy \(\dim W \leq \dim V\), with equality iff \(W = V\).

## Dimension formulas
- **Rank-nullity**: For a {{< knowl id="linear-map" section="linear-algebra" text="linear map" >}} \(T: V \to W\), \(\dim V = \dim \ker T + \dim \text{im}\, T\).
- **Sum formula**: \(\dim(U + W) = \dim U + \dim W - \dim(U \cap W)\).
- **Quotient**: \(\dim(V/W) = \dim V - \dim W\).

## Infinite dimension
Spaces like \(\mathbb{R}[x]\) (polynomials) or \(C([0,1])\) (continuous functions) are infinite-dimensional: no finite set spans them.
