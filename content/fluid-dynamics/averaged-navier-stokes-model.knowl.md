+++
id = "fluid-dynamics/averaged-navier-stokes-model"
title = "Averaged Navier–Stokes model"
kind = "definition"
summary = "Replace the Euler bilinear term by an average of transformed Euler trilinear forms."
aliases = []
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/leray-projection", "harmonic-analysis/order-zero-fourier-multiplier", "probability/expectation", "functional-analysis/fourier-sobolev-space", "lie-groups/special-orthogonal-group"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

An **averaged Navier–Stokes model** is
\[
u_t=\nu\Delta u+\widetilde B(u,u),\qquad\operatorname{div}u=0,
\]
where, on divergence-free \(H^{10}(\mathbb R^3)\) fields, the [[fluid-dynamics/leray-projection|Euler bilinear operator]] \(B\) is replaced through
\[
\langle\widetilde B(u,v),w\rangle
=\mathbb E\langle B(A_1u,A_2v),A_3w\rangle.
\]
Set \(A_i=m_i(D)\operatorname{Rot}_{R_i}\operatorname{Dil}_{\lambda_i}\), with
\[
\operatorname{Rot}_R u(x)=Ru(R^{-1}x),\qquad
\operatorname{Dil}_\lambda u(x)=\lambda^{3/2}u(\lambda x).
\]
The \(R_i\) are random [[lie-groups/special-orthogonal-group|rotations]], the \(m_i\) are real [[harmonic-analysis/order-zero-fourier-multiplier|order-zero multipliers]], and \(\mathbb E\) is [[probability/expectation|expectation]]. Require \(C^{-1}\leq\lambda_i\leq C\) almost surely and \(\mathbb E\prod_iM_{k_i}(m_i)<\infty\) for every triple of orders. Pairings use the \(L^2\) duality on the indicated [[functional-analysis/fourier-sobolev-space|Sobolev spaces]].

## Energy cancellation

Energy-preserving models additionally require \(\langle\widetilde B(u,u),u\rangle=0\). Arbitrary choices of the three transformations do not guarantee this identity. Results for a specified \(\widetilde B\) concern that modified equation.

## References

- [Tao, Finite time blowup for an averaged three-dimensional Navier–Stokes equation, §1](https://arxiv.org/abs/1402.0290).
