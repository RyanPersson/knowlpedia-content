+++
id = "proofs/grh/spanning-unfolding-b/remainder-against-a-central-idempotent"
title = "The remainder against a central idempotent of one factor"
kind = "lemma"
summary = "For a central idempotent x of the group algebra of the factor of the residue group above one level prime, the x-average of P_t minus r_psi(t) has squared Hilbert–Schmidt norm at most b^(-12) times the source dimension."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.HasAmplitudeBlocks.hilbertSchmidtNorm_sum_smul_sub_besselTranslate_sq_le", "New.IsCentralProj.isSymmetricProjection"]
lean_files = ["src/New/Spanning/Unfolding/Moments.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S\) be an [[proofs/grh/spanning-unfolding-b/filling-admissible|admissible]] [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over a CM field containing a primitive \(5040\)-th root of unity, and \((\rho,P)\) a pair with [[proofs/grh/spanning-unfolding-b/amplitude-blocks|amplitude blocks]], \(\rho\) unitary, \(V\) finite-dimensional. Write \(\bar G=G_0\times G_1\), with \(G_i=\prod_{w\in C_i}\mathrm{GL}_r(\mathbb{F}_w)\) embedded in \(\bar G\) by \(\phi_i\) (trivial above the other prime). Let \(x=\sum_tx(t)\,t\) be a [[?lean:New.IsCentralProj|central idempotent]] of \(\mathbb{C}[G_i]\): \(x^2=x\) and \(t\mapsto x(t)\) is a class function. Then
\[
\Bigl\lVert\sum_{t\in G_i}x(t)\bigl(P_{\phi_i(t)}-r_\psi(\phi_i(t))\bigr)\Bigr\rVert^2\le b^{-12}\dim_S .
\]
Also: in a unitary representation of a finite group, a central idempotent acts as an orthogonal projection.

## Proof

Put \(P'_s=P_s-r_\psi(s)\) and \(P'_x=\sum_tx(t)P'_{\phi_i(t)}\). For \(s\in\bar R_0\) and all \(u\): \(P'_{su}=r_\psi(s)P'_u\), by [[proofs/grh/spanning-unfolding-b/equivariance-of-maps-with-amplitude-blocks|left equivariance]] and [[proofs/grh/spanning-unfolding-b/bessel-translate-is-a-unitary-representation|multiplicativity of \(r_\psi\)]]. Let \(\Omega\) be the set of \(s\in\bar G\) that agree with an element of \(\bar R_0\) above the other prime \(p_{i+1}\), and let \(f(s)=P'_s\) for \(s\in\Omega\), \(f(s)=0\) otherwise, as a function with values in the Hilbert space of operators. For \(s\in\bar R_0\) and \(t\in G_i\) we have \(s\phi_i(t)\in\Omega\), so
\[
\sum_tx(t)f(s\phi_i(t))=r_\psi(s)P'_x,\qquad\text{of norm }\lVert P'_x\rVert .
\]
Convolution with a central idempotent along a homomorphism is a contraction of \(\ell^2\) ([[?lean:New.IsCentralProj.sum_norm_sq_conv_le|contraction by a central idempotent]]): \(\sum_{s\in\bar G}\lVert\sum_tx(t)f(s\phi_i(t))\rVert^2\le\sum_s\lVert f(s)\rVert^2\) (apply the cited form to \(s\mapsto f(s^{-1})\) and substitute \(s\to s^{-1}\)). Hence
\[
\lvert\bar R_0\rvert\,\lVert P'_x\rVert^2\le\sum_{s\in\Omega}\lVert P'_s\rVert^2\le b^{-12}\mathcal{M}_{\mathrm{id}}=b^{-12}\lvert\bar R_0\rvert\dim_S
\]
by part 1 of [[proofs/grh/spanning-unfolding-b/second-moments-of-the-poincare-operators|the moment bounds]].

For the last statement: the image of an idempotent is idempotent, and a central idempotent acts by a self-adjoint operator in a unitary representation ([[?lean:New.IsCentralProj.self_adjoint|self-adjointness of central idempotents]]).

## References

1. Lean: `New.Filling.HasAmplitudeBlocks.hilbertSchmidtNorm_sum_smul_sub_besselTranslate_sq_le`, `New.IsCentralProj.isSymmetricProjection` in `src/New/Spanning/Unfolding/Moments.lean`.
