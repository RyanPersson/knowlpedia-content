+++
id = "proofs/grh/spanning-core/local-bounds-of-a-bessel-function"
title = "Local bounds of a Bessel function at a real place"
kind = "definition"
summary = "A sieve system of forms on tuples of nonzero complex numbers whose top form is an inner product of normalised orbital integrals of the Bessel function."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.HasLocalBounds", "New.besselOrbitalIntegral", "New.normalizedOrbitalIntegral", "New.Shape.openCellConst", "New.Shape.openCellConst_pos", "New.Shape.scaledVolumeRatio", "New.pairingBoundSq"]
lean_files = ["src/New/Spanning/Bessel/Basic.lean"]
+++

Let \(\mathfrak s\) be a [[?lean:New.Shape|shape]], \(n=\varrho+1\), \(k=\lvert\kappa\rvert\), \(r\) the rank, \(G_1\) the real unitary group with Haar measure, and \(W\colon G_1\to\mathbb{C}^I\).

**Constants.** With \(\operatorname{vol}U(j)=\prod_{i<j}2\pi^{i+1}/i!\) ([[?lean:New.volU|`volU`]]):
\[
c_G=\frac{\operatorname{vol}U(k)}{\operatorname{vol}U(r)}\cdot\frac{2\pi^k}{(k-1)!}>0\quad(\textbf{open cell constant}),\qquad\Theta=\frac{\operatorname{vol}U(k)}{\operatorname{vol}U(r)}\,\pi^{(2\varrho+1)k}.
\]
**Orbital integral.** For a group \(G\) with measure \(\mu\) and \(\gamma\in G\), \(J(\gamma)=\int W(y)\otimes\overline{W(\gamma^{-1}y)}\,d\mu(y)\in\mathbb{C}^{I\times I}\), with coordinates \(\int W_i(y)\overline{W_j(\gamma^{-1}y)}d\mu(y)\). For \(y\in G_1\) and a sequence \(p=(p_0,p_1,\dots)\) of nonzero complex numbers, the **normalised orbital integral** is
\[
\widetilde J_y(p)=\frac{\sqrt{c_G}\,\bigl(\sqrt{\lvert p_\varrho\rvert^2-1}\bigr)^{k-1}}{\lvert I\rvert}\prod_{a<\varrho}\lvert p_a\rvert^{k+1+2(\varrho-a-1)}\cdot J(w_p\,y),
\]
where \(w_p\) is the [[?lean:New.Floors.FloorGroups.weylElem|Weyl element]] mapping \(e_a\mapsto p_ae_a^*\), \(e_a^*\mapsto e_a/\bar p_a\) for \(a<\varrho\) (indices from \(0\)) and fixing the other basis vectors (real square roots are \(0\) at negative arguments).

**Definition.** Given \(b,\deg\in\mathbb{R}\) and forms \(J_i(p,q)\in\mathbb{C}\) \((i\ge0)\) on pairs of sequences of nonzero complex numbers, \(W\) **has local bounds** \((b,\deg,J)\) if

* (a) \(J\) is a [[?lean:New.SieveSystem|sieve system]] over \(\mathbb{C}\) of length \(\varrho\), with entries \(c\mapsto c\) (and \(1\) for \(c=0\)), return map \(x\mapsto x^{-1}\), character \(c\mapsto e^{c-\bar c}\), bound \((1+b^{-10})/\deg\) for the bottom form \(J_0\), weights the [[?lean:New.headWeight|head weights]] with radius \(b^{60n^2}\) and exponent \(n^6\), and decay \(\xi\mapsto\Theta\,b^{2000n^9}\,\ell_{k-n^7}(1/\lvert\xi\rvert)\), where \(\ell_j(t)=t^j\min(1,t)^6\);
* (b) for every \(\sigma\) in the [[?lean:New.Shape.Form.floorGroup|floor group]] of level \(\varrho\) (the isometries fixing the hyperbolic basis vectors) and all \(p,q\) with \(p_\varrho=q_\varrho=h(z,\sigma z)\), the top form is \(J_n(p,q)=\bigl\langle\widetilde J_\sigma(p),\widetilde J_\sigma(q)\bigr\rangle\).

The **pairing bound** at \(y\in G_1\), for reals \(\deg,\rho,d\), is \(\bigl(\rho^{9n}/\mathsf g\bigr)^{10^5n^4}\cdot d^2/\bigl(\deg\cdot c_G\cdot(\mathsf g/2)^{k-1}\bigr)\) with \(\mathsf g=\mathsf g(Z(y))\) the real [[proofs/grh/spanning-core/frame-discriminant|frame discriminant]] of the [[proofs/grh/spanning-core/frame-gram-matrix-of-an-isometry|frame Gram matrix]] of \(y\).

## Remarks

The subtraction \(k-n^7\) is of natural numbers (it is \(0\) if \(k<n^7\)), as is \(k-1\).

## References

1. Lean: `New.HasLocalBounds`, `New.besselOrbitalIntegral`, `New.normalizedOrbitalIntegral`, `New.Shape.openCellConst`, `New.Shape.scaledVolumeRatio`, `New.pairingBoundSq` in `src/New/Spanning/Bessel/Basic.lean`.
