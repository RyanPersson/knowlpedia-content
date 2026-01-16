---
title: "Extremal Gibbs measures are ergodic (pure phases)"
description: "Extremality in the convex set of Gibbs measures is equivalent to trivial tail σ-algebra; with translation invariance, this implies translation ergodicity."
---

Fix a lattice interaction/specification and let $\mathcal{G}$ denote the convex set of all {{< knowl id="infinite-volume-gibbs-measure" section="stat-mech-lattice" text="infinite-volume Gibbs measures" >}} consistent with it.

Let $\mathcal{T}$ be the tail $\sigma$-algebra,
$$
\mathcal{T}=\bigcap_{\Lambda\Subset\mathbb{Z}^d}\mathcal{F}_{\Lambda^c},
$$
i.e. events that depend only on spins “arbitrarily far away”.

## Statement
For $\mu\in\mathcal{G}$, the following are equivalent:

1. $\mu$ is {{< knowl id="extremal-gibbs-measure" section="stat-mech-lattice" text="extremal" >}} in $\mathcal{G}$ (it cannot be written as a nontrivial convex combination of two distinct measures in $\mathcal{G}$).

2. The tail $\sigma$-algebra is $\mu$-trivial: for every $A\in\mathcal{T}$, one has $\mu(A)\in\{0,1\}$.

If, in addition, the interaction/specification is translation-covariant and $\mu$ is translation invariant, then these conditions imply (and in common settings are equivalent to) translation ergodicity: every translation-invariant event has probability $0$ or $1$ under $\mu$.

## Key hypotheses
- $\mathcal{G}$ is the convex set of all DLR-consistent {{< knowl id="infinite-volume-gibbs-measure" section="stat-mech-lattice" text="Gibbs measures" >}} for a fixed specification.
- (For the translation-ergodic refinement) translation covariance of the specification and translation invariance of $\mu$.

## Conclusions
- Extremal Gibbs measures are “pure phases”: they have no nontrivial decomposition into distinct Gibbs components.
- Tail-triviality provides a practical criterion for purity, often used in phase-transition analysis (compare {{< knowl id="phase-transition-gibbs" section="stat-mech-lattice" text="phase transition" >}} and coexistence phenomena).

## Proof idea / significance
If the tail $\sigma$-algebra is nontrivial, one can condition $\mu$ on a tail event $A\in\mathcal{T}$ with $0<\mu(A)<1$ and obtain two distinct conditional measures that are still DLR-consistent; this yields a nontrivial convex decomposition of $\mu$, so $\mu$ is not extremal. Conversely, if $\mu$ admits a nontrivial convex decomposition, the component label can be realized as a tail-measurable random variable, producing a nontrivial tail event. This links convex geometry (extreme points) to probabilistic ergodic/tail behavior.
