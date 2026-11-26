+++
id = "proofs/grh/upper-elementary-divisors/root-data"
title = "Root data: the SL2 of a root and the auxiliary substitution"
kind = "definition"
summary = "For a root (a,a') and a letter i: the copy of SL_2(W) in GL_k(W), the variables X_s and Y_s, the signs, the pole and zero weights, the matrices relating infinity to finite points, and the substitution defining the auxiliary polynomial."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.rootSL", "New.FrobeniusCycle.RootAt", "New.FrobeniusCycle.RootAt.varX", "New.FrobeniusCycle.RootAt.varY", "New.FrobeniusCycle.RootAt.sign", "New.FrobeniusCycle.RootAt.poleOrder", "New.FrobeniusCycle.RootAt.zeroOrder", "New.FrobeniusCycle.RootAt.swapTransvection", "New.FrobeniusCycle.RootAt.mainSubst", "New.FrobeniusCycle.RootAt.crossSubst", "New.FrobeniusCycle.RootAt.mergedCoeff", "New.FrobeniusCycle.RootAt.HasBoundedIncrements", "New.FrobeniusCycle.RootAt.slope", "New.FrobeniusCycle.RootAt.defectWeight_eq", "New.FrobeniusCycle.RootAt.polyAction_swapTransvection_X", "New.FrobeniusCycle.RootAt.swapTransvection_mem_rootSL", "New.rootSL_le_levi"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/RootLemma.lean"]
+++

Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] for \((N,W,R)\) with \(N\ge1\), let \(a\ne a'\) be indices in \(\{0,\dots,k-1\}\) and \(i\in\mathbb{Z}/N\) a letter (a **root at a letter**). Use \(X_s,Y_s,P_s=P^{[s-i]}\) as in the [[proofs/grh/upper-elementary-divisors/defect-of-monomial|defect]].

- **\(\mathrm{SL}_2\) of the root.** \(\mathrm{SL}_2^{a,a'}(W)\subseteq\mathrm{GL}_k(W)\) is the subgroup of matrices of determinant \(1\) that agree with the identity at every entry \((i,j)\) unless both \(i,j\in\{a,a'\}\). It lies in the Levi subgroup \(L_\tau(W)\) of any labelling with \(\tau(a)=\tau(a')\).
- **Signs.** \(\varepsilon_s=-1\) if \(s\) has the parity of \(i\), and \(\varepsilon_s=+1\) otherwise.
- **Weights.** The **pole weight** is \(qP_s\) at \(X_s\) and \(0\) at all other variables; the **zero weight** is \(q\) at \(Y_i\), \(P_s\) at \(Y_s\) for \(s\ne i\), and \(0\) elsewhere. For an exponent \(\alpha\) write \(d(\alpha)\) and \(\nu(\alpha)\) for its pole and zero weights. Then the defect weight is \((\text{zero weight}-\text{pole weight}/q)/(q-1)\), so
\[
\operatorname{def}_{i,a,a'}(\alpha)=\frac{\nu(\alpha)-d(\alpha)/q}{q-1}.
\]
- **Matrices \(g_r\).** For \(r\in W\), \(g_r\in\mathrm{SL}_2^{a,a'}(W)\) is the matrix \(\begin{pmatrix}0&1\\-1&x\end{pmatrix}\) in the rows and columns \(a,a'\), where \(x=-r\) if \(i\) is even and \(x=r\) if \(i\) is odd (the product of the transposition of \(a,a'\), the transvection with entry \(x\) at \((a,a')\), and the diagonal matrix with \(-1\) at \(a\)). Under the [[proofs/grh/upper-elementary-divisors/twisted-action|twisted action]], up to a sign \(\pm1\) depending only on the variable (\(-1\) exactly for variables with index \(a\)),
\[
g_r\cdot X_s=\pm Y_s,\qquad g_r\cdot Y_s=\pm\bigl(X_s+\varepsilon_s\,\iota_s(r)\,Y_s\bigr),
\]
and \(g_r\) fixes the other variables up to that sign.
- **Auxiliary substitution.** With a new variable \(t\), \(\mathrm{S}\colon R[x_{b,s}]\to R[t][x_{b,s}]\) is the \(R\)-algebra map
\[
Y_i\mapsto X_i,\quad X_i\mapsto t^{q}X_i,\qquad X_s\mapsto t^{qP_s}X_s-\varepsilon_s t^{P_s}Y_s,\quad Y_s\mapsto Y_s-\varepsilon_sX_s\quad(s\ne i),
\]
fixing the other variables. Its **main part** \(\mathrm{S}_0\) is \(Y_i\mapsto X_i\), \(z\mapsto t^{\text{pole weight of }z}z\) otherwise; \(\mathrm{S}=\mathrm{S}_0-\) (cross terms).
- **Merged coefficient.** For an exponent \(\alpha\) let \(\bar\alpha\) be obtained by moving the exponent of \(Y_i\) onto \(X_i\). For \(p\in R[t][x]\), \(\Phi_\alpha(p)\in R[t]\) is the coefficient of \(x^{\bar\alpha}\) in \(p\).
- **Bounded increments.** Real weights \(c\) of the variables have bounded increments if \(\tfrac12\le c(Y_s)-c(X_s)\le1\) for all \(s\). The **slope** is \(\rho=(c(Y_i)-c(X_i))/q>0\). Then \(P_s\rho\le\tfrac15\) for all \(s\) (as \(5P_s\le q\)) and \(qP_s\rho\ge2\) for \(s\ne i\) (as \(P_s\ge5\), \(q\rho\ge\frac12\)).

## References

1. Lean: `New.rootSL`, `New.FrobeniusCycle.RootAt`, `New.FrobeniusCycle.RootAt.varX`, `New.FrobeniusCycle.RootAt.varY`, `New.FrobeniusCycle.RootAt.sign`, `New.FrobeniusCycle.RootAt.poleOrder`, `New.FrobeniusCycle.RootAt.zeroOrder`, `New.FrobeniusCycle.RootAt.swapTransvection`, `New.FrobeniusCycle.RootAt.mainSubst`, `New.FrobeniusCycle.RootAt.crossSubst`, `New.FrobeniusCycle.RootAt.mergedCoeff`, `New.FrobeniusCycle.RootAt.HasBoundedIncrements`, `New.FrobeniusCycle.RootAt.slope`, `New.FrobeniusCycle.RootAt.defectWeight_eq`, `New.FrobeniusCycle.RootAt.polyAction_swapTransvection_X`, `New.FrobeniusCycle.RootAt.swapTransvection_mem_rootSL`, `New.rootSL_le_levi` in `src/New/UpperBound/ElementaryDivisors/RootLemma.lean`.
