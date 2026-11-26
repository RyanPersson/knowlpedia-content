+++
id = "proofs/grh/upper-elementary-divisors/volume-of-pieri-cone-in-slab"
title = "Volume of the Pieri cone in a slab"
kind = "theorem"
summary = "For P > 1 and q = P^N, a set that pulls back to the Pieri cone under the step map fills exactly the fraction prod (q-1)/(q^(l+1)-1) of every degree slab."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.prod_mul_volume_real_inter_degreeSlab", "New.volume_real_pieriCone_inter_degreeSlab_one", "New.volume_real_degreeSlab_one_pos"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/PieriCone.lean"]
proof_status = "full"
+++

**Theorem.** Let \(N\ge1\), \(k\ge0\), signs \(v\colon\mathbb{Z}/N\to\{+,-\}\), \(P>1\), \(q=P^{N}\), and \(D\colon\mathbb{Z}/N\to\mathbb{R}\). Let \(\Omega\subseteq\mathbb{R}^{k\times\mathbb{Z}/N}\) be a set such that \(\mathrm{St}\,\nu\in\Omega\iff\nu\in\mathcal{C}_{v,P}\) for all \(\nu\) ([[proofs/grh/upper-elementary-divisors/step-map-pieri-cone-slab|step map, Pieri cone, slab]]). Then
\[
\Bigl(\prod_{l=0}^{k-1}\frac{q^{l+1}-1}{q-1}\Bigr)\cdot\operatorname{vol}\bigl(\Omega\cap\mathrm{Slab}_k(D)\bigr)=\operatorname{vol}\bigl(\mathrm{Slab}_k(D)\bigr).
\]

## Proof

By the [[proofs/grh/upper-elementary-divisors/volume-of-cone-in-slab-signed-sum|signed-sum formula]] (with \(m=N-1\)), \(\operatorname{vol}(\Omega\cap\mathrm{Slab}_k(D))=c(k,q)\operatorname{vol}(\mathrm{Slab}_k(D))\), where \(c(k,q)=\frac{\lvert\Delta_q(1)\rvert}{k!}\sum_\pi\operatorname{sgn}\pi/\lvert\Delta_q(\pi)\rvert\) depends only on \(k\) and \(q\). So \(c(k,q)\) may be computed in the case of one letter, sign \(+\), with \(q\) in the place of \(P\), \(D=1\) and \(\Omega=\mathcal{C}_{+,q}\): there the step map is \(\nu\mapsto(q-1)\nu\), a positive homothety, which preserves the cone \(\mathcal{C}_{+,q}=\{\beta:q\beta_{b+1}\le\beta_b\}\), so the hypothesis holds and \(\operatorname{vol}(\mathcal{C}_{+,q}\cap\mathrm{Slab}_k(1))=c(k,q)\operatorname{vol}(\mathrm{Slab}_k(1))\).

*One letter.* \(\mathrm{Slab}_k(1)=\{\beta\ge0,\sum_b\beta_b\le1\}\) has positive volume (it contains the cube \([0,1/k]^{k}\)). Let \(d_i=(q^{i+1}-1)/(q-1)>0\), so \(d_0=1\) and \(d_{i+1}-1=qd_i\). Define the linear map \(F\) by \((F\beta)_b=d_b(\beta_b-q\beta_{b+1})\), with \(\beta_k:=0\). It is triangular with \(\det F=\prod_bd_b>0\), and it preserves the degree: \(\sum_b\bigl((F\beta)_b-\beta_b\bigr)=\sum_b\bigl((d_b-1)\beta_b-(d_{b+1}-1)\beta_{b+1}\bigr)\) telescopes to \((d_0-1)\beta_0-(d_k-1)\beta_k=0\). Moreover \(F\beta\ge0\) iff \(q\beta_{b+1}\le\beta_b\) for all \(b<k-1\) and \(\beta_{k-1}\ge0\), which (by descending induction, \(\beta_b\ge q\beta_{b+1}\ge0\)) is equivalent to \(\beta\in\mathcal{C}_{+,q}\) and \(\beta\ge0\). Hence \(\mathcal{C}_{+,q}\cap\mathrm{Slab}_k(1)=F^{-1}(\mathrm{Slab}_k(1))\), of volume \((\prod_bd_b)^{-1}\operatorname{vol}\mathrm{Slab}_k(1)\).

Comparing, \(c(k,q)=\prod_{b<k}(q-1)/(q^{b+1}-1)\). \(\square\)

## References

1. Lean: `New.prod_mul_volume_real_inter_degreeSlab`, `New.volume_real_pieriCone_inter_degreeSlab_one`, `New.volume_real_degreeSlab_one_pos` in `src/New/UpperBound/ElementaryDivisors/PieriCone.lean`.
2. The head of the Lean file DefectCount.lean names as related work: Forrester–Zhang, Corank-1 projections and the randomised Horn problem, 2021 (after Dixon, 1905; Anderson, 1991).
