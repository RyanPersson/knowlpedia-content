+++
id = "measure-theory/standard-borel-space"
title = "Standard Borel space"
kind = "definition"
summary = "A measurable space isomorphic to the Borel space of a Polish space."
aliases = []
domains = ["measure-theory"]
section_mode = "progressive"
prerequisites = ["measure-theory/measurable-space", "measure-theory/borel-sigma-algebra", "topology/polish-space"]
+++

A **standard Borel space** is a [[measure-theory/measurable-space|measurable space]] \((X,\Sigma)\) for which there are a [[topology/polish-space|Polish space]] \(Y\) and a bijection \(b:X\to Y\) such that both \(b\) and \(b^{-1}\) are measurable, with \(Y\) carrying its [[measure-theory/borel-sigma-algebra|Borel sigma-algebra]].

## Examples

Finite and countable discrete spaces, Euclidean spaces, compact metric spaces, and their Borel subsets are standard Borel. The definition specifies measurable structure; it does not choose a preferred topology on \(X\).

## Completion

Completing a Borel probability measure adds subsets of null sets. The completed measurable space need not itself be standard Borel. The related notion of a [[measure-theory/standard-probability-space|standard probability space]] allows this completion and identification modulo null sets.
