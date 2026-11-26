+++
id = "proofs/grh/reduction-main/covolume-bound"
title = "Covolume bound for a family in a twisted lattice"
kind = "definition"
summary = "A finite family has covolume at most c if the Gram determinant of its untwisted lifts, formed after applying any automorphism of C to the coordinates, has absolute value at most exp(c)."
aliases = ["covolume at most c", "CovolumeLe", "conjugate squared norm in a twisted lattice"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.TwistedLattice.conjCoord", "New.TwistedLattice.normSqAt", "New.TwistedLattice.CovolumeLe"]
lean_files = ["src/New/Reduction/Lattices/TwistedLattice.lean"]
+++

Let \(L\) be a [[proofs/grh/reduction-main/twisted-lattice|twisted lattice]] on \(V\), with lift \(\Theta_1:V\to S_1\) for the trivial twist, coordinates \(\operatorname{coord}:S_1\to\mathbb C^C\) and rational Gram matrix \(G\). For a [[algebra-fields-galois/field-automorphism|field automorphism]] \(\sigma\) of \(\mathbb C\) and \(y\in V\) let
\[
\sigma\Theta_1y:=\bigl(\sigma(\operatorname{coord}(\Theta_1y)_c)\bigr)_{c\in C}\in\mathbb C^C ,
\]
the coordinate vector of \(\Theta_1y\) with \(\sigma\) applied to every coordinate, and for \(v,w\in\mathbb C^C\) put \(\langle v,w\rangle_G:=\bar v^{\mathsf T}Gw\).

- The **squared norm of \(y\) at \(\sigma\)** is \(\lVert\Theta_1y\rVert_\sigma^2:=\langle\sigma\Theta_1y,\sigma\Theta_1y\rangle_G\), a nonnegative real number.
- A family \(y=(y_k)_{k\in S}\) in \(V\), \(S\) finite, **has covolume at most \(c\)** (\(c\in\mathbb R\)) if for every automorphism \(\sigma\) of \(\mathbb C\)
\[
\Bigl\lvert\det\bigl(\langle\sigma\Theta_1y_i,\sigma\Theta_1y_k\rangle_G\bigr)_{i,k\in S}\Bigr\rvert\le e^{c}.
\]

For \(\sigma=\mathrm{id}\) the determinant is the [[?c:Gram determinant|Gram determinant]] of the vectors \(\Theta_1y_k\) in \(S_1\), i.e. the squared covolume of the lattice they span; \(c\) thus bounds the logarithm of a *squared* covolume, at every conjugate. Rules are in [[proofs/grh/reduction-main/covolume-calculus|the calculus of covolumes]].

## References

1. Lean: `New.TwistedLattice.conjCoord`, `New.TwistedLattice.normSqAt`, `New.TwistedLattice.CovolumeLe` in `src/New/Reduction/Lattices/TwistedLattice.lean`; the matrix \((\langle v_i,v_k\rangle_G)\) is `New.formGram` in `src/Lib/General/LinearAlgebra/GramDeterminant.lean`.
