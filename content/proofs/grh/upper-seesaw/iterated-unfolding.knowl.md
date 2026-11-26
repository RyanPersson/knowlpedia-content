+++
id = "proofs/grh/upper-seesaw/iterated-unfolding"
title = "Iterated unfolding of the lower chain applied to a Poincaré series"
kind = "proposition"
summary = "Pairing the first k+1 lifts of the Poincaré series of a ramified source form with a form on Y_{k+1} equals a constant times the weighted sum over the cuts of the finite parts of the unfolded periods."
aliases = ["transposed lift", "descent", "unfolded period"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.ConjFormY", "New.Data.transposedLiftY", "New.Data.transposedLiftY_apply", "New.Data.integral_mul_liftY", "New.Data.twistedPairWeil_datumY_of_mem_levelY", "New.Data.hasLevel_transposedLiftY", "New.Data.isRapid_conjFormY", "New.Data.unfoldedPeriod", "New.Data.integrable_unfoldStage_mul", "New.Data.integral_unfoldStageOn_mul_transposedLiftY", "New.Data.sum_quotient_chosenLevel_eq_sum_cutPoints", "New.Data.integral_mul_liftY_poincareAt", "New.Data.exists_integral_mul_lowerChainUpTo_eq_cutSum"]
lean_files = ["src/New/UpperBound/Seesaw/SeesawIdentity.lean"]
proof_status = "full"
+++

Notation: \(G_j=U(Y_j)(\mathbb{A})\); \(J_j\) the level of \(Y_j\) for the tame character
\(\vartheta\) and \(K_j\) the lattice stabiliser; \(\ell_j\) the
[[?lean:New.Data.liftY|theta lift \(Y_j\to Y_{j+1}\)]] with twist \(\vartheta\), normalised by the
index \([K_j:J_j]\); \(\Theta^{\le k}_{\vartheta}=\ell_{k-1}\circ\dots\circ\ell_0\)
([[?lean:New.Data.lowerChainUpTo|Lean: the lower chain up to \(k\)]]); \(\mathcal{P}_{g,t}\) the
[[?lean:New.Data.poincareAt|Poincaré map]] from source forms on \(X_0\) to forms on \(Y_0\), for an
archimedean point \(g\) of \(U(Y_0)\) and a linear form \(t\);
[[proofs/grh/upper-seesaw/unfolding-stages|\(\mathcal{W}_{k}\)]] the functions of the unfolding
with outer variables \((\xi_i,y_i)\); and
[[proofs/grh/upper-seesaw/cut-sum|\(\Sigma_k\)]] the cut sums.

A **conjugate form** on \(Y_j\) is a form of the complex conjugate archimedean type. The
**descent** \(\ell_j^{\top}\) from conjugate forms on \(Y_{j+1}\) to conjugate forms on \(Y_j\) is
\[
(\ell_j^{\top}z)(g)=[K_j:J_j]\int_{[G_{j+1}]}\theta\bigl(\omega_{\mu_{j+1}}(g,h)F_j\bigr)\,z(h)\,dh .
\]
The **unfolded period** is
\(\Xi_{k+1}(\xi,y;z)=\int_{R_{k+1}(E)\backslash G_{k+1}}\mathcal{W}_{k+1}(h)z(h)\,dh\).

**Proposition.**

1. (**Transposition.**) \(\int_{[G_{j+1}]}z\cdot\ell_j f=\int_{[G_j]}\ell_j^{\top}z\cdot f\) for
   \(j<m\); \(\ell_j^{\top}z\) is right invariant under \(J_j\); conjugate forms on \(Y_{j+1}\) are
   [[?c:Rapidly decreasing automorphic function|rapidly decreasing]].
2. (**Recursion.**)
   \(\int_{[R_k]}\mathcal{W}^{R}_k(r)\,(\ell_k^{\top}z)(r\,g_k)\,dr=[K_k:J_k]\;\Xi_{k+1}(\xi,y;z)\).
3. (**First step.**)
   \(\int_{[G_1]}z\cdot\ell_0(\mathcal{P}_{g,t}\varphi)=[K_0:K_0^{M}]\sum_{c\in\Omega_0}\Xi_1\bigl((g,1,\dots),(\tilde c,1,\dots);z\bigr)\),
   where \(K_0^{M}\) is the chosen level and \(\tilde c\) a representative of \(c\).
4. (**All steps.**) Let \(k\le m-1\), \(Y\) a grading of \(Y_{k+1}\) with a string of length
   \(m-2-k\), and \(a\) a function of the archimedean tuples \(\xi\). There is a constant \(c\)
   (depending on \(t,g,k,Y,a\) only) such that for every tame \(\vartheta\), every ramified source
   form \(\varphi\), every conjugate form \(z\) on \(Y_{k+1}\) and every function \(S\) of tuples of
   classes: if
   \(\Xi_{k+1}(\xi,y;z)=a(\xi)\,S([y])\) whenever \(y_0\) lies in the chosen level and \(y_m=1\),
   then
   \[
   \int_{[G_{k+1}]}z\cdot\Theta^{\le k+1}_{\vartheta}(\mathcal{P}_{g,t}\varphi)=c\cdot\Sigma_{k+1}(S).
   \]

## Proof

(1) The datum \(F_j\) is an arrow for the theta kernel of the lift and for the swapped kernel
([[?lean:New.Data.isArrow_datumY|the datum of lift \(j+1\) is an arrow]],
[[?lean:New.Data.isArrow_swap_thetaKernelY_datumY|and for the swapped kernel]]); hence the descent
is the stated theta integral, lift and descent are transposes
([[?lean:New.IsArrow.integral_mul_formLift_swap|transposition of a lift]]), and conjugate
forms on \(Y_{j+1}\) are rapidly decreasing (this is part of the arrow property, read off for the
trivial twist). For \(u\in J_j\), the pair \(((1,u),1)\) fixes \(F_j\): its real factor is
untouched and its finite factor, the point datum, is fixed because \(u\) reduces to \(1\) at the
level places, where the tame characters then contribute \(1\). Hence
\((\ell_j^{\top}z)(gu)=(\ell_j^{\top}z)(g)\), by moving \((1,u)\) into the datum.

(2) By the theta integral formula for the descent,
\[
\int_{[R_k]}\mathcal{W}^{R}_k(r)(\ell_k^{\top}z)(rg_k)\,dr=[K_k:J_k]\int_{[R_k]}\mathcal{W}^{R}_k(r)\int_{[G_{k+1}]}\theta\bigl(\omega_{\mu_{k+1}}(rg_k,h)F_k\bigr)z(h)\,dh\,dr ,
\]
and the right side is \([K_k:J_k]\,\Xi_{k+1}\) by one unfolding step
([[proofs/grh/upper-seesaw/unfolding-stages|property 3 of the functions of the unfolding]]),
applicable because \(z\) is automorphic and rapidly decreasing.

(3) Let \(J=J_0\subseteq K_0^{M}\subseteq K_0\), so \([K_0^{M}:J]\,[K_0:K_0^{M}]=[K_0:J]\). For a
finite point \(x\) put
\(\operatorname{per}(x)=\int_{[R_0]}\mathcal{W}^{R}_0(r)\,(\ell_0^{\top}z)(r\,(g,x))\,dr\). By (1),
\(\operatorname{per}(xu)=\operatorname{per}(x)\) for \(u\in J\); by (2) with outer variable
\(g_0=(g,x)\), \(\operatorname{per}(x)=[K_0:J]\;\Xi_1((g,1,\dots),(x,1,\dots);z)\). Now
\[
[K_0^{M}:J]\int_{[G_1]}z\cdot\ell_0(\mathcal{P}_{g,t}\varphi)
=[K_0^{M}:J]\int_{[G_0]}\ell_0^{\top}z\cdot\mathcal{P}_{g,t}\varphi
=\sum_{\gamma\in K_0^{M}/J}\operatorname{per}(\tilde\gamma)
=\sum_{c\in\Omega_0}\operatorname{per}(\tilde c),
\]
by (1), by the [[?lean:New.Data.integral_mul_poincareAt|unfolding of the Poincaré map]] against a
\(J\)-invariant form of conjugate type, and because \(\Omega_0\) is the set of classes modulo \(J\)
of the elements of \(K_0^{M}\) and \(\operatorname{per}\) is \(J\)-invariant. Dividing by
\([K_0^{M}:J]\ne0\) gives the claim.

(4) Induction on \(k\), for all gradings, all \(a\) and all \(S\).

*\(k=0\).* Take \(c=[K_0:K_0^{M}]\cdot a(g,1,1,\dots)\). On \(\Omega_0\) the multiplicities are
\(1\), and for \(c'\in\Omega_0\) the hypothesis (with \(y=(\tilde c',1,\dots)\), where
\(\tilde c'\) lies in the chosen level) evaluates \(\Xi_1=a(g,1,\dots)\,S(c',1,\dots)\). Sum over
\(\Omega_0\) with (3).

