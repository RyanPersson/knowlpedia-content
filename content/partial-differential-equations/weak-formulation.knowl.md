+++
id = "partial-differential-equations/weak-formulation"
title = "Weak formulation of a differential equation"
kind = "definition"
summary = "An equation expressed by integral or distributional identities against specified test functions."
aliases = ["weak solution of a PDE", "distributional solution"]
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["functional-analysis/distributional-derivative", "functional-analysis/test-function-space", "partial-differential-equations/partial-differential-equation"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **weak formulation** of a [[partial-differential-equations/partial-differential-equation|differential equation]] specifies admissible unknowns, [[functional-analysis/test-function-space|test functions]], and identities obtained by transferring derivatives to tests through [[functional-analysis/distributional-derivative|distributional differentiation]]. A **weak solution** is an admissible unknown satisfying every prescribed identity.

## Example and scope

For \(-\Delta u=f\) on an open set, the distributional formulation for locally integrable \(u,f\) is \(\int u(-\Delta\phi)=\int f\phi\) for every compactly supported smooth \(\phi\). A variational formulation may instead require a Sobolev space and use \(\int\nabla u\cdot\nabla\phi=\int f\phi\). Initial and boundary conditions need their own trace or test conventions. Nonlinear products must exist in the stated function spaces; an integral identity alone does not supply their integrability.
