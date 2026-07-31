+++
id = "differential-geometry/de-rham-homotopy-operator"
title = "de Rham homotopy operator"
kind = "definition"
summary = "The degree-minus-one operator obtained by integrating a pulled-back form along a smooth homotopy, yielding a chain homotopy between endpoint pullbacks."
aliases = ["homotopy operator for differential forms", "chain homotopy on forms"]
domains = ["differential-geometry", "topology"]
section_mode = "progressive"
+++

Let \(F:M\times[0,1]\to N\) be a [[differential-geometry/smooth-homotopy|smooth homotopy]], with \(F_t(x)=F(x,t)\). The **de Rham homotopy operator** associated to \(F\) is the degree-\(-1\) [[linear-algebra/linear-map|linear map]]
\[
K_F:\Omega^k(N)\longrightarrow\Omega^{k-1}(M),\qquad
K_F\omega=\int_0^1\iota_{\partial_t}(F^*\omega)\,dt.
\]
Here contraction extracts the component of the [[fiber-bundles/pullback-of-differential-forms|pulled-back form]] containing \(dt\), and integration removes the interval variable. With this sign and interval orientation, the operator satisfies
\[
dK_F+K_Fd=F_1^*-F_0^*.
\]
It is therefore a concrete [[algebra-homological/chain-homotopy|chain homotopy]] between the two endpoint pullback maps.

## Chain-homotopy interpretation

The endpoint pullbacks \(F_0^*\) and \(F_1^*\) are cochain maps between [[differential-geometry/de-rham-complex|de Rham complexes]]. The displayed identity says precisely that \(K_F\) is a cochain homotopy between them. It follows that smoothly homotopic maps induce the same homomorphism on de Rham cohomology.

The formula follows from Cartan's identity for the [[fiber-bundles/lie-derivative|Lie derivative]] and the fundamental theorem of calculus applied in the interval direction. Reversing the orientation of \([0,1]\) or defining contraction with the opposite product order changes the overall sign.

## Canonical contraction example

On a star-shaped open set \(U\subseteq\mathbb R^n\), the radial homotopy \(F(x,t)=tx\) joins the constant map at the origin to the identity. For a closed form \(\omega\) of positive degree,
\[
\omega=d(K_F\omega),
\]
because pullback by the constant endpoint vanishes in positive degree. This is the standard homotopy-operator proof of the [[differential-geometry/poincare-lemma|Poincaré lemma]].

## Scope

The operator depends on the chosen homotopy, not only on its endpoints, but the induced equality on cohomology does not. For \(k=0\), the target \(\Omega^{-1}(M)\) is understood to be zero; the homotopy formula then says that endpoint pullbacks agree on locally constant functions. Boundary or support conditions require checking that fiber integration preserves the relevant class of forms.

## References

1. Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology*, Springer, 1982. [Publisher record](https://doi.org/10.1007/978-1-4757-3951-0). Relevant: Chapter I, homotopy operators, the Poincaré lemma, and homotopy invariance.
2. Loring W. Tu, *An Introduction to Manifolds*, 2nd ed., Springer, 2011. [Publisher record](https://doi.org/10.1007/978-1-4419-7400-6). Relevant: Chapter 17, the homotopy operator.
