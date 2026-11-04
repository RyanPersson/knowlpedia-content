+++
id = "mathematical-physics/dirac-equation"
title = "Dirac equation"
kind = "definition"
summary = "The relativistic first-order field equation for a spinor of prescribed mass."
aliases = ["free Dirac equation", "relativistic spinor equation", "massive Dirac equation"]
domains = ["mathematical-physics", "partial-differential-equations", "differential-geometry"]
section_mode = "progressive"
prerequisites = ["mathematical-physics/minkowski-spacetime", "mathematical-physics/minkowski-dirac-operator", "mathematical-physics/gamma-matrices"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
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

## Worked example: four coupled spinor components

Use natural units \(\hbar=c=1\), coordinates \(x^0=t,x^1,x^2,x^3\),
and \(\partial_\mu=\partial/\partial x^\mu\). Let
\(\psi=(\psi_1,\psi_2,\psi_3,\psi_4)^{\mathsf T}:\mathbb R^{1,3}\to\mathbb C^4\)
be smooth, with each \(\psi_a\) a complex-valued function. In the explicit
Dirac representation constructed in the
[[mathematical-physics/gamma-matrices|gamma matrices]] knowl,
\(\gamma^0=\operatorname{diag}(I_2,-I_2)\) and
\(\gamma^j=\begin{pmatrix}0&\sigma^j\\-\sigma^j&0\end{pmatrix}\),
where \(\sigma^j\) are the Pauli matrices and \(I_n\) denotes the
\(n\times n\) identity matrix. Expanding
\((i\gamma^\mu\partial_\mu-mI_4)\psi=0\), with summation over
\(\mu=0,1,2,3\), gives the matrix differential equation
\[
\begin{pmatrix}
i\partial_0-m&0&i\partial_3&i\partial_1+\partial_2\\
0&i\partial_0-m&i\partial_1-\partial_2&-i\partial_3\\
-i\partial_3&-i\partial_1-\partial_2&-i\partial_0-m&0\\
-i\partial_1+\partial_2&i\partial_3&0&-i\partial_0-m
\end{pmatrix}
\begin{pmatrix}\psi_1\\\psi_2\\\psi_3\\\psi_4\end{pmatrix}=0.
\]
Every derivative acts on the component to its right; each mass term means
multiplication by the constant \(m\). Row by row, this is precisely the four
coupled equations
\[
(i\partial_0-m)\psi_1+i\partial_3\psi_3
+(i\partial_1+\partial_2)\psi_4=0,
\]
\[
(i\partial_0-m)\psi_2+(i\partial_1-\partial_2)\psi_3
-i\partial_3\psi_4=0,
\]
\[
-i\partial_3\psi_1-(i\partial_1+\partial_2)\psi_2
+(-i\partial_0-m)\psi_3=0,
\]
\[
(-i\partial_1+\partial_2)\psi_1+i\partial_3\psi_2
+(-i\partial_0-m)\psi_4=0.
\]
The component labels \(1,2,3,4\) are spinor-component labels, not spacetime
indices. These equations use the collection's metric
\(\eta=\operatorname{diag}(-1,1,1,1)\) and geometric Clifford sign.
They are numerically identical to the usual mostly-minus physics equations
because \(-2\eta^{\mu\nu}=2\eta_{\mathrm{phys}}^{\mu\nu}\) for
\(\eta_{\mathrm{phys}}=-\eta\).

## Mass shell

A plane-wave spinor \(\psi(x)=u(p)e^{-ip_\mu x^\mu}\) satisfies an algebraic equation for \(u(p)\). Multiplication by the conjugate first-order factor implies
\[
(\Box_\eta+m^2)\psi=0.
\]
Here the collection's wave-operator convention is
\[
\Box_\eta=-\eta^{\mu\nu}\partial_\mu\partial_\nu
=\partial_0^2-\partial_1^2-\partial_2^2-\partial_3^2.
\]
Indeed, \(D_{\mathrm M}^{\,2}=\Box_\eta I_4\), so
\[
(iD_{\mathrm M}+m)(iD_{\mathrm M}-m)
=-(\Box_\eta+m^2)I_4.
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
