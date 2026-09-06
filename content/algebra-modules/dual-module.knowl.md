+++
id = "algebra-modules/dual-module"
title = "Dual module"
kind = "knowl"
summary = "The Hom module Hom_R(M,R) for a module over a commutative ring."
aliases = ["dual-module", "Dual module"]
domains = ["algebra-modules"]
prerequisites = ["algebra-modules/tensor-hom-adjunction", "algebra-modules/free-module", "algebra-modules/basis-module"]
dependency_review_count = 1
legacy_source_path = "algebra-modules/dual-module.md"
+++

Let \(R\) be a commutative ring and \(M\) an \(R\)-module. The **dual module** of \(M\) is
\[
M^\vee := \mathrm{Hom}_R(M,R),
\]
with scalar multiplication \((r\varphi)(m)=r\varphi(m)\).

Duality is contravariant and interacts tightly with tensors via the [[algebra-modules/tensor-hom-adjunction|tensor–Hom adjunction]]; it packages bilinear pairings \(M\times N\to R\) as linear maps \(M\to N^\vee\). For [[algebra-modules/free-module|free modules]] of finite rank, duality is well-behaved and compatible with the notion of a [[algebra-modules/basis-module|basis]], producing a dual basis.

## Examples

- If \(M\cong R^n\) is free with basis \(e_1,\dots,e_n\), then \(M^\vee\cong R^n\) with dual basis \(e_1^\vee,\dots,e_n^\vee\) characterized by \(e_i^\vee(e_j)=\delta_{ij}\).
- If \(V\) is a finite-dimensional vector space over a [[algebra-rings/field|field]], then \(V^\vee\) is the usual linear dual space.
