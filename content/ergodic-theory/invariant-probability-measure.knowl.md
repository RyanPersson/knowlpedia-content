+++
id = "ergodic-theory/invariant-probability-measure"
title = "Invariant probability measure"
kind = "definition"
summary = "A probability measure unchanged by pushforward under a specified measurable map."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["measure-theory/pushforward-measure", "probability/probability-measure"]
+++

For a measurable self-map \(T:X\to X\), a [[probability/probability-measure|probability measure]] \(\mu\) is **invariant** if \(T_*\mu=\mu\), equivalently \(\mu(T^{-1}E)=\mu(E)\) for every measurable \(E\). Specifying an invariant measure turns a measurable map into a probability-preserving system.

## Topological systems

For a continuous map of a nonempty compact metric space, the [[ergodic-theory/krylov-bogolyubov-theorem|Krylov–Bogolyubov theorem]] guarantees existence. Uniqueness is the additional property of [[analysis/unique-ergodicity|unique ergodicity]].
