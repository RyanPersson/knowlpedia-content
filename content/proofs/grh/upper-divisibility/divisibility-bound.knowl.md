+++
id = "proofs/grh/upper-divisibility/divisibility-bound"
title = "Divisibility bound of a stage at a prime"
kind = "definition"
summary = "A contribution to the exponent of p for the lift of stage j when the long rows at a set of places are removed: predicted divisibility of what remains, plus the full gain per removed box, less a logarithmic term."
aliases = ["divisibility bound", "low columns", "low boxes", "long row", "partner term"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.divisibilityBound", "New.Data.lowColumns", "New.Data.lowBoxes", "New.Data.longRow", "New.Data.partnerTerm"]
lean_files = ["src/New/UpperBound/Divisibility/JetExponent.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]], \(\Phi\) the group of infinite places of \(E\) (there are \(f\)), \(c(\tau,h)\) the [[?lean:New.Data.columnCount|number of columns of height \(h\)]] of the weight at \(\tau\), and \(n_{j+1}=k+(j+1)(t+1)\). Let \(p\) be a prime number, \(j\ge0\) a stage and \(\mathrm{ev}\subset\Phi\) a finite set of places. Put, for \(\tau\in\Phi\),
\[
L(\tau)=\begin{cases}a&\tau\in\Phi_a\setminus\mathrm{ev}\\0&\text{otherwise,}\end{cases}\qquad
c_j(\tau)=\sum_{\substack{h<n_{j+1}\\h\ne1}}c(\tau,h),\qquad
l_j(\tau)=\sum_{\substack{h<n_{j+1}\\h\ne1}}h\,c(\tau,h),
\]
the **long row** after removal, the number of **low columns** and the number of **low boxes**. Let \(\tau^{(e)}=u(-p^{e})\tau\) be the partner of \(\tau\) for the exponent \(e\), \(I_p\) the set of [[?lean:New.positivePartnerExponents|positive partner exponents]], \(v(\pi_p)\) the [[?lean:New.piPrimeValuation|valuation of the prime element]] and \(\gamma_p=v(\pi_p)\sum_{e\in I_p}p^{-e}\) the [[?lean:New.gammaPrime|full gain per box]] (\(0\), \(p/(p^2-1)\), \(1/(2p-2)\) for \(p\) split, inert, \(p=d\)). The **partner term** is, for \(e\in I_p\),
\[
T_{p,j,\mathrm{ev}}(\tau,e)=\Bigl(\frac{L(\tau)}{p^{e}}-L(\tau^{(e)})-c_j(\tau^{(e)})\Bigr)^{+}+\Bigl(\frac{l_j(\tau)}{p^{e}}-l_j(\tau^{(e)})\Bigr)^{+}-\frac{c_j(\tau)}{p^{e}},
\]
and \(0\) for \(e\notin I_p\). The [[?lean:New.predictedDivisibility|predicted divisibility]] of the diagrams with the columns of height one at \(\mathrm{ev}\) removed, read at heights below \(n_{j+1}\), is
\[
\operatorname{pd}_{p,j}(\mathrm{ev})=v(\pi_p)\sum_{e}\sum_{\tau}T_{p,j,\mathrm{ev}}(\tau,e)\;-\;[p=d]\cdot\tfrac12\sum_\tau\Bigl(\min\bigl(L(\tau),L(\tau^{(0)})+c_j(\tau^{(0)})\bigr)+c_j(\tau)+\min\bigl(l_j(\tau),l_j(\tau^{(0)})\bigr)\Bigr).
\]
Let \(B\) be the number of boxes of the diagrams in columns of height below \(n_{j+1}\), before the removal, and \(B'\) the number after. The **divisibility bound** of stage \(j\) at \(p\) for \(\mathrm{ev}\) is
\[
\operatorname{db}_{p,j}(\mathrm{ev})=\operatorname{pd}_{p,j}(\mathrm{ev})+\gamma_p\,(B-B')-f\,n_{j+1}^{3}\bigl(1+\log_p\max(B,1)\bigr).
\]

## Remarks

The source defines these quantities for every natural number \(p\); there \(\log_p y\) means \(\log y/\log p\) with the convention that a quotient by \(0\) is \(0\), so the logarithmic term reduces to \(f\,n_{j+1}^{3}\) for \(p\le1\). Only primes are used.

For \(j<m\) one has \(B-B'=a\cdot\lvert\Phi_a\cap\mathrm{ev}\rvert\): the removed boxes are the \(a\) boxes of the long row at each a-place of \(\mathrm{ev}\). The lower bound of \(\operatorname{db}\) by the gain is [[proofs/grh/upper-divisibility/only-collisions-lose|"only collisions lose"]].

The number \(\operatorname{db}_{p,j}(\mathrm{ev})\) is a contribution to an exponent, not by itself the valuation of a lift:

- For \(\mathrm{ev}=\emptyset\) and \(\chi_K(p)\ne1\), a [[?lean:New.Parameters.standardData|standard datum]] for \(\delta=1\) of the lift \(X_j\to X_{j+1}\) raises \(p\)-adic gauges by at most \(p^{-\operatorname{db}_{p,j}(\emptyset)}\) ([[?lean:New.Parameters.mem_raises_predictedDivisibility|gauge bound by the predicted divisibility]]; see [[proofs/grh/upper-divisibility/one-lift-evaluated-at-a-neighbor|one lift evaluated at a neighbour]], last statement).
- For \(\mathrm{ev}\ne\emptyset\) the [[?lean:New.Parameters.norm_schurJet_jetSeries_le_of_charges|estimate for jets with charges]] bounds a Schur jet by \(p^{\,C-\operatorname{db}_{p,j}(\mathrm{ev})}\), where \(C\) is the number of charged boxes of the row filling, for a charge function that charges, for every partner exponent, each index at the place or at its partner. In the application \(\mathrm{ev}\) is the set of places inducing a marked set, the charges and the entries of the neighbour diagonal cost \(\sum_{\mathfrak l}A_{\mathfrak l}+\mathfrak r\sum c_j\), and the resulting exponent is the Hecke scaling exponents plus the [[proofs/grh/upper-divisibility/neighbor-exponents-and-lift-loss|lift loss]].

## References

1. Lean: `New.Data.divisibilityBound` and the auxiliary definitions listed in the front matter, in `src/New/UpperBound/Divisibility/JetExponent.lean`; `New.predictedDivisibility` in `src/New/Derivatives/Divisibility/Count.lean`.
