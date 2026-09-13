+++
id = "real-analysis/cumulative-weighted-integral"
title = "Cumulative weighted integral"
kind = "definition"
summary = "The integral of a weighted source up to a variable upper endpoint."
aliases = ["cumulative radial integral"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/weighted-radial-moment", "real-analysis/fundamental-theorem-of-calculus-i"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a locally integrable weighted source \(r^ef(r)\), its **cumulative weighted integral** from a fixed \(a>0\) is
\[
I_e f(R)=\int_a^R r^e f(r)\,dr.
\]
When integration from zero converges, \(a=0\) is also allowed. The upper endpoint \(R\) remains a variable, unlike a total [[real-analysis/weighted-radial-moment|radial moment]].

## Derivatives and constants

If the source is continuous, \(\partial_R I_ef(R)=R^ef(R)\). An arbitrary primitive differs by a constant, which can depend on any additional parameters. Matching sources on an exterior interval therefore does not by itself match their primitives there; the accumulated integral or an integration constant must also agree.
