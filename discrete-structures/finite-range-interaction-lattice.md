---
title: "Finite-range interaction on a lattice"
description: "An interaction in which local energy terms depend only on spins within a bounded distance."
---

Fix a set of spin values \(S\). A **configuration** is a {{< knowl id="function" section="shared-foundations" >}} \(\sigma:\mathbb{Z}^d\to S\).

An **interaction** (also called a potential) is a family
\[
\Phi=\{\Phi_A\}_{A\subset \mathbb{Z}^d,\ |A|<\infty},
\]
where each \(\Phi_A\) is a function \(\Phi_A:S^A\to \mathbb{R}\) that depends only on the spins in the finite set \(A\).

Given a finite region \(\Lambda\subset\mathbb{Z}^d\), the associated finite-volume Hamiltonian is typically written as
\[
H_\Lambda^\Phi(\sigma)=\sum_{\varnothing\neq A\subseteq \Lambda}\Phi_A(\sigma|_A),
\]
where \(\sigma|_A\) is the restriction of \(\sigma\) to \(A\).

**Finite range.** The interaction \(\Phi\) is **finite range** with range \(R\) if
\[
\Phi_A \equiv 0 \quad\text{whenever}\quad \operatorname{diam}(A)>R,
\]
where the diameter is computed using the nearest-neighbor graph distance on \(\mathbb{Z}^d\):
\[
\operatorname{diam}(A):=\max_{x,y\in A}\operatorname{dist}(x,y),
\]
and \(\operatorname{dist}(x,y)\) is the minimal number of {{< knowl id="nearest-neighbor-zd" >}} steps needed to go from \(x\) to \(y\).

**Example (nearest-neighbor interactions).** A nearest-neighbor pair interaction only uses terms supported on single sites and on pairs \(\{x,y\}\) with \(x\sim y\); this is a finite-range interaction (with a small range, depending on the chosen distance convention).
