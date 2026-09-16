+++
id = "ergodic-theory/time-average"
title = "Time average of an observable"
kind = "definition"
summary = "The Cesaro average of an observable along the first N iterates of a transformation."
aliases = ["orbit average", "ergodic average", "Birkhoff average"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/observable"]
+++

For an [[ergodic-theory/observable|observable]] \(f\) and a probability-preserving transformation \(T\), its **time average** over \(N\geq1\) steps is
\[
A_Nf(x)=\frac1N\sum_{n=0}^{N-1}f(T^nx).
\]
Compare this orbit sample with the [[ergodic-theory/space-average|space average]] under \(\mu\).

## Visits to events

For \(f=1_E\), the time average is the fraction of the first \(N\) iterates lying in \(E\). The [[ergodic-theory/birkhoff-ergodic-theorem|pointwise ergodic theorem]] identifies its almost-everywhere limit. In a nonergodic system, that limit can depend on the starting point.
