+++
id = "measure-theory/atom-of-measure"
title = "Atom of a measure"
kind = "definition"
summary = "A positive-measure measurable set with no measurable part of intermediate measure."
aliases = []
domains = ["measure-theory"]
section_mode = "progressive"
prerequisites = ["measure-theory/measure-space"]
+++

For a [[measure-theory/measure-space|measure space]] \((X,\Sigma,\mu)\), an **atom** is a measurable set \(A\) of positive measure such that every measurable \(B\subseteq A\) satisfies \(\mu(B)=0\) or \(\mu(B)=\mu(A)\).

## Examples

A point of positive probability is an atom. On a finite uniform space, every singleton is an atom. Lebesgue measure on an interval has no atoms: each positive-measure set can be divided into two measurable parts of positive measure.
