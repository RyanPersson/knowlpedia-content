+++
id = "differential-geometry/time-dependent-hamiltonian-system"
title = "Time-dependent Hamiltonian system"
kind = "definition"
summary = "A symplectic phase space with a smoothly time-varying Hamiltonian that generates nonautonomous dynamics."
aliases = ["nonautonomous Hamiltonian system"]
domains = ["differential-geometry", "classical-mechanics"]
section_mode = "progressive"
prerequisites = ["differential-geometry/symplectic-manifold", "differential-geometry/classical-phase-space", "differential-geometry/hamiltonian-vector-field"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(I\subseteq\mathbb R\) be an open interval and let \((M,\omega)\) be a [[differential-geometry/symplectic-manifold|symplectic manifold]]. A **time-dependent Hamiltonian system** is a smooth function
\[
H:I\times M\to\mathbb R,\qquad H_t(x)=H(t,x),
\]
together with this fixed [[differential-geometry/classical-phase-space|symplectic phase space]]. For each \(t\), its [[differential-geometry/hamiltonian-vector-field|Hamiltonian vector field]] \(X_{H_t}\) is defined by
\[
\iota_{X_{H_t}}\omega=d_MH_t.
\]
A trajectory is a curve \(\gamma\) satisfying the nonautonomous equation \(\dot\gamma(t)=X_{H_t}(\gamma(t))\). The differential \(d_M\) acts only in the \(M\)-direction.

## Evolution and symplecticity

Local existence and uniqueness produce evolution maps \(\Phi_{t,s}\) with \(\Phi_{s,s}=\operatorname{id}\) and
\[
\Phi_{t,r}\circ\Phi_{r,s}=\Phi_{t,s}
\]
wherever all terms are defined. Each \(\Phi_{t,s}\) is symplectic because every instantaneous field \(X_{H_t}\) preserves \(\omega\). In general there is no one-parameter group \(\Phi_t\): the evolution depends on both initial and final time.

## Energy balance and autonomous extension

Along a trajectory,
\[
\frac{d}{dt}H(t,\gamma(t))=\frac{\partial H}{\partial t}(t,\gamma(t)),
\]
because \(d_MH_t(X_{H_t})=0\). Thus explicit time dependence obstructs conservation of the instantaneous Hamiltonian.

The system can be encoded as an [[differential-geometry/hamiltonian-system|autonomous Hamiltonian system]] on an extended phase space by adjoining time and its conjugate momentum.

## Conventions and scope

**Warning.** A time-dependent Hamiltonian is a smooth family \(H_t\), not a single function on \(M\). Adding an arbitrary function of time to \(H\) leaves \(X_{H_t}\) and the trajectories unchanged but changes the displayed instantaneous energy. The sign convention here matches the corpus convention \(\iota_{X_H}\omega=dH\).

## References

1. V. I. Arnol'd, *Mathematical Methods of Classical Mechanics*, 2nd ed., Springer, 1989. [DOI record](https://doi.org/10.1007/978-1-4757-1693-1). Relevant: Chapter 9, time-dependent Hamiltonian mechanics and extended phase space.
2. Ralph Abraham and Jerrold E. Marsden, *Foundations of Mechanics*, 2nd ed., AMS Chelsea Publishing, 2008. [DOI record](https://doi.org/10.1090/chel/364). Relevant: §3.3, Hamiltonian systems and time-dependent flows.
