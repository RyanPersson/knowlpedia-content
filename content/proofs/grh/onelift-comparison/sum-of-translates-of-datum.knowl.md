+++
id = "proofs/grh/onelift-comparison/sum-of-translates-of-datum"
title = "Translates of a datum give the same period"
kind = "lemma"
summary = "Against a rapidly decreasing automorphic function of full level, right translates of a datum by GL_b of the residue ring give the same theta integral."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Rows.integral_mul_modKernel_sum_translates"]
lean_files = ["src/New/OneLift/ComparisonOperator/OneExchange.lean"]
proof_status = "outline"
+++

Throughout, \(E\) is a [[?c:CM field|CM field]] with a CM type and [[?c:Weil representation|Weil data]]; a [[?lean:New.Modulus|modulus]] \(\mathfrak m\) is a nonzero ideal of \(\mathcal{O}_E\) prime to its complex conjugate; for [[?c:Hermitian space|hermitian spaces]] \(S,T\) over \(E\) (with adelic points, [[?lean:New.Space|spaces]]) \(\Theta^{S,T}_{\Psi,P}(g,h)\) denotes the [[?lean:New.modKernel|theta kernel modulo \(\mathfrak m\)]] of the pair \((S,T)\) at \(g\in U(S)(\mathbb{A})\), \(h\in U(T)(\mathbb{A})\), for a function \(\Psi\) on matrices over \(\mathcal{O}_E/\mathfrak m\) (of size \(\operatorname{rk}T\times\operatorname{rk}S\)), a polynomial \(P\) in the Fock variables, and two twisting automorphic characters of \(U(1)\) which are suppressed from the notation; \(\Sigma_K f\) is the [[?lean:New.stdClassSum|class sum]] at level \(K\) on a standard definite space \(E^b\): the sum of \(f(g_c)/\#\operatorname{Aut}(g_c)\) over the double cosets \(c\) of rational points and \(K\); \(K_0\) is the [[?lean:New.stdLevel|full level]], the stabilizer of the standard lattice.

**Lemma.** Let \(V'\), \(W'\) be hermitian spaces of ranks \(\lvert b\rvert,\lvert n\rvert\), and let \(F\) be an automorphic function on \(U(V')(\mathbb{A})\) that is rapidly decreasing ([[?lean:New.Space.rapidFunctions|rapid functions]]) and right invariant under the full level \(K_0\). Let the character \(\beta'\) twisting the action of \(U(V')\) in the kernel of \((V',W')\) have trivial tame part (and some weight). Let \(\mathfrak m'\subseteq\mathfrak m\) be moduli, \(\psi\) a function on \((\mathcal{O}_E/\mathfrak m)^{n\times b}\), \(P\) a polynomial and \(g\in U(W')(\mathbb{A})\). Then
\[
\int_{[U(V')]}F(x)\,\Theta^{V',W'}_{\tilde\psi,P}(x,g)\,dx=\#\mathrm{GL}_b(\mathcal{O}_E/\mathfrak m)\cdot\int_{[U(V')]}F(x)\,\Theta^{V',W'}_{\psi,P}(x,g)\,dx ,
\]
where \(\tilde\psi(y)=\sum_{\gamma\in\mathrm{GL}_b(\mathcal{O}_E/\mathfrak m)}\psi(\bar y\gamma)\) is a datum modulo \(\mathfrak m'\) and \(\bar y\) is \(y\) reduced modulo \(\mathfrak m\).

## Proof

Outline. The kernel with datum \(\psi(\cdot\,\gamma)\) is the kernel with datum \(\psi\), right translated in \(x\) by a lift \(k_\gamma\in K_0\) of \(\gamma\) (no character factor appears, because the tame part of \(\beta'\) is trivial). Since \(F\) is right \(K_0\)-invariant and the measure on \([U(V')]\) is right invariant, the substitution \(x\mapsto xk_\gamma^{-1}\) shows that each of the \(\#\mathrm{GL}_b(\mathcal{O}_E/\mathfrak m)\) terms has the same integral; reading a datum modulo \(\mathfrak m\) as a datum modulo the multiple \(\mathfrak m'\) does not change the kernel. Integrability of each term comes from the rapid decay of \(F\). The Lean proof (25 lines) was read through its summary comment.

## References

1. Lean: `New.Rows.integral_mul_modKernel_sum_translates` in `src/New/OneLift/ComparisonOperator/OneExchange.lean`.
