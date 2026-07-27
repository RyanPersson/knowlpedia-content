+++
id = "differential-geometry/jet-of-a-smooth-map"
title = "Jet of a smooth map"
kind = "definition"
summary = "A finite-order jet records the derivatives of a smooth map at one point through a specified order."
aliases = ["r-jet", "jet equivalence of maps"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(M,N\) be smooth manifolds, \(x\in M\), and \(r\geq 0\) an integer. Two [[fiber-bundles/smooth-map|smooth maps]] \(f,g\), defined near \(x\), have the same **\(r\)-jet at \(x\)** if \(f(x)=g(x)\) and, in local coordinates about \(x\) and their common value, all partial derivatives of their coordinate representatives of total order at most \(r\) agree at \(x\). This relation is independent of the chosen coordinates. The equivalence class is denoted \(j_x^r f\). Varying \(x\), the value \(f(x)\), and the class produces the [[fiber-bundles/jet-bundle|jet bundle]] \(J^r(M,N)\).

## Source, target, and prolongation

The maps
\[
\alpha(j_x^r f)=x,\qquad \beta(j_x^r f)=f(x)
\]
are the source and target projections \(J^r(M,N)\to M\) and \(J^r(M,N)\to N\). Every smooth map \(f:M\to N\) has an \(r\)-jet prolongation \(j^r f:M\to J^r(M,N)\), \(x\mapsto j_x^r f\). For \(s\leq r\), forgetting derivatives of order greater than \(s\) defines a truncation \(J^r(M,N)\to J^s(M,N)\).

## Special orders and composition

A \(0\)-jet remembers only \((x,f(x))\), so \(J^0(M,N)\cong M\times N\). A \(1\)-jet additionally remembers the linear map \(df_x:T_xM\to T_{f(x)}N\). Jets compose: \(j_{f(x)}^r g\) and \(j_x^r f\) determine \(j_x^r(g\circ f)\) by the chain rule through order \(r\).

## Relation to jets of sections

When \(E\to M\) is a smooth fiber bundle, jets of local sections are precisely those map jets \(j_x^r s\) for which the source is \(x\) and the composite \(M\xrightarrow{s}E\to M\) is the identity. The section jet bundle \(J^rE\) is therefore a constrained version of the general map-jet construction. For \(r>1\), these bundles are generally affine in their highest-order data rather than canonically vector bundles.

## References

1. M. W. Hirsch, *Differential Topology*, Springer, 1976. [DOI record](https://doi.org/10.1007/978-1-4684-9449-5). Relevant: Chapter 2.
2. M. Golubitsky and V. Guillemin, *Stable Mappings and Their Singularities*, Springer, 1973. [DOI record](https://doi.org/10.1007/978-1-4615-7904-5). Relevant: Chapter II.
