+++
id = "operator-algebras/cstar-dynamical-system"
title = "C*-dynamical system"
kind = "definition"
summary = "A C*-algebra equipped with a point-norm continuous action of a locally compact group by automorphisms."
aliases = ["C*-algebraic dynamical system", "group action on a C*-algebra"]
domains = ["operator-algebras", "dynamical-systems"]
section_mode = "progressive"
+++

A **\(C^*\)-dynamical system** is a triple \((A,G,\alpha)\) consisting of a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]] \(A\), a [[topology/locally-compact-group|locally compact group]] \(G\), and a [[algebra-groups/group-homomorphism|group homomorphism]]
\[
\alpha:G\longrightarrow\operatorname{Aut}(A),\qquad s\longmapsto\alpha_s,
\]
such that the action is **strongly continuous** in the \(C^*\)-algebraic sense: for every \(a\in A\), the orbit map \(s\mapsto\alpha_s(a)\) is continuous in the norm of \(A\). Equivalently, \(\alpha\) is continuous when \(\operatorname{Aut}(A)\) has the point-norm topology. Neither \(A\) nor \(G\) is required to be unital or discrete.

## Why the continuity axiom matters

Point-norm continuity ensures that \(s\mapsto f(s)\alpha_s(a)\) has the continuity needed in the convolution and integration constructions underlying crossed products. It is stronger than requiring continuity after applying only selected representations or functionals. When \(G\) is discrete the condition is automatic, so an action by \(*\)-automorphisms is already a \(C^*\)-dynamical system.

## Standard examples

The trivial action \(\alpha_s=\operatorname{id}_A\) gives a \(C^*\)-dynamical system for every \(A\) and \(G\). If \(G\) acts continuously on a locally compact [[topology/hausdorff-space|Hausdorff space]] \(X\), then
\[
(\alpha_s f)(x)=f(s^{-1}x)
\]
defines a point-norm continuous action on \(C_0(X)\). For a non-example, a homomorphism \(G\to\operatorname{Aut}(A)\) whose orbit map is discontinuous for some \(a\) is an algebraic [[algebra-groups/group-action|group action]] but not a \(C^*\)-dynamical system in this sense.

## Conventions and scope

Many sources define a \(C^*\)-dynamical system for an arbitrary [[topology/topological-group|topological group]]. Crossed-product theory typically assumes that \(G\) is locally compact Hausdorff so that [[harmonic-analysis/haar-measure|Haar integration]] is available; that convention is built into this knowl. “Strong continuity” here means point-norm continuity of automorphisms, not continuity in the [[operator-algebras/strong-operator-topology|strong operator topology]] of a particular Hilbert-space representation [Williams, §2.1, Definition 2.6](https://doi.org/10.1090/surv/134).

## References

1. Dana P. Williams, Crossed Products of \(C^*\)-Algebras, Mathematical Surveys and Monographs 134, American Mathematical Society, 2007. [DOI record](https://doi.org/10.1090/surv/134). Relevant: §2.1, especially Definition 2.6 on \(C^*\)-dynamical systems.
2. Gert K. Pedersen, \(C^*\)-Algebras and Their Automorphism Groups, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: Chapter 7 on automorphism groups and covariant representations.
