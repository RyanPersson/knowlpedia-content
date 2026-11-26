+++
id = "proofs/grh/onelift-comparison/class-sum-at-row-stabilizer"
title = "Class sums at the level of a row stabilizer"
kind = "lemma"
summary = "A class sum at full level of a kernel with datum chi(det x) F(x^-1 x-prime) equals the class sum at the level of a row stabilizer of the kernel with the datum cut down to the stabilizer."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Rows.stdClassSum_tower", "New.Rows.signedRowSubst", "New.Rows.realPairWeil_ratEmbed_inv_polyVector", "New.Rows.modKernelStdSpace_stdEmbFin_mul", "New.Rows.fixesLeft_modKernelStdSpace", "New.Rows.stdClassSum_rowStabilizer_eq"]
lean_files = ["src/New/OneLift/ComparisonOperator/OneExchange.lean"]
proof_status = "outline"
+++

Throughout, \(E\) is a [[?c:CM field|CM field]] with a CM type and [[?c:Weil representation|Weil data]]; a [[?lean:New.Modulus|modulus]] \(\mathfrak m\) is a nonzero ideal of \(\mathcal{O}_E\) prime to its complex conjugate; for [[?c:Hermitian space|hermitian spaces]] \(S,T\) over \(E\) (with adelic points, [[?lean:New.Space|spaces]]) \(\Theta^{S,T}_{\Psi,P}(g,h)\) denotes the [[?lean:New.modKernel|theta kernel modulo \(\mathfrak m\)]] of the pair \((S,T)\) at \(g\in U(S)(\mathbb{A})\), \(h\in U(T)(\mathbb{A})\), for a function \(\Psi\) on matrices over \(\mathcal{O}_E/\mathfrak m\) (of size \(\operatorname{rk}T\times\operatorname{rk}S\)), a polynomial \(P\) in the Fock variables, and two twisting automorphic characters of \(U(1)\) which are suppressed from the notation; \(\Sigma_K f\) is the [[?lean:New.stdClassSum|class sum]] at level \(K\) on a standard definite space \(E^b\): the sum of \(f(g_c)/\#\operatorname{Aut}(g_c)\) over the double cosets \(c\) of rational points and \(K\); \(K_0\) is the [[?lean:New.stdLevel|full level]], the stabilizer of the standard lattice.

Write \(\Theta^{W}_{\Psi,P}(g,h)\) for the kernel of the pair of a hermitian space \(W\) and the standard definite space \(E^b\), at \(g\in U(W)(\mathbb{A})\) and at the point of \(U(E^b)\) with real part \(1\) and finite part \(h\) ([[?lean:New.modKernelStdSpace|kernel with a standard definite space]]). For a subgroup \(H\subseteq\mathrm{GL}_b(\mathcal{O}_E/\mathfrak m)\) let \(K_H\subseteq K_0\) be the elements reducing modulo \(\mathfrak m\) into \(H\).

**Lemma.**

1. (Tower.) Let \(f_0\) on \(U(E^b)(\mathbb{A}_f)\) be left invariant under the rational points and right invariant under \(K_H\), and let \(f(h)=\sum_{q\in\mathrm{GL}_b(\mathcal{O}_E/\mathfrak m)/H}f_0(h\,\tilde q)\), \(\tilde q\in K_0\) a [[?lean:New.Rows.liftMod|lift]] of a representative of \(q\), be right \(K_0\)-invariant. Then \(\Sigma_{K_H}f_0=\Sigma_{K_0}f\).

2. (Rational translation.) Let \(W\) have signs \(s\) with \(q\) signs \(-1\), let the character \(\alpha\) twisting the action of \(U(E^b)\) have exponents \(\gamma_\tau\) at the infinite places \(\tau\), and let \(\delta\in U(E^b)(\mathbb{Q})\). Then
\[
\Theta^W_{\Psi,P}(g,\delta h)=\prod_\tau\tau(\det\delta)^{\,q-\gamma_\tau}\ \Theta^W_{\Psi,\,\delta\cdot P}(g,h),
\]
where \(\delta\cdot P\) is obtained from \(P\) by the substitution \(x_\tau\mapsto(\delta^{-1})^{\mathsf T}x_\tau\) in the columns of sign \(+1\) and \(x_\tau\mapsto\delta x_\tau\) in the columns of sign \(-1\) (\(\delta\) read in the embedding of the CM type at \(\tau\)). Consequently, if \(\alpha\) is [[?lean:New.Exchange.IsTameFor|tame for \(\mathfrak m\)]] and the Fock vector \(P(\zeta x)e^{-\lvert x\rvert^2/2}\) of \(P\) is fixed by the real group \(U(E^b)(\mathbb{R})\) (acting by the Weil action twisted by \(\det^{\gamma}\)), then \(h\mapsto\Theta^W_{\Psi,P}(g,h)\) is left invariant under the rational points.

3. (Row stabilizer.) Let \(W\) have rank \(\lvert n\rvert+\lvert b\rvert\), let \(\alpha\) be tame for \(\mathfrak m\) with exponents \(\gamma\) and character \(\chi\) on \(\mathcal{O}_E/\mathfrak m\), and let the Fock vector of \(P\) be fixed by \(U(E^b)(\mathbb{R})\). Let \(H=H(\varphi,w,e)\) be a [[proofs/grh/onelift-comparison/row-stabilizer-and-column-datum|row stabilizer]] in \(\mathrm{GL}_b(\mathcal{O}_E/\mathfrak m)\) with column datum \(\kappa\), and \(F\) a function on \((\mathcal{O}_E/\mathfrak m)^{b\times n}\) with \(F(Ay)=F(y)\) for \(A\in H\). Writing \(x=(x'\mid x'')\) with \(x''\) square,
\[
\Sigma_{K_H}\Bigl(\Theta^W_{\Phi_H,P}(g,\cdot)\Bigr)=\Sigma_{K_0}\Bigl(\Theta^W_{\Phi,P}(g,\cdot)\Bigr),
\]
\[
\Phi(x)=\chi(\det x'')F(x''^{-1}x'),\qquad \Phi_H(x)=\kappa\bigl(x''^{(e)}\bigr)\,[x''\text{ has the columns of }1\text{ off }e]\,F(x').
\]

## Proof

Outline; the Lean proofs were read through their comments.

1. Each class at level \(K_0\) splits into classes at level \(K_H\); the number of cosets cancels against the ratio of the automorphism weights (the index of the level).

2. The kernel is invariant under the rational point \(\delta^{-1}\) acting on both the finite and the real component. This cancels the finite translation by \(\delta\) and leaves the real part of \(\delta^{-1}\) acting on the Fock vector. As \(E^b\) is definite this real point is block diagonal and acts on \(P(\zeta x)e^{-\lvert x\rvert^2/2}\) by the stated substitution times the character \(\prod_\tau\tau(\det\delta)^{q-\gamma_\tau}\). The kernel is linear in the Fock vector. Under the invariance hypothesis the scalar times the substituted polynomial has the same Fock vector as \(P\).

3. By the [[proofs/grh/onelift-comparison/row-stabilizer-and-column-datum|product lemma]], \(\Phi_H\) is \(\Phi\) cut down to \(x''\in H\). Right translation of the kernel by \(k\in K_0\) with reduction \(A\) is the translation of the datum twisted by \(\chi(\det A)^{-1}\); this twist cancels the factor that the translation adds to \(\chi(\det x'')\). An invertible \(x''\) lies in exactly one coset of \(H\), and at non-invertible \(x''\) all terms vanish, so the translates of \(\Phi_H\) by coset representatives add up to \(\Phi\). Now apply 1 with \(f_0\) the kernel of \(\Phi_H\) (left invariant by 2).

## References

1. Lean: `New.Rows.stdClassSum_tower`, `New.Rows.signedRowSubst`, `New.Rows.realPairWeil_ratEmbed_inv_polyVector`, `New.Rows.modKernelStdSpace_stdEmbFin_mul`, `New.Rows.fixesLeft_modKernelStdSpace`, `New.Rows.stdClassSum_rowStabilizer_eq` in `src/New/OneLift/ComparisonOperator/OneExchange.lean`.
