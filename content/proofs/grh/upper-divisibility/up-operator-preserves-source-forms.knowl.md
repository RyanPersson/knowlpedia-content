+++
id = "proofs/grh/upper-divisibility/up-operator-preserves-source-forms"
title = "The operator U at N preserves the source forms; ramified source forms are ramified vectors"
kind = "proposition"
summary = "The operator U_p at Sigma_N, in a basis of L_0, maps source forms to source forms, and a ramified source form is a ramified vector of the representation at Sigma_N."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.upOperator_mem_sourceForm", "New.Data.mem_ramified_of_mem_ramifiedSourceForms"]
lean_files = ["src/New/UpperBound/Divisibility/SetupAtLevel.lean"]
proof_status = "outline"
+++

Notation of the [[proofs/grh/upper-divisibility/setup-at-the-level-prime|set-up at \(N\)]]; \(\rho_0\) is the representation of \(\mathrm{GL}(X_0)\) at \(\Sigma_N\) on forms on \(X_0\), and \(U\) its [[?lean:New.IsSplitLevel.upOperator|operator \(U_p\)]].

**Proposition.**

1. If \(\varphi\) is a source form, so is \(U\varphi\).
2. If \(\varphi\) is a [[proofs/grh/upper-divisibility/ramified-source-forms|ramified source form]], then \(\varphi\) is a [[?lean:New.IsSplitLevel.ramified|ramified vector]] of \(\rho_0\): for each \(w\in\Sigma_N\) there are a form \(\psi\) and a scalar matrix \(x\) at \(\Sigma_N\), an integral unit that is congruent to \(1\) modulo \(N\) at the places of \(\Sigma_N\) other than \(w\), with \(\varphi=\psi-\rho_0(x)\psi\). (The proof produces an \(x\) that is equal to \(1\) at the other places, which is more than the definition asks.)

## Proof

(1) Let \(k\in K_0\). Let \(a\) be the matrix of \(\delta_0^{-1}k\delta_0\) at \(\Sigma_N\); it is mirabolic, and \(\langle a\rangle_0\in K_0\) ([[proofs/grh/upper-divisibility/level-at-n-as-a-mirabolic-group|the level as a mirabolic group]]). Put \(b=\langle a\rangle_0^{-1}k\in K_0\); its components at \(\Sigma_N\) (and conjugates) are trivial. Translation by \(b\) commutes with \(U\), which is built from translations supported above \(N\); so \(b\,U\varphi=U\,b\varphi=U\varphi\). And \(U\) preserves the vectors fixed by the mirabolic group ([[?lean:New.IsSplitLevel.mirabolic_fix_upOperator|`mirabolic_fix_upOperator`]], quoted), so \(\langle a\rangle_0U\varphi=U\varphi\). Hence \(k\,U\varphi=U\varphi\).

(2) Let \(w\in\Sigma_N\); one of \(w,\bar w\) is a prime \(u\mid\pi_N\). The [[proofs/grh/upper-divisibility/scaling-generator|scaling generator]] \(z_u\) is an integral norm-one idele trivial away from \(u,\bar u\), hence its scalar matrix is \(\tilde x\) for an integral unit scalar \(x\) at \(w\) that is \(1\) at the other places of \(\Sigma_N\); a scalar commutes with \(\delta_0\), so \(\langle x\rangle_0\) is the scalar matrix of \(z_u\). A ramified source form is \(\psi-z_u\psi\) for a source form \(\psi\) ([[proofs/grh/upper-divisibility/ramified-source-forms-are-the-image-of-the-ramifying-operator|description as an image]]). \(\blacksquare\)

*Status.* The definition of \(U_p\) and its invariance property are another area's; they are quoted.

## References

1. Lean: `New.Data.upOperator_mem_sourceForm`, `New.Data.mem_ramified_of_mem_ramifiedSourceForms` in `src/New/UpperBound/Divisibility/SetupAtLevel.lean`.
