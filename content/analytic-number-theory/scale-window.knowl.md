+++
id = "analytic-number-theory/scale-window"
title = "Window of scales"
kind = "definition"
summary = "An interval of cutoffs on which a bound must hold with common parameters."
aliases = ["windows", "power window"]
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["real-analysis/interval"]
+++

A **window of scales** is an [[real-analysis/interval|interval]] of values of a size parameter \(x\) on which an estimate is required to hold uniformly. A common choice is a **power window** \(Y\le x\le Y^\lambda\), with \(Y>1\) and a fixed \(\lambda>1\). A bound on arbitrarily late power windows means that for every starting threshold \(Y_0\) there exists a \(Y\ge Y_0\) for which the bound holds throughout that window.

## A power window

With \(Y=100\) and \(\lambda=3/2\), the window runs from \(100\) through \(1000\). A bound \(F(x)\le x^{2/3}\) on this window must hold at \(x=500\) as well as at both endpoints. It places no condition on \(F(1001)\).
