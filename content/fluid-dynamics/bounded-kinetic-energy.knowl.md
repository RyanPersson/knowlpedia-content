+++
id = "fluid-dynamics/bounded-kinetic-energy"
title = "Uniformly bounded kinetic energy"
kind = "definition"
summary = "A uniform-in-time bound on the spatial square-integral of velocity."
aliases = ["bounded energy", "uniform energy bound"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/kinetic-energy", "measure-theory/essential-supremum", "measure-theory/lp-space", "measure-theory/mixed-lebesgue-norm"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

A velocity \(u(t,x)\) has **uniformly bounded kinetic energy** on a time interval \(I\) if
\[
\operatorname*{ess\,sup}_{t\in I}\frac12\int_\Omega|u(t,x)|^2\,dx<\infty.
\]
The integral is [[fluid-dynamics/kinetic-energy|kinetic energy]] at unit density. This is the condition \(u\in L^\infty_t(I;L^2_x(\Omega))\).

## Time and space distinctions

The essential supremum ignores a null set of times. For an \(L^2\)-continuous representative, it agrees with the ordinary supremum on a compact interval. Finite energy separately at each time is weaker than a uniform bound. Neither condition controls the maximum velocity or its spatial derivatives without additional estimates.
