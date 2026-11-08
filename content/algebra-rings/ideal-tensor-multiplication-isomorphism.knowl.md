+++
id = "algebra-rings/ideal-tensor-multiplication-isomorphism"
title = "Multiplication as a tensor product of compatible ideals"
kind = "theorem"
summary = "An invertible ideal bimodule identifies its tensor product with the ordinary product of compatible ideals."
aliases = ["ideal tensor multiplication isomorphism"]
domains = ["algebra-rings", "algebra-modules"]
section_mode = "progressive"
prerequisites = ["algebra-modules/bimodule", "algebra-modules/tensor-product"]
+++

Let \(A\) be a unital ring and \(\Lambda,\mathcal O,\Gamma\subseteq A\) unital subrings with the same identity. Let \(I\subseteq A\) be a \((\Lambda,\mathcal O)\)-[[algebra-modules/bimodule|bimodule]] and \(J\subseteq A\) an \((\mathcal O,\Gamma)\)-bimodule, with actions inherited from multiplication. Suppose a \((\mathcal O,\Lambda)\)-bimodule \(I'\subseteq A\) satisfies
\[
II'=\Lambda,\qquad I'I=\mathcal O.
\]
Products mean finite sums of elementwise products. Then the canonical multiplication map
\[
\mu:I\otimes_{\mathcal O}J\longrightarrow IJ,
\qquad x\otimes y\longmapsto xy
\]
is an isomorphism of \((\Lambda,\Gamma)\)-bimodules. In particular, it suffices that the first ideal be invertible with these specified left and right orders; invertibility of \(J\) is not required.

## Proof by an explicit inverse

Associativity gives \((xo)y=x(oy)\) for \(o\in\mathcal O\), so multiplication is balanced and induces \(\mu\). It is surjective by the definition of \(IJ\).

Choose finitely many \(x_s\in I\) and \(u_s\in I'\) with \(\sum_s x_su_s=1\). For \(z\in IJ\), each \(u_sz\) belongs to \(J\), since \(I'I\subseteq\mathcal O\). Define the additive map
\[
\nu:IJ\longrightarrow I\otimes_{\mathcal O}J,
\qquad \nu(z)=\sum_s x_s\otimes u_sz.
\]
Then \(\mu\nu(z)=\sum_s x_su_sz=z\). Conversely, the balancing relation and \(u_sx\in\mathcal O\) give
\[
\nu\mu(x\otimes y)
=\sum_s x_s\otimes (u_sx)y
=\sum_s x_s(u_sx)\otimes y
=x\otimes y.
\]
Thus \(\nu=\mu^{-1}\); it is automatically a bimodule map because \(\mu\) is one.

## Locally principal ideals and maximal orders

There is also a useful local sufficient condition. Let \(R\) be a Dedekind domain, \(K=\operatorname{Frac}(R)\), \(A\) a finite-dimensional \(K\)-algebra, and \(\mathcal O\subseteq A\) an \(R\)-order. Let \(I,J\) be full \(R\)-lattices with \(I\mathcal O\subseteq I\) and \(\mathcal OJ\subseteq J\). Suppose that for every nonzero prime \(\mathfrak p\) of \(R\),
\[
I_{\mathfrak p}=a_{\mathfrak p}\mathcal O_{\mathfrak p}
\quad\text{with }a_{\mathfrak p}\in A^\times.
\]
Here subscripts denote localization over \(R\). Locally, multiplication becomes the isomorphism
\[
a_{\mathfrak p}\mathcal O_{\mathfrak p}
\otimes_{\mathcal O_{\mathfrak p}}J_{\mathfrak p}
\longrightarrow a_{\mathfrak p}J_{\mathfrak p},
\qquad a_{\mathfrak p}o\otimes y\longmapsto a_{\mathfrak p}oy,
\]
whose inverse is \(a_{\mathfrak p}y\mapsto a_{\mathfrak p}\otimes y\). Localization commutes with the tensor product and the product lattice. A map of \(R\)-modules is an isomorphism if it is one at every maximal ideal, proving the claim globally. If \(R\) is a field, the full lattices here are all \(A\), and the conclusion is immediate.

Consequently, for a maximal quaternion order over a number ring, any full right ideal \(I\) and full left ideal \(J\) satisfy \(I\otimes_{\mathcal O}J\cong IJ\): the right ideal is [[algebra-rings/locally-principal-quaternion-ideal|locally principal]]. For invertible ideals between orders, the first proof applies whenever the middle orders agree. In particular it applies to all full two-sided fractional ideals of the [[algebra-rings/maximal-order|maximal orders in the central simple setting]]. Over a commutative Dedekind domain this recovers the usual statement for all nonzero fractional ideals.

## Warning: typing alone is insufficient

For arbitrary right and left ideals the map is defined and surjective, but need not be injective. For example, let \(k\) be a field, let \(S=k[\varepsilon]/(\varepsilon^2)\), and let \(L=(\varepsilon)\subset S\). Then \(L\cong S/(\varepsilon)\) as an \(S\)-module, so \(L\otimes_SL\cong k\), whereas \(L^2=0\). This example is not a maximal order; it shows why extra hypotheses cannot simply be omitted.

## References

1. John Voight, *Quaternion Algebras*, [Chapter 16](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_16), §16.3 (invertible lattices), and [Chapter 18](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_18), Theorem 18.1.2 (application to maximal orders). The multiplication isomorphism is proved directly above.
