+++
id = "lie-groups/derived-pullback-representation"
title = "Derived inverse-pullback representation"
kind = "theorem"
summary = "Differentiating the inverse-pullback action gives minus the Lie derivative along the fundamental vector field."
aliases = ["infinitesimal inverse pullback", "Lie derivative of a pullback representation"]
domains = ["lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/smooth-action-lie-group", "lie-groups/fundamental-vector-field-left-action", "fiber-bundles/lie-derivative", "lie-groups/representation-of-a-lie-algebra"]
+++

Let a Lie group \(G\) [[lie-groups/smooth-action-lie-group|act smoothly from the left]] on a smooth manifold \(M\). On \(C^\infty(M;\mathbb C)\), define
\[
(\pi(g)f)(p)=f(g^{-1}\cdot p).
\]
For the [[lie-groups/fundamental-vector-field-left-action|fundamental field]] \(X_M(p)=\left.\frac d{dt}\right|_0\exp(tX)\cdot p\), differentiation gives the [[lie-groups/representation-of-a-lie-algebra|Lie-algebra action]]
\[
d\pi(X)f=-X_Mf=-\mathcal L_{X_M}f,
\]
where \(\mathcal L\) is the [[fiber-bundles/lie-derivative|Lie derivative]] on functions.

## Chain-rule calculation

The inverse in the group action produces the minus sign:
\[
\left.\frac d{dt}\right|_0 f(\exp(-tX)\cdot p)
=-df_p(X_M(p)).
\]
Inverse pullback is a left representation: \(\pi(g)\pi(h)=\pi(gh)\). The identity \([X_M,Y_M]=-[X,Y]_M\) then gives the usual derived commutator identity.

## Hilbert-space realizations

If the action preserves a positive smooth measure on \(M\), inverse pullback also defines a strongly continuous unitary representation on \(L^2(M)\). The same derivative formula holds on \(C_c^\infty(M)\) and on other smooth functions when their orbit maps have the required \(L^2\) derivatives. A pointwise smooth \(L^2\) function need not itself be a smooth vector.

For a flow, the forward [[ergodic-theory/koopman-generator|Koopman convention]] \(U_t f=f\circ T_t\) instead differentiates to \(+X_Mf\). Specifying forward or inverse pullback prevents a sign mismatch.
