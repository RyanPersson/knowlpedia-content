+++
id = "proofs/grh/upper-elementary-divisors/translate-conditions"
title = "Coefficient conditions on all Levi translates; deep forms"
kind = "definition"
summary = "Submodules of coefficient vectors whose translates under a Levi subgroup have prescribed coefficients in an ideal: the defect conditions and the deep forms."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.translatesIn", "New.FrobeniusCycle.defectConditions", "New.FrobeniusCycle.deepForms", "New.twoBlock", "New.defectThreshold"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/TwistingData.lean"]
+++

Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] for \((N,W,R)\) with \(N\ge 1\), let \(k,n\ge0\), and let \(\rho_n\) be the [[proofs/grh/upper-elementary-divisors/twisted-action|twisted representation]]. For a labelling \(\tau\colon\{0,\dots,k-1\}\to\mathbb{N}\) let \(L_\tau(W)\subseteq\mathrm{GL}_k(W)\) be the [[?lean:New.levi|Levi subgroup]] of the matrices \(g\) with \(g_{ij}=0\) whenever \(\tau(i)\ne\tau(j)\). For an [[algebra-rings/ideal|ideal]] \(I\subseteq R\) and a set \(B\subseteq\mathcal{E}(N,k,n)\) of exponents, define the [[algebra-modules/submodule|submodule]]
\[
\mathcal{T}_n(\tau,I,B)=\bigl\{F\colon\mathcal{E}(N,k,n)\to R\ \bigm|\ (\rho_n(g)F)_\beta\in I\ \text{ for all }g\in L_\tau(W),\ \beta\in B\bigr\}.
\]
Two cases are used.

- **Defect conditions.** For a root \((a,a')\), an ideal \(I\) and a real number \(h\): \(\mathcal{T}_n(\tau_{a'},I,B_h)\), where \(\tau_{a'}(b)=0\) for \(b<a'\) and \(1\) for \(b\ge a'\) (so \(L_{\tau_{a'}}\) is block diagonal with blocks of sizes \(a'\) and \(k-a'\)), and \(B_h\) is the set of \(\beta\) whose [[proofs/grh/upper-elementary-divisors/defect-of-monomial|defect]] \(\operatorname{def}_{i,a,a'}(\beta)\) exceeds \(h\) at some letter \(i\).
- **Deep forms.** For \(r,d\ge0\): \(\mathcal{D}_n(r,d)=\mathcal{T}_n(0,\,0,\,\{\beta:\operatorname{depth}_r(\beta)<d\})\), with the constant labelling (so \(L_0(W)=\mathrm{GL}_k(W)\)) and the zero ideal: the coefficient vectors \(F\) such that for every \(g\in\mathrm{GL}_k(W)\) all monomials of the translate \(\rho_n(g)F\) have [[proofs/grh/upper-elementary-divisors/depth-of-monomial|depth]] at least \(d\).

## Remarks

The **defect threshold** for a rank \(k\) and a precision \(c\) is the number \(c^{*}=3kc\); the later files state their thresholds for defects in this unit. For \(k>0\) it satisfies \(3c\le c^{*}\).

## References

1. Lean: `New.FrobeniusCycle.translatesIn`, `New.FrobeniusCycle.defectConditions`, `New.FrobeniusCycle.deepForms`, `New.twoBlock`, `New.defectThreshold` in `src/New/UpperBound/ElementaryDivisors/TwistingData.lean`.
