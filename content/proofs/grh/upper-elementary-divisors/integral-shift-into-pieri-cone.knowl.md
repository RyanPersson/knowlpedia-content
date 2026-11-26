+++
id = "proofs/grh/upper-elementary-divisors/integral-shift-into-pieri-cone"
title = "An integral shift into the cone of Pieri's inequalities"
kind = "lemma"
summary = "There is a nonnegative integral vector of small degree whose defect is at most -1 along one simple root and at most 0 along the others; adding a multiple of it moves vectors of bounded defect into the defect cone."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.exists_mem_defectCone_sum_le", "New.FrobeniusCycle.smul_add_mem_defectCone_inter_degreeSlab"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/DefectCount.lean"]
proof_status = "full"
+++

**Lemma.** Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] with \(N\ge1\) and \(a\) an index below \(k\).

1. There is \(\sigma\in\mathcal{K}(a,-1)\) ([[proofs/grh/upper-elementary-divisors/defect-cone|defect cone]]) with integer entries, \(\sigma\ge0\), and \(\sum_b\sigma(b,s)\le P^{2(a+1)}-1\) for every letter \(s\).
2. If \(h\ge0\), \(\sigma\ge0\) lies in \(\mathcal{K}(a,-1)\), and \(\beta\in\mathcal{K}(a,h)\cap\mathrm{Slab}_k(d)\) (constant degrees \(d\)), then \(h\sigma+\beta\in\mathcal{K}(a,0)\cap\mathrm{Slab}_k(D)\) with \(D_s=d+h\sum_b\sigma(b,s)\).

## Proof

(1) Let \(\mu_b=P^{2(a-b)}\) for \(b\le a\) and \(\mu_b=0\) for \(b>a\), so \(\mu_b=P^{2}\mu_{b+1}+[b=a]\). Let \(\nu(b,s)=\mu_b\) for even and \(P\mu_b\) for odd \(s\), and \(\sigma=\mathrm{St}\,\nu\). Then \(\sigma(b,s)=P\cdot P\mu_b-\mu_b=(P^{2}-1)\mu_b\) for even \(s\) and \(\sigma(b,s)=-(P\mu_b-P\mu_b)=0\) for odd \(s\): integral, nonnegative, of degree \((P^{2}-1)\sum_{j\le a}P^{2j}=P^{2(a+1)}-1\) or \(0\). By [[proofs/grh/upper-elementary-divisors/defect-of-steps|the defect of steps]], for even \(i\): \(\operatorname{def}_{i,b,b+1}(\sigma)=(P^{2}-1)\mu_{b+1}-(\mu_b-\mu_{b+1})=-[b=a]\); for odd \(i\): \(\operatorname{def}_{i,b,b+1}(\sigma)=0-P(\mu_b-\mu_{b+1})=-P\bigl((P^{2}-1)\mu_{b+1}+[b=a]\bigr)\le-[b=a]\).

(2) Defects and degrees are linear, and \(h\cdot(-1)+h=0\), \(h\cdot0+0=0\). \(\square\)

## References

1. Lean: `New.FrobeniusCycle.exists_mem_defectCone_sum_le`, `New.FrobeniusCycle.smul_add_mem_defectCone_inter_degreeSlab` in `src/New/UpperBound/ElementaryDivisors/DefectCount.lean`.
