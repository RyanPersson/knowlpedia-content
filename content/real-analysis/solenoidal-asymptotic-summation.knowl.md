+++
id = "real-analysis/solenoidal-asymptotic-summation"
title = "Asymptotic summation preserving divergence freedom"
kind = "theorem"
summary = "Summing localized potentials before taking curl retains incompressibility and the asymptotic tail estimates."
aliases = []
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["asymptotics/shrinking-cutoff-asymptotic-summation", "real-analysis/solenoidal-localization", "real-analysis/divergence-free-field", "real-analysis/vector-potential", "real-analysis/product-rule"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

On a space-time domain in \(\mathbb R^3\times\mathbb R\), let \(q>0\) satisfy the hypotheses of [[asymptotics/shrinking-cutoff-asymptotic-summation|shrinking-cutoff summation]]. Suppose smooth representatives \(A_j,B_j\) satisfy its increasing-order derivative estimates and
\[
\nabla_x\cdot B_j=0,\qquad B_j\cdot\nabla_xq=0.
\]
For a smooth divergence-free base \(u_0\), cutoff scales can be chosen so that
\[
u=u_0+\sum_{j\ge1}\left(\nabla_x\times(\chi(a_jq)A_j)+\chi(a_jq)B_j\right)
\]
is smooth, locally finite, and divergence-free. Its difference from the uncut finite states has the same kind of increasing-order tail estimate, with a derivative loss independent of the stage.

## Constraint and estimates

Each curl has zero divergence. The direct term has divergence \(\chi\nabla\cdot B_j+a_j\chi'(a_jq)\nabla q\cdot B_j=0\). The curl product rule adds \(a_j\chi'(a_jq)\nabla q\times A_j\); estimates for the potential through one extra derivative control this term. At stage \(j\), impose the finite list of output derivative bounds through order \(j\) before choosing \(a_j\). The diagonal and tail arguments then proceed as for scalar summation.

## Geometry and boundaries

An axisymmetric azimuthal field \(B_j=b_j(r,z,t)e_\theta\) satisfies these two constraints when \(q\) is independent of the angle and the field has a smooth Cartesian representative. Smooth zero extensions across lateral support boundaries are hypotheses on the representatives. Multiplying velocities by cutoffs after taking curl would generally introduce a divergence defect.
