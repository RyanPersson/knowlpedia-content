+++
id = "algebra-modules/direct-sum-modules"
title = "Direct sum of modules"
kind = "knowl"
summary = "The coproduct of modules: tuples with finite support under coordinatewise operations."
aliases = ["direct-sum-modules", "Direct sum of modules"]
domains = ["algebra-modules"]
prerequisites = ["algebra-modules/module", "algebra-modules/direct-product-modules", "shared-foundations/cartesian-product", "algebra-modules/direct-sum-universal-property"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "algebra-modules/direct-sum-modules.md"
+++

Given a family of \(R\)-[[algebra-modules/module|modules]] \((M_i)_{i\in I}\), their **direct sum** is the module
\[
\bigoplus_{i\in I} M_i=\{(m_i)\in \prod_{i\in I} M_i : m_i=0 \text{ for all but finitely many } i\},
\]
with coordinatewise addition and scalar multiplication. It is naturally a submodule of the [[algebra-modules/direct-product-modules|direct product]], which itself is modeled on the [[shared-foundations/cartesian-product|Cartesian product]] of sets.

The direct sum is characterized by the [[algebra-modules/direct-sum-universal-property|universal property of the direct sum]]: for every \(R\)-module \(N\), an arbitrary family of homomorphisms \(f_i:M_i\to N\) determines a unique homomorphism \(\bigoplus_iM_i\to N\).

## Examples

- For a finite index set, \(\bigoplus_{i=1}^n M_i=\prod_{i=1}^n M_i\).
- \(\bigoplus_{n\ge 1}\mathbb Z\) consists of integer sequences with finite support.
- If \(I=\varnothing\), then \(\bigoplus_{i\in I}M_i\) is the zero module.
