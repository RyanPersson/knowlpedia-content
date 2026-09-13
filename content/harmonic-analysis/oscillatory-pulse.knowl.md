+++
id = "harmonic-analysis/oscillatory-pulse"
title = "Oscillatory pulse"
kind = "definition"
summary = "A wave with an amplitude localized in a finite time or path-coordinate interval."
aliases = ["localized oscillatory wave packet"]
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/wave-amplitude", "harmonic-analysis/pulse-envelope", "real-analysis/cutoff-function"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

An **oscillatory pulse** is a field of the form
\[
w(v,x)=\chi(v)a(v,x)e^{i\kappa\Phi(v,x)},
\]
where a [[real-analysis/cutoff-function|cutoff]] or decay of the amplitude localizes it in the pulse coordinate \(v\). The phase produces rapid oscillations; a [[harmonic-analysis/pulse-envelope|pulse envelope]] describes the amplitude's growth and decay. Additional spatial cutoffs can localize the pulse in space.

## Effect of localization

Multiplying a solution amplitude by \(\chi\) creates a term \(\chi'a\) in a first-order evolution equation. It is small only if one has bounds for the amplitude where \(\chi'\ne0\). Exponential smallness near pulse endpoints can control this error; localization alone does not preserve an exact equation.
