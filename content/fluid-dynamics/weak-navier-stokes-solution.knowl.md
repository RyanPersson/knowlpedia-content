+++
id = "fluid-dynamics/weak-navier-stokes-solution"
title = "Weak Navier–Stokes solution"
kind = "definition"
summary = "Locally square-integrable velocity and locally integrable pressure satisfying momentum and incompressibility against tests."
aliases = ["distributional Navier–Stokes solution"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["partial-differential-equations/weak-formulation", "fluid-dynamics/navier-stokes-equations", "measure-theory/locally-integrable-function", "linear-algebra/outer-product", "real-analysis/divergence", "functional-analysis/test-function-space", "measure-theory/lp-space", "real-analysis/gradient", "real-analysis/laplacian"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

On an open space-time cylinder \(Q\subset\mathbb R^n\times\mathbb R\), a **weak Navier–Stokes solution** with viscosity \(\nu>0\) and locally integrable force \(f\) is a pair \(u\in L^2_{\rm loc}(Q)\), \(p\in L^1_{\rm loc}(Q)\) satisfying the [[partial-differential-equations/weak-formulation|integral identities]]
\[
\int_Q\bigl(u\cdot\partial_t\phi+(u\otimes u):\nabla\phi
 +\nu u\cdot\Delta\phi+p\,\operatorname{div}\phi+f\cdot\phi\bigr)=0,
\qquad \int_Q u\cdot\nabla\psi=0
\]
for all compactly supported smooth vector tests \(\phi\) and scalar tests \(\psi\). Here the [[linear-algebra/outer-product|outer product]] has entries \(u_i u_j\), and \((u\otimes u):\nabla\phi=\sum_{i,j}u_i u_j\partial_j\phi_i\). The indicated [[measure-theory/locally-integrable-function|local integrability]] makes these products meaningful. These are the distributional [[fluid-dynamics/navier-stokes-equations|momentum and incompressibility equations]].

Here \(L^2_{\rm loc}\) uses [[measure-theory/lp-space|Lebesgue square integrability]] on compact subsets. The tests are from the [[functional-analysis/test-function-space|smooth test-function space]]; \(\nabla\), \(\operatorname{div}\), and \(\Delta\) are the spatial [[real-analysis/gradient|gradient]], [[real-analysis/divergence|divergence]], and [[real-analysis/laplacian|Laplacian]].

## Initial data and pressure elimination

On \(\mathbb R^n\times(0,T)\), initial datum \(u_0\) is imposed by allowing tests supported in \([0,T)\) and adding \(\int u_0(x)\cdot\phi(x,0)\,dx\) to the first identity. Restricting to divergence-free vector tests removes the pressure term. Recovering a pressure from that restricted formulation is a separate assertion depending on the domain and function spaces.

## Energy conditions

This definition alone imposes neither finite global energy nor an energy inequality. See [[fluid-dynamics/navier-stokes-energy-class|the energy class]], [[fluid-dynamics/leray-hopf-solution|Leray–Hopf solutions]], and [[fluid-dynamics/suitable-weak-solution|suitable weak solutions]].

## References

- [Ryzhik, Math 256B lecture notes (2024), weak solutions and partial regularity](https://math.stanford.edu/~ryzhik/notes-256B-24.pdf).
