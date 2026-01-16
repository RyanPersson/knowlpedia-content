---
title: "Tangent Bundle"
description: "The manifold formed by gluing together all tangent spaces of a smooth manifold."
---
Let \(M\) be a {{< knowl id="smooth-manifold" section="fiber-bundles" text="smooth manifold" >}} of dimension \(n\). The **tangent bundle** of \(M\) is the space of all tangent vectors on \(M\) organized into a single geometric object.

## Construction
Define the set
$$
TM := \bigsqcup_{p\in M} T_pM,
$$
the disjoint union of the {{< knowl id="tangent-space" section="differential-geometry" text="tangent spaces" >}}. There is a natural projection map
$$
\pi: TM \to M,\qquad \pi(v)=p \ \text{if } v\in T_pM.
$$
The pair \((TM,\pi)\) is a vector bundle over \(M\) with fiber \(\pi^{-1}(p)=T_pM\).

## Smooth structure
A smooth atlas on \(M\) induces a smooth atlas on \(TM\): if \((U,x)\) is a chart on \(M\) with \(x=(x^1,\dots,x^n)\), then \(TM|_U := \pi^{-1}(U)\) is identified with \(x(U)\times \mathbb{R}^n\) via
$$
v \in T_pM \ \longmapsto\ \big(x(p), (v^1,\dots,v^n)\big),
$$
where \(v=\sum_i v^i \left.\frac{\partial}{\partial x^i}\right|_p\). With this structure, \(TM\) is a smooth manifold of dimension \(2n\), and \(\pi\) is smooth.

## Key properties
- Each fiber \(T_pM\) is a {{< knowl id="vector-space" section="linear-algebra" text="vector space" >}} varying smoothly with \(p\).
- Smooth maps \(f:M\to N\) induce maps \(df:TM\to TN\) on bundles via the {{< knowl id="differential-of-a-smooth-map" section="fiber-bundles" text="differential" >}}.

## Example
For \(M=\mathbb{R}^n\), one has a global trivialization
$$
T\mathbb{R}^n \cong \mathbb{R}^n \times \mathbb{R}^n,
$$
sending \((p,v)\) to the tangent vector \(v\) based at \(p\).
