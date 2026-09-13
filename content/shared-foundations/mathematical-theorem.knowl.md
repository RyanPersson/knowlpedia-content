+++
id = "shared-foundations/mathematical-theorem"
title = "Mathematical theorem"
kind = "definition"
summary = "A statement established from the axioms and hypotheses of a theory."
aliases = ["theorem", "lemma", "corollary"]
domains = ["shared-foundations"]
section_mode = "progressive"
prerequisites = ["shared-foundations/mathematical-proposition", "shared-foundations/mathematical-proof"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **theorem** is a [[shared-foundations/mathematical-proposition|statement]] established by a [[shared-foundations/mathematical-proof|proof]] from the axioms and stated hypotheses of a theory. Its usable content includes all assumptions and quantifiers, not just the conclusion.

## Lemmas and corollaries

The labels “lemma,” “proposition,” and “corollary” primarily describe a result's role in an exposition. A lemma is organized to support another argument; a corollary is presented as a consequence of preceding results. These labels do not change the standard of proof or permit dropping hypotheses.

## Using a result

To apply a theorem to particular data, first verify that the data satisfy its hypotheses. When a theorem asserts an object exists for each parameter, any additional claim that the choices vary continuously or smoothly requires justification in its own right.
