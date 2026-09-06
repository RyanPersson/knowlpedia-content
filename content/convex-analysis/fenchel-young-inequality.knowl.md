+++
id = "convex-analysis/fenchel-young-inequality"
title = "Fenchel-Young inequality"
kind = "knowl"
summary = "An inequality relating a function and its Fenchel conjugate via the dual pairing."
aliases = ["fenchel-young-inequality", "Fenchel-Young inequality"]
domains = ["convex-analysis"]
prerequisites = ["shared-foundations/function", "convex-analysis/convex-conjugate-fenchel", "convex-analysis/subdifferential"]
dependency_review_count = 1
legacy_source_path = "convex-analysis/fenchel-young-inequality.md"
+++

**Fenchel–Young inequality.** Let \(f:\mathbb R^n\to(-\infty,+\infty]\) be a proper [[shared-foundations/function|function]], and let \(f^*\) be its [[convex-analysis/convex-conjugate-fenchel|Fenchel conjugate]]. Then, for all \(x,y\in\mathbb R^n\),
\[
f(x)+f^*(y)\ge \langle x,\,y\rangle.
\]

If \(f\) is convex, equality holds if and only if \(y\in\partial f(x)\), where \(\partial f\) is the [[convex-analysis/subdifferential|subdifferential]]. If \(f\) is also lower semicontinuous, this is equivalent to \(x\in\partial f^*(y)\).

## Remarks

The inequality follows immediately from the definition, since \(f^*(y)\ge\langle y,x\rangle-f(x)\). It is the basic mechanism behind weak duality in [[convex-analysis/convex-duality-primal-dual|convex primal-dual pairs]].
