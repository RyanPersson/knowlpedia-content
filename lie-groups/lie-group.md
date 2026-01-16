---
title: "Lie Group"
description: "A smooth manifold equipped with a group structure for which multiplication and inversion are smooth."
---

A **Lie group** is a {{< knowl id="smooth-manifold" section="fiber-bundles" text="smooth manifold" >}} \(G\) together with a group structure such that the maps
$$
\mu: G \times G \to G,\quad (g,h)\mapsto gh,
\qquad
\iota: G \to G,\quad g\mapsto g^{-1}
$$
are {{< knowl id="smooth-map" section="fiber-bundles" text="smooth maps" >}}.

Equivalently, a Lie group is a {{< knowl id="topological-group" section="topology" text="topological group" >}} whose underlying space is a smooth manifold and whose structure maps are smooth.

## Basic examples
- \((\mathbb{R}^n,+)\) and tori \(T^n=\mathbb{R}^n/\mathbb{Z}^n\) (see {{< knowl id="abelian-lie-group" text="abelian Lie group" >}}).
- Matrix groups such as \(\operatorname{GL}(n,\mathbb{R})\), \(\operatorname{SO}(n)\), \(\operatorname{SU}(n)\).
- {{< knowl id="connected-lie-group" text="connected Lie groups" >}} and {{< knowl id="compact-lie-group" text="compact Lie groups" >}} are important special classes.

## Infinitesimal structure
Every Lie group \(G\) has an associated {{< knowl id="lie-algebra-of-a-lie-group" text="Lie algebra" >}}
\(\mathfrak{g}=T_eG\), the {{< knowl id="tangent-space" section="differential-geometry" text="tangent space" >}} at the identity, with a canonical {{< knowl id="lie-bracket" text="Lie bracket" >}}.

The {{< knowl id="exponential-map-lie-group" text="exponential map" >}} \(\exp:\mathfrak{g}\to G\) relates \(\mathfrak{g}\) to {{< knowl id="one-parameter-subgroup" text="one-parameter subgroups" >}}, and the {{< knowl id="lie-correspondence" text="Lie correspondence" >}} explains how much of \(G\) is determined by \(\mathfrak{g}\).
