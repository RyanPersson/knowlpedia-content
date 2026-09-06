+++
id = "operator-algebras/upper-semicontinuous-cstar-bundle"
title = "Upper-semicontinuous C*-bundle"
kind = "definition"
summary = "A topological bundle of C*-algebras whose fiber norm is upper semicontinuous."
aliases = ["upper semicontinuous C*-algebra bundle", "USC C*-bundle"]
domains = ["operator-algebras", "topology"]
section_mode = "progressive"
prerequisites = ["topology/topological-space", "operator-algebras/cstar-algebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

An **upper-semicontinuous \(C^*\)-bundle** over a [[topology/topological-space|topological space]] \(X\) is an open continuous surjection \(p\colon\mathcal A\to X\) whose fiber \(\mathcal A_x=p^{-1}(x)\) is a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]]. Fiberwise addition, scalar multiplication, multiplication, and involution are continuous, while \(a\mapsto\lVert a\rVert\) is upper semicontinuous. The zero elements satisfy the convergence axiom: if \(p(a_i)\to x\) and \(\lVert a_i\rVert\to0\), then \(a_i\to0_x\).
These axioms relate the fiber topologies without requiring local product charts or a fixed model fiber.

## Upper semicontinuity

Upper semicontinuity of the norm means that
\[
\{a\in\mathcal A:\lVert a\rVert<r\}
\]
is open for every \(r>0\). Equivalently, for a convergent net \(a_i\to a\),
\[
\limsup_i\lVert a_i\rVert\leq\lVert a\rVert.
\]
The norm need not be continuous. Requiring continuity defines the stricter notion of a continuous \(C^*\)-bundle.

## Continuous sections

A section is a map \(s\colon X\to\mathcal A\) with \(p\circ s=\operatorname{id}_X\). Continuity is measured in the topology of the total space, not by first identifying all fibers with a fixed algebra. For every continuous section, the function \(x\mapsto\lVert s(x)\rVert\) is upper semicontinuous.

When \(X\) is [[topology/locally-compact-space|locally compact]] Hausdorff, sections vanishing at infinity form the [[operator-algebras/section-algebra-cstar-bundle|section \(C^*\)-algebra]] \(\Gamma_0(X,\mathcal A)\).

## Why local triviality is not assumed

The fibers may vary in isomorphism type and dimension, so an upper-semicontinuous \(C^*\)-bundle need not be locally trivial. This flexibility is essential: every [[operator-algebras/c0-x-algebra|\(C_0(X)\)-algebra]] has such a bundle model, whereas continuous or locally trivial bundles describe only special cases.

## References

1. May Nilsen, “C*-Bundles and \(C_0(X)\)-Algebras,” *Indiana University Mathematics Journal* 45 (1996), 463–477. [DOI record](https://doi.org/10.1512/iumj.1996.45.1086). Relevant: the bundle construction and sectional representation theorem.
2. Dana P. Williams, *Crossed Products of C*-Algebras*, Mathematical Surveys and Monographs 134, American Mathematical Society, 2007. [DOI record](https://doi.org/10.1090/surv/134). Relevant: Appendix C on upper-semicontinuous bundles.
