---
title: "Translation-invariant interaction"
description: "An interaction on the lattice whose local energy terms are unchanged under lattice shifts."
---

Let \(S\) be a set of spin values, and let \(\Phi=\{\Phi_A\}\) be an interaction on \(\mathbb{Z}^d\) (as in {{< knowl id="finite-range-interaction-lattice" >}}).

For a vector \(a\in\mathbb{Z}^d\) and a finite set \(A\subset\mathbb{Z}^d\), define the translated set
\[
A+a := \{x+a : x\in A\}.
\]
If \(\eta\in S^A\) is a spin assignment on \(A\), define its translate \(\eta^{a}\in S^{A+a}\) by
\[
\eta^{a}(x+a)=\eta(x)\quad\text{for all }x\in A.
\]

**Definition.** The interaction \(\Phi\) is **translation invariant** if for every finite \(A\subset\mathbb{Z}^d\) and every \(a\in\mathbb{Z}^d\),
\[
\Phi_{A+a}(\eta^{a})=\Phi_A(\eta)\quad\text{for all }\eta\in S^A.
\]

Intuitively, translation invariance means that the interaction does not depend on absolute position in the lattice; it depends only on relative patterns of spins.

**Example.** An Ising-type nearest-neighbor coupling with the same coupling constant on every edge (and the same external field at every site, if present) is translation invariant.

Translation invariance can be broken by spatially varying couplings/fields or by imposing boundary conditions on a finite region (see {{< knowl id="boundary-finite-region" >}}).
