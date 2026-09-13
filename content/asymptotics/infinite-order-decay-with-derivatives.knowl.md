+++
id = "asymptotics/infinite-order-decay-with-derivatives"
title = "Infinite-order decay with derivatives"
kind = "definition"
summary = "Every fixed derivative is bounded by every positive power of a chosen vanishing scale."
aliases = ["flat residual with all derivatives", "flat remainder in a scale"]
domains = ["asymptotics"]
section_mode = "progressive"
prerequisites = ["asymptotics/big-o", "real-analysis/cartesian-jet", "real-analysis/multi-index-notation", "asymptotics/uniform-parameter-estimate", "real-analysis/class-ck-function", "real-analysis/real-power"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Let \(q:\Omega\to(0,1]\) be a positive scale and \(f\) smooth on \(\Omega\). Write \(|f|_m(x)=\max_{|\alpha|\le m}|\partial^\alpha f(x)|\), the size of its [[real-analysis/cartesian-jet|Cartesian jet]]. The function has **infinite-order decay with derivatives as \(q\to0\)** if
\[
\forall m,N\ge0\quad\exists C_{m,N},\delta_{m,N}>0:
\quad |f|_m(x)\le C_{m,N}q(x)^N\quad\text{when }q(x)<\delta_{m,N}.
\]
This is also called a flat remainder in the stated derivative topology.

## Uniformity and extension

Constants are uniform over the specified points or labels, but may depend on \(m,N\). One positive decay order is insufficient. A bound for \(f\) alone does not imply derivative bounds. When \(q\) tends to zero at an ordinary smooth boundary and these estimates imply locally uniform vanishing of every mixed derivative there, the smooth zero-extension criterion applies. The definition itself concerns decay on \(\Omega\) and does not assume that its missing boundary has already been parametrized.
