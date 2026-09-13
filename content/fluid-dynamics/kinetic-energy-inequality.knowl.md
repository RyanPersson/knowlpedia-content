+++
id = "fluid-dynamics/kinetic-energy-inequality"
title = "Kinetic-energy inequality"
kind = "definition"
summary = "An integrated upper bound allowing energy loss beyond the explicitly recorded viscous dissipation."
aliases = ["global energy inequality"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/kinetic-energy", "fluid-dynamics/viscous-dissipation", "measure-theory/lebesgue-integral", "measure-theory/lp-space"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A velocity-force pair satisfies the **kinetic-energy inequality from time \(s\)** if, for the stated later times \(t\),
\[
\frac12\|u(t)\|_2^2+\nu\int_s^t\|\nabla u(r)\|_2^2\,dr
\le\frac12\|u(s)\|_2^2+\int_s^t\int f\cdot u\,dx\,dr.
\]
The [[fluid-dynamics/viscous-dissipation|dissipation]] and forcing integrals must be defined. The domain, time representative, and admissible starting and ending times form part of the condition.

## Inequality versus equality

A smooth solution with justified energy integration satisfies equality, hence also this inequality. In a weak-solution definition the inequality is an additional admissibility condition. A limit can lose equality because norm convergence is weaker than strong convergence. Requiring the inequality from the initial time only is different from requiring it from almost every intermediate time as well.
