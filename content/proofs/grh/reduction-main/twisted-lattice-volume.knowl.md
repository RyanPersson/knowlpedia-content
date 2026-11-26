+++
id = "proofs/grh/reduction-main/twisted-lattice-volume"
title = "Volume Z(xi) of a twist in a twisted lattice"
kind = "definition"
summary = "The number Z(xi) = det(Theta_xi* Theta_xi), the Gram determinant of the images under Theta_xi of an orthonormal basis."
aliases = ["Z(xi)", "volume of a twisted lattice"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.TwistedLattice.volume", "New.TwistedLattice.volume_eq_det_adjoint_comp", "New.TwistedLattice.volume_ne_zero"]
lean_files = ["src/New/Reduction/Lattices/TwistedLattice.lean"]
+++

Let \(L\) be a [[proofs/grh/reduction-main/twisted-lattice|twisted lattice]] on \(V\), and assume now that \(V\) is a finite-dimensional complex [[?c:inner product space|inner product space]]. For a twist \(\xi\), the **volume** of \(\xi\) is
\[
Z(\xi):=\det\bigl(\langle\Theta_\xi e_i,\Theta_\xi e_k\rangle\bigr)_{i,k}\ \in\mathbb R_{\ge0}\subset\mathbb C ,
\]
the [[?c:Gram determinant|Gram determinant]] of the images of an [[?c:orthonormal basis|orthonormal basis]] \((e_i)\) of \(V\); it does not depend on the basis. If \(S_\xi\) is finite-dimensional, \(Z(\xi)=\det(\Theta_\xi^*\Theta_\xi)\) with \(\Theta_\xi^*\) the [[?c:adjoint of a linear map between inner product spaces|adjoint]].

## Properties

1. If \(\Theta_\xi\) is injective, then \(Z(\xi)\ne0\).
2. For any family \(x_1,\dots,x_d\) in \(V\) with \(d=\dim V\): \(\det(\langle\Theta_\xi x_i,\Theta_\xi x_k\rangle)=Z(\xi)\cdot\det(\langle x_i,x_k\rangle)\). (Write \(x=Pe\) for a matrix \(P\); both Gram matrices get multiplied by \(\bar P\) and \(P^{\mathsf T}\).)

In the Lean source \(Z(\xi)\) is defined as the square of `normDet`, the nonnegative square root of \(\det(\Theta_\xi^*\Theta_\xi)\).

## References

1. Lean: `New.TwistedLattice.volume`, `.volume_eq_det_adjoint_comp`, `.volume_ne_zero` in `src/New/Reduction/Lattices/TwistedLattice.lean`; property (2) is `New.det_gram_comp` in `src/Lib/General/LinearAlgebra/GramDeterminant.lean`.
