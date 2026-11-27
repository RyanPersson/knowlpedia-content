+++
id = "proofs/grh/spanning-unfolding-a/unique-coset-moving-a-point-to-a-reduced-point"
title = "Exactly one coset of unipotent elements moves a point to a reduced point"
kind = "theorem"
summary = "For a residue domain D, the elements u of the unipotent congruence subgroup with u y reduced form exactly one right coset of the subgroup fixing the frame."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.IsResidueDomain.exists_mul_mem_reducedPoints_iff_rightCoset", "New.Filling.ratTriangle_eq_sum"]
lean_files = ["src/New/Spanning/Unfolding/ReducedPoints.lean"]
proof_status = "full"
+++

**Theorem.** Let \(E\) be a [[?c:CM field|CM field]] containing a primitive 5040-th root of unity, \(S\) [[?lean:New.Filling|filling data]] over \(E\) with level \(M\), and \(G_\infty=\prod_v G_1\) the product over the [[?c:Infinite place of a number field|infinite places]] of the real unitary group [[?lean:New.Shape.G₁|\(G_1\)]]; rational [[?c:Isometry of a hermitian space|isometries]] act on \(G_\infty\) through the [[?lean:New.Filling.ratToInf|rescaled embedding at the infinite places]]. For \(y\in G_\infty\) and frame indices \(a,b\) let \(t_{ab}(y)\in\mathbb C^{\{v\}}\) be the tuple whose \(v\)-component is the \((a,b)\) entry of the [[?lean:New.gramSchmidtMatrix|Gram–Schmidt matrix]] of \(y_v\), multiplied by \(\sigma_v(f_a)/\sigma_v(f_b)\), where \(\sigma_v\) is the [[?lean:New.Filling.basisScale|scale of the normalised basis at \(v\)]] ([[?lean:New.Filling.ratTriangle|triangular matrix in the rational frame]]). Let \(D\subseteq\mathbb C^{\{v\}}\) be a [[?lean:New.Filling.IsResidueDomain|residue domain]]: a measurable set, with all coordinates of modulus at most \(b^{26}\), containing exactly one translate of every tuple by the lattice \(\{(\Phi_v(Mx))_v : x\in\mathcal O_E\}\). A point \(y\) is [[?lean:New.Filling.reducedPoints|reduced]] for \(D\) if \(t_{ab}(y)\in D\) for all \(a<b\).

Then for every [[?lean:New.Filling.Classes|class]] \(c\) and every \(y\in G_\infty\) there is \(u_0\in\mathsf U_c(M)\) (the [[?lean:New.Filling.classUnipotent|unipotent congruence subgroup]]) such that for all \(u\in\mathsf U_c(M)\)
\[
u\,y\ \text{is reduced for } D\iff u\,u_0^{-1}\in\mathsf U^{0}_c(M),
\]
where \(\mathsf U^{0}_c(M)\) is the [[?lean:New.Filling.classUnipotent₀|subgroup fixing the frame]]. That is, the set of such \(u\) is the single right coset \(\mathsf U^0_c(M)\,u_0\).

## Proof

Let \(\varphi:E\to\mathbb C^{\{v\}}\), \(\varphi(x)=(\Phi_v(x))_v\), an injective ring homomorphism, and let \(\mathcal T\) be the group of [[?c:Unitriangular matrix|upper unitriangular]] matrices of size \(\varrho+1\) over the ring \(\mathbb C^{\{v\}}\).

*The homomorphism \(\theta\).* For \(u\in\mathsf U_c(M)\) let \(\theta(u)=\varphi(\Theta(u))\), where \(\Theta(u)\) is the [[?lean:New.frameMatrix|frame matrix]]. On the unipotent group \(\mathsf U\) the frame matrix is multiplicative and unitriangular, so \(\theta:\mathsf U_c(M)\to\mathcal T\) is a homomorphism. An element of \(\mathsf U\) fixes the frame if and only if its frame matrix is \(1\); as \(\varphi\) is injective, \(\ker\theta=\mathsf U^0_c(M)\).

*The triangle.* Let \(T(y)\) be the matrix with entries \(t_{ab}(y)\); it is upper unitriangular, so \(T(y)\in\mathcal T\). We claim
\[
T(y)=T(u\,y)\,\theta(u)\qquad(u\in\mathsf U_c(M)).\tag{1}
\]
Indeed, at each place \(v\) the image \(u_v\) of \(u\) in \(G_1\) lies in the Bessel subgroup, and the Gram–Schmidt matrices satisfy \(\operatorname{gs}(u_vy_v)\,\Theta(u_v)=\operatorname{gs}(y_v)\) ([[?lean:New.gramSchmidtMatrix_besselS_mul|Gram–Schmidt matrix under the Bessel subgroup]]). By the formula for the entries of the rescaled embedding, \(\Theta(u_v)_{lb}=\Phi_v(\Theta(u)_{lb})\,\sigma_v(f_b)/\sigma_v(f_l)\). Multiplying the \((a,b)\) entry of the Gram–Schmidt identity by \(\sigma_v(f_a)/\sigma_v(f_b)\), the scales of the summation index \(l\) cancel, and we get \(t_{ab}(y)_v=\sum_l t_{al}(uy)_v\,\Phi_v(\Theta(u)_{lb})\), which is (1). Hence \(T(uy)=T(y)\,\theta(u^{-1})\).

*Reduction.* Let \(L=\varphi(M\mathcal O_E)\) and \(\Gamma=\theta(\mathsf U_c(M))\subseteq\mathcal T\). By the proposition on [[proofs/grh/spanning-unfolding-a/frame-matrices-of-unipotent-congruence-subgroup|frame matrices of the unipotent congruence subgroup]], the entries of elements of \(\Gamma\) above the diagonal lie in \(L\), and \(\Gamma\) contains \(1+lE_{ab}\) for all \(a<b\), \(l\in L\) (this is where the root of unity is used). By the defining property of \(D\) and the lemma on [[proofs/grh/spanning-unfolding-a/reduction-of-unitriangular-matrices|reduction of unitriangular matrices]], there is exactly one \(\gamma_0\in\Gamma\) with all entries of \(T(y)\gamma_0\) above the diagonal in \(D\). Write \(\gamma_0=\theta(w)\) and put \(u_0=w^{-1}\).

*Conclusion.* For \(u\in\mathsf U_c(M)\): \(uy\) is reduced \(\iff\) the entries of \(T(y)\theta(u^{-1})\) above the diagonal are in \(D\) \(\iff\) \(\theta(u^{-1})=\theta(w)\) (existence and uniqueness of \(\gamma_0\)) \(\iff\) \(\theta(u\,w)=1\) \(\iff\) \(u\,u_0^{-1}\in\mathsf U^0_c(M)\).

## References

1. Lean: `New.Filling.IsResidueDomain.exists_mul_mem_reducedPoints_iff_rightCoset` in `src/New/Spanning/Unfolding/ReducedPoints.lean`.
2. Lean: `New.Filling.ratTriangle_eq_sum` in `src/New/Spanning/Unfolding/ReducedPoints.lean`.
