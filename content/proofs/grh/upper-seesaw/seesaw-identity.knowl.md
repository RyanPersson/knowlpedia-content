+++
id = "proofs/grh/upper-seesaw/seesaw-identity"
title = "The seesaw identity"
kind = "theorem"
summary = "On ramified source forms, the lower chain of lifts of the Poincaré series is a nonzero constant, independent of the twist, times the composite lift of a chain datum of the twist."
aliases = ["seesaw identity", "iterated seesaw identity"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.seesaw_identity"]
lean_files = ["src/New/UpperBound/Seesaw/SeesawIdentity.lean"]
proof_status = "full"
+++

**Theorem (seesaw identity).** Let \(D\) be the [[?lean:New.Data|data]] of the proof, with field
\(E\), \(m\) lifts, and the chains of [[?c:Hermitian space|hermitian spaces]] \(X_0,\dots,X_m\) (definite) and
\(Y_0,\dots,Y_m\). Let \(t\) be a linear form on the values of forms on \(U(X_0)\) and \(g\) an
archimedean point of \(U(Y_0)\). Then there is a complex number \(c\neq0\) such that for every
[[?lean:New.Data.Twist|twist]] \(\vartheta\) there is a
[[?lean:New.Data.IsChainDatum|chain datum]] \(\Psi\) for \(\vartheta\) with
\[
\Theta_\vartheta\bigl(\mathcal{P}_{g,t}\,\varphi\bigr)=c\cdot\operatorname{CL}_\vartheta(\Psi)(\varphi)
\qquad\text{for all ramified source forms }\varphi .
\]
Here \(\mathcal{P}_{g,t}\) is the [[?lean:New.Data.poincareAt|Poincaré map]] from source forms on
\(X_0\) to forms on \(Y_0\); \(\Theta_\vartheta\) is the
[[?lean:New.Data.lowerChain|lower chain]] \(Y_0\to Y_m\) of \(m\) [[?c:Theta lift|theta lifts]] twisted by
\(\vartheta\); and \(\operatorname{CL}_\vartheta(\Psi)\) is the
[[?lean:New.Data.compositeLift|composite lift]]: the chain of \(m\) lifts \(X_0\to X_m\) whose
tensor of finite data is the [[?lean:New.Data.gluedTensor|glued tensor]]
\(\sum_x\Psi(x)\,\mathrm{gv}(x)\), followed by the restriction to \(Y_m\).

That \(\Psi\) — a finitely supported function on the tuples \(x\) of [[?c:Finite adele ring of a number field|finite adelic]] matrices, one
for each lift of the upper chain — is a *chain datum for \(\vartheta\)* means, with \(Q\) the
modulus of \(\vartheta\) (for a twist, the set of places where its tame part is nontrivial) and \(q=\mathrm{N}Q\):

* its support consists of tuples that are admissible for \(q\) (\(\bar\pi_Mx_k\) integral away from
  \(q\)) and [[?lean:New.Data.supportedTranslations|supported at the level \(Mq\)]] (each \(x_k\) vanishes at every finite place not dividing \(Mq\));
* its values are [[proofs/grh/upper-seesaw/integral-away|integral away from \(q\)]];
* if \(Q=\emptyset\), then \(\sum_x\lvert\sigma\Psi(x)\rvert\le M^{3fmn_m^{2}}\) for every
  automorphism \(\sigma\) of \(\mathbb{C}\);
* its glued tensor is [[?lean:New.Data.ChainTensor.IsInvariant|jointly invariant]]: it is fixed by every tuple \(b=(b_j)\) with \(b_j\) in the level of \(U(X_j)\) for \(j<m\) and \(b_m=1\) (the level of \(X_m\) is not required to act trivially; cf. [[proofs/grh/upper-seesaw/seesaw-datum|property 1 of the seesaw datum]]).

The constant \(c\) does not depend on \(\vartheta\) or \(\varphi\). The theorem does not assert
that either side is nonzero.

## Proof

By [[proofs/grh/upper-seesaw/lower-chain-of-poincare-series|the theorem on the lower chain of a
Poincaré series]] there is \(c_0\) with
\(\Theta^{\le m}_\vartheta(\mathcal{P}_{g,t}\varphi)=c_0\operatorname{res}\mathrm{Ch}_\vartheta(\varphi;\varphi_\vartheta)\)
for all tame \(\vartheta\) and ramified \(\varphi\), and by
[[proofs/grh/upper-seesaw/seesaw-datum|the admissibility of the seesaw datum]] there is \(C\) such
that \(\varphi_\vartheta\) is an [[proofs/grh/upper-seesaw/admissible-combination|admissible
combination]] of the \(C\,\mathrm{gv}(x)\), \(x\) admissible for \(q\), with denominator
\(d=\mathcal{C}^{2m}\) away from \(q\) and size \(\mathcal{C}^{m}\) under \(Q=\emptyset\), where
\(\mathcal{C}=M^{fn_m^{2}}\).

*The constant.* Put \(u=d/(c_0C)\) if \(c_0C\ne0\) and \(u=1\) otherwise, and \(c=u^{-1}\). Both
\(c_0\) and \(C\) are independent of \(\vartheta\), hence so is \(c\ne0\).

*Clearing the denominator.* By rule 8 of the
[[proofs/grh/upper-seesaw/admissible-combination-calculus|calculus of admissible combinations]]
(with \(a=c_0\); \(d\ne0\)), the tensor \(u\,c_0\,\varphi_\vartheta\) is an admissible combination
of the \(\mathrm{gv}(x)\), \(x\) admissible for \(q\), with denominator \(1\) and size
\(d\cdot\mathcal{C}^{m}=\mathcal{C}^{3m}=M^{3fmn_m^{2}}\).

*Support.* Every admissible tuple \(x\) can be replaced by an admissible tuple \(x'\) supported at
the level \(Mq\) with \(\mathrm{gv}(x')=\mathrm{gv}(x)\)
([[?lean:New.Data.exists_supported_translateDatum_eq|Lean: replacing a translation by a supported
one]]). By rule 5 of the calculus (with \(\zeta=1\)) the same tensor is an admissible combination
over the admissible supported tuples, with the same denominator and size. Let \(\Psi\) be its
coefficient function: \(u\,c_0\,\varphi_\vartheta=\sum_x\Psi(x)\mathrm{gv}(x)\) is the glued tensor
of \(\Psi\), and the three conditions on support, integrality and size are exactly the
admissibility of the coefficients.

*Invariance.* The glued tensor of \(\Psi\) is a scalar multiple of \(\varphi_\vartheta\), which is
jointly invariant ([[proofs/grh/upper-seesaw/seesaw-datum|property 1 of the seesaw datum]]). So
\(\Psi\) is a chain datum.

*The identity.* By linearity of the chain of lifts in the tensor,
\[
\Theta^{\le m}_\vartheta\bigl(u\,\mathcal{P}_{g,t}\varphi\bigr)=u\,c_0\operatorname{res}\mathrm{Ch}_\vartheta(\varphi;\varphi_\vartheta)
=\operatorname{res}\mathrm{Ch}_\vartheta\Bigl(\varphi;\sum_x\Psi(x)\mathrm{gv}(x)\Bigr),
\]
and by [[proofs/grh/upper-seesaw/top-of-the-chain|the passage from automorphic to algebraic forms
at the top]] this reads \(\Theta_\vartheta(u\,\mathcal{P}_{g,t}\varphi)=\operatorname{CL}_\vartheta(\Psi)(\varphi)\).
Multiplying by \(c=u^{-1}\) gives the theorem. \(\blacksquare\)

## Remarks

If \(c_0C=0\) the argument gives \(\Psi\) with glued tensor \(0\) and both sides vanish; the
statement is still true with \(c=1\). That the composite lift is nonzero on suitable forms is not
part of this theorem.

The head of the Lean file describes the result as an iterated seesaw identity: the transfer of a
Bessel or Fourier–Jacobi period under one theta lift, applied \(m\) times, where each period is a
constant times a finite sum over cosets of a small level weighted by reciprocals of stabiliser
indices dividing powers of \(q\), the norm of the modulus of the twist; hence no new denominators
away from the modulus.

## References

1. Lean: `New.Data.seesaw_identity` in `src/New/UpperBound/Seesaw/SeesawIdentity.lean`.
2. S. Kudla, *Seesaw dual reductive pairs*, in *Automorphic forms of several variables* (Katata 1983), Progress in Mathematics 46, Birkhäuser, 1984, 244–268.
3. Related work named in the head of the Lean file: B. Wang, *Global theta lifting and periods associated to nilpotent orbits*, 2025; R. Gomez and C.-B. Zhu, *Local theta lifting of generalized Whittaker models*, 2014; W. T. Gan and A. Ichino, *The Gross–Prasad conjecture and local theta correspondence*, 2016; B. Gross, *Algebraic modular forms*, 1999.
