+++
id = "proofs/grh/upper-elementary-divisors/defect-of-steps"
title = "Defect of a vector of steps; the defect cone is the image of the Pieri cone"
kind = "lemma"
summary = "The defect of the step vector of nu along a root is one step minus a difference of entries of nu, so the defect cone with bound 0 pulls back to the Pieri cone and fills the fraction prod (q-1)/(q^(l+1)-1) of every slab."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.defectWeight_dotProduct_permStep", "New.FrobeniusCycle.permStep_mem_defectCone_iff", "New.FrobeniusCycle.prod_mul_volume_defectCone_inter_degreeSlab"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/DefectCount.lean"]
proof_status = "full"
+++

**Lemma.** Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] with \(N\ge1\), and let \(\mathrm{St}\) be the [[proofs/grh/upper-elementary-divisors/step-map-pieri-cone-slab|step map]] with trivial permutations, the real number \(P\), and the sign \(+\) exactly on even letters. For \(\nu\in\mathbb{R}^{k\times\mathbb{Z}/N}\), indices \(a,a'\) and a letter \(i\):

1. \(\operatorname{def}_{i,a,a'}(\mathrm{St}\,\nu)=(\mathrm{St}\,\nu)(Y_i)-\bigl(\nu(a,i)-\nu(a',i)\bigr)\), where \(Y_i=(a',i)\) for even and \((a,i)\) for odd \(i\).
2. \(\mathrm{St}\,\nu\in\mathcal{K}(a,0)\) ([[proofs/grh/upper-elementary-divisors/defect-cone|defect cone]]) if and only if \(\nu\) lies in the Pieri cone \(\mathcal{C}_{v,P}\).
3. For every \(D\colon\mathbb{Z}/N\to\mathbb{R}\): \(\bigl(\prod_{l<k}\frac{q^{l+1}-1}{q-1}\bigr)\operatorname{vol}\bigl(\mathcal{K}(a,0)\cap\mathrm{Slab}_k(D)\bigr)=\operatorname{vol}\mathrm{Slab}_k(D)\).

## Proof

(1) Put \(D_s=\nu(a,s)-\nu(a',s)\). In every letter \(s\),
\[
(\mathrm{St}\nu)(Y_s)-(\mathrm{St}\nu)(X_s)=D_s-P\,D_{s+1}:
\]
for even \(s\), \(Y_s=(a',s)\), \(X_s=(a,s)\) and the steps are \(P\nu(b,s+1)-\nu(b,s)\); for odd \(s\), \(Y_s=(a,s)\), \(X_s=(a',s)\) and the steps are \(-(P\nu(b,s+1)-\nu(b,s))\). Let \(\tau_s=P^{1+[s-i]}D_{s+1}/(q-1)\), so that \(\tau_{s-1}=P^{[s-i]}D_s/(q-1)\) for \(s\ne i\) and \(\tau_{i-1}=qD_i/(q-1)\). For \(s\ne i\) the defect weights at \(Y_s,X_s\) are \(\pm P^{[s-i]}/(q-1)\), and the letter \(s\) contributes \(P^{[s-i]}(D_s-PD_{s+1})/(q-1)=\tau_{s-1}-\tau_s\). For \(s=i\) the weights are \(1+\frac1{q-1}\) at \(Y_i\) and \(-\frac1{q-1}\) at \(X_i\), and the contribution is \((\mathrm{St}\nu)(Y_i)+(D_i-PD_{i+1})/(q-1)=\tau_{i-1}-\tau_i+(\mathrm{St}\nu)(Y_i)-D_i\). The sum of \(\tau_{s-1}-\tau_s\) around the cycle vanishes, which leaves \((\mathrm{St}\nu)(Y_i)-D_i\).

(2) By (1) for the simple root \((b,b+1)\), \(\operatorname{def}_{i,b,b+1}(\mathrm{St}\nu)\le0\) reads \((\mathrm{St}\nu)(Y_i)\le\nu(b,i)-\nu(b+1,i)\), which is the defining inequality of the Pieri cone at \((i,b)\).

(3) is the [[proofs/grh/upper-elementary-divisors/volume-of-pieri-cone-in-slab|volume theorem]] applied to \(\Omega=\mathcal{K}(a,0)\), by (2), as \(P>1\). \(\square\)

## References

1. Lean: `New.FrobeniusCycle.defectWeight_dotProduct_permStep`, `New.FrobeniusCycle.permStep_mem_defectCone_iff`, `New.FrobeniusCycle.prod_mul_volume_defectCone_inter_degreeSlab` in `src/New/UpperBound/ElementaryDivisors/DefectCount.lean`.
