+++
id = "differential-equations/ordinary-differential-equation"
title = "Ordinary differential equation"
kind = "definition"
summary = "An equation relating a function of one independent variable to its derivatives."
aliases = ["ODE", "ODE system"]
domains = ["differential-equations"]
section_mode = "progressive"
prerequisites = ["real-analysis/derivative", "shared-foundations/function", "real-analysis/interval"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

An **ordinary differential equation** (ODE) relates an unknown function \(y(t)\) of one independent variable to its [[real-analysis/derivative|derivatives]]. A first-order system in explicit form is
\[
y'(t)=F(t,y(t)),\qquad y(t)\in\mathbb R^m
\]
or \(\mathbb C^m\). A classical solution is a differentiable function on an interval that satisfies the equation at every point. Higher-order equations can often be written as first-order systems by including successive derivatives as additional state variables.

## Data and parameters

An [[differential-equations/initial-value-problem|initial value]] selects the state at one time. Additional parameters may enter \(F\) without being differentiated in \(t\). An equation is autonomous when \(F\) does not depend explicitly on \(t\). Ordinary refers to the single independent variable, even when the state has many components.
