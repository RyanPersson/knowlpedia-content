+++
id = "proofs/grh/derivatives-vacuum/hermitian-product-of-lattice-vectors-is-integral"
title = "Hermitian products of vectors of the lattice a0 are integers of K"
kind = "lemma"
summary = "For x, y in the lattice a0 of E, the sum over the CM type of the products of the image of x with the conjugate image of y is an integer of K."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.sum_mul_conj_mem_quadInt", "New.Parameters.exists_coe_eq_trace_of_isIntegral", "New.Parameters.coe_trace_eq_sum", "New.Parameters.finiteImage_id_eq_inv_alpha_mul", "New.Parameters.mul_sum_mul_conj_mem_lattice"]
lean_files = ["src/New/Derivatives/Vacuum/TightFrames.lean"]
proof_status = "full"
+++

Let \(P\) be [[?lean:New.Parameters|parameters]], \(s\in\mathbb{N}\), \(K=\mathbb{Q}(\sqrt{-d})\), \(E=K(\zeta)\) with \(\zeta\) a primitive \(q_1\)-th root of unity, and \(\Phi_\tau\colon E\to\mathbb{C}\) the embeddings of the [[?c:CM type|CM type]], indexed by the infinite places \(\tau\) of \(E\); all \(\Phi_\tau\) restrict to the fixed inclusion \(K\subset\mathbb{C}\). Let \(\alpha\) be the [[?lean:New.Parameters.α|finite idele of the Weil data]], \(\widehat{\mathcal{O}}_E\) the ring of integral [[?c:Finite adele ring of a number field|finite adeles]], and
\[ \mathfrak{a}_0=E\cap\alpha\,\widehat{\mathcal{O}}_E=\{x\in E:\ \alpha^{-1}x\in\widehat{\mathcal{O}}_E\}. \]

**Lemma.** For \(x,y\in\mathfrak{a}_0\),
\[ \langle x,y\rangle:=\sum_{\tau}\Phi_\tau(x)\,\overline{\Phi_\tau(y)}\ \in\ \mathcal{O}_K. \]
Consequently, if \(C\) is a [[?lean:New.CMLattice|CM lattice]] for \(d\) with lattice \(\Lambda\) and \(a\in\Lambda\), then \(a\,\langle y,x\rangle\in\Lambda\).

## Proof

Let \(g=\Phi_{q_1}'(\zeta)\) be the [[?lean:New.Parameters.relDifferentGen|generator of the relative different]] of \(E/K\) (the value at \(\zeta\) of the derivative of the \(q_1\)-th cyclotomic polynomial).

*Step 1: \(x\bar y g\) is an algebraic integer.* In the finite adeles,
\[ x\,\bar y\,g=(\alpha\bar\alpha g)\cdot(\alpha^{-1}x)\cdot\overline{(\alpha^{-1}y)} . \]
The idele \(\alpha\bar\alpha g\) is a unit at every finite place ([[?lean:New.Parameters.v_alpha_mul_star_mul_relDifferentGen|its valuation is \(1\) at every finite place]]), in particular integral; \(\alpha^{-1}x\) is integral by hypothesis, and \(\overline{\alpha^{-1}y}\) is integral because complex conjugation preserves \(\widehat{\mathcal{O}}_E\). An element of \(E\) whose image in the finite adeles is integral is an algebraic integer.

*Step 2: the trace of \(z=x\bar y\) lies in \(\mathcal{O}_K\).* The ideal \((g)\) of \(\mathcal{O}_E\) is the [[?c:Different ideal|different]] \(\mathfrak{D}_{E/K}\). Since \(zg\in\mathcal{O}_E\), we have \(z\in (g)^{-1}=\mathfrak{D}_{E/K}^{-1}\), and by the definition of the different the [[?c:Field trace|trace]] \(\operatorname{Tr}_{E/K}\) maps \(\mathfrak{D}_{E/K}^{-1}\) into \(\mathcal{O}_K\).

*Step 3: the trace is the sum over the CM type.* The extension \(E/K\) is Galois and the infinite places of \(E\) are in bijection with \(\operatorname{Gal}(E/K)\) in such a way that \(\Phi_\tau=\Phi_1\circ g_\tau\). Hence, applying \(\Phi_1\) (which is the inclusion on \(K\)) to \(\operatorname{Tr}_{E/K}(z)=\sum_{g}g(z)\) gives \(\operatorname{Tr}_{E/K}(z)=\sum_\tau\Phi_\tau(z)\) in \(\mathbb{C}\). With \(z=x\bar y\) and \(\Phi_\tau(\bar y)=\overline{\Phi_\tau(y)}\) (a CM type commutes with complex conjugation) this is \(\langle x,y\rangle\).

The consequence follows because \(\Lambda\) is stable under multiplication by \(\mathcal{O}_K\).

## References

1. Lean: `New.Parameters.sum_mul_conj_mem_quadInt`, `New.Parameters.exists_coe_eq_trace_of_isIntegral`, `New.Parameters.coe_trace_eq_sum`, `New.Parameters.finiteImage_id_eq_inv_alpha_mul`, `New.Parameters.mul_sum_mul_conj_mem_lattice` in `src/New/Derivatives/Vacuum/TightFrames.lean`.
