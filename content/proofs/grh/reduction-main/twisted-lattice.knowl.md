+++
id = "proofs/grh/reduction-main/twisted-lattice"
title = "Twisted lattice"
kind = "definition"
summary = "A family of linear maps from one complex vector space to inner product spaces, one for each twist, with integral vectors at every finite place of C and rational coordinates for the trivial twist."
aliases = ["TwistedLattice", "integral vectors of a twisted lattice", "matrix carrying a family with loss"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.TwistedLattice", "New.TwistedLattice.integralVectors", "New.TwistedLattice.mem_integralVectors", "New.PrimePadicIso.Carries", "New.PrimePadicIso.Carries.fromBlocks"]
lean_files = ["src/New/Reduction/Lattices/TwistedLattice.lean"]
+++

Let \(V\) be a complex [[?c:vector space|vector space]] and \(T\) a set, whose elements are called *twists*, with a distinguished element \(1\in T\) (the *trivial twist*). A **twisted lattice** \(L\) on \(V\) with twists \(T\) consists of the following data, where \(\iota\mid\ell\) runs over the [[proofs/grh/reduction-main/prime-padic-iso|finite places of \(\mathbb C\)]], with valuation rings \(\mathcal O_\iota\) and conjugates \(\bar\iota\):

1. for each \(\xi\in T\), a complex [[?c:inner product space|inner product space]] \(S_\xi\) (inner product \(\langle\cdot,\cdot\rangle\), conjugate-linear in the first variable) and a \(\mathbb C\)-[[?c:linear map|linear map]] \(\Theta_\xi:V\to S_\xi\), the *lift*;
2. a relation "\(\xi\) is **allowed** at \(\ell\)" between natural numbers \(\ell\) and twists \(\xi\);
3. for each \(\xi\) and each \(\iota\), an \(\mathcal O_\iota\)-[[?c:submodule|submodule]] \(\Lambda_{\xi,\iota}\subseteq S_\xi\), the vectors *integral at \(\iota\)*;
4. a finite set \(C\) of *coordinates*, a \(\mathbb C\)-linear map \(\operatorname{coord}:S_1\to\mathbb C^{C}\), and a matrix \(G\in\mathbb Q^{C\times C}\);

subject to the axioms

- **(integrality of products)** if \(\xi\) is allowed at \(\ell\) and \(\iota\mid\ell\), then \(\lvert\langle\varphi,\varphi'\rangle\rvert_\iota\le1\) for all \(\varphi\in\Lambda_{\xi,\bar\iota}\) and \(\varphi'\in\Lambda_{\xi,\iota}\);
- **(rational form)** \(G\), viewed in \(\mathbb C^{C\times C}\), is [[?c:positive definite hermitian matrix|positive definite hermitian]], and \(\langle\varphi,\varphi'\rangle=\overline{\operatorname{coord}(\varphi)}^{\,\mathsf T}\,G\,\operatorname{coord}(\varphi')\) for all \(\varphi,\varphi'\in S_1\).

The **integral vectors of \(L\) at \(\iota\mid\ell\)** are
\[
L_\iota:=\{\,y\in V:\ \Theta_\xi(y)\in\Lambda_{\xi,\iota}\ \text{for every twist }\xi\text{ allowed at }\ell\,\},
\]
an \(\mathcal O_\iota\)-submodule of \(V\).

## Carrying a family with loss

Let \(\iota\mid\ell\), let \(W\) be an \(\mathcal O_\iota\)-module, \(M\subseteq W\) a submodule, \(S\) a finite set, \(y=(y_k)_{k\in S}\) a family in \(W\), \(u\in\mathcal O_\iota^{S\times S}\) and \(a\in\mathbb R\). We say **\(u\) carries \(y\) into \(M\) with loss \(a\)** if
\[
\lvert\det u\rvert_\iota\ge\ell^{-a}\qquad\text{and}\qquad\sum_{k\in S}u_{ik}y_k\in M\ \text{ for all } i\in S .
\]
If \(u\) carries \(y\) into \(M\) with loss \(a\) and \(u'\) carries \(y'\) into \(M\) with loss \(a'\), then the block diagonal matrix \(\operatorname{diag}(u,u')\) carries the concatenated family \((y,y')\) into \(M\) with loss \(a+a'\), since its determinant is \(\det u\det u'\).

## Remarks

- No inner product on \(V\) and no finiteness is part of the definition; they are assumed only where the [[proofs/grh/reduction-main/twisted-lattice-volume|volume \(Z(\xi)\)]] is used.
- Integrality in \(V\) refers to all twists allowed at \(\ell\) simultaneously, whereas the [[proofs/grh/reduction-main/covolume-bound|covolume]] refers to the trivial twist only. The [[proofs/grh/reduction-main/index-bound|index]] measures how far a family is from being integral.
- The instance used in the proof is the [[proofs/grh/reduction-main/target-lattice|twisted lattice of target forms]].

## References

1. Lean: `New.TwistedLattice`, `New.TwistedLattice.integralVectors`, `New.PrimePadicIso.Carries`, `New.PrimePadicIso.Carries.fromBlocks` in `src/New/Reduction/Lattices/TwistedLattice.lean`.
2. Related work named in the Lean file head: J.-B. Bost, *Algebraic leaves of algebraic foliations over number fields*, 2001; M. Laurent, *Linear forms in two logarithms and interpolation determinants*, 1994.
