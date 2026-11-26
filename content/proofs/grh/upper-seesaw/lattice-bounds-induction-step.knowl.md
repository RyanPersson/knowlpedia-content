+++
id = "proofs/grh/upper-seesaw/lattice-bounds-induction-step"
title = "Lattice bounds along the tower: the induction step and the dichotomy"
kind = "proposition"
summary = "The upper bound on one graded space gives the lower bound on the next; a lower bound gives both bounds unless the string is odd and the lattice splits at a place above N."
aliases = ["sandwich of lattices", "bounds or splitting"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Grading.smul_latticeMinus_le_of_map_latticePlus", "New.Grading.latticeSplitsAt_of_generates", "New.Grading.SpansLattice.hasLatticeBounds_or_latticeSplitsAt", "New.Grading.HasBoundedOrbit.of_forall", "New.Grading.SpansLattice.hasBoundedOrbit_zero"]
lean_files = ["src/New/UpperBound/Seesaw/Sandwich.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/upper-seesaw/lattice-splitting-and-scalings|lattices that split]]:
for a finite point \(x\), \(\Lambda_x^{\pm}\) are the projection to and the intersection with the
span of the string; \(\Lambda^{\pm}=\Lambda_1^{\pm}\). For a [[?c:Idele group|finite idele]] \(q\) and \(k\ge0\) the
point \(x\) [[?lean:New.Grading.HasLatticeBounds|has the lattice bounds]] \((q,k)\) if
\(\bar q^{\,k}\Lambda^{-}\subseteq\Lambda_x^{-}\) and \(q^{k}\Lambda_x^{-}\subseteq\Lambda^{-}\).

**Proposition.**

1. (**Step to the next space.**) Let \(V,V'\) have gradings \(Y,Y'\) with strings of \(s\) and
   \(s-1\) vectors, with [[?lean:New.Grading.stringMapFin|shift]] \(\operatorname{sh}\), and let
   \(M_{x'}^{-}\) denote the lattices \(\Lambda^{-}\) of \(V'\). Let \(a,q\) be finite ideles,
   \(x\in G_f(V)\), \(x'\in G_f(V')\). If
   \(\operatorname{sh}(\Lambda^{+})=aM^{-}_1\),
   \((\bar q/a)\operatorname{sh}(\Lambda_x^{+})\subseteq M^{-}_{x'}\) and
   \(q^{k}\Lambda_x^{-}\subseteq\Lambda^{-}\), then \(\bar q^{\,k+1}M_1^{-}\subseteq M_{x'}^{-}\).
2. (**Dichotomy.**) Let \(Y\) grade \(V\) by \(X\sqcup\{y_0\}\) and a string of \(s\) vectors and
   [[proofs/grh/upper-seesaw/graded-lattice-basis|span the lattice]] of \((a,\pi,u)\); let
   \((P,N,\pi)\) be a [[proofs/grh/upper-seesaw/split-squarefree-factorisation|split squarefree
   factorisation]] and \(q\) a finite idele that is a unit at the places of \(P\cup\bar P\). If
   \(\bar q^{\,k}\Lambda^{-}\subseteq\Lambda_x^{-}\), then either \(x\) has the lattice bounds
   \((q,k)\), or \(s\) is odd and the lattice of \(x\) splits along \(X\sqcup\{y_0\}\) at some
   \(w\in P\).
3. (**Orbits.**) Assume \(E\) contains a primitive \(5040\)-th [[?c:Root of unity|root of unity]]. If every translate
   \(rx\) by the [[?lean:New.Grading.besselFin|finite Bessel subgroup]] whose lattice is graded
   has the lattice bounds \((q,k)\), then the orbit of \(x\)
   [[?lean:New.Grading.HasBoundedOrbit|is bounded]] for \((q,k)\) (some translate in the Bessel
   orbit has a graded lattice with these bounds). If \(Y\) spans the lattice of \((a,\pi,u)\) and
   some translate \(rx\) stabilises the standard lattice, the orbit of \(x\) is bounded for
   \((q,0)\).

## Proof

(1) Let \(y\in M_1^{-}\). Choose \(z\in\Lambda^{+}\) with \(\operatorname{sh}z=ay\). The upper bound
\(q^{k}\Lambda_x^{-}\subseteq\Lambda^{-}\) dualises to \(\bar q^{\,k}\Lambda^{+}\subseteq\Lambda_x^{+}\)
([[?lean:New.Grading.star_smul_latticePlus_le|duality]]: an inclusion \(c\,\Lambda_x^{-}\subseteq\Lambda_{x'}^{-}\) gives \(\bar c\,\Lambda_{x'}^{+}\subseteq\Lambda_x^{+}\)). So \(\bar q^{\,k}z\in\Lambda_x^{+}\) and
\[
\bar q^{\,k+1}y=(\bar q/a)\operatorname{sh}(\bar q^{\,k}z)\in M_{x'}^{-}.
\]

(2) The lower bound dualises to \(q^{k}\Lambda_x^{+}\subseteq\Lambda^{+}\) (same duality). Suppose
the upper bound fails: there is \(y\in\Lambda_x^{-}\) with \(q^{k}y\notin\Lambda^{-}\). Since
\(\Lambda_x^{-}\subseteq\Lambda_x^{+}\), \(q^{k}y\in\Lambda^{+}\setminus\Lambda^{-}\). By
[[proofs/grh/upper-seesaw/generator-of-plus-over-minus|the generator lemma]], \(s\) is odd and
\(q^{k}y\) generates \(\Lambda^{+}\) over \(\Lambda^{-}\) at some \(w\in P\cup\bar P\). We show the
lattice of \(x\) splits at \(w\). Let \(z\in\Lambda_x^{+}\); then \(q^{k}z\in\Lambda^{+}\), so
\(1_w(q^{k}z-\gamma q^{k}y)\in\Lambda^{-}\) for some integral \(\gamma\). Multiply by \(\bar q^{\,k}\)
(lower bound): \(\bar q^{\,k}1_w(q^kz-\gamma q^ky)\in\Lambda_x^{-}\). With \(n=(q\bar q)^{k}\), a unit
at \(w\) so that \(1_wn^{-1}\) is integral,
\[
1_wz=(1_wn^{-1})\,\bar q^{\,k}\,1_w(q^{k}z-\gamma q^{k}y)+1_w\gamma y\in\Lambda_x^{-}.
\]
Here both \(q\) and \(\bar q\) are units at \(w\) because \(w,\bar w\in P\cup\bar P\). Thus it splits at \(w\); by part 1 of the splitting lemma it splits at \(\bar w\) too, and one of
\(w,\bar w\) is in \(P\).

(3) For every finite point \(x\) there is \(u\) in the [[?c:Unipotent radical|unipotent radical]], which is contained in the Bessel subgroup, such that the lattice of \(ux\) is graded ([[?lean:New.Grading.exists_isGraded|Iwasawa decomposition for the flag of the grades]]; this uses the root of unity hypothesis); apply the hypothesis to it. If \(rx\) stabilises the standard
lattice then \(\Lambda_{rx}=\Lambda_1\), which is graded by
[[proofs/grh/upper-seesaw/standard-lattice-membership|the membership criterion]] and trivially has
the bounds with \(k=0\). \(\blacksquare\)

## References

1. Lean: `New.Grading.smul_latticeMinus_le_of_map_latticePlus`, `New.Grading.latticeSplitsAt_of_generates`, `New.Grading.SpansLattice.hasLatticeBounds_or_latticeSplitsAt`, `New.Grading.HasBoundedOrbit.of_forall`, `New.Grading.SpansLattice.hasBoundedOrbit_zero` in `src/New/UpperBound/Seesaw/Sandwich.lean`.
