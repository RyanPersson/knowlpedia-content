+++
id = "algebra-modules/projective-implies-flat"
title = "Projective implies flat"
kind = "knowl"
summary = "Every projective module is flat, so tensoring with it preserves exact sequences."
aliases = ["projective-implies-flat", "Projective implies flat"]
domains = ["algebra-modules"]
prerequisites = ["algebra-modules/projective-module", "algebra-modules/flat-module"]
dependency_review_count = 1
legacy_source_path = "algebra-modules/projective-implies-flat.md"
+++

Let \(P\) be a [[algebra-modules/projective-module|projective]] right \(R\)-module. Then \(P\) is [[algebra-modules/flat-module|flat]]: for every short exact sequence of left \(R\)-modules
\[
0\to A\to B\to C\to 0,
\]
the induced sequence
\[
0\to P\otimes_R A\to P\otimes_R B\to P\otimes_R C\to 0
\]
is exact.

## Proof idea

Projective modules are direct summands of [[algebra-modules/free-module|free modules]]. The functor \(P\otimes_R-\) is therefore a direct summand of a direct sum of identity functors, so it preserves injections; as every tensor functor is right exact, it is exact.
