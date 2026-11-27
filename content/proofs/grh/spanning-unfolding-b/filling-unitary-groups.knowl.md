+++
id = "proofs/grh/spanning-unfolding-b/filling-unitary-groups"
title = "Unitary groups of a filling datum and the maps between them"
kind = "construction"
summary = "The unitary group of V over a ring, its finite adelic form in the lattice basis, and the maps from rational points to the rescaled real groups and to the finite adelic group."
aliases = ["ratToInf", "ratToFin", "lattice basis of the filling datum"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.G", "New.Filling.GFin", "New.Filling.latticeBasis", "New.Filling.toLatticeBasis", "New.Filling.ratToAdelic", "New.Filling.adelicToInf", "New.Filling.adelicToFin", "New.Filling.ratToInf", "New.Filling.ratToFin", "New.Filling.inclHFin", "New.Filling.basisScale", "New.Filling.basisScaleGL", "New.Filling.basisScale_ne_zero", "New.Filling.realM", "New.Filling.coe_realM", "New.Filling.conjTranspose_basisScaleGL_mul_splitGram_mul", "New.Filling.ratToInf_apply", "New.Filling.adelicToInf_apply", "New.Filling.coe_ratToFin", "New.Filling.map_splitGram_ratMiddle"]
lean_files = ["src/New/Spanning/Unfolding/Setup.lean"]
+++

Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] over \(E\) of shape \((\varrho,\kappa,k_0)\). Let \(V\) be the free module with basis
\[
e_0,\dots,e_{\varrho-1};\quad x_i\ (i\in\kappa),\ z;\quad e_0^*,\dots,e_{\varrho-1}^*
\]
and let \(J\) be the [[?lean:New.Shape.Form.splitGram|split Gram matrix]] with \(h(e_a,e_a^*)=h(e_a^*,e_a)=1\), \(h(x_i,x_i)=1\), \(h(z,z)=-N\) and all other products of basis vectors zero. The *frame* is \((f_0,\dots,f_\varrho)=(e_0,\dots,e_{\varrho-1},z)\).

**The groups.** For a commutative ring \(R\) with involution, \(G(R)\) is the [[?c:Unitary group of a hermitian form|unitary group]] of \(J\) over \(R\): the invertible matrices \(g\) over \(R\) with \(g^{*}Jg=J\), where \(g^*\) is the conjugate transpose. The group \(G_{\mathrm{fin}}\) is the unitary group over the finite adeles \(\mathbb{A}_f\) of the Gram matrix \(J^{\mathrm{lat}}\) of the same form in the *lattice basis*, obtained from the standard basis by replacing \(x_{k_0}\) with \(x_{k_0}/\bar\pi+z/N\). If \(B\) denotes the matrix whose columns are the lattice basis ([[?lean:New.besselLatticeBasis|lattice basis matrix]]; \(B^{*}JB=J^{\mathrm{lat}}\) by [[?lean:New.gram_besselLatticeBasis|its Gram matrix]]), then \(g\mapsto B^{-1}gB\) is an isomorphism \(G(\mathbb{A}_f)\to G_{\mathrm{fin}}\).

**Scales.** For an infinite place \(v\) put
\[
\kappa_v=\operatorname{Re}\frac{M\,\Phi_v(\varpi)}{2\pi i}\in\mathbb{R}.
\]
The *scales of the normalised basis at \(v\)* are
\[
\sigma_v(e_a)=\frac{\kappa_v^{\varrho-a}}{\sqrt N},\qquad \sigma_v(x_i)=1,\qquad \sigma_v(z)=\frac1{\sqrt N},\qquad \sigma_v(e_a^*)=\sigma_v(e_a)^{-1},
\]
so that \(\sigma_v(f_a)=\kappa_v^{\varrho-a}/\sqrt N\) for all \(0\le a\le\varrho\). Let \(D_v=\operatorname{diag}(\sigma_v)\). Let \(G_1\) be the [[?lean:New.Shape.G₁|real group]], the unitary group over \(\mathbb{C}\) of the split Gram matrix \(J_1\) with middle block \(\operatorname{diag}(1,\dots,1,-1)\), and \(G_\infty=\prod_v G_1\).

**The maps.**

* \(\gamma\mapsto\gamma_\infty\colon G(E)\to G_\infty\) sends \(\gamma\) to the tuple \(\bigl(D_v^{-1}\,\Phi_v(\gamma)\,D_v\bigr)_v\); in entries,
\[
(\gamma_\infty)_v(i,j)=\Phi_v(\gamma_{ij})\,\frac{\sigma_v(j)}{\sigma_v(i)} .
\]
* \(\gamma\mapsto\gamma_{\mathrm{fin}}\colon G(E)\to G_{\mathrm{fin}}\) sends \(\gamma\) to \(B^{-1}\gamma B\), where \(\gamma\) is read in \(\mathbb{A}_f\) by the diagonal embedding.
* \(\iota_H\colon U(X_0)(\mathbb{A}_f)\to G_{\mathrm{fin}}\) is the [[?lean:New.toBesselH|inclusion]] of the unitary group of \(X_0\) (acting trivially on \(z\) and on the \(e_a,e_a^*\)) followed by \(g\mapsto B^{-1}gB\).

Both of the first two maps are [[algebra-groups/group-homomorphism|group homomorphisms]] that factor through the adelic group \(G(\mathbb{A})\).

## Well-definedness

**\(\kappa_v\) is real and nonzero.** Since \(\bar\varpi=-\varpi\), the number \(\Phi_v(\varpi)\) is purely imaginary, so \(M\Phi_v(\varpi)/(2\pi i)\) is real and equals \(\kappa_v\); it is nonzero because \(\varpi\neq0\) and \(M\ne0\). Moreover \(\lvert\kappa_v\rvert=M\lvert\Phi_v(\varpi)\rvert/(2\pi)\).

**Rescaling.** All scales are real and nonzero, and \(D_v^{*}J_{\mathbb{C}}D_v=J_1\): the scales of \(e_a\) and \(e_a^*\) are inverse to each other, and \(-N\cdot(1/\sqrt N)^2=-1\). Hence \(g\mapsto D_v^{-1}gD_v\) carries the unitary group of \(J\) over \(\mathbb{C}\) onto \(G_1\). A ring homomorphism \(R\to R'\) maps \(J\) over \(R\) to \(J\) over \(R'\), since its entries are \(0\), \(1\) and \(-N\); so it induces \(G(R)\to G(R')\).

## References

1. Lean: `New.Filling.G`, `New.Filling.GFin`, `New.Filling.ratToInf`, `New.Filling.ratToFin`, `New.Filling.inclHFin`, `New.Filling.basisScale`, `New.Filling.realM` in `src/New/Spanning/Unfolding/Setup.lean`.
