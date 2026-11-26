+++
id = "proofs/grh/spanning-core/bessel-lattice-basis"
title = "Lattice basis of the Bessel space"
kind = "construction"
summary = "The basis in which the distinguished vector of X_0 is replaced by v = x/p-bar + z/N, and its Gram matrix."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.latticeMiddleGram", "New.middleInclusionMatrix", "New.besselLatticeBasis", "New.gram_besselLatticeBasis", "New.fromCols_middleInclusionMatrix"]
lean_files = ["src/New/Spanning/Bessel/Basic.lean"]
+++

Let \(R\) be a commutative ring with involution \(x\mapsto\bar x\), \(\mathfrak s\) a [[?lean:New.Shape|shape]] with distinguished index \(k_0\in\kappa\), \(p\in R^\times\) and \(N=p\bar p\). Consider the free module with basis \(e_a\ (a\le\varrho)\); \(x_i\ (i\in\kappa)\), \(z\); \(e_a^*\), with the hermitian form \(h\) whose Gram matrix is: hyperbolic pairs \((e_a,e_a^*)\), the identity on the \(x_i\), and \(h(z,z)=-N\).

The **lattice basis** is the basis obtained by replacing \(x_{k_0}\) by
\[
v=\frac{x_{k_0}}{\bar p}+\frac zN ,
\]
keeping all other basis vectors. Its matrix in the standard basis is invertible; the inverse expresses \(x_{k_0}=\bar p\,v-p^{-1}z\).

**Gram matrix.** In the lattice basis the Gram matrix of \(h\) again consists of the hyperbolic pairs and a middle block, the **lattice middle Gram matrix**: \(1\) at \((x_i,x_i)\) for \(i\neq k_0\), \(0\) at \((v,v)\), \(-N\) at \((z,z)\), \(-1\) at \((v,z)\) and \((z,v)\), and \(0\) elsewhere.

## Proof

\(h(v,v)=\frac1{p\bar p}-\frac{N}{N^2}=0\), \(h(v,z)=\frac1{\bar N}\cdot(-N)=-1\) (as \(\bar N=N\)), and \(v\) is orthogonal to the \(x_i\), \(i\ne k_0\), and to the \(e_a,e_a^*\). \(\blacksquare\)

## References

1. Lean: `New.besselLatticeBasis`, `New.latticeMiddleGram`, `New.gram_besselLatticeBasis` in `src/New/Spanning/Bessel/Basic.lean`.
