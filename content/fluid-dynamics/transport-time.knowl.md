+++
id = "fluid-dynamics/transport-time"
title = "Advective transport time scale"
kind = "definition"
summary = "The characteristic time L/U to move across length L at speed U."
aliases = ["advection time", "transport time"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["shared-foundations/real-numbers"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Given characteristic length \(L>0\) and speed \(U>0\), the **transport time scale** is
\[
t_{\mathrm{adv}}=\frac{L}{U}.
\]
It estimates the time needed for advection to traverse the chosen length. A nonuniform or time-dependent trajectory need not take exactly this time.

## Comparison with diffusion

At the same length and speed scales,
\[
\frac{t_{\mathrm{diff}}}{t_{\mathrm{adv}}}
=\frac{UL}{\nu}=\mathrm{Re}.
\]
Thus the [[fluid-dynamics/reynolds-number|Reynolds number]] also compares the characteristic diffusion time to the transport time. A flow with several geometric directions may have different transport times in each direction.
