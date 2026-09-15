+++
id = "ergodic-theory/koopman-generator"
title = "Infinitesimal generator of a Koopman flow"
kind = "definition"
summary = "The skew-adjoint operator obtained by differentiating a strongly continuous Koopman group in time."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/measure-preserving-flow", "lie-groups/stone-theorem-one-parameter-unitary-groups", "lie-groups/strongly-continuous-unitary-representation"]
+++

Let \(\Phi^t\) be a [[ergodic-theory/measure-preserving-flow|probability-preserving flow]] such that \(U_tf=f\circ\Phi^t\) is strongly continuous on \(L^2\). Its **Koopman generator** is
\[
Lf=\lim_{t\to0}\frac{U_tf-f}{t},\qquad
D(L)=\{f:\text{this limit exists in }L^2\}.
\]
By [[lie-groups/stone-theorem-one-parameter-unitary-groups|Stone's theorem]], \(L\) is densely defined and skew-adjoint, \(L=iA\) for a self-adjoint \(A\), and \(U_t=e^{tL}=e^{itA}\).

## Smooth dynamics

If a smooth vector field \(V\) generates a flow on a compact smooth manifold with an invariant probability measure, smooth observables belong to this domain and
\[
Lf=df(V)=V\cdot\nabla f
\]
in local coordinates. Consequently \(u(t,x)=f(\Phi^t x)\) solves the linear equation \(\partial_tu=Lu\). The inverse-pullback representation has generator \(-L\).

## Domain matters

For noncompact spaces or nonsmooth observables the displayed derivative need not belong to \(L^2\). Formal differentiation alone does not specify the domain or establish skew-adjointness.
