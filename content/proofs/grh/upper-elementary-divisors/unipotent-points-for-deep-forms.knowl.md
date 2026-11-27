+++
id = "proofs/grh/upper-elementary-divisors/unipotent-points-for-deep-forms"
title = "Points attached to unipotent matrices, and the orders of the deep variables"
kind = "construction"
summary = "For k = 2r + m: the positions in rows below r and columns at least r, the unipotent matrix 1 + A with given residues at these positions, the point of affine space it defines, and the degree given to each variable."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.entryRow", "New.FrobeniusCycle.entryCol", "New.FrobeniusCycle.entryCoeff", "New.FrobeniusCycle.entryFormValue", "New.FrobeniusCycle.deepOrder", "New.FrobeniusCycle.specializeShallow", "New.FrobeniusCycle.prod_deepOrder_le", "New.FrobeniusCycle.sum_deepIndicator", "New.FrobeniusCycle.exists_specializeShallow_polyAction_X_eq_sub", "New.FrobeniusCycle.specializeShallow_injective"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/Depth.lean"]
+++

Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] for \((N,W,K)\) with \(N\ge1\) and \(K\) a field, and let \(k=2r+m\). Let \(\kappa_W\) be the residue field of \(W\), with \(q\) elements; fix a lift \(\tilde y\in W\) of each \(y\in\kappa_W\). Let \(L\) be a field and \(x\colon K[x_{b,s}]\to L\) a ring homomorphism (in the application \(L\) is the fraction field of \(K[x_{b,s}]\) and \(x\) the inclusion).

- **Positions.** \(\mathcal{P}=\{(a,l):0\le a<r,\ 0\le l\le m\}\), a set of \(r(m+1)\) elements. The position \(t=(a,l)\) has row \(\operatorname{row}(t)=a<r\) and column \(\operatorname{col}(t)=a+r\) if \(l=0\), \(\operatorname{col}(t)=k-l\ (\ge2r)\) if \(l\ge1\). The map \(t\mapsto(\operatorname{row}t,\operatorname{col}t)\) is injective.
- **Unipotent matrices.** For \(y\in\kappa_W^{\mathcal{P}}\) let \(A_y\in M_k(W)\) have the entry \(\tilde y_t\) at \((\operatorname{row}t,\operatorname{col}t)\) and \(0\) elsewhere. As all rows are \(<r\) and all columns \(\ge r\), \(A_y^{2}=0\) and \(g_y=1+A_y\in\mathrm{GL}_k(W)\) with \(g_y^{-1}=1-A_y\).
- **Coefficients.** For a variable \(v=x_{b,s}\) and a position \(t\), \(\epsilon(v,t)\in K[x]\) is \(x_{\operatorname{row}t,\,s}\) if \(s\) is even and \(b=\operatorname{col}t\); \(-x_{\operatorname{col}t,\,s}\) if \(s\) is odd and \(b=\operatorname{row}t\); and \(0\) otherwise. A direct computation with the [[proofs/grh/upper-elementary-divisors/twisted-action|twisted action]] (for even \(s\) the matrix of \(g_y^{-1}\) is \(\iota_s(1-A_y)\), for odd \(s\) it is \(\iota_s(1+{}^{t}A_y)\)) gives
\[
g_y^{-1}\cdot v=v-\sum_{t\in\mathcal{P}}\iota_s(\tilde y_t)\,\epsilon(v,t).
\]
The right side differs from \(v\) only when \(v\) is [[proofs/grh/upper-elementary-divisors/depth-of-monomial|deep for \(r\)]], and each \(\epsilon(v,t)\) is \(0\) or \(\pm\) a variable that is not deep.
- **Points.** \(z_y\in L^{\{0..k-1\}\times\mathbb{Z}/N}\) has the coordinate \(z_y(v)=\sum_t x(\iota_s(\tilde y_t))\,x(\epsilon(v,t))\) at \(v=x_{b,s}\).
- **Specialisation.** \(\operatorname{sp}\colon K[x_{b,s}]\to L[x_{b,s}]\) is the ring homomorphism that keeps the deep variables and sends the constants and the variables that are not deep to their images under \(x\). Then \(\operatorname{sp}(g_y^{-1}\cdot v)=v-z_y(v)\) for every deep variable \(v\). If \(x\) is injective, so is \(\operatorname{sp}\) (since \(x\) is \(\operatorname{sp}\) followed by evaluation of every variable \(v\) at \(x(v)\)).
- **Orders.** \(\kappa(v)=P^{2r}\) if \(v=x_{b,s}\) is deep and \(b\ge2r\); \(\kappa(v)=P\) if \(v\) is deep and \(b<2r\); \(\kappa(v)=1\) if \(v\) is not deep.

## Properties

For each index \(b\), the variable \(x_{b,s}\) is deep for exactly \(\lfloor N/2\rfloor\) letters \(s\) (shifting \(s\) by one exchanges deep and not deep, so twice the number is \(N\)). Hence
\[
\prod_v\kappa(v)=P^{\lfloor N/2\rfloor(2r\cdot1+m\cdot2r)}=P^{\lfloor N/2\rfloor\cdot2\cdot r(m+1)}\le P^{N\,r(m+1)}=q^{\,r(m+1)}=\#\kappa_W^{\mathcal{P}} .
\]

## References

1. Lean: `New.FrobeniusCycle.entryRow`, `New.FrobeniusCycle.entryCol`, `New.FrobeniusCycle.entryCoeff`, `New.FrobeniusCycle.entryFormValue`, `New.FrobeniusCycle.deepOrder`, `New.FrobeniusCycle.specializeShallow`, `New.FrobeniusCycle.prod_deepOrder_le`, `New.FrobeniusCycle.sum_deepIndicator`, `New.FrobeniusCycle.exists_specializeShallow_polyAction_X_eq_sub`, `New.FrobeniusCycle.specializeShallow_injective` in `src/New/UpperBound/ElementaryDivisors/Depth.lean`.
