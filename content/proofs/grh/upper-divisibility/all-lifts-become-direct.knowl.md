+++
id = "proofs/grh/upper-divisibility/all-lifts-become-direct"
title = "At N all lifts become direct lifts after a power of U"
kind = "theorem"
summary = "On ramified source forms the chain of glued double lifts equals a scalar of N-adic absolute value at most N^(m f b) times the chain of m direct lifts applied to U^(m/2) of the form."
aliases = ["lift character at N", "glued factor"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.doubleLiftChain_gluedDoubleLiftDatum_eq_smul_chain", "New.Data.liftLaw_liftAtN", "New.Data.liftInPairs_gluedDoubleLiftDatum", "New.Data.lift_schrodingerOpAt_comp", "New.Data.norm_gluedFactor_le", "New.Data.norm_detCharAt_diagN_le", "New.Data.gluedFactor", "New.Data.upCommutationFactor", "New.Data.liftCharAtN", "New.Data.liftAtN", "New.Data.liftAtN_apply"]
lean_files = ["src/New/UpperBound/Divisibility/ValuationAtLevel.lean"]
proof_status = "outline"
+++

Notation of the [[proofs/grh/upper-divisibility/setup-at-the-level-prime|set-up at \(N\)]] and of [[proofs/grh/upper-divisibility/direct-lifts-lose-little|direct lifts]]; \(\vartheta\) is a tame character and \(\chi_i\) the base change to \(E\) of the [[?lean:New.Data.chainChar|character of the lift \(i\)]] (from \(X_{i-1}\) to \(X_i\)). For \(r\ge0\) the **lift character at \(N\)** is \(\chi_{i,r}(g)=\chi_i(\det g)\lvert\det g\rvert^{-r/2}\) on \(\mathrm{GL}\) over \(\prod_{w\in\Sigma_N}E_w\). Let \(D_S=\operatorname{diag}(1,\dots,1,N)\) at the places of \(\Sigma_N\) in \(S\) and \(1\) at the others.

**Theorem.** There is a complex number \(c\) with \(\lvert\iota c\rvert_N\le N^{mfb}\) such that for all families \(v=(v_j)\) of data and every [[proofs/grh/upper-divisibility/ramified-source-forms|ramified source form]] \(\varphi\):
\[
\bigl(\text{chain of the }\varrho+1\text{ double lifts with glued data }\mathrm{Glue}(\mathrm{pr}\,v)\bigr)(\varphi)=c\cdot\bigl(\text{chain of the }m\text{ lifts with data }\mathrm{Dir}_j(v_j)\bigr)\bigl(U^{\varrho+1}\varphi\bigr),
\]
where \(\mathrm{pr}\) is the projection on the vacuum at the places above \(N\).

## Proof

*Step 1 (values of lift characters).* For \(i\le2m\) and any \(j,r,S\): \(\lvert\iota\chi_{i,r}(D_S)\rvert_N\le\prod_{\tau:\ \overline{w_\tau}\in S}N^{2b}\). Indeed the absolute value decreases with \(r\) ([[?lean:New.norm_detCharAt_diagN_anti|`norm_detCharAt_diagN_anti`]], quoted), so take \(r=0\); \(\chi_i\) has weight \(\kappa_i(\tau)\) at \(\tau\), so the \(N\)-adic absolute value of its value at the determinant of the unitary point \(\delta(S)\) is \(\prod_\tau\lvert(\det)_\tau\rvert^{\kappa_i(\tau)}\) with \((\det)_\tau\in\{N^{-1},1\}\), and \(\kappa_i(\tau)\le2b\) ([[?lean:New.Data.liftWeight_le_two_mul_b|`liftWeight_le_two_mul_b`]], quoted).

*Step 2 (equivariance of a lift in the function at \(\Sigma_N\)).* For a function \(F\) of matrices modulo \(N\) (read on integral matrices, zero elsewhere), \(g\in\mathrm{GL}(X_j)\), \(k\in\mathrm{GL}(X_{j+1})\) at \(\Sigma_N\), the lift \(\theta_F\) with function \(F\) at \(\Sigma_N\) satisfies
\[
\theta_{T\mapsto F(k^{-1}Tg)}(\varphi)=\frac{\chi_{j+1,n_{j+1}}(g)}{\chi_{j+1,n_j}(k)}\;k\cdot\theta_F(g^{-1}\varphi),
\]
by the formula for the Weil action of the pair of general linear groups on functions and the equivariance of the theta lift (quoted: [[?lean:New.IsSplitLevel.pairWeilFinite_schrodingerOpAt|`pairWeilFinite_schrodingerOpAt`]], `lift_equivariant`).

*Step 3 (lift laws).* Write \(L_j(F)\) for the lift with function \(F\) in bases of \(L_j,L_{j+1}\). From Step 2: (i) \(b\circ L_j(T\mapsto F(bTa))\circ a=L_j(F)\) for integral invertible \(a,b\), because the lift characters are unramified above \(N\); (ii) with \(d=\operatorname{diag}(1,\dots,1,N^{-1})\), \(d\circ L_j(\text{last-row datum})=\gamma_j\,L_j(\text{direct datum})\circ d\), where \(\gamma_j=\chi_{j+1,n_{j+1}}(D_{\Sigma_N})/\chi_{j+1,n_j}(D_{\Sigma_N})\) is the **commutation factor**; \(\lvert\iota\gamma_j\rvert\le1\) since \(n_j\le n_{j+1}\). These are the two rules of a [[?lean:New.IsSplitLevel.LiftLaw|lift law]].

*Step 4 (one glued double lift).* The glued datum of the double lift \(i\) is a sum over vectors \(y\) modulo \(N\) of tensors of a function of the last column and a character of the last row ([[?lean:New.IsSplitLevel.doubleLiftGluing_eq_sum_schrodingerOpAt|`doubleLiftGluing_eq_sum_schrodingerOpAt`]], quoted). Moving the matrices \(D_{\{w\mid\pi_N\}}\) and \(D_{\Sigma_N\setminus\{w\mid\pi_N\}}\) out of the functions by Step 2 costs the **glued factor**
\[
G_i=\chi_{2i+2,n_{2i+1}}\bigl(D_{\Sigma_N\setminus\{w\mid\pi_N\}}\bigr)\cdot\chi_{2i+1,n_{2i+1}}\bigl(D_{\{w\mid\pi_N\}}\bigr),
\]
and the points \(\delta_{2i+1}\) cancel between the two lifts. So the double lift is \(G_i\cdot d\circ\sum_yL_{2i+1}(\text{char}_y)\circ L_{2i}(\text{col}_y)\). By Step 1, \(\lvert\iota G_i\rvert\le N^{2fb}\) for \(i\le\varrho\): each \(\tau\) contributes to exactly one of the two factors.

*Step 5 (the chain).* By the general statement on chains of glued lifts obeying lift laws, applied to ramified vectors ([[?lean:New.IsSplitLevel.compUpTo_gluedLift_eq_smul|`compUpTo_gluedLift_eq_smul`]], quoted from the file on characters at the level; ramified source forms are ramified vectors by [[proofs/grh/upper-divisibility/up-operator-preserves-source-forms|the earlier proposition]]), the composite of the \(\varrho+1\) double lifts equals
\[
c=\prod_{i\le\varrho}\Bigl(G_i\cdot\#\{\text{primitive vectors on }X_{2i+1}\text{ modulo }N\}\cdot\prod_{l<2i+2}\gamma_l\Bigr)
\]
times the chain of the \(m\) direct lifts after \(U^{\varrho+1}\). Natural numbers and the \(\gamma_l\) have \(N\)-adic absolute value at most \(1\), so \(\lvert\iota c\rvert\le(N^{2fb})^{\varrho+1}=N^{mfb}\). \(\blacksquare\)

*Status.* Steps 1, 3 and the bound on \(c\) were followed in the Lean text. The inputs of Steps 2, 4 and 5, in particular the combinatorial identity `compUpTo_gluedLift_eq_smul` that trades the gluing for powers of \(U\) on ramified vectors, belong to `New/UpperBound/Objects/CharactersAtLevel.lean` (another area) and are quoted.

## References

1. Lean: `New.Data.doubleLiftChain_gluedDoubleLiftDatum_eq_smul_chain` and the declarations listed in the front matter, in `src/New/UpperBound/Divisibility/ValuationAtLevel.lean`.
