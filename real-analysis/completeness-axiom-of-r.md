---
title: "Completeness axiom of R"
description: "Every nonempty set of real numbers bounded above has a least upper bound."
---

The **completeness axiom** (or **least upper bound property**) states: every nonempty subset \(S \subseteq \mathbb{R}\) that is bounded above has a {{< knowl id="supremum" text="supremum" >}} in \(\mathbb{R}\).

This axiom distinguishes \(\mathbb{R}\) from \(\mathbb{Q}\): the rationals satisfy all field axioms and order axioms, but not completeness (e.g., \(\{q \in \mathbb{Q} : q^2 < 2\}\) has no rational supremum).

## Equivalent formulations
The following are equivalent to completeness:

1. **Greatest lower bound property**: Every nonempty set bounded below has an {{< knowl id="infimum" text="infimum" >}}.
2. **Nested intervals**: If \([a_n, b_n]\) is a nested sequence of closed intervals with \(b_n - a_n \to 0\), then \(\bigcap_n [a_n, b_n]\) contains exactly one point.
3. **Cauchy completeness**: Every {{< knowl id="cauchy-sequence" section="topology" text="Cauchy sequence" >}} converges.
4. **Bolzano-Weierstrass**: Every {{< knowl id="bounded-sequence" text="bounded sequence" >}} has a convergent {{< knowl id="subsequence" text="subsequence" >}}.

## Consequences
- Existence of \(\sqrt{2}\) and all real numbers.
- {{< knowl id="intermediate-value-theorem" text="Intermediate value theorem" >}}.
- {{< knowl id="extreme-value-theorem" section="topology" text="Extreme value theorem" >}}.
