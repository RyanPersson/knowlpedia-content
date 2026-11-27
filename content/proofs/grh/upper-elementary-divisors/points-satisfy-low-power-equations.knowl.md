+++
id = "proofs/grh/upper-elementary-divisors/points-satisfy-low-power-equations"
title = "The unipotent points satisfy equations with small leading powers"
kind = "lemma"
summary = "In characteristic p, each power z(v)^kappa(v) of a coordinate of a unipotent point is the value of a fixed polynomial with monomials of cost below 1, and the point determines the residues."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.lowPowerForms", "New.FrobeniusCycle.exists_eval_entryFormValue_eq_pow_deepOrder", "New.FrobeniusCycle.exists_eval_entryFormValue_eq_dotProduct", "New.FrobeniusCycle.mem_lowPowerForms", "New.FrobeniusCycle.single_mem_lowPowerForms_of_ne_zero", "New.FrobeniusCycle.single_zero_mem_lowPowerForms", "New.FrobeniusCycle.entryFormValue_pow", "New.FrobeniusCycle.entryFormValue_injective", "New.det_X_pow_ne_zero", "New.exists_eval_eq_dotProduct_of_mem_span", "New.FrobeniusCycle.exists_div_two_eq_and_isEven_sub", "New.FrobeniusCycle.residue_eq_of_embedding_eq"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/Depth.lean"]
proof_status = "full"
+++

**Lemma.** In the setting of the [[proofs/grh/upper-elementary-divisors/unipotent-points-for-deep-forms|unipotent points]] (\(k=2r+m\), \(N\ge1\)), assume \(K\) and \(L\) are fields of characteristic \(p\) and \(x\colon K[x_{b,s}]\to L\) is injective. Define the **cost** of a monomial \(x^{\alpha}\) as \(\sum_v\alpha(v)/\kappa(v)\).

1. For every letter \(i\) and every vector \(u\in L^{\mathcal{P}}\) there is \(G\in L[x_{b,s}]\), all of whose monomials have cost \(<1\), with \(G(z_y)=\sum_tu_t\,x(\iota_i(\tilde y_t))\) for all \(y\in\kappa_W^{\mathcal{P}}\).
2. For every variable \(v\) there is \(G_v\in L[x_{b,s}]\), all of whose monomials have cost \(<1\), with \(G_v(z_y)=z_y(v)^{\kappa(v)}\) for all \(y\).
3. The map \(y\mapsto z_y\) is injective.

## Proof

*Powers of coordinates.* In characteristic \(p\) the congruence of a Frobenius cycle is an equality \(\iota_{s+j}(u)=\iota_s(u)^{P^{j}}\), and \(P^{j}\)-th powers are additive, so for \(v=x_{b,s}\)
\[
z_y(v)^{P^{j}}=\sum_tx(\epsilon(v,t))^{P^{j}}\,x(\iota_{s+j}(\tilde y_t)).\tag{*}
\]
*Spanning.* Fix \(i\). Let \(\Lambda_i\subseteq L^{\mathcal{P}}\) (the space of **low power forms** at the letter \(i\)) be the span of the vectors \(\lambda_{v,j}=\bigl(x(\epsilon(v,t))^{P^{j}}\bigr)_t\) over the pairs \((v,j)\), \(v=x_{b,s}\), with \(s+j=i\) and \(P^{j}<\kappa(v)\). We claim \(\Lambda_i=L^{\mathcal{P}}\).

(a) *Unit vector at \((b,l)\), \(l\ge1\).* Let \(c=k-l\ge2r\); the positions with column \(c\) are exactly \((b',l)\), \(b'<r\). Since parities alternate, for each \(u<r\) one of \(J\in\{2u,2u+1\}\) has \(i-J\) even; call it \(J_u\). The variable \(v_u=x_{c,\,i-J_u}\) is deep with \(\kappa(v_u)=P^{2r}>P^{J_u}\), so \(\lambda_{v_u,J_u}\in\Lambda_i\); its entry at \((b',l)\) is \(x\bigl(x_{b',\,i-J_u}^{P^{J_u}}\bigr)\) and its other entries vanish. The \(r\times r\) matrix \(M=(x_{b',\,i-J_u}^{P^{J_u}})_{u,b'}\) over \(K[x]\) has nonzero determinant: in the Leibniz expansion the permutation \(\pi\) contributes the monomial \(\prod_{b'}x_{b',\,i-J_{\pi(b')}}^{P^{J_{\pi(b')}}}\), and these monomials are pairwise distinct because the exponents \(P^{J_u}\) are positive and distinct (\(u=\lfloor J_u/2\rfloor\)); in particular the monomial of the identity has coefficient \(1\). As \(x\) is injective, \(x(M)\) is invertible over \(L\), and the unit vector at \((b,l)\) is a combination of its rows.

(b) *Unit vector at \((b,0)\).* Let \(v=x_{b+r,i}\) if \(i\) is even and \(v=x_{b,i}\) if \(i\) is odd. It is deep with \(\kappa(v)=P>P^{0}\), so \(\lambda_{v,0}\in\Lambda_i\). Its entry at \((b,0)\) is \(\pm x(\text{a variable})\ne0\), its entries at \((b',0)\), \(b'\ne b\), vanish, and its remaining entries are at positions with \(l\ge1\), handled by (a).

*Proof of 1.* By \((*)\), for a generator \(u=\lambda_{v,j}\) we have \(\sum_tu_tx(\iota_i(\tilde y_t))=z_y(v)^{P^{j}}\), the value at \(z_y\) of the monomial \(v^{P^{j}}\) of cost \(P^{j}/\kappa(v)<1\). Linear combinations of such monomials give all \(u\in\Lambda_i=L^{\mathcal{P}}\).

*Proof of 2.* \(\kappa(v)=P^{j}\) for some \(j\); by \((*)\), \(z_y(v)^{\kappa(v)}\) is a linear form in \((x(\iota_{s+j}(\tilde y_t)))_t\) with coefficients independent of \(y\); apply 1 with \(i=s+j\).

*Proof of 3.* By 1 with \(i=0\) and \(u\) the unit vector at \(t\), \(x(\iota_0(\tilde y_t))\) is a function of \(z_y\). As \(x\) is injective, \(z_y=z_{y'}\) gives \(\iota_0(\tilde y_t-\tilde y'_t)=0\); a unit of \(W\) maps to a unit of \(K\), so \(\tilde y_t-\tilde y'_t\) is not a unit and \(y_t=y'_t\). \(\square\)

## References

1. Lean: `New.FrobeniusCycle.lowPowerForms`, `New.FrobeniusCycle.exists_eval_entryFormValue_eq_pow_deepOrder`, `New.FrobeniusCycle.exists_eval_entryFormValue_eq_dotProduct`, `New.FrobeniusCycle.mem_lowPowerForms`, `New.FrobeniusCycle.single_mem_lowPowerForms_of_ne_zero`, `New.FrobeniusCycle.single_zero_mem_lowPowerForms`, `New.FrobeniusCycle.entryFormValue_pow`, `New.FrobeniusCycle.entryFormValue_injective`, `New.det_X_pow_ne_zero`, `New.exists_eval_eq_dotProduct_of_mem_span`, `New.FrobeniusCycle.exists_div_two_eq_and_isEven_sub`, `New.FrobeniusCycle.residue_eq_of_embedding_eq` in `src/New/UpperBound/ElementaryDivisors/Depth.lean`.
