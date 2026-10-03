+++
id = "ergodic-theory/finite-uniform-system"
title = "Dynamics on a finite uniform probability space"
kind = "example"
summary = "Uniform finite dynamics is permutation dynamics, with ergodicity exactly when there is one cycle."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/measure-preserving-system", "ergodic-theory/ergodic-transformation", "algebra-groups/symmetric-group", "operator-algebras/state-cstar-algebra"]
+++

On \(X=\{1,\ldots,n\}\), \(n\geq1\), let \(\Sigma=\mathcal P(X)\) and \(\mu(E)=|E|/n\). The measure-preserving self-maps are exactly the permutations \(S_n\). Such a map is [[ergodic-theory/ergodic-transformation|ergodic]] exactly when it is one \(n\)-cycle.

## Proof and invariant functions

Preservation of each singleton's probability forces exactly one preimage of each point. If the disjoint cycles are \(C_1,\ldots,C_r\), invariant sets are precisely their unions. Fixed functions are constant on each cycle, so \(\dim\ker(U_T-I)=r\).

## Function algebra and state

The algebra is \(A=\mathbb C^n\) with coordinatewise multiplication, complex conjugation as involution, unit \((1,\ldots,1)\), and maximum norm. Its state is \(\varphi(z)=n^{-1}\sum_j z_j\). Inverse pullback is
\[
\alpha_T(z)_j=z_{T^{-1}(j)},\qquad A^{\alpha_T}\cong\mathbb C^r.
\]
The vector-space dimension is \(n\); this algebra is not the matrix algebra \(M_n(\mathbb C)\), whose dimension is \(n^2\).

## Three points

For \(T=(123)\), \(\alpha_T(z_1,z_2,z_3)=(z_3,z_1,z_2)\), and only constant triples are fixed. For \(T=(12)\), fixed triples have form \((a,a,b)\). The identity fixes every triple. The state of the event \(\{1,3\}\) is \(\varphi(1,0,1)=2/3\).

## Frequencies and averages

For \(X=\mathbb Z/n\mathbb Z\), \(T(k)=k+1\), the functions \(e_j(k)=e^{2\pi ijk/n}\) form an orthonormal eigenbasis, with \(U_Te_j=e^{2\pi ij/n}e_j\). For \(n>1\), the system is ergodic but not weakly mixing. An orbit average converges to the average over the starting point's cycle.