*Step \(k\to k+1\).* Let \(Y_0\) be the grading \(\mathcal{Y}_{k+1}\) of \(Y_{k+1}\) and apply
[[proofs/grh/upper-seesaw/integral-as-sum-over-cut|the integral as a sum over a cut]] to \(Y_0\),
the level \(A=K_{k+1}\) and, for each archimedean tuple \(\xi\), the function
\(x_\infty\mapsto a(\xi\text{ with entry }k+1\text{ replaced by }x_\infty)\): it gives a constant
\(a'(\xi)\). Let \(c\) be the constant of the induction hypothesis for \((k,Y_0,a')\).

Given \(\vartheta,\varphi,z,S\) with the hypothesis at step \(k+1\), put \(z'=\ell_{k+1}^{\top}z\).
By (1), \(\int z\cdot\Theta^{\le k+2}(\mathcal{P}\varphi)=\int z'\cdot\Theta^{\le k+1}(\mathcal{P}\varphi)\),
and by the induction hypothesis applied to \(z'\) this is \(c\,\Sigma_{k+1}(S')\) provided
\[
\Xi_{k+1}(\xi,y;z')=a'(\xi)\,S'([y]),\qquad S'(c)=\sum_{x\in\Omega_{k+1}}\mu_{k+1}(x)^{-1}S(c\text{ with entry }k+1\text{ replaced by }x),
\]
for \(y_0\) in the chosen level and \(y_m=1\); and \(c\,\Sigma_{k+1}(S')=c\,\Sigma_{k+2}(S)\) by the
recursive definition of the cut sum. To prove the displayed identity, apply the cut theorem to
\(f=\mathcal{W}_{k+1}\cdot z'\) on \(G_{k+1}\), \(J=J_{k+1}\), \(T=\Omega_{k+1}\) and
\(b(q)=S(\dots,q,\dots)\). Its hypotheses hold:

* \(f\) is continuous, left invariant under the rational points of the Bessel subgroup, and
  integrable ([[proofs/grh/upper-seesaw/unfolding-stages|properties 2, 3]]);
* \(\Omega_{k+1}\) is stable under \(R_{k+1,f}\cap K_{k+1}\)
  ([[proofs/grh/upper-seesaw/stage-cuts|stage cut]]);
* if \(f(x)\ne0\) then \(\mathcal{W}_{k+1}(x)\ne0\), so by
  [[proofs/grh/upper-seesaw/support-of-unfolding-stages|the support theorem]] (here \(\varphi\)
  ramified and \(y_0\) in the chosen level are used) every graded translate of \(x_f\) has the
  bounds \((\mathfrak q,k+1)\), hence the orbit of \(x_f\) is bounded and the multiplicity is
  nonzero (property 4 of a stage cut);
* the Bessel periods factor: for every \(x\in G_{k+1}\),
  \[
  \int_{[R_{k+1}]}f(rx)\,dr=\int_{[R_{k+1}]}\mathcal{W}^{R,x}_{k+1}(r)\,(\ell_{k+1}^{\top}z)(rx)\,dr
  =[K_{k+1}:J_{k+1}]\;a(\xi^{x})\,S([y^{x}]),
  \]
  where \(\xi^{x},y^{x}\) are \(\xi,y\) with entry \(k+1\) replaced by \(x_\infty,x_f\) and
  \(\mathcal{W}^{R,x}_{k+1}(r)=\mathcal{W}_{k+1}(rx)\) is the function of the unfolding for the outer
  variable \(x\) (recall \(\mathcal{W}_{k+1}\) does not depend on the outer variable of index
  \(k+1\)); the second equality is (2) followed by the hypothesis at step \(k+1\) (note
  \(k+1\ne0,m\), so \(y^{x}_0=y_0\) and \(y^{x}_m=1\)).

The cut theorem then gives
\(\Xi_{k+1}(\xi,y;z')=\int_{R_{k+1}(E)\backslash G_{k+1}}f=a'(\xi)\sum_{x\in\Omega_{k+1}}\mu_{k+1}(x)^{-1}S(\dots,x,\dots)\).
\(\blacksquare\)

## References

1. Lean: `New.Data.exists_integral_mul_lowerChainUpTo_eq_cutSum`, `New.Data.integral_mul_liftY_poincareAt`, `New.Data.integral_unfoldStageOn_mul_transposedLiftY`, `New.Data.transposedLiftY` and the lemmas listed in the front matter, in `src/New/UpperBound/Seesaw/SeesawIdentity.lean`.
