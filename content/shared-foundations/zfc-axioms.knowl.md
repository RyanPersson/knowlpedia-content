+++
id = "shared-foundations/zfc-axioms"
title = "ZFC axioms"
kind = "knowl"
summary = "Standard axioms of set theory: Zermelo-Fraenkel axioms plus the Axiom of Choice."
aliases = ["zfc-axioms", "ZFC axioms"]
domains = ["shared-foundations"]
prerequisites = ["shared-foundations/axiom-of-choice", "shared-foundations/empty-set", "shared-foundations/union", "shared-foundations/power-set", "shared-foundations/natural-numbers", "shared-foundations/subset"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "shared-foundations/zfc-axioms.md"
+++

**ZFC axioms:** ZFC is the first-order theory in the language with equality and the membership relation \(\in\) whose axioms are the Zermelo–Fraenkel axioms together with the [[shared-foundations/axiom-of-choice|Axiom of Choice]]. A common presentation includes:
- **Extensionality:** sets with the same elements are equal.
- **Empty set:** an [[shared-foundations/empty-set|empty set]] exists.
- **Pairing:** for any \(a,b\) there exists a set \(\{a,b\}\).
- **Union:** for any set \(A\) there exists \(\bigcup A\) (a set containing exactly the elements of the members of \(A\)), aligning with [[shared-foundations/union|union]] constructions.
- **Power set:** for any set \(A\) there exists its [[shared-foundations/power-set|power set]] \(\mathcal P(A)\).
- **Infinity:** an inductive set exists, enabling the construction of the [[shared-foundations/natural-numbers|natural numbers]].
- **Separation schema:** definable [[shared-foundations/subset|subsets]] of a set are sets.
- **Replacement schema:** images of sets under definable functions are sets.
- **Foundation (regularity):** every nonempty set has an \(\in\)-minimal element.
- **Choice:** every set of nonempty sets has a choice function.

## Remarks

Within ZFC one can develop most standard mathematics, and ZFC proves statements equivalent in strength to choice such as [[shared-foundations/zorns-lemma|Zorn's lemma]] and the [[shared-foundations/well-ordering-theorem|well-ordering theorem]].
