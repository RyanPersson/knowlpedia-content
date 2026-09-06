+++
id = "mathematical-physics/dirac-equation"
title = "Dirac equation"
kind = "definition"
summary = "The relativistic first-order field equation for a spinor of prescribed mass."
aliases = ["free Dirac equation", "relativistic spinor equation", "massive Dirac equation"]
domains = ["mathematical-physics", "partial-differential-equations", "differential-geometry"]
prerequisites = ["mathematical-physics/minkowski-spacetime","mathematical-physics/minkowski-dirac-operator","mathematical-physics/gamma-matrices"]
dependency_review_count = 1
section_mode = "progressive"
+++

For a spinor field \(\psi\) of mass \(m\geq0\) on [[mathematical-physics/minkowski-spacetime|Minkowski spacetime]], the **free Dirac equation** in the convention of this collection is
\[
(iD_{\mathrm M}-m)\psi=0,
\]
where \(D_{\mathrm M}=\gamma^\mu\partial_\mu\) is the [[mathematical-physics/minkowski-dirac-operator|Minkowski Dirac operator]] and the [[mathematical-physics/gamma-matrices|Clifford matrices]] obey
\[
\gamma^\mu\gamma^\nu+\gamma^\nu\gamma^\mu=-2\eta^{\mu\nu}I
\]
for \(\eta=\operatorname{diag}(-1,1,1,1)\).

## Mass shell

A plane-wave spinor \(\psi(x)=u(p)e^{-ip_\mu x^\mu}\) satisfies an algebraic equation for \(u(p)\). Multiplication by the conjugate first-order factor implies
\[
(\Box_\eta+m^2)\psi=0.
\]
Thus each spinor component satisfies the [[mathematical-physics/klein-gordon-equation|Klein–Gordon equation]] and the momentum lies on the relativistic mass shell.

## Massless equation

For \(m=0\), the equation is \(D_{\mathrm M}\psi=0\). In even spacetime dimension the complex spin representation has a chirality decomposition, and the massless equation can split into equations for [[differential-geometry/weyl-spinor|chiral spinors]]. A nonzero mass term couples the two chiralities.

## Curved and coupled forms

On a [[differential-geometry/lorentzian-spinor-bundle|Lorentzian spinor bundle]], the curved equation is
\[
(iD_g-m)\psi=0,
\qquad D_g=c\circ\nabla^S.
\]
A gauge potential replaces the [[fiber-bundles/spin-connection|spin connection]] by a coupled connection. Squaring a curved or gauge-coupled equation produces curvature or field-strength terms, so only the flat free equation has the elementary componentwise factorization stated above.

## Convention warning

Some sources use the mostly-minus metric and matrices satisfying \(\{\gamma^\mu,\gamma^\nu\}=2\eta^{\mu\nu}I\); others absorb the factor \(i\) into the [[noncommutative-geometry/dirac-operator|geometric Dirac operator]]. Equivalent formulas can therefore look different. The metric, Clifford relation, and differential operator must be compared together.

## References

1. Paul A. M. Dirac, “The Quantum Theory of the Electron,” *Proceedings of the Royal Society A* 117 (1928), 610–624. [Journal record](https://doi.org/10.1098/rspa.1928.0023).
2. Michael E. Peskin and Daniel V. Schroeder, *An Introduction to Quantum Field Theory*, Addison-Wesley, 1995. [Publisher record](https://doi.org/10.1201/9780429503559). Relevant: Chapters 3–4.
3. Christian Bär, Nicolas Ginoux, and Frank Pfäffle, *Wave Equations on Lorentzian Manifolds and Quantization*, European Mathematical Society, 2007. [Publisher record](https://doi.org/10.4171/037). Relevant: §3.4.
