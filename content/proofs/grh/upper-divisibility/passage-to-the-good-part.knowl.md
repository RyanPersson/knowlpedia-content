+++
id = "proofs/grh/upper-divisibility/passage-to-the-good-part"
title = "Passage to target forms by the good projection"
kind = "proposition"
summary = "Replacing a form of principal level on Y_0 by its good part keeps integrality of scalar multiples of its lift and enlarges the bound exp(B) on the values of the lift to exp(x^99 + B) on the class sum."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.lowerChain_goodProjTranslate_apply", "New.Data.goodProjTranslate_mem_integralForms", "New.Data.normSqAt_goodProjTranslate_le", "New.Data.coe_lowerChainAtLevel_apply"]
lean_files = ["src/New/UpperBound/Size/ArchimedeanSize.lean"]
proof_status = "outline"
+++

Let \(D\) be [[?lean:New.Data|admissible data]], \(\mathsf G\) the finite group [[?lean:New.Data.chosenGL|\(\prod\mathrm{GL}_r(\mathbb{F}_w)\) over the chosen places]], \(e_0\in\mathbb{C}[\mathsf G]\) the [[?lean:New.Data.e₀|good idempotent]], \(\vartheta\) a tame character and \(\Theta_\vartheta\) the [[?lean:New.Data.lowerChain|chain of the \(m\) lifts from \(Y_0\) to \(Y_m\)]]. For \(s\in\mathsf G\) and a form \(z\) of principal level on \(Y_0\), the **good part** is \(z_s=\lvert\mathsf G\rvert\,e_0\,s\,z\) ([[?lean:New.Data.goodProjTranslate|`goodProjTranslate`]]).

**Proposition.**

1. \(\Theta_\vartheta(z_s)(g)=\sum_{t\in\mathsf G}\lvert\mathsf G\rvert e_0(t)\cdot\Theta_\vartheta(z)\bigl(g\,\beta(ts)\bigr)\), where \(\beta(u)\) is an integral element of \(G_f(Y_m)\) attached to \(u\in\mathsf G\) ([[?lean:New.Data.firstBlockLift|`firstBlockLift`]]).
2. For a prime \(\ell\), an embedding \(\mathbb{C}\to\mathbb{C}_\ell\) and \(c\in\mathbb{C}\): if \(c\,\Theta_\vartheta(z)\) is integral (gauge at most \(1\) everywhere), so is \(c\,\Theta_\vartheta(z_s)\).
3. For the trivial twist and an automorphism \(\sigma\) of \(\mathbb{C}\): if \(\lVert\sigma(\Theta_1(z)(g))\rVert^{2}\le e^{B}\) for all \(g\), then the [[?lean:New.LevelPlaces.LevelForm.normSqAt|class sum of squared norms]] of \(\sigma\Theta_1(z_s)\) is at most \(\exp(x^{99}+B)\).

## Proof

(1) Expand the action of \(e_0\) as a sum over \(\mathsf G\); the chain turns the action of \(u\in\mathsf G\) on forms of principal level into right translation by \(\beta(u)\) ([[?lean:New.Data.lowerChain_principalRep|`lowerChain_principalRep`]], quoted).

(2) The numbers \(\lvert\mathsf G\rvert e_0(t)\) are algebraic integers, being values of a character of \(\mathsf G\) (\(e_0\) is a central idempotent; [[?lean:New.IsCentralProj.isChar_card_mul_coeff|`isChar_card_mul_coeff`]], quoted), so their \(\ell\)-adic absolute values are at most \(1\); right translation by the integral element \(\beta(ts)\) does not change gauges; and the gauge is ultrametric.

(3) The conjugate \(\sigma e_0\) is again such an idempotent, so \(\lvert\sigma e_0(t)\rvert\le1\). Each value of \(\sigma\Theta_1(z_s)\) is a sum of \(\lvert\mathsf G\rvert\) terms of norm at most \(\lvert\mathsf G\rvert e^{B/2}\), hence has squared norm at most \(\lvert\mathsf G\rvert^{4}e^{B}\). The level of the lift contains the principal congruence subgroup of level \(\pi_M\pi_N\), so there are at most \(\exp(x^{30})\) classes ([[proofs/grh/upper-divisibility/class-count-at-levels-containing-a-principal-level|class count]]). Finally \(\exp(x^{30})\lvert\mathsf G\rvert^{4}\le\exp(x^{99})\), as \(\lvert\mathsf G\rvert\) divides the [[?lean:New.Data.chosenGroupOrder|chosen group order]], whose logarithm is small against \(x^{99}\) (quoted). \(\blacksquare\)

## References

1. Lean: `New.Data.lowerChain_goodProjTranslate_apply`, `New.Data.goodProjTranslate_mem_integralForms`, `New.Data.normSqAt_goodProjTranslate_le` in `src/New/UpperBound/Size/ArchimedeanSize.lean`.
