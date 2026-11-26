+++
id = "proofs/grh/upper-seesaw/generator-of-plus-over-minus"
title = "A vector of Lambda-plus outside Lambda-minus generates the quotient at a place above N"
kind = "lemma"
summary = "Lambda-plus differs from Lambda-minus only for odd strings, and any vector of the difference generates Lambda-plus over Lambda-minus at some place above N."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Grading.SpansLattice.exists_pole_of_notMem_latticeMinus", "New.Grading.SpansLattice.odd_of_notMem_latticeMinus", "New.Grading.SpansLattice.exists_place_generates_of_notMem_latticeMinus", "New.Grading.SpansLattice.odd_and_exists_place_of_notMem_latticeMinus"]
lean_files = ["src/New/UpperBound/Seesaw/StandardLines.lean"]
proof_status = "full"
+++

**Lemma.** In the setting of
[[proofs/grh/upper-seesaw/string-lattices-line-by-line|the string lattices]], with any unitary
scale \(u\) and a [[proofs/grh/upper-seesaw/split-squarefree-factorisation|split squarefree
factorisation]] \((P,N,\pi)\), let \(y\in\Lambda^{+}\setminus\Lambda^{-}\). Then:

1. \(s\) is odd; with \(c\) the middle index, the number \(\lambda_c^{-1}y_c\) has a pole at some
   place \(w\in P\cup\bar P\);
2. for this \(w\), every \(z\in\Lambda^{+}\) admits \(\gamma\in\widehat{\mathcal{O}}\) such that the
   component at \(w\) of \(z-\gamma y\) (all other components replaced by \(0\)) lies in
   \(\Lambda^{-}\).

## Proof

Write \(\kappa_b(x)=\lambda_b^{-1}x_b\). By the line-by-line description, \(x\in\Lambda^{-}\) iff
all \(\kappa_b(x)\) are integral, and \(x\in\Lambda^{+}\) iff \(\kappa_b(x)\) is integral off the
middle and \(N\kappa_c(x)\) is integral at the middle (for \(x\) in the span of the string).

(1) Since \(y\notin\Lambda^{-}\), some \(\kappa_m(y)\) has a pole at some place \(w\). As
\(y\in\Lambda^{+}\), this forces \(m\) to be the middle index (so \(s\) is odd) and \(N\) to be a
non-unit at \(w\), i.e. \(w\in P\cup\bar P\).

(2) Let \(z\in\Lambda^{+}\). Since \(N\) is a [[?c:Uniformizer|uniformiser]] at \(w\), \(\kappa_c(z)\) has at most a
simple pole at \(w\), while \(\kappa_c(y)\) has a pole; so
\(\lvert\kappa_c(z)\rvert_w\le\lvert\kappa_c(y)\rvert_w\), and there is
\(\gamma\in\widehat{\mathcal{O}}\) with \(1_w\,\kappa_c(z)=\gamma\,\kappa_c(y)\) (take
\(\gamma_w=\kappa_c(z)_w/\kappa_c(y)_w\) and \(\gamma_{w'}=0\) for \(w'\ne w\)). Then the
\(w\)-component of \(z-\gamma y\) lies in the span of the string, has middle coordinate
\(\kappa_c=0\) at \(w\), and for \(b\ne c\) its coordinate
\(1_w(\kappa_b(z)-\gamma\kappa_b(y))\) is integral. Hence it lies in \(\Lambda^{-}\).
\(\blacksquare\)

## References

1. Lean: `New.Grading.SpansLattice.odd_and_exists_place_of_notMem_latticeMinus` and the three lemmas it combines, in `src/New/UpperBound/Seesaw/StandardLines.lean`.
