+++
id = "proofs/grh/upper-elementary-divisors/root-lemma"
title = "Root lemma: an extreme term has nonpositive defect"
kind = "theorem"
summary = "A term of least w-adic order plus weight among all translates by the SL_2 of a root has defect at most 0 at every letter, for weights rising by an amount in [1/2, 1] from X_s to Y_s."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.defect_nonpos_of_extreme_term", "New.FrobeniusCycle.weight_defectWeight_nonpos_of_least"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/RootLemma.lean"]
proof_status = "full"
+++

**Theorem (root lemma).** Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] for \((N,W,R)\) with \(N\ge1\), let \(a\ne a'\) be indices below \(k\), \(i\) a letter, and let \(c\) be real weights of the variables \(x_{b,s}\) with \(\tfrac12\le c(Y_s)-c(X_s)\le1\) for every letter \(s\) (\(X_s,Y_s\) as in the [[proofs/grh/upper-elementary-divisors/defect-of-monomial|defect]]). Let \(f\in R[x_{b,s}]\), \(\alpha\) an exponent and \(l\in\mathbb{N}\) be such that

- for every \(g\) in the [[proofs/grh/upper-elementary-divisors/root-data|\(\mathrm{SL}_2\) of the root]], every term of the [[proofs/grh/upper-elementary-divisors/twisted-action|translate]] \(g\cdot f\) has \(w\)-adic order plus \(c\)-weight at least \(l+c\cdot\alpha\), i.e. \(g\cdot f\in\mathrm{G}_{l+c\cdot\alpha}(F^{w},c)\);
- \(w^{l+1}\nmid f_\alpha\).

Then \(\operatorname{def}_{i,a,a'}(\alpha)\le0\).

**Corollary (characteristic \(p\)).** If \(R=K\) is a field of characteristic \(p\) (so \(w=0\)), \(h\) are weights rising by exactly \(1\) from \(X_s\) to \(Y_s\) for all \(s\), \(f_\alpha\ne0\), and every monomial occurring in any translate \(g\cdot f\), \(g\in\mathrm{SL}_2^{a,a'}(W)\), has \(h\)-weight at least \(h\cdot\alpha\), then \(\operatorname{def}_{i,a,a'}(\alpha)\le0\).

## Proof

By [[proofs/grh/upper-elementary-divisors/zeros-against-degree|zeros against degree]], \(q\,\nu(\alpha)\le d(\alpha)\). Since \(\operatorname{def}_{i,a,a'}(\alpha)=(\nu(\alpha)-d(\alpha)/q)/(q-1)\) and \(q>1\), the defect is \(\le0\).

For the corollary take \(c=h\), \(l=0\): with \(w=0\), membership in \(F^{w}_t\) means "zero if \(t>0\)", so the hypothesis is the Gauss condition of level \(h\cdot\alpha\), and \(w^{1}\nmid f_\alpha\) means \(f_\alpha\ne0\). \(\square\)

## Remarks

These bounds along the roots are Pieri's inequalities for the exponent of a term that is least among all translates.

## References

1. Lean: `New.FrobeniusCycle.defect_nonpos_of_extreme_term`, `New.FrobeniusCycle.weight_defectWeight_nonpos_of_least` in `src/New/UpperBound/ElementaryDivisors/RootLemma.lean`.
2. Related work named in the head of the Lean file: Ghate–Jana, Modular representations of GL2(F_q) using calculus, 2025; Imai–Koskivirta, Automorphic vector bundles on the stack of G-zips, 2021; E. Bombieri, Counting points on curves over finite fields (d'après S. A. Stepanov), Séminaire Bourbaki 430, 1973.
