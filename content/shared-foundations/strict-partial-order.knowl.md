+++
id = "shared-foundations/strict-partial-order"
title = "Strict partial order"
kind = "definition"
summary = "An irreflexive and transitive binary relation."
aliases = []
domains = ["shared-foundations"]
section_mode = "progressive"
prerequisites = ["shared-foundations/relation", "shared-foundations/set"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **strict partial order** on a set \(P\) is a [[shared-foundations/relation|relation]] \(<\) that is irreflexive, meaning \(a\not<a\) for every \(a\), and transitive, meaning \(a<b\) and \(b<c\) imply \(a<c\). These properties imply asymmetry: \(a<b\) excludes \(b<a\).

## Nonstrict form

Setting \(a\le b\) when \(a=b\) or \(a<b\) gives a [[shared-foundations/partial-order|partial order]]. Conversely, deleting the diagonal from a partial order gives a strict partial order. Comparability of every distinct pair is not required. A strict partial order on an infinite set may have infinite descending chains.
