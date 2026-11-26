+++
id = "complex-analysis/analytic-zero-order"
title = "Order of an analytic zero"
kind = "definition"
summary = "The least exponent with nonzero coefficient in a local Taylor series."
domains = ["complex-analysis"]
section_mode = "progressive"
prerequisites = ["complex-analysis/holomorphic-germ", "real-analysis/power-series"]
+++

Let \(f\) be a [[complex-analysis/holomorphic-germ|holomorphic germ]] at \(z\) which is not identically zero. Its **order at \(z\)** is the unique \(m\ge0\) for which \(f(w)=(w-z)^m u(w)\) with \(u\) holomorphic and \(u(z)\ne0\). It is the first nonzero coefficient’s index in the [[real-analysis/power-series|Taylor series]].

## Detecting multiplicity

The [[complex-analysis/logarithmic-derivative|logarithmic derivative]] is \(m/(w-z)+u'(w)/u(w)\). Its [[complex-analysis/residue|residue]] at \(z\) is therefore \(m\). A nonzero function value gives \(m=0\).
