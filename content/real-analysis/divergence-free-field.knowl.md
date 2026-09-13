+++
id = "real-analysis/divergence-free-field"
title = "Divergence-free field"
kind = "definition"
summary = "A vector field whose divergence vanishes."
aliases = ["solenoidal field", "divergence-free vector field"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/divergence"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **divergence-free** or **solenoidal field** is a differentiable [[real-analysis/euclidean-vector-field|vector field]] \(u\) satisfying \(\operatorname{div}u=0\). A nonsmooth field may satisfy the same condition in the [[functional-analysis/distribution|distributional sense]], which must be specified when pointwise derivatives are unavailable.

## Constructions and cutoffs

Every curl of a \(C^2\) [[real-analysis/vector-potential|vector potential]] is divergence-free. A scalar cutoff does not generally preserve the condition: \(\operatorname{div}(\chi u)=\nabla\chi\cdot u\) for divergence-free \(u\). Cutting off a potential and then taking its curl preserves zero divergence.

## Fluid constraint

The kinematic condition for [[fluid-dynamics/incompressible-flow|incompressible flow]] is spatial divergence freedom at every time. The [[fluid-dynamics/navier-stokes-equations|Navier–Stokes equations]] couple this constraint to a momentum equation.
