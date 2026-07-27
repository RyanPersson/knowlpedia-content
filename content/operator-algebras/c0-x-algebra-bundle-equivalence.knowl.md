+++
id = "operator-algebras/c0-x-algebra-bundle-equivalence"
title = "C_0(X)-algebras and upper-semicontinuous C*-bundles"
kind = "theorem"
summary = "C_0(X)-algebras are precisely section algebras of upper-semicontinuous C*-bundles over X."
aliases = ["C_0(X)-algebra bundle correspondence", "sectional representation theorem"]
domains = ["operator-algebras", "topology"]
section_mode = "progressive"
+++

Let \(X\) be a [[topology/locally-compact-space|locally compact Hausdorff space]]. Every [[operator-algebras/c0-x-algebra|\(C_0(X)\)-algebra]] \(A\) is \(C_0(X)\)-linearly [[operator-algebras/star-isomorphism|\(*\)-isomorphic]] to the [[operator-algebras/section-algebra-cstar-bundle|section algebra]]
\[
\Gamma_0(X,\mathcal A)
\]
of an [[operator-algebras/upper-semicontinuous-cstar-bundle|upper-semicontinuous \(C^*\)-bundle]] \(p\colon\mathcal A\to X\). Its fiber at \(x\) is canonically the [[operator-algebras/fiber-c0-x-algebra|quotient \(A_x\)]]. Conversely, the section algebra of every such bundle is a \(C_0(X)\)-algebra, and reconstructing its bundle recovers \(\mathcal A\) up to bundle isomorphism.

## Construction from an algebra

For each \(x\in X\), form \(A_x=A/I_x\) and the disjoint union
\[
\mathcal A=\bigsqcup_{x\in X}A_x.
\]
There is a unique upper-semicontinuous bundle topology compatible with the quotient norms and making every canonical section
\[
\widehat a(x)=a+I_x
\]
continuous. The map \(a\mapsto\widehat a\) is then an isometric \(C_0(X)\)-linear \(*\)-isomorphism from \(A\) onto \(\Gamma_0(X,\mathcal A)\).

## Construction from a bundle

Starting with \(p\colon\mathcal A\to X\), scalar multiplication of sections by functions in \(C_0(X)\) defines the central nondegenerate structure map
\[
C_0(X)\longrightarrow ZM(\Gamma_0(X,\mathcal A)).
\]
The quotient of the section algebra at \(x\) evaluates onto \(\mathcal A_x\). These evaluation maps assemble to the original bundle, including its topology.

## Scope

The theorem uses upper-semicontinuous bundles, not only continuous or locally trivial ones. Restricting to continuous bundles would omit \(C_0(X)\)-algebras for which some norm function \(x\mapsto\lVert a(x)\rVert\) is discontinuous. The correspondence is relative to the chosen \(C_0(X)\)-action; forgetting that action loses the base-space information.

## References

1. May Nilsen, “C*-Bundles and \(C_0(X)\)-Algebras,” *Indiana University Mathematics Journal* 45 (1996), 463–477. [DOI record](https://doi.org/10.1512/iumj.1996.45.1086). Relevant: the sectional representation theorem.
2. Dana P. Williams, *Crossed Products of C*-Algebras*, Mathematical Surveys and Monographs 134, American Mathematical Society, 2007. [DOI record](https://doi.org/10.1090/surv/134). Relevant: Appendix C, especially the bundle realization of \(C_0(X)\)-algebras.
