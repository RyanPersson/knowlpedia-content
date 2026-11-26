+++
id = "proofs/grh/upper-seesaw/lattice-splitting-and-scalings"
title = "Lattices that split along X at a place"
kind = "lemma"
summary = "If the lattice of a finite point splits along X at a place w different from its conjugate, the integral scalings of X supported at w and its conjugate preserve the lattice."
aliases = ["lattice splits at a place", "LatticeSplitsAt"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Grading.LatticeSplitsAt", "New.Grading.LatticeSplitsAt.conj", "New.Grading.inclXFin_scalarFin_mulVec", "New.Grading.LatticeSplitsAt.idem_smul_sub_stringProj_mem", "New.Grading.LatticeSplitsAt.conj_scalarFin_mem"]
lean_files = ["src/New/UpperBound/Seesaw/Sandwich.lean"]
proof_status = "full"
+++

Let \(V\) be a [[?lean:New.Space|hermitian space with a point]] over a [[?c:CM field|CM field]]
\(E\) with a [[?lean:New.Grading|grading]] \(Y\) into \(X\) and a string spanning \(X^{\perp}\),
and let \(\operatorname{pr}\) be the projection to \(X^{\perp}\) along \(X\). For a point \(x\) of
the [[?lean:New.Gf|finite adelic unitary group]] \(G_f\), let
\(\Lambda_x=x_f x\,\widehat{\mathcal{O}}^{\iota}\) be [[?lean:New.Space.lattice|its lattice]],
\(\Lambda_x^{-}=\Lambda_x\cap X^{\perp}\) and \(\Lambda_x^{+}=\operatorname{pr}(\Lambda_x)\).

**Definition.** The lattice of \(x\) **splits along \(X\) at the [[algebra-fields-galois/place-of-global-field|finite place]] \(w\)** if the
\(w\)-component of \(\Lambda_x^{+}\) lies in \(\Lambda_x^{-}\):
\(1_w\cdot\Lambda_x^{+}\subseteq\Lambda_x^{-}\), where \(1_w\in\mathbb{A}_{E,f}\) is the idempotent
that is \(1\) at \(w\) and \(0\) elsewhere.

**Lemma.** Suppose the lattice of \(x\) splits along \(X\) at \(w\).

1. It splits at the conjugate place \(\bar w\).
2. For \(y\in\Lambda_x\), the vector \(1_w\,(y-\operatorname{pr}y)\) lies in \(\Lambda_x\).
3. Suppose \(\bar w\ne w\). Let \(z\in\mathbb{A}_{E,f}\) with \(z\bar z=1\), \(z\) integral, and
   \(z_{u}=1\) at all places \(u\notin\{w,\bar w\}\). Let \(\sigma_z\in G_f\) be the element that
   scales \(X\) by \(z\) and fixes \(X^{\perp}\) (in rational coordinates). Then
   \(x^{-1}\sigma_z x\) lies in the maximal compact subgroup at \(w\): it stabilises
   \(\widehat{\mathcal{O}}^{\iota}\) and is trivial at all places other than \(w,\bar w\).

## Proof

(1) Duality between \(\Lambda_x^{+}\) and \(\Lambda_x^{-}\) under the hermitian form gives: if
\(c\,\Lambda_x^{+}\subseteq\Lambda_x^{-}\) for a finite adele \(c\), then
\(\bar c\,\Lambda_x^{+}\subseteq\Lambda_x^{-}\)
([[?lean:New.Grading.star_smul_latticePlus_le_latticeMinus|duality for one lattice]]). Apply it to
\(c=1_w\), whose conjugate is \(1_{\bar w}\).

(2) \(1_w\operatorname{pr}(y)\in 1_w\Lambda_x^{+}\subseteq\Lambda_x^{-}\subseteq\Lambda_x\), and
\(1_wy\in\Lambda_x\); subtract.

(3) In rational coordinates \(\sigma_z y=y+(z-1)(y-\operatorname{pr}y)\). Since \(z-1\) is supported
at \(w\) and \(\bar w\), \(z-1=(z-1)(1_w+1_{\bar w})\). For \(y\in\Lambda_x\), by (1) and (2) both
\(1_w(y-\operatorname{pr}y)\) and \(1_{\bar w}(y-\operatorname{pr}y)\) lie in \(\Lambda_x\), and
\(z-1\) is integral, so \(\sigma_zy\in\Lambda_x\). The same holds for \(\sigma_z^{-1}=\sigma_{\bar z}\).
So \(\sigma_z\) stabilises \(\Lambda_x\), i.e. \(x^{-1}\sigma_zx\) stabilises the standard lattice.
At a place \(u\notin\{w,\bar w\}\), \(z_u=1\) and \(\sigma_z\) is the identity there. \(\blacksquare\)

## References

1. Lean: `New.Grading.LatticeSplitsAt`, `New.Grading.LatticeSplitsAt.conj_scalarFin_mem` in `src/New/UpperBound/Seesaw/Sandwich.lean`.
