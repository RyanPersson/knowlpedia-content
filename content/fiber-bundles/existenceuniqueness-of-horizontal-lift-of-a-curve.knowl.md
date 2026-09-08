+++
id = "fiber-bundles/existenceuniqueness-of-horizontal-lift-of-a-curve"
title = "Theorem: Existence and uniqueness of horizontal lifts of curves"
kind = "knowl"
summary = "Given a connection, any curve in the base has a unique horizontal lift through a chosen point in the fiber."
aliases = ["existenceuniqueness-of-horizontal-lift-of-a-curve", "Theorem: Existence and uniqueness of horizontal lifts of curves"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/existenceuniqueness-of-horizontal-lift-of-a-curve.md"
prerequisites = ["fiber-bundles/principal-g-bundle", "fiber-bundles/principal-connection", "fiber-bundles/horizontal-lift-of-a-curve", "fiber-bundles/smooth-map"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(\pi:P\to M\) be a [[fiber-bundles/principal-g-bundle|principal G-bundle]] with a [[fiber-bundles/principal-connection|principal connection]] \(\omega\), and let \(H=\ker(\omega)\subset TP\) be its horizontal distribution.

Let \(\gamma:[a,b]\to M\) be a smooth curve, and choose a point \(p_0\in P\) with \(\pi(p_0)=\gamma(a)\).


There exists a unique smooth curve \(\widetilde\gamma:[a,b]\to P\) such that:

1. \(\pi\circ \widetilde\gamma=\gamma\),
2. \(\widetilde\gamma(a)=p_0\),
3. \(\dot{\widetilde\gamma}(t)\in H_{\widetilde\gamma(t)}\) for all \(t\) (i.e. \(\widetilde\gamma\) is horizontal).

## Remarks

- In a local trivialization \(P|_U\cong U\times G\), the horizontality condition becomes an ODE in \(G\) driven by the local connection \(1\)-form, so local existence and uniqueness follow from ODE theory. On each compact parameter interval the time-dependent invariant field is bounded in a complete invariant metric on \(G\), giving existence throughout that interval; finitely many bundle charts then cover the base curve. A general Ehresmann connection need not have this global property.
- Horizontal lifting is the basic input for [[fiber-bundles/parallel-transport|parallel transport]] on principal and associated bundles.

## Examples

1. **Trivial bundle with connection form.** For \(P=M\times G\) and a connection given by a \(\mathfrak g\)-valued \(1\)-form \(A\) on \(M\), writing \(\widetilde\gamma(t)=(\gamma(t),g(t))\), horizontality is
   \[
   \dot g(t)g(t)^{-1} = -A_{\gamma(t)}(\dot\gamma(t)),
   \]
   in matrix notation. Intrinsically, \(\dot g=(dR_g)_e(-A(\dot\gamma))\). This is a time-dependent right-invariant ODE, with unique solution given \(g(a)\); the equivalent left logarithmic derivative is \(g^{-1}\dot g=-\operatorname{Ad}_{g^{-1}}A(\dot\gamma)\).

2. **Product (flat) connection.** If \(A=0\), then the equation is \(\dot g(t)=0\), so the horizontal lift is simply \((\gamma(t),g_0)\): constant group component.

3. **Circle bundles.** For a principal \(U(1)\)-bundle with a connection \(1\)-form, horizontal lifts of closed curves encode holonomy as a phase factor; this is the simplest instance of connection-induced transport.
