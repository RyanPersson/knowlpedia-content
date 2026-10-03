+++
id = "operator-algebras/gns-implementation-dynamics"
title = "GNS implementation of state-preserving dynamics"
kind = "construction"
summary = "A state-preserving endomorphism induces an isometry on the GNS Hilbert space."
aliases = []
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/gns-construction", "operator-algebras/state-preserving-dynamical-system"]
+++

For a [[operator-algebras/state-preserving-dynamical-system|state-preserving]] system \((A,\varphi,\alpha)\), let \((H_\varphi,\pi_\varphi,\Omega_\varphi)\) be its GNS representation. The rule
\[
V_\alpha\pi_\varphi(a)\Omega_\varphi
=\pi_\varphi(\alpha(a))\Omega_\varphi
\]
extends uniquely to an isometry of \(H_\varphi\). If \(\alpha\) is an automorphism, this isometry is unitary and fixes \(\Omega_\varphi\).

## Why it is well defined

The squared norm of the vector on the right is \(\varphi(\alpha(a)^*\alpha(a))=\varphi(\alpha(a^*a))=\varphi(a^*a)\). Thus null vectors remain null, and the isometry extends from the dense cyclic subspace. Invertibility supplies the inverse implementation.

## Covariance and classical recovery

For an automorphism,
\[
V_\alpha\pi_\varphi(a)V_\alpha^*=\pi_\varphi(\alpha(a)).
\]
Group actions give unitary representations by the same construction. For integration on \(L^\infty(X,\mu)\), the GNS space is \(L^2(X,\mu)\); inverse pullback recovers the classical Koopman representation.
