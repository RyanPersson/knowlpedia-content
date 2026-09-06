+++
id = "mathematical-physics/klein-gordon-operator"
title = "Klein–Gordon operator"
kind = "definition"
summary = "The normally hyperbolic scalar operator obtained by adding mass and curvature coupling to the wave operator."
aliases = ["massive wave operator", "Klein-Gordon operator", "Klein Gordon operator"]
domains = ["mathematical-physics", "partial-differential-equations", "differential-geometry"]
section_mode = "progressive"
prerequisites = ["differential-geometry/lorentzian-manifold", "mathematical-physics/dalembert-operator"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

On a [[differential-geometry/lorentzian-manifold|Lorentzian manifold]] \((M,g)\), the **minimally coupled Klein–Gordon operator** of mass \(m\geq0\) is
\[
P_m=\Box_g+m^2,
\]
where \(\Box_g=-\operatorname{tr}_g\nabla d\) is the [[mathematical-physics/dalembert-operator|d’Alembert operator]]. More generally, a curvature coupling gives
\[
P_{m,\xi}=\Box_g+m^2+\xi\,\operatorname{Scal}_g
\]
for a real coupling constant \(\xi\).

## Symbol and hyperbolicity

The mass and curvature terms have order zero, so
\[
\sigma_2(P_{m,\xi})(x,\zeta)
=-g_x^{-1}(\zeta,\zeta).
\]
Consequently every \(P_{m,\xi}\) is a [[mathematical-physics/normally-hyperbolic-operator|normally hyperbolic operator]], with the same characteristic null cone and finite propagation speed as the massless wave operator.

## Minkowski dispersion relation

On [[mathematical-physics/minkowski-spacetime|Minkowski spacetime]],
\[
P_m=\partial_t^2-\sum_j\partial_{x_j}^2+m^2.
\]
For a plane wave \(e^{-i\omega t+i k\cdot x}\), the equation \(P_m\phi=0\) becomes
\[
\omega^2=|k|^2+m^2.
\]

## Convention warning

If a source uses \(\widetilde\Box_g=\operatorname{tr}_g\nabla d=-\Box_g\) with the same \((-+\cdots+)\) signature, it usually writes the equivalent equation as \((\widetilde\Box_g-m^2)\phi=0\). Neither the sign of the mass term nor the symbol \(\Box\) is meaningful without the wave-operator convention.

## References

1. Christian Bär, Nicolas Ginoux, and Frank Pfäffle, *Wave Equations on Lorentzian Manifolds and Quantization*, European Mathematical Society, 2007. [Publisher record](https://doi.org/10.4171/037). Relevant: §§3.2 and 4.3.
2. Robert M. Wald, *Quantum Field Theory in Curved Spacetime and Black Hole Thermodynamics*, University of Chicago Press, 1994. [Publisher record](https://press.uchicago.edu/ucp/books/book/chicago/Q/bo3684008.html). Relevant: Chapters 3–4.
