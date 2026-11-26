+++
id = "proofs/grh/upper-elementary-divisors/volume-of-cone-in-slab-signed-sum"
title = "Share of the Pieri cone in the slab as a signed sum"
kind = "proposition"
summary = "A set pulling back to the Pieri cone under the step map fills a fraction of the degree slab given by a signed sum over permutations that depends only on k and q = P^(m+1)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.volume_real_inter_degreeSlab_eq_signed_sum"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/PieriCone.lean"]
proof_status = "full"
+++

**Proposition.** Let \(\mathcal{T}=\{0,\dots,m\}\) with addition modulo \(m+1\), signs \(v\), \(P>1\), \(q=P^{m+1}\), and \(D\colon\mathcal{T}\to\mathbb{R}\). Let \(\Omega\subseteq\mathbb{R}^{k\times\mathcal{T}}\) satisfy \(\mathrm{St}\,\nu\in\Omega\iff\nu\in\mathcal{C}_{v,P}\) for all \(\nu\) ([[proofs/grh/upper-elementary-divisors/step-map-pieri-cone-slab|notation]]). Then
\[
\operatorname{vol}\bigl(\Omega\cap\mathrm{Slab}_k(D)\bigr)=\frac{\lvert\Delta_q(1)\rvert}{k!}\Bigl(\sum_{\pi\in S_k}\frac{\operatorname{sgn}\pi}{\lvert\Delta_q(\pi)\rvert}\Bigr)\operatorname{vol}\bigl(\mathrm{Slab}_k(D)\bigr).
\]

## Proof

Integrate the pointwise identity (2) of the [[proofs/grh/upper-elementary-divisors/signed-count-of-positive-steps|signed count]] over \(\nu\in\mathbb{R}^{k\times\mathcal{T}}\). All sets \(\mathrm{Pos}_D(\sigma,\tau,Y)\) involved are measurable (defined by finitely many linear inequalities) of finite volume, by the [[proofs/grh/upper-elementary-divisors/determinant-of-step-map|volume formula]] and boundedness of the slab. With \(\det\mathrm{St}_\sigma=c\,\Delta_q(\sigma_0\cdots\sigma_m)\), \(c\ne0\), \(\Delta_q(1)\neq0\), the volume formula gives
\[
\sum_{\tau}\frac{\operatorname{vol}(\Omega\cap\mathrm{Slab})}{\lvert c\rvert\lvert\Delta_q(1)\rvert}=\sum_{\sigma}\operatorname{sgn}(\sigma_0\cdots\sigma_m)\frac{\operatorname{vol}(\mathrm{Slab})}{\lvert c\rvert\,\lvert\Delta_q(\sigma_0\cdots\sigma_m)\rvert}.
\]
The left side has \((k!)^{m+1}\) equal terms; the right side equals \((k!)^{m}\sum_\pi\operatorname{sgn}(\pi)\operatorname{vol}(\mathrm{Slab})/(\lvert c\rvert\lvert\Delta_q(\pi)\rvert)\) by part 3 of the signed count. Solve for \(\operatorname{vol}(\Omega\cap\mathrm{Slab})\). \(\square\)

## References

1. Lean: `New.volume_real_inter_degreeSlab_eq_signed_sum` in `src/New/UpperBound/ElementaryDivisors/PieriCone.lean`.
