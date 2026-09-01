+++
id = "algebra-modules/tensor-hom-adjunction-lemma"
title = "Tensor–Hom adjunction lemma"
kind = "knowl"
summary = "Natural isomorphism between Hom out of a tensor product and Hom into a Hom-module."
aliases = ["tensor-hom-adjunction-lemma", "Tensor–Hom adjunction lemma"]
domains = ["algebra-modules"]
prerequisites = ["algebra-rings/unital-ring", "algebra-modules/bimodule", "algebra-modules/module"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "algebra-modules/tensor-hom-adjunction-lemma.md"
+++

Let \(R,S\) be [[algebra-rings/unital-ring|unital rings]], let
\({}_S M_R\) be an \((S,R)\)-[[algebra-modules/bimodule|bimodule]], let
\({}_R N\) be a left \(R\)-[[algebra-modules/module|module]], and let
\({}_S P\) be a left \(S\)-module. Give \(\operatorname{Hom}_S(M,P)\) the
left \(R\)-module structure \((r\varphi)(m)=\varphi(mr)\). Then the
**Tensor–Hom adjunction** is the natural isomorphism of abelian groups
\[
\operatorname{Hom}_S(M\otimes_R N,\,P)\;\cong\;\operatorname{Hom}_R\!\bigl(N,\,\operatorname{Hom}_S(M,P)\bigr),
\]
functorial in \(N\) and \(P\).

## Remarks

This is the concrete form of the [[algebra-modules/tensor-hom-adjunction|Tensor–Hom adjunction]] for a [[algebra-modules/bimodule|bimodule]], relating [[algebra-modules/tensor-product|tensor products]] and [[algebra-modules/hom-module|Hom-modules]].
