---
title: "Smooth Manifold"
description: "A topological manifold equipped with an atlas whose transition maps are smooth."
---

A **smooth manifold** is a topological space that locally looks like Euclidean space and whose coordinate changes are differentiable to all orders.

## Setup
Let \(M\) be a {{< knowl id="topological-space" section="topology" text="topological space" >}}. A **chart** of dimension \(n\) is a pair \((U,\varphi)\) where \(U \subseteq M\) is an {{< knowl id="open-set" section="topology" text="open set" >}} and \(\varphi:U\to \varphi(U)\subseteq \mathbb{R}^n\) is a homeomorphism.

An **atlas** is a collection of charts \(\{(U_\alpha,\varphi_\alpha)\}\) whose domains cover \(M\).

## Smoothness condition
An atlas is **smooth** (or \(C^\infty\)) if for any overlapping charts the transition map
$$
\varphi_\beta\circ \varphi_\alpha^{-1}:\ \varphi_\alpha(U_\alpha\cap U_\beta)\to \varphi_\beta(U_\alpha\cap U_\beta)
$$
is a smooth map between open subsets of \(\mathbb{R}^n\) (in the usual multivariable calculus sense).

A **smooth manifold** is a pair \((M,\mathcal{A})\) where \(M\) is a topological manifold (typically assumed Hausdorff and second countable; see {{< knowl id="hausdorff-space" section="topology" text="Hausdorff" >}}) and \(\mathcal{A}\) is a smooth atlas. Two atlases are considered equivalent if their union is still smooth; each equivalence class has a unique **maximal** smooth atlas.

## Key properties
- The integer \(n\) is the **dimension** of \(M\), written \(\dim M=n\).
- A smooth structure lets you define smooth functions \(f:M\to \mathbb{R}\), smooth maps between manifolds, and the {{< knowl id="tangent-space" text="tangent space" >}} at each point.

## Examples
- \(\mathbb{R}^n\) with the single global chart \((\mathbb{R}^n,\mathrm{id})\).
- Any open subset \(U\subseteq \mathbb{R}^n\) (with the inherited topology) is a smooth manifold.
- The sphere \(S^n\) admits smooth atlases (e.g., via stereographic projection).
