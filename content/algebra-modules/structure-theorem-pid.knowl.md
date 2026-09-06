+++
id = "algebra-modules/structure-theorem-pid"
title = "Structure theorem for finitely generated modules over a PID"
kind = "knowl"
summary = "A finitely generated module over a PID splits as a free part plus cyclic torsion factors."
aliases = ["structure-theorem-pid", "Structure theorem for finitely generated modules over a PID"]
domains = ["algebra-modules"]
prerequisites = ["algebra-rings/pid", "algebra-modules/finitely-generated-module", "algebra-modules/direct-sum-modules"]
dependency_review_count = 1
legacy_source_path = "algebra-modules/structure-theorem-pid.md"
+++

Let \(R\) be a [[algebra-rings/pid|principal ideal domain]] and let \(M\) be a [[algebra-modules/finitely-generated-module|finitely generated \(R\)-module]]. Then there exist an integer \(r\ge 0\) and nonzero nonunits \(d_1,\dots,d_t\in R\), with \(d_1\mid d_2\mid\cdots\mid d_t\), such that
\[
M \;\cong\; R^{\,r}\;\oplus\;\bigoplus_{i=1}^t R/(d_i),
\]
a decomposition as a [[algebra-modules/direct-sum-modules|direct sum]] of a free part and cyclic torsion factors. The integer \(r\), the number \(t\), and the invariant factors \(d_i\) are unique, with each \(d_i\) determined up to multiplication by a unit.

## Consequences

The theorem gives the [[algebra-modules/classification-fg-abelian-groups|classification of finitely generated abelian groups]] when \(R=\mathbb Z\). It is equivalent to [[algebra-modules/smith-normal-form-theorem|Smith normal form]] and also has an [[algebra-modules/elementary-divisor-theorem|elementary-divisor form]].
