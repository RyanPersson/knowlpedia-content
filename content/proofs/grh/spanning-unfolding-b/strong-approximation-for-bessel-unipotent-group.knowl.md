+++
id = "proofs/grh/spanning-unfolding-b/strong-approximation-for-bessel-unipotent-group"
title = "Strong approximation for the Bessel unipotent group"
kind = "theorem"
summary = "The rational points of the Bessel unipotent group are dense in its finite adelic points; hence every finite adelic unipotent element is approximated by a rational one modulo any conjugate of the principal level."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.besselU_dense", "New.Filling.exists_besselU_approx", "New.continuous_heisenbergElem_finAdele", "New.denseRange_skewPart_algebraMap", "New.map_heisenbergElem_finAdele"]
lean_files = ["src/New/Spanning/Unfolding/BesselLevelStructure.lean"]
proof_status = "full"
+++

**Theorem.** Let \(E\) be a [[?c:CM field|CM field]] and \((\varrho,\kappa,k_0)\) a shape.

1. Let \(T\) be a hermitian invertible matrix over \(E\) on \(\kappa\sqcup\{z\}\), \(J\) the split Gram matrix of \(\varrho\) hyperbolic planes and \(T\), and \(\mathsf{U}\) the [[?lean:New.Shape.Form.besselU|Bessel unipotent group]] of \(J\). Then \(\mathsf{U}(\mathbb{A}_f)\) is contained in the closure of the image of \(\mathsf{U}(E)\) in the unitary group of \(J\) over the finite adeles.
2. Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over \(E\). For every \(x\in\mathsf{U}\subset G_{\mathrm{fin}}\) and every \(y\in G_{\mathrm{fin}}\) there is a rational \(u\in\mathsf{U}(E)\) with
\[
y^{-1}\,x^{-1}u_{\mathrm{fin}}\,y\in K(M).
\]

## Proof

(1) Let \(C\) be the closure of the image of \(\mathsf{U}(E)\); it is a subgroup. The group \(\mathsf{U}\) is built floor by floor: with \(N_l\) the [[?lean:New.Floors.FloorGroups.floorUnipotent|unipotent group of floor \(l\)]], every element of \(\mathsf{U}\) is a product of elements of \(N_{\varrho-1},\dots,N_0\) ([[?lean:New.Floors.FloorGroups.unipotentBelow_induction|induction along the floors]]). So it suffices to show \(N_l(\mathbb{A}_f)\subset C\) for each \(l\). For \(l\ge\varrho\) the group \(N_l\) is trivial. For \(l<\varrho\), every element of \(N_l\) is a [[?lean:New.Floors.TraceOne.heisenbergElem|Heisenberg element]] \(\nu_l(v,\beta)\), the Eichler transformation with \(e_l^*\mapsto e_l^*+v+(\beta-\tfrac12h(v,v))e_l\), for a vector \(v\) on the basis indices of floor \(>l\) and a skew element \(\beta=-\bar\beta\) ([[?lean:New.Floors.FloorGroups.exists_eq_heisenbergElem_of_mem|parametrisation of a floor]]); here the element of trace one is \(\tau=\tfrac12\). The entries of \(\nu_l(v,\beta)\) are polynomials in the coordinates of \(v\), their conjugates and \(\beta\), so \((v,\beta)\mapsto\nu_l(v,\beta)\) is continuous, and it maps rational parameters \((v,t-\bar t)\), \(v\) and \(t\) over \(E\), to images of rational Heisenberg elements, which lie in \(\mathsf{U}(E)\). Rational parameters are dense: \(E\) is dense in \(\mathbb{A}_f\) ([[?lean:New.denseRange_algebraMap_finAdele|density of \(E\) in the finite adeles]]), and the map \(t\mapsto t-\bar t\) from \(\mathbb{A}_f\) onto the skew adeles is continuous and surjective (\(\beta\) is the image of \(\beta/2\)), so the elements \(t-\bar t\), \(t\in E\), are dense in the skew adeles. Hence \(\nu_l(v,\beta)\in C\) for all parameters.

(2) The map \(g\colon G(\mathbb{A}_f)\to G_{\mathrm{fin}}\), \(g(w)=y^{-1}x^{-1}(B^{-1}wB)\,y\), is continuous, and \(K(M)\) is open in \(G_{\mathrm{fin}}\): by [[proofs/grh/spanning-unfolding-b/principal-level-is-congruence-subgroup|its description as a congruence subgroup]] it is cut out by the conditions that the entries of \(k\), \(k^{-1}\) and \(M^{-1}(k-1)\) lie in the open subring \(\widehat{\mathcal{O}}\). So \(V=g^{-1}(K(M))\) is an open set containing \(x_0=BxB^{-1}\). By [[proofs/grh/spanning-unfolding-b/bessel-groups-in-the-lattice-basis|the change of basis]], \(x_0\in\mathsf{U}(\mathbb{A}_f)\) for the rational form. By (1), applied to the middle form \(\operatorname{diag}(1,\dots,1,-N)\), which is hermitian and invertible over \(E\), the open set \(V\) contains the image of some \(u\in\mathsf{U}(E)\); then \(g(u)=y^{-1}x^{-1}u_{\mathrm{fin}}y\in K(M)\).

## Remarks

This is strong approximation for a unipotent group, proved here directly from the density of \(E\) in \(\mathbb{A}_f\).

## References

1. Lean: `New.besselU_dense`, `New.Filling.exists_besselU_approx` in `src/New/Spanning/Unfolding/BesselLevelStructure.lean`.
