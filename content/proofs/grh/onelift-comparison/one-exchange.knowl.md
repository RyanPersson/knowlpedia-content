+++
id = "proofs/grh/onelift-comparison/one-exchange"
title = "One exchange: confining the twist to a pair of equal rank"
kind = "lemma"
summary = "Given the exchange identity on E^b + W-prime, for an invariant datum the class sum of the kernel on E^n equals the integral over U(V-prime) of the kernel of (V-prime, E^b) with datum chi of det times the kernel of (V-prime, W-prime)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Rows.isRapid_modKernel", "New.Rows.hasLeftInv_of_isUnit_det_toRows\u2081", "New.Rows.areMatched_det_mul", "New.Rows.integrable_and_mul_stdClassSum_eq_integral_mul", "New.Rows.mul_stdClassSum_eq_integral_mul_modKernel"]
lean_files = ["src/New/OneLift/ComparisonOperator/OneExchange.lean"]
proof_status = "outline"
+++

Throughout, \(E\) is a [[?c:CM field|CM field]] with a CM type and [[?c:Weil representation|Weil data]]; a [[?lean:New.Modulus|modulus]] \(\mathfrak m\) is a nonzero ideal of \(\mathcal{O}_E\) prime to its complex conjugate; for [[?c:Hermitian space|hermitian spaces]] \(S,T\) over \(E\) (with adelic points, [[?lean:New.Space|spaces]]) \(\Theta^{S,T}_{\Psi,P}(g,h)\) denotes the [[?lean:New.modKernel|theta kernel modulo \(\mathfrak m\)]] of the pair \((S,T)\) at \(g\in U(S)(\mathbb{A})\), \(h\in U(T)(\mathbb{A})\), for a function \(\Psi\) on matrices over \(\mathcal{O}_E/\mathfrak m\) (of size \(\operatorname{rk}T\times\operatorname{rk}S\)), a polynomial \(P\) in the Fock variables, and two twisting automorphic characters of \(U(1)\) which are suppressed from the notation; \(\Sigma_K f\) is the [[?lean:New.stdClassSum|class sum]] at level \(K\) on a standard definite space \(E^b\): the sum of \(f(g_c)/\#\operatorname{Aut}(g_c)\) over the double cosets \(c\) of rational points and \(K\); \(K_0\) is the [[?lean:New.stdLevel|full level]], the stabilizer of the standard lattice.

Let \(b,n\) be finite index sets, \(V'\) a hermitian space of rank \(\lvert b\rvert\) and \(W'\) one of rank \(\lvert n\rvert\) (arbitrary signs at the infinite places), \(E^b\) the standard definite space, and \(W=E^b\oplus W'\). Let \(\mathfrak m\neq(1)\) be a modulus, \(\chi\) a multiplicative character of \(\mathcal{O}_E/\mathfrak m\), \(P\) a polynomial in the Fock variables of the pair \((V',W')\), \(h'\in U(E^b)(\mathbb{A}_f)\), \(g\in U(W')(\mathbb{A})\). Matrices \(x\in(\mathcal{O}_E/\mathfrak m)^{n\times(b\sqcup n)}\) are written \(x=(x'\mid x'')\), and \(y\in(\mathcal{O}_E/\mathfrak m)^{(b\sqcup n)\times b}\) as \(y=\binom{y'}{y''}\).

**Lemma (one exchange).** Let \(\Psi'\colon(\mathcal{O}_E/\mathfrak m)^{n\times b}\to\mathbb{C}\) satisfy \(\Psi'(y\gamma)=\Psi'(y)\) for all \(\gamma\in\mathrm{GL}_b(\mathcal{O}_E/\mathfrak m)\). Let \(\Phi\mapsto K_\Phi\) assign to each function \(\Phi\) on \((\mathcal{O}_E/\mathfrak m)^{n\times(b\sqcup n)}\) a function on \(U(E^n)(\mathbb{A}_f)\), and let \(c\in\mathbb{C}\). **Assume** the exchange identity: for all \(\Phi,\Psi\) that are [[?lean:New.Exchange.AreMatched|matched]] for \(\chi^{-1}\),
\[
c\,\Sigma_{K_0}(K_\Phi)=\int_{[U(V')]}\Theta^{V',W}_{\Psi,P}\bigl(x,(h',g)\bigr)\,dx ,
\]
the integral over the automorphic quotient of \(U(V')\), \(P\) being read in the variables of \(W'\). Then, with \(\Phi_0(x'\mid x'')=\chi(\det x'')\,\Psi'(x''^{-1}x')\):

1. the function \(x\mapsto\Theta^{V',E^b}_{\chi\circ\det,\,1}(x,h')\cdot\Theta^{V',W'}_{\Psi',P}(x,g)\) is integrable on \([U(V')]\), and
\[
c\,\Sigma_{K_0}(K_{\Phi_0})=\int_{[U(V')]}\Theta^{V',E^b}_{\chi\circ\det,\,1}(x,h')\,\Theta^{V',W'}_{\Psi',P}(x,g)\,dx .
\]
2. (Summed form.) If moreover \(K\) depends on \(h'\), the exchange identity holds for every \(h'\), and \(c_0\,\Sigma_{K_0}\bigl(h'\mapsto\operatorname{coef}(h')\,\Theta^{V',E^b}_{\chi\circ\det,1}(x,h')\bigr)=F(x)\) for all \(x\), for some function \(\operatorname{coef}\) and \(c_0\in\mathbb{C}\), then
\[
c\,c_0\,\Sigma_{K_0}\Bigl(h'\mapsto\operatorname{coef}(h')\,\Sigma_{K_0}\bigl(K_{\Phi_0,h'}\bigr)\Bigr)=\int_{[U(V')]}F(x)\,\Theta^{V',W'}_{\Psi',P}(x,g)\,dx .
\]

## Proof

Outline.

*Matching.* The function matched with \(\Phi_0\) is \(\Psi_0\binom{y'}{y''}=\chi(\det y')\Psi'(y'')\): the general block lemma [[?lean:New.Exchange.areMatched_block|matching of block data]] gives \(\chi(\det y')\Psi'(-y''y'^{-1})\), and the right \(\mathrm{GL}_b\)-invariance of \(\Psi'\) removes the factor \(-y'^{-1}\).

*Factorisation.* \(\Psi_0\) is a product of a function of the \(E^b\)-block and one of the \(W'\)-block, so the kernel of \((V',E^b\oplus W')\) at a block-diagonal point \((h',g)\) is the product of the kernels of \((V',E^b)\) and \((V',W')\). Substituting in the assumed identity gives the formula in 1.

*Convergence.* \(\chi(\det y')\ne0\) forces \(y'\) invertible, so \(\Psi_0\) is supported on matrices with a left inverse. For such data and \(\mathfrak m\neq(1)\) the theta kernel is rapidly decreasing in \(x\) (its product with any power of the [[?lean:New.Space.height|height]] is bounded; [[?lean:New.pairTheta_modDatum_decay|decay of theta kernels with left-invertible data]]), hence integrable on the quotient, which has finite measure.

2. Multiply 1 by \(\operatorname{coef}(h')\), sum over the finitely many classes of \(U(E^b)\) (the class sum is a finite sum and commutes with the integral), and use the hypothesis on \(F\).

## Remarks

The exchange identity itself is an input here, proved in [[?lean:New.Exchange.exchange_identity|the exchange identity]] (of Siegel–Weil type). The effect of the lemma: the character \(\chi\) is confined to the kernel of the equal-rank pair \((V',E^b)\).

## References

1. Lean: `New.Rows.isRapid_modKernel`, `New.Rows.hasLeftInv_of_isUnit_det_toRows₁`, `New.Rows.areMatched_det_mul`, `New.Rows.integrable_and_mul_stdClassSum_eq_integral_mul`, `New.Rows.mul_stdClassSum_eq_integral_mul_modKernel` in `src/New/OneLift/ComparisonOperator/OneExchange.lean`.
