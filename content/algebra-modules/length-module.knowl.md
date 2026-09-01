+++
id = "algebra-modules/length-module"
title = "Length of a module"
kind = "knowl"
summary = "The number of simple factors in a composition series (when finite)."
aliases = ["length-module", "Length of a module"]
domains = ["algebra-modules"]
prerequisites = ["algebra-modules/module", "algebra-modules/composition-series-module", "algebra-modules/noetherian-module", "algebra-modules/artinian-module", "algebra-modules/artinian-noetherian-finite-length"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "algebra-modules/length-module.md"
+++

If an \(R\)-[[algebra-modules/module|module]] \(M\) admits a [[algebra-modules/composition-series-module|composition series]]
\[
0=M_0 \subset M_1 \subset \cdots \subset M_n=M,
\]
then the **length** of \(M\), denoted \(\ell_R(M)\), is \(n\). The Jordan–Hölder theorem implies that this number is independent of the chosen composition series. A module admitting such a series is a **finite-length module**.

Finite length is tightly linked to chain conditions: modules that are both [[algebra-modules/noetherian-module|Noetherian]] and [[algebra-modules/artinian-module|Artinian]] have finite length; see [[algebra-modules/artinian-noetherian-finite-length|Artinian + Noetherian ⇒ finite length]].

## Examples

- As a \(\mathbb Z\)-module, \(\ell_{\mathbb Z}(\mathbb Z/p^k\mathbb Z)=k\).
- If \(V\) is an \(n\)-dimensional vector space over a field \(K\), then \(\ell_K(V)=n\).
- The \(\mathbb Z\)-module \(\mathbb Z\) has no finite composition series.
