+++
id = "proofs/grh/derivatives-divisibility/count-with-charges"
title = "The count with charges"
kind = "theorem"
summary = "The jet of a series with the normal form along a product of minors has, after adding the charges on the rows, valuation at least the predicted divisibility of the diagrams without their marked columns, up to an explicit error."
aliases = ["count with charges", "charge exponent", "filling charge"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.norm_jet_minorProd_le_of_charges", "New.Parameters.norm_jet_minorProd_le_of_isChargeExponent", "New.IsChargeExponent", "New.fillingCharge", "New.directionSubst", "New.columnDetProd", "New.DirectionVar", "New.jet_columnDetProd_subst", "New.norm_jet_columnDetProd_subst", "New.isHomogeneous_columnDetProd", "New.dvd_subst_coupling", "New.dvd_subst_coupling_directionSubst", "New.dvd_subst_coupling_directionSubst_of_charges", "New.card_directionVar_le", "New.linSubst_directionSubst_X", "New.fillingCharge_congr"]
lean_files = ["src/New/Derivatives/Divisibility/Count.lean"]
proof_status = "full"
+++

**Theorem (the count with charges).** Let \(E=K(\zeta)\) with its group \(\Phi\) of \(f=\lvert\Phi\rvert\) infinite places (see the [[proofs/grh/reduction-main/field-e-and-its-places|field \(E\)]]), and let \(p\) be a prime with \(\chi_K(p)\ne1\) and a \(p\)-adic place. Let \(n,n'\) be finite sets, \(N=\lvert n'\rvert\), and let \(F\in\mathbb{C}_p[\![z_{(\tau,b,a)}:\tau\in\Phi,b\in n',a\in n]\!]\) have the [[proofs/grh/derivatives-divisibility/normal-form|normal form]] with data \((I_p^\circ,\operatorname{pr},\varpi,\lambda)\), where \(\operatorname{pr}_e\tau=-p^e\tau\) is the [[proofs/grh/derivatives-divisibility/partner-of-a-place|partner]], the index set is \(\Phi\times c\) with \(c=n'\times n\), and \(\lvert\varpi\rvert=p^{-\rho_p}\). Let \(\kappa\) be column counts with \(B\) boxes, \(i'\) a filling, \(y_{\tau,a,k}\in\mathcal{O}\), and \(P_y\) the [[proofs/grh/derivatives-divisibility/product-of-minors|product of minors]]. Let \(\mathrm{ev}\subseteq\Phi\) be a finite set of marked places and let \(w(\tau,h,b)\in\mathbb{N}\) (place, height, row) be **charge exponents** such that, for all \(e\in I_p^\circ\), \(\tau\in\Phi\), \(h\ge0\), \(b\in n'\), with \(\tau'=\operatorname{pr}_e\tau\):
\[
\kappa(\tau,1)\ne0,\ \ \kappa(\tau',h)\neq 0,\ \ \bigl(\tau\in\mathrm{ev}\ \text{or}\ (h=1\ \text{and}\ \tau'\in\mathrm{ev})\bigr)\ \Longrightarrow\ w(\tau,1,b)\ne0\ \text{or}\ w(\tau',h,b)\neq 0 .
\]
Let \(w(i')=\sum_\tau\sum_{h<N}\sum_{j<\kappa(\tau,h)}\sum_{b<h}w\bigl(\tau,h,i'(\tau,h,j,b)\bigr)\) be the **filling charge**. Then, with \(v\) the valuation of \(\mathbb{C}_p\) and \(\kappa^\circ\), \(\operatorname{pd}\) as in the [[proofs/grh/derivatives-divisibility/predicted-divisibility|predicted divisibility]],
\[
v\bigl(P_y(\partial)F(0)\bigr)+w(i')\ \ge\ \operatorname{pd}(\kappa^\circ)+\gamma_p\bigl(B-B(\kappa^\circ)\bigr)-f\,N^3\bigl(1+\log_p\max(B,1)\bigr).
\]
(If the jet vanishes the statement is void; the source states it as an upper bound for the norm.)

**Truncated form.** Put \(\lfloor\log_p0\rfloor=0\). If the implication above holds for all \(\tau,h,b\) without the two conditions on \(\kappa\), then more precisely, with the [[proofs/grh/derivatives-divisibility/deduction-term|deduction terms]] \(D_{\mathrm{ev}}\),
\[
v\bigl(P_y(\partial)F(0)\bigr)+w(i')\ \ge\ \gamma_pB-v(\pi_p)\sum_{\substack{e\in I_p^\circ\\ e\le\lfloor\log_pB\rfloor}}\sum_{\tau}D_{\mathrm{ev}}(\tau,\operatorname{pr}_e\tau,e)-f\,N^3\bigl(\lfloor\log_pB\rfloor+1\bigr).
\]

## Proof

We prove the truncated form first. Let \(\pi=\iota_p\pi_p\); it divides \(p\). Let \(S=\{e\in I_p^\circ:e\le\lfloor\log_pB\rfloor\}\) and \(D=\sum_{e\in S}\sum_\tau D_{\mathrm{ev}}(\tau,\operatorname{pr}_e\tau,e)\).

**Step 1: new directions and the chain rule.** The [[proofs/grh/derivatives-divisibility/change-of-directions|change of directions]], applied to \(\pi\), \(\operatorname{pr}\), \(S\), \(N\), \(\kappa\), \(\mathrm{ev}\), \(y\), gives matrices \(g_{\tau,h}\) and new directions \(\beta_{\tau,h,k}\in\mathcal{O}^n\) whose pairings are divisible by \(\pi\) outside the exempt pairs, with \(\lvert\pi\rvert^D\le\prod_\tau\prod_{h<N}\lvert\det g_{\tau,h}\rvert^{\kappa(\tau,h)}\). Introduce new variables \(s_{\tau,h,k,b}\) (\(\tau\in\Phi\), \(h<N\), \(k<h\), \(b\in n'\)); there are at most \(fN^3\) of them. Consider the linear substitution
\[
z_{(\tau,b,a)}(s)=\sum_{h<N}\sum_{k<h}p^{\,w(\tau,h,b)}\,(\beta_{\tau,h,k})_a\;s_{\tau,h,k,b},
\]
the series \(G(s)=F(\varpi\,z(s))\), and the polynomial
\[
P_*(s)=\prod_\tau\prod_{h<N}\prod_{j<\kappa(\tau,h)}\det\bigl(s_{\tau,h,k,\,i'(\tau,h,j,b)}\bigr)_{0\le b,k<h},
\]
homogeneous of degree \(B\) with integer coefficients. For a linear substitution \(z=Ms\), the [[?lean:New.jet_subst_linearSeries|chain rule for jets]] says that the jet of \(F(Ms)\) along \(Q(s)\) is the jet of \(F\) along the polynomial obtained from \(Q\) by replacing each \(s_o\) by \(\sum_xM_{x,o}z_x\). Here \(s_{\tau,h,k,b}\) is replaced by \(\varpi p^{w(\tau,h,b)}\sum_a(\beta_{\tau,h,k})_az_{(\tau,b,a)}\), and since \(\beta_{\tau,h,k}=\sum_{k'}(g_{\tau,h})_{k,k'}y_{\tau,\cdot,k'}\), the matrix in the determinant of a column of height \(h\) at \(\tau\) becomes
\[
\operatorname{diag}\bigl(\varpi p^{w(\tau,h,r_b)}\bigr)_b\cdot\Bigl(\sum_ay_{\tau,a,k'}z_{(\tau,r_b,a)}\Bigr)_{b,k'}\cdot g_{\tau,h}^{\mathsf T},\qquad r_b=i'(\tau,h,j,b).
\]
Taking determinants and the product over the columns,
\[
\lvert P_*(\partial)G(0)\rvert=\lvert\varpi\rvert^{B}\,p^{-w(i')}\prod_\tau\prod_{h<N}\lvert\det g_{\tau,h}\rvert^{\kappa(\tau,h)}\cdot\lvert P_y(\partial)F(0)\rvert .\tag{1}
\]

**Step 2: \(G\) is integral in degree \(B\).** By Step 4 of the [[proofs/grh/derivatives-divisibility/normal-form-of-theta-products|normal form of theta products]], \(\lvert c_\varpi\pi\rvert=p^{-1/(p-1)}\). By the [[proofs/grh/derivatives-divisibility/normal-form-integrality|integrality criterion]], applied to the linear forms \(Z_x=z_x(s)\) (integral, without constant term), it suffices that \(\Gamma_e(z(s))\equiv0\pmod\pi\) for \(e\in S\). Write \(z_x(s)=\sum_oM_{x,o}s_o\). As \(p^e\)-th powers are additive modulo \(\pi\),
\[
\Gamma_e(z(s))=\sum_{x=(\tau,b,a)}z_x(s)^{p^e}z_{(\operatorname{pr}_e\tau,b,a)}(s)\equiv\sum_{o,o'}\Bigl(\sum_xM_{x,o}^{\,p^e}M_{(\operatorname{pr}_e\tau,b,a),o'}\Bigr)s_o^{p^e}s_{o'} .
\]
For \(o=(\tau,h,k,b)\) and \(o'=(\tau',h',k',b')\) the inner coefficient vanishes unless \(\tau'=\operatorname{pr}_e\tau\) and \(b'=b\), and then equals
\[
p^{\,w(\tau,h,b)p^e+w(\tau',h',b)}\ \sum_{a}(\beta_{\tau,h,k})_a^{\,p^e}(\beta_{\tau',h',k'})_a .
\]
If the pair \((h,h')\) is not exempt, \(\pi\) divides the pairing. If it is exempt, then \(h=1\) and \(\tau\in\mathrm{ev}\), or \(h=h'=1\) and \(\tau'\in\mathrm{ev}\); by the hypothesis on the charges \(w(\tau,1,b)\ne0\) or \(w(\tau',h',b)\ne0\), so \(p\), hence \(\pi\), divides the power of \(p\) in front.

**Step 3: Legendre's bound.** By Step 2 and [[proofs/grh/derivatives-divisibility/legendre-bound-for-jets|Legendre's bound]] in at most \(fN^3\) variables, \(v(P_*(\partial)G(0))\ge B/(p-1)-fN^3(\lfloor\log_pB\rfloor+1)\). By (1), \(v(\varpi)=\rho_p\) and \(v(\prod\det g^{\kappa})\le v(\pi_p)D\),
\[
v\bigl(P_y(\partial)F(0)\bigr)\ge\frac{B}{p-1}-\rho_pB-w(i')-v(\pi_p)D-fN^3(\lfloor\log_pB\rfloor+1),
\]
and \(\gamma_p=\tfrac1{p-1}-\rho_p\). This is the truncated form.

**Step 4: the theorem.** Replace \(w\) by \(w'\) with \(w'(\tau,h,b)=1\) if \(\kappa(\tau,h)=0\) and \(w'=w\) otherwise. Then \(w'\) satisfies the unconditional hypothesis (if one of the two heights does not occur, its exponent is \(1\)), and \(w'(i')=w(i')\), since only heights with \(\kappa(\tau,h)\ne0\) have boxes. Apply the truncated form, bound the deduction by [[proofs/grh/derivatives-divisibility/predicted-divisibility|\(\gamma_pB(\kappa^\circ)-\operatorname{pd}(\kappa^\circ)\)]], and use \(\lfloor\log_pB\rfloor\le\log_p\max(B,1)\). \(\blacksquare\)

## References

1. Lean: `New.Parameters.norm_jet_minorProd_le_of_isChargeExponent`, `New.Parameters.norm_jet_minorProd_le_of_charges`, `New.IsChargeExponent`, `New.fillingCharge`, `New.directionSubst`, `New.columnDetProd`, `New.jet_columnDetProd_subst`, `New.dvd_subst_coupling_directionSubst_of_charges` in `src/New/Derivatives/Divisibility/Count.lean`.
