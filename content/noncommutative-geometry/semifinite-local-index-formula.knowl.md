+++
id = "noncommutative-geometry/semifinite-local-index-formula"
title = "Semifinite local index formula"
kind = "theorem"
summary = "A residue-cocycle formula computing trace-valued index pairings for regular summable spectral triples in semifinite von Neumann algebras."
aliases = ["semifinite residue cocycle", "local index formula relative to tau"]
domains = ["noncommutative-geometry", "operator-algebras"]
prerequisites = ["noncommutative-geometry/tau-summable-spectral-triple", "noncommutative-geometry/semifinite-index-pairing", "noncommutative-geometry/spectral-flow"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((\mathcal A,\mathcal N,D,\tau)\) be a regular, finitely [[noncommutative-geometry/tau-summable-spectral-triple|tau-summable semifinite spectral triple]] with isolated dimension spectrum and the analytic-continuation hypotheses of Carey–Phillips–Rennie–Sukochev. The **semifinite local index formula** represents its Chern character by a finite residue cocycle built from \(\tau\), elements \(a_j\), commutators \([D,a_j]\), and iterated commutators with \(D^2\). Pairing this cocycle with \(K_1(\mathcal A)\) in odd parity or \(K_0(\mathcal A)\) in even parity equals the [[noncommutative-geometry/semifinite-index-pairing|Breuer-index pairing]]. In odd parity it also computes semifinite [[noncommutative-geometry/spectral-flow|spectral flow]] from \(D\) to \(uDu^*\).

## Residue structure

The formula replaces ordinary traces in the [[noncommutative-geometry/local-index-formula|Connes–Moscovici local index formula]] by the chosen [[operator-algebras/faithful-normal-semifinite-trace|faithful normal semifinite trace]] \(\tau\). Its cochains are finite [[convex-analysis/linear-combination|linear combinations]] of residues of zeta functions having the schematic form
\[
z\longmapsto
\tau\!\left(
a_0[D,a_1]^{(k_1)}\cdots[D,a_m]^{(k_m)}
(1+D^2)^{-z}
\right),
\]
where \(T^{(k)}\) denotes the \(k\)-fold commutator with \(D^2\). Universal coefficients and residue points depend on parity, degree, and normalization; the schematic expression is not a substitute for the full formulas.

Part I derives the odd formula through spectral flow. Part II proves the even formula and a generalized McKean–Singer identity.

## Meaning and consequences

The bounded-transform pairing is defined globally through a Breuer–Fredholm compression. The residue cocycle computes the same class using finitely many commutators and spectral asymptotics. This makes index pairings accessible to heat-kernel, pseudodifferential, and zeta-function calculations even when \(\mathcal N\) has nontrivial center and the index is real-valued rather than integral.

When \(\mathcal N=B(H)\) and \(\tau\) is the ordinary trace, the formula specializes to the usual local index formula under the corresponding hypotheses. The extension is substantive: tau-compactness and tau-summability can hold even when the relevant operators are not compact or summable in the ordinary Hilbert-space sense.

## Conventions and scope

**Warning.** Regularity and tau-summability alone do not guarantee the meromorphic continuation needed to take residues. An isolated or discrete dimension-spectrum condition is an additional hypothesis. Multiple poles require higher residue functionals, and nonunital triples require local hypotheses and often a unitization.

The theorem identifies cyclic-cohomology classes or their pairings; differently normalized residue representatives may differ by coboundaries. Sign conventions for spectral flow and the [[noncommutative-geometry/odd-index-pairing|odd index pairing]] must be coordinated.

## References

1. A. L. Carey, J. Phillips, A. Rennie, and F. A. Sukochev, “The Local Index Formula in Semifinite von Neumann Algebras I: Spectral Flow,” *Advances in Mathematics* 202 (2006), 451–516. [Stable preprint](https://arxiv.org/abs/math/0411019). Relevant: Theorem 4.1 and §§7–8, the odd residue cocycle and spectral-flow pairing.
2. A. L. Carey, J. Phillips, A. Rennie, and F. A. Sukochev, “The Local Index Formula in Semifinite von Neumann Algebras II: The Even Case,” *Advances in Mathematics* 202 (2006), 517–554. [DOI record](https://doi.org/10.1016/j.aim.2005.03.010). Relevant: §§4–6, the even residue cocycle and generalized McKean–Singer formula.
