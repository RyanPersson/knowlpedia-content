+++
id = "ergodic-theory/hamiltonian-koopman-dynamics"
title = "Koopman dynamics of a Hamiltonian flow"
kind = "construction"
summary = "Hamiltonian state evolution induces a linear equation for observables with Poisson-bracket generator."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/koopman-generator", "differential-geometry/hamiltonian-flow", "differential-geometry/poisson-bracket-symplectic", "differential-geometry/liouville-volume-theorem"]
+++

For a complete [[differential-geometry/hamiltonian-flow|Hamiltonian flow]] \(\Phi^t\) with an invariant probability measure and a strongly continuous Koopman group \(U_tf=f\circ\Phi^t\), the generator on smooth observables in its domain is
\[
Lf=X_Hf=\{f,H\}.
\]
The Poisson bracket uses the convention \(\iota_{X_H}\omega=dH\). Thus state evolution \(\dot x=X_H(x)\) induces the linear observable equation \(\partial_tu=Lu\).

## Densities and conserved quantities

The adjoint evolution is \(U_t^*=U_{-t}\), which transports densities relative to the invariant measure. A conserved observable satisfies \(Lf=0\) on the generator domain and is fixed by the flow.

The Hamiltonian itself is conserved. If it is not almost everywhere constant, some bounded function of it is a nonconstant invariant observable, obstructing ergodicity for a probability measure spread across multiple energies. Ergodicity is consequently often studied on a fixed energy surface with its own invariant probability measure.
