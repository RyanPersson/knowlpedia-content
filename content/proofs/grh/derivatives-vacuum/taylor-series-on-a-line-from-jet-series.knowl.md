+++
id = "proofs/grh/derivatives-vacuum/taylor-series-on-a-line-from-jet-series"
title = "The jet series restricts to the Taylor series of the theta function on every line"
kind = "lemma"
summary = "For a vector f of the finite part of a space with all signs 1, the Taylor series at 0 of the entire theta function of f along the line spanned by v, at scale a, is the jet series of f with v_p X substituted for the variable X_p."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Space.taylor_line_eq_subst_jetSeries", "New.Space.iteratedDeriv_integral_exp_mul_realVac"]
lean_files = ["src/New/Derivatives/Vacuum/TightFrames.lean"]
proof_status = "outline"
+++

Let \(E\) be a CM field with a [[?c:CM type|CM type]] \(\Phi\) and [[?lean:New.WeilData|Weil data]], let \(n\) be a finite index set, and let \(V\) be a [[?lean:New.Space|hermitian space]] over \(E\) with index set \(n\) and all signs \(+1\). Write \(\mathcal{S}(V)\) for the [[?lean:New.𝒮|Banach model of the Weil representation]] of \(V\) (a space of integrable functions on \(\mathbb{A}_E^{\,n}\) with the \(L^1\) norm, on which adelic vectors \(x\) act by the isometries \(\varrho(x)\) of the Heisenberg representation), \(\theta\) for the [[?lean:New.Space.θ|theta functional]], a bounded linear form on \(\mathcal{S}(V)\), and \(Z=\mathbb{C}^{\Sigma\times n}\), \(\Sigma\) the set of infinite places of \(E\). A vector \(f\in\mathcal{S}(V)\) is evaluated at an adelic vector \(x\) by \(f(x):=\theta(\varrho(x)f)\); thus \(\lvert f(x)\rvert\le\lVert\theta\rVert\,\lVert f\rVert\). For \(f\in\mathcal{S}(V)\) recall

* the [[?lean:New.Space.entireTheta|entire theta function]] \(\Theta_f(y)=\theta(\varrho(y)f)\,e^{\lvert y\rvert^2/2}\), \(y\in Z\) a real vector in Fock coordinates. It is defined for every \(f\); it is an entire function of \(y\) when all signs are \(+1\) and \(f\) is fixed by the projection to the real vacuum (Lean `New.Space.differentiable_entireTheta`), and the latter holds for \(f\) in the finite part defined below;
* the [[?lean:New.Space.jetSeries|jet series]] \(J_a(f)\in\mathbb{C}[\![X_p:p\in\Sigma\times n]\!]\) for \(a\in\mathbb{C}\), whose coefficient of \(X^k\) is \(a^{\lvert k\rvert}/k!\) times the value of \(\theta\) at \(f\) tensored at the real places with the Fock vector of the monomial \(z^k\) (\(\lvert k\rvert=\sum_pk_p\), \(k!=\prod_pk_p!\));
* the [[?lean:New.Space.finitePart|finite part]] of \(V\), the span of the translates of the vacuum under the finite Heisenberg operators.

**Lemma.** Let \(f\) lie in the finite part of \(V\), \(a\in\mathbb{C}\) and \(v\in Z\). Then the [[?c:Taylor series|Taylor series]] at \(t=0\) of the function \(t\mapsto\Theta_f(a\,t\,v)\) of one complex variable is obtained from \(J_a(f)\) by the [[?c:Substitution of formal power series|substitution]] \(X_p\mapsto v_p\,X\):
\[ \sum_{k\ge0}\frac{1}{k!}\frac{d^k}{dt^k}\Theta_f(atv)\Big|_{t=0}X^k=J_a(f)\bigl((v_pX)_{p}\bigr). \]

## Proof

Let \(\mu\) be Lebesgue measure on \(Z\) divided by \(\pi^{\lvert\Sigma\times n\rvert}\), and put
\[ g(w)=e^{-\lvert w\rvert^2/2}\,f(\operatorname{realVec}w),\qquad L(w)=a\sum_{p}v_p\,\overline{w_p}, \]
where \(\operatorname{realVec}w\) is the adelic vector with finite part \(0\) and real part \(w\) rescaled at each place. The proof compares both sides with \(\int L^k g\,d\mu\).

*Step 1 (asserted; Lean `New.Space.entireTheta_eq_integral`).* Because all signs are \(1\) and \(f\) is fixed by the projection to the real vacuum (true on the finite part), the reproducing formula of the Fock model gives, for all \(t\in\mathbb{C}\),
\[ \Theta_f(atv)=\int_Z e^{tL(w)}g(w)\,d\mu(w). \]

*Step 2 (differentiation under the integral; proved in full).* For a continuous conjugate-linear form \(L\) the function \(I(t)=\int e^{tL}g\,d\mu\) has \(I^{(k)}(0)=\int L^kg\,d\mu\). Indeed \(\lvert g(w)\rvert\le e^{-\lvert w\rvert^2/2}\lVert\theta\rVert\lVert f\rVert\) (the evaluation \(f(\operatorname{realVec}w)=\theta(\varrho(\operatorname{realVec}w)f)\) is bounded by the norm of \(\theta\), \(\varrho\) being isometric) and \(\lvert L(w)\rvert\le\lVert L\rVert\lvert w\rvert\), so the terms of \(e^{tL}g=\sum_j (tL)^jg/j!\) are dominated by the terms of the series with sum \(e^{\lvert t\rvert\lVert L\rVert\lvert w\rvert}e^{-\lvert w\rvert^2/2}\lVert\theta\rVert\lVert f\rVert\), which is integrable. By [[?c:Dominated convergence theorem|dominated convergence]], \(I(t)=\sum_j t^j\int L^jg\,d\mu/j!\) for every \(t\), a power series expansion on all of \(\mathbb{C}\); its \(k\)-th derivative at \(0\) is \(\int L^kg\,d\mu\).

*Step 3 (asserted; Lean `New.Space.jet_jetSeries_eq_theta`, `New.Space.theta_integrated`, `New.jet_subst_linearSeries`).* Let \(T\) be the right-hand side of the lemma. Its \(k\)-th coefficient times \(k!\) is the [[?lean:New.jet|jet]] of \(T\) along \(X^k\), which by the chain rule for jets under a linear substitution is the jet of \(J_a(f)\) along the polynomial \(Q=(\sum_pv_pX_p)^k\). The jet of \(J_a(f)\) along a polynomial \(Q\) equals \(\int Q(a\bar w)\,g(w)\,d\mu(w)\), and \(Q(a\bar w)=L(w)^k\).

Steps 1–3 give \(k!\,[X^k]T=\int L^kg\,d\mu=\frac{d^k}{dt^k}\Theta_f(atv)|_{t=0}\).

## References

1. Lean: `New.Space.taylor_line_eq_subst_jetSeries`, `New.Space.iteratedDeriv_integral_exp_mul_realVac` in `src/New/Derivatives/Vacuum/TightFrames.lean`.
