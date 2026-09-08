+++
id = "fiber-bundles/jet-bundle"
title = "Jet bundle (first jets of sections)"
kind = "knowl"
summary = "A bundle whose points record the value and first derivative of a local section at a basepoint."
aliases = ["jet-bundle", "Jet bundle (first jets of sections)"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/jet-bundle.md"
prerequisites = ["fiber-bundles/smooth-fiber-bundle", "fiber-bundles/smooth-manifold", "fiber-bundles/section-of-a-fiber-bundle", "fiber-bundles/differential-of-a-smooth-map", "fiber-bundles/fiber-coordinates", "real-analysis/partial-derivative"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(\pi:E\to M\) be a [[fiber-bundles/smooth-fiber-bundle|smooth fiber bundle]]. Two [[fiber-bundles/section-of-a-fiber-bundle|smooth local sections]] \(s,t\), defined near \(x\in M\), have the same **first jet at \(x\)** if
\[
s(x)=t(x)=e,\qquad ds_x=dt_x:T_xM\longrightarrow T_eE,
\]
where \(ds_x\) and \(dt_x\) are their [[fiber-bundles/differential-of-a-smooth-map|differentials]]. The equivalence class is denoted \(j_x^1s\).

The **first jet bundle** \(J^1E\) consists of all such classes, with projections
\[
\pi_{1,0}(j_x^1s)=s(x),\qquad \pi_1(j_x^1s)=x.
\]
Its smooth structure is defined by the following jet charts. In local bundle coordinates \((x^i,y^\alpha)\), assign to \(j_x^1s\) the coordinates
\[
\left(x^i,y^\alpha(s(x)),y_i^\alpha\right),\qquad
 y_i^\alpha=\frac{\partial(y^\alpha\circ s)}{\partial x^i}(x).
\]
The derivative coordinates range freely over real matrices; changes of jet coordinates are the smooth transformations obtained by the chain rule. These charts define the smooth bundle structures \(J^1E\to E\) and \(J^1E\to M\), not merely smooth projections of an unspecified structure.

## Affine structure and connections

For fixed \(e\in E_x\), the fiber of \(J^1E\to E\) identifies with linear maps \(L:T_xM\to T_eE\) satisfying \(d\pi_e\circ L=\operatorname{id}\). Such maps are precisely the differentials of local sections with value \(e\). Their differences lie in \(\operatorname{Hom}(T_xM,V_eE)\), so this is an affine space modeled on that vector space. Here \(V_eE=\ker d\pi_e\) is the vertical tangent space.

For a principal bundle \(P\to M\), the quotient \(J^1P/G\) is the [[fiber-bundles/bundle-of-connections|bundle of connections]].

## Examples
1. **Jets of functions.** For the trivial [[fiber-bundles/line-bundle|real line bundle]] \(E=M\times \mathbb{R}\), a section is a function \(f\colon M\to \mathbb{R}\), and \(j_x^1 f\) is determined by \((x,f(x),df_x)\). Thus \(J^1(M\times \mathbb{R})\) identifies with \(\mathbb{R}\times T^*M\) over \(M\).
2. **Trivial bundle with fiber F.** For \(E=M\times F\), a section is a map \(f\colon M\to F\), and \(j_x^1 f\) records \((x, f(x), df_x)\).
3. **Local coordinate description.** In coordinates \((x^i)\) on \(M\) and [[fiber-bundles/fiber-coordinates|fiber coordinates]] \((y^\alpha)\) on \(E\), a jet is described by \((x^i, y^\alpha, y^\alpha_i)\), where \(y^\alpha_i\) represent the first [[real-analysis/partial-derivative|partial derivatives]] of the section components.
