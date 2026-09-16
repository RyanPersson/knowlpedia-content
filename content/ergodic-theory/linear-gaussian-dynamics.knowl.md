+++
id = "ergodic-theory/linear-gaussian-dynamics"
title = "Linear Gaussian-preserving dynamics"
kind = "theorem"
summary = "The linear maps preserving standard finite-dimensional Gaussian measure are orthogonal, and none is ergodic."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["probability/standard-gaussian-probability-space", "lie-groups/orthogonal-group", "ergodic-theory/ergodic-transformation"]
+++

For \(d\geq1\), a real linear map \(T_Q(x)=Qx\) preserves standard Gaussian probability \(\gamma_d\) if and only if \(Q\in O(d)\). None of these transformations is [[ergodic-theory/ergodic-transformation|ergodic]] on the full Gaussian probability space. An affine map \(x\mapsto Qx+b\) preserves \(\gamma_d\) exactly when \(b=0\) and \(Q\in O(d)\).

## Proof

Preserving mean and covariance forces \(b=0\) and \(QQ^{\mathsf T}=I_d\). Conversely, an orthogonal map preserves the norm, the Gaussian density, and Lebesgue measure. Every such map fixes the ball \(\{\|x\|<1\}\), whose Gaussian probability lies strictly between zero and one. Hence ergodicity fails.

## Koopman interpretation

For linear observables \(f_v(x)=v^{\mathsf T}x\), forward composition gives \(U_Qf_v=f_{Q^{\mathsf T}v}\). This finite-dimensional subrepresentation can have no fixed vectors while the full Koopman representation has one: \(r(x)=\|x\|^2-d\) is a nonzero mean-zero fixed vector. The bounded function \(e^{-\|x\|^2}\) also witnesses a nontrivial fixed-point algebra.

Thus studying only coordinate observables can miss an invariant nonlinear quantity.
