+++
id = "proofs/grh/upper-seesaw/lower-chain-of-poincare-series"
title = "The lower chain of a Poincaré series is a restricted upper chain"
kind = "theorem"
summary = "The m lifts along Y_0,...,Y_m take the Poincaré series of a ramified source form to a constant times the restriction to Y_m of the upper chain with the seesaw datum."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.exists_lowerChainUpTo_poincareAt_eq"]
lean_files = ["src/New/UpperBound/Seesaw/SeesawIdentity.lean"]
proof_status = "full"
+++

**Theorem.** Fix an archimedean point \(g\) of \(U(Y_0)\) and a linear form \(t\) on the values of
source forms. There is a constant \(c_0\in\mathbb{C}\) such that for every tame character
\(\vartheta\) and every [[?lean:New.Data.ramifiedSourceForms|ramified source form]] \(\varphi\):
\[
\Theta^{\le m}_{\vartheta}\bigl(\mathcal{P}_{g,t}\varphi\bigr)
=c_0\cdot\operatorname{res}\Bigl(\mathrm{Ch}_\vartheta(\varphi;\varphi_\vartheta)\Bigr),
\]
where \(\Theta^{\le m}_\vartheta\) is the composite of the \(m\) lifts of the lower chain,
\(\mathcal{P}_{g,t}\) the Poincaré map, \(\varphi_\vartheta\) the
[[proofs/grh/upper-seesaw/seesaw-datum|seesaw datum]],
\(\mathrm{Ch}_\vartheta(\varphi;T)\) the image of \(\varphi\) under the
[[?lean:New.Data.chainOfTensor|chain of lifts \(X_0\to\dots\to X_m\)]] with twist \(\vartheta\) and
tensor of finite data \(T\) (linear in \(T\)), and \(\operatorname{res}\) the
[[proofs/grh/upper-seesaw/top-of-the-chain|restriction to \(Y_m\)]].

## Proof

*Top stage.* By [[proofs/grh/upper-seesaw/unfolding-stage-as-coefficient-of-chain|part 2 of the
coefficient theorem]] for the last pair \(i=\varrho\) (whose evaluation is by definition that of
the last double lift) with \(x=1\): for every archimedean tuple \(\xi\) there is a linear form
\(l_\xi\), independent of \(\vartheta,\varphi,y\), such that for all \(y\) with \(y_m=1\) and all
\(k\in U(Y_m)(\mathbb{A})\)
\[
\mathcal{W}_m(k)=l_\xi\Bigl(\bigl(\mathrm{Ch}_\vartheta(\varphi;E(\vartheta,[y]))\bigr)(\operatorname{diag}(k,1))\Bigr),
\]
because the chain of \(\varrho+1\) double lifts with data \(E_0,\dots,E_\varrho\) is
\(\mathrm{Ch}_\vartheta(\varphi;\cdot)\) at the [[?c:Tensor product of vector spaces|pure tensor]] \(E(\vartheta,[y])\), and for the last
double lift \(\epsilon(k)=\operatorname{diag}(k,1)\).

*Periods at the top.* Let \(x\) be a form on \(Y_m\) and \(L_x(T)=\langle x,\operatorname{res}\mathrm{Ch}_\vartheta(\varphi;T)\rangle\),
a linear form on chain tensors. By [[proofs/grh/upper-seesaw/top-of-the-chain|the top of the
chain]] with \(F=\mathcal{W}_m\), \(\psi=\mathrm{Ch}_\vartheta(\varphi;E(\vartheta,[y]))\) and
\(t=l_\xi\):
\[
\Xi_m(\xi,y;\bar x)=C_{l_\xi}\cdot L_x\bigl(E(\vartheta,[y])\bigr)\qquad(y_m=1).
\]

*Outer integrals.* Apply part 4 of [[proofs/grh/upper-seesaw/iterated-unfolding|the iterated
unfolding]] with \(k=m-1\), the last grading, \(a(\xi)=C_{l_\xi}\) and
\(S(c)=L_x(E(\vartheta,c))\); this gives a constant \(c_0\), independent of
\(\vartheta,\varphi,x\), with
\[
\bigl\langle x,\Theta^{\le m}_\vartheta(\mathcal{P}_{g,t}\varphi)\bigr\rangle
=c_0\,\Sigma_m\bigl(L_x\circ E(\vartheta,\cdot)\bigr)=c_0\,L_x\bigl(\Sigma_m(E(\vartheta,\cdot))\bigr)=c_0\,L_x(\varphi_\vartheta),
\]
using the linearity of the cut sum. (The pairing \(\int z\cdot f\) with \(z=\bar x\) is the inner
product with \(x\).) As this holds for all \(x\) in the finite-dimensional space of forms on
\(Y_m\), the two forms agree. \(\blacksquare\)

## References

1. Lean: `New.Data.exists_lowerChainUpTo_poincareAt_eq` in `src/New/UpperBound/Seesaw/SeesawIdentity.lean`.
