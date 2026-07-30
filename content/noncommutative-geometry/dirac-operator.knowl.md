+++
id = "noncommutative-geometry/dirac-operator"
title = "Dirac operator"
kind = "definition"
summary = "The spin-geometric first-order operator obtained by Clifford contraction of the spin connection."
aliases = ["Atiyah-Singer Dirac operator", "spin Dirac operator", "geometric Dirac operator"]
domains = ["noncommutative-geometry", "differential-geometry"]
section_mode = "progressive"
+++

Let \(M\) be an oriented [[differential-geometry/riemannian-manifold|Riemannian manifold]] without boundary equipped with a
[[fiber-bundles/spin-structure|spin structure]], \(S\to M\) its
[[differential-geometry/spinor-bundle|spinor bundle]], and \(\nabla^S\) its
[[fiber-bundles/spin-connection|spin connection]]. The **spin Dirac operator**
is the Clifford contraction of the covariant derivative:
\[
\not D=c\circ\nabla^S:\Gamma_c^\infty(S)\longrightarrow\Gamma_c^\infty(S),\qquad
\not D\psi=\sum_{j=1}^{\dim M}c(e^j)\nabla^S_{e_j}\psi,
\]
where \((e_j)\) is any local orthonormal frame. The expression is independent of that frame. Its principal symbol is Clifford multiplication, so \(\not D\) is a formally self-adjoint [[noncommutative-geometry/dirac-type-operator|Dirac-type operator]].

## Analytic realization

With the Riemannian measure and Hermitian spinor metric, \(\not D\) is an unbounded [[functional-analysis/symmetric-operator|symmetric operator]] on \(L^2(M,S)\). If \(M\) is complete, \(\not D\) is [[functional-analysis/essentially-self-adjoint-operator|essentially self-adjoint]], so its closure is self-adjoint. If \(M\) is closed, this realization has compact resolvent and discrete real spectrum of finite multiplicity; see [Roe, chapter 5](https://doi.org/10.1201/b16418).

## Geometric identities and variants

The Lichnerowicz formula
\[
\not D^{\,2}=(\nabla^S)^*\nabla^S+\frac{1}{4}\operatorname{Scal}
\]
relates the operator to scalar curvature. Twisting \(S\) by a Hermitian bundle with connection yields a twisted Dirac operator with an additional curvature term in its square. In even dimensions the spinor bundle is \(\mathbb Z/2\)-graded and \(\not D\) interchanges the two graded pieces.

## Conventions and scope

**Warning.** This knowl uses “Dirac operator” for the spin-geometric operator. The broader class of Dirac-type operators includes Hodge–de Rham and signature operators. The Dirac monopole connection is instead a connection associated with a magnetic monopole and is not this operator.

This page is specifically Riemannian: its principal symbol is invertible away from the zero section, so \(\not D\) is elliptic, and its analytic realization uses a positive-definite \(L^2\) inner product. On a [[differential-geometry/lorentzian-spinor-bundle|Lorentzian spinor bundle]], Clifford contraction instead gives a nonelliptic operator whose characteristic covectors are null. Its flat model is the [[mathematical-physics/minkowski-dirac-operator|Minkowski Dirac operator]], and its evolution equation is the [[mathematical-physics/dirac-equation|Dirac equation]]. These operators share a Clifford-geometric construction but belong to different analytic categories.

## References

1. H. B. Lawson Jr. and M.-L. Michelsohn, *Spin Geometry*, Princeton University Press, 1989. [Publisher record](https://doi.org/10.1515/9781400883912). Relevant: chapter II, §5, spinor bundles and the Dirac operator.
2. J. Roe, *Elliptic Operators, Topology and Asymptotic Methods*, 2nd ed., Chapman & Hall/CRC, 1998. [Publisher record](https://doi.org/10.1201/b16418). Relevant: chapters 3 and 5, Clifford operators and analytic properties.
