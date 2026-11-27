+++
id = "proofs/grh/derivatives-divisibility/the-count"
title = "The count: divisibility of jets along products of minors"
kind = "theorem"
summary = "At a non-split prime, the jet of a series with the normal form along a product of minors has valuation at least the predicted divisibility of the diagrams, less f N^3 (1 + log_p max(B,1))."
aliases = ["the count", "divisibility bound for jets"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.norm_jet_minorProd_le_of_hasNormalForm"]
lean_files = ["src/New/Derivatives/Divisibility/Count.lean"]
proof_status = "full"
+++

**Theorem (the count).** Let \(E=K(\zeta)\) with its group \(\Phi\) of \(f\) infinite places (see the [[proofs/grh/reduction-main/field-e-and-its-places|field \(E\)]]), \(p\) a prime with \(\chi_K(p)\ne1\) and a \(p\)-adic place, \(n,n'\) finite sets and \(N=\lvert n'\rvert\). Let \(F\in\mathbb{C}_p[\![z_{(\tau,b,a)}]\!]\) (\(\tau\in\Phi\), \(b\in n'\), \(a\in n\)) have the [[proofs/grh/derivatives-divisibility/normal-form|normal form]] with data \((I_p^\circ,\operatorname{pr},\varpi,\lambda)\), where \(\operatorname{pr}_e\tau=-p^e\tau\) is the [[proofs/grh/derivatives-divisibility/partner-of-a-place|partner]] and \(\lvert\varpi\rvert=p^{-\rho_p}\). Let \(\kappa\) be column counts with \(B\) boxes in the columns of height below \(N\), \(i'\) a filling, \(y_{\tau,a,k}\in\mathcal{O}\), and \(P_y\) the [[proofs/grh/derivatives-divisibility/product-of-minors|product of minors]]. Then
\[
\bigl\lvert P_y(\partial)F(0)\bigr\rvert\ \le\ p^{-\bigl(\operatorname{pd}(\kappa)-f\,N^3\,(1+\log_p\max(B,1))\bigr)},
\]
where \(\operatorname{pd}(\kappa)\) is the [[proofs/grh/derivatives-divisibility/predicted-divisibility|predicted divisibility]] for \(d\), \(p\), \(\operatorname{pr}\), \(\kappa\), \(N\).

## Proof

This is the [[proofs/grh/derivatives-divisibility/count-with-charges|count with charges]] with no marked places and all charge exponents \(w=0\): the hypothesis on the charges is void, \(\kappa^\circ=\kappa\), and the filling charge is \(0\). \(\blacksquare\)

## Remarks

*Idea.* A linear substitution makes the couplings that matter in degree \(B\) divisible by \(\pi_p\), so the series becomes integral in that degree; Legendre's bound gives about \(1/(p-1)\) per box, the scaling by \(\varpi\) costs \(\rho_p\) per box, and the determinants of the substitution cost the deduction. Each box thus gains about \(\gamma_p\).

By the [[proofs/grh/derivatives-divisibility/normal-form-of-theta-products|normal form of theta products]] the theorem applies to \(F=\prod_j\theta(u_j^\dagger z)^{m_j}H\) for resolutions of the identity integral above \(p\) and for multipliers \(H\) that are integral series in the \(y(u_j^\dagger z)\), \(j\in J\) (the hypothesis \(H\in\mathcal{O}[\![y(\mu z)]\!]\) of that theorem), with the \(\varpi\) of valuation \(\rho_p\) supplied there. Without the integrality of \(H\) the bound fails (take \(H\) a constant of large norm and the empty diagram).

*Literature.* The source notes that one- and two-variable divisibility at inert \(p\) over an imaginary quadratic field is known, and cites as related work: Katz, *Divisibilities, congruences, and Cartier duality* (1981); Chellali, *Congruences entre nombres de Bernoulli–Hurwitz dans le cas supersingulier* (1990); Fujiwara, *On divisibilities of special values of real analytic Eisenstein series* (1988); Bannai–Kobayashi–Yasuda, *Radius of convergence of the p-adic sigma function* (2017).

## References

1. Lean: `New.Parameters.norm_jet_minorProd_le_of_hasNormalForm` in `src/New/Derivatives/Divisibility/Count.lean`.
