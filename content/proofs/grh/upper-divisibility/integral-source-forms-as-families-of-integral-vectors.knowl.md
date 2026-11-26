+++
id = "proofs/grh/upper-divisibility/integral-source-forms-as-families-of-integral-vectors"
title = "Integral source forms as families of integral vectors"
kind = "lemma"
summary = "Evaluation at class representatives that are integral above p identifies the integral source forms with families of p-integral vectors indexed by the classes."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Columns.range_sourceFormOfValues", "New.Columns.sourceFormOfValues", "New.Columns.sourceFormOfValues_apply_rep"]
lean_files = ["src/New/UpperBound/Divisibility/HeckeEdges.lean"]
proof_status = "outline"
+++

**Lemma.** Let \(D\) be [[?lean:New.Data|admissible data]], \(p\) a prime, \(\iota\colon\mathbb{C}\to\mathbb{C}_p\) an embedding and \(O_\iota=\{z\in\mathbb{C}:\lvert\iota z\rvert_p\le1\}\). Let \(K_0\) be the level of stage \(0\), and for each class \(x\in\Gamma\backslash G_f/K_0\) of the unitary group of \(X_0\) let \(\rho_x\) be a representative that is integral at all places above \(p\). Let \(\mathcal W\) be the index set of the basis of the weight space of \(X_0\). Then the map
\[
F\longmapsto\varphi_F,\qquad\varphi_F(\rho_x)=F(x),
\]
from families \(F\colon(\text{classes})\to O_\iota^{\mathcal W}\) to source forms is well defined, \(O_\iota\)-linear and injective, and its image is the module of [[proofs/grh/upper-divisibility/marked-set-of-primes|integral source forms]].

## Proof

The level \(K_0\) is free ([[?lean:New.Data.classAut_levelX_zero_eq_bot|`classAut_levelX_zero_eq_bot`]]), so a source form is determined by, and may be prescribed arbitrarily through, its values at the representatives ([[?lean:New.freeLevelEquiv|`freeLevelEquiv`]], quoted). Every \(g\in G_f\) is \(\eta\rho_xu\) with \(\eta\in\Gamma\), \(u\in K_0\), and \(\varphi(g)=\eta\cdot\varphi(\rho_x)\). The gauge of \(\varphi(g)\) at \(g\) equals the gauge of \(\varphi(\rho_x)\) at \(\rho_x\): the gauge is unchanged by right multiplication by integral elements and by the simultaneous action of a rational point on the point and the vector ([[?lean:New.weylGauge_mul_of_mem_integralAbove|`weylGauge_mul_of_mem_integralAbove`]], [[?lean:New.weylGauge_embFin|`weylGauge_embFin`]], quoted). Since \(\rho_x\) is integral above \(p\), the gauge at \(\rho_x\) of a vector is at most \(1\) exactly when its coordinates lie in \(O_\iota\) ([[?lean:New.weylGauge_le_one_iff|`weylGauge_le_one_iff`]], quoted). So \(\varphi\) is integral iff all \(\varphi(\rho_x)\) have coordinates in \(O_\iota\). \(\blacksquare\)

## References

1. Lean: `New.Columns.range_sourceFormOfValues` in `src/New/UpperBound/Divisibility/HeckeEdges.lean`.
