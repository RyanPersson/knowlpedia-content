+++
id = "proofs/grh/upper-objects/grid-steps-correspond"
title = "The parameters at the two ends of every step of a grid correspond"
kind = "theorem"
summary = "Each step of the grids and of the triangles inserts one block, so the Harish-Chandra parameters of its two nodes satisfy the block rule at every infinite place, for explicit weights."
aliases = ["parameters of every step correspond"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.paramsCorrespond_grid_succ_left", "New.Data.paramsCorrespond_grid_succ_right", "New.Data.paramsCorrespond_grid", "New.Data.paramsCorrespond_neg_gridParam_insert_first", "New.Data.paramsCorrespond_leftPair", "New.Data.gridWeight_not"]
lean_files = ["src/New/UpperBound/Objects/Parameters.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/upper-objects/grid-nodes|grid nodes]]: for the grid \(z\), offset \(o\) and node \((i,j)\), let \(s^{o}_{i,j}\) be the signs, \(l^{o}_{i,j}\) the doubled parameter (a function of \(\tau\)), \(N_{i,j}\) the rank, and \(\operatorname{gw}_{c,l}\) the weights of a step. Two parameters [[?lean:New.ParamsCorrespond|correspond]] for weights \(\gamma,\gamma'\) if at every infinite place they satisfy the [[?lean:New.IsBlockRule|block rule]] for \(\gamma_\tau,\gamma'_\tau\).

**Theorem.**

1. *(Step to the right in the first coordinate.)* If \(i+1\le m\), \(j\le m\): \(-l^0_{i,j}\) and \(-l^0_{i+1,j}\) correspond for the weights \(\operatorname{gw}_{z,i}\) of the two nodes (signs \(s^0_{i,j}\), \(s^0_{i+1,j}\)).
2. *(Step in the second coordinate.)* If \(i\le m\), \(j+1+o\le m\), and \(o=0\) or \(i=0\): \(l^o_{i,j}\) and \(l^o_{i,j+1}\) correspond for the weights \(\operatorname{gw}_{1-z,\,j+o}\) of the two nodes.
3. *(First block of an interval.)* If \(i+j<m\): \(-l^{i+1}_{0,j}\) and \(-l^{i}_{0,j+1}\) correspond for the weights \(N-\operatorname{gw}_{1-z,i}\) of the two nodes (\(N\) the rank of the node); and also in the other order (the block rule is used in both directions).

## Proof

By the [[proofs/grh/upper-objects/grid-centres|centre system of the grid]], for \(o+j\le m\) and (\(o=0\) or \(i=0\)) the doubled parameter of the node \((i,j)\) with offset \(o\) is twice the parameter \(\lambda_{B_{o,i,j}}\) of \(\mathcal C_{\tau,z}\), with common sign \((-1)^o\); below "is \(\lambda_B\)" is said of the halved vector, and the insertion theorem is applied to the halved vectors. The system is separated with bound \(\Delta-t-2\), and \(\Delta-t-2\ge500(N+N')^3\) for the ranks \(N,N'\) of two nodes all four of whose coordinates are at most \(m\); in each of the three statements the hypotheses give these bounds for both end nodes (and then \(B\subseteq C\)).

*1.* \(B_{0,i+1,j}=B_{0,i,j}\cup\{u_i\}\) with \(u_i\) an up centre of value \(w_{i+1}\), both nodes with common sign \(+1\). The [[proofs/grh/upper-objects/inserting-a-block-satisfies-the-block-rule|insertion theorem]] (up case) gives the block rule for the negatives with \(\gamma=-w_{i+1}+\lceil N/2\rceil\). This equals \(\operatorname{gw}_{z,i}\): for \(z=0\) the weight is defined with the ceiling, and for \(z=1\) the rank is even, so floor and ceiling agree.

*2.* \(B_{o,i,j+1}=B_{o,i,j}\cup\{d_{j+o}\}\) with a down centre of value \(-w_{j+o+1}\), common sign \((-1)^o\) on both sides. The insertion theorem (down case) gives the block rule with \(\gamma=-w_{j+o+1}+\lfloor N/2\rfloor=\operatorname{gw}_{1-z,j+o}\) (for \(z=0\) the weight \(\operatorname{gw}_{1,\cdot}\) has the floor; for \(z=1\) the rank is even).

*3.* \(B_{i,0,j+1}=B_{i+1,0,j}\cup\{d_i\}\). The common signs \((-1)^{i+1}\) and \((-1)^i\) differ, so regard the smaller node on the opposite space: with signs \(-s^{i+1}_{0,j}\) its parameter is \(\lambda_{B_{i+1,0,j}}\) with common sign \((-1)^i\) (see the remarks on [[proofs/grh/upper-objects/centre-system|centre systems]]). The insertion theorem (down case, centre \(d_i\)) gives the block rule for \((l^{i+1}_{0,j},l^i_{0,j+1})\) with signs \((-s^{i+1}_{0,j},s^i_{0,j+1})\) and weights \(\operatorname{gw}_{1-z,i}\). Now apply the Lean theorem `New.IsBlockRule.neg` (cited; its content: if \((\gamma,\gamma',l,l')\) satisfy the block rule for signs \((s,t)\) on spaces of ranks \(n,n'\), then \((n-\gamma,n'-\gamma',-l,-l')\) satisfy it for signs \((-s,t)\)): this gives the statement, with the original signs of the smaller node and the weights \(N-\operatorname{gw}_{1-z,i}\). The other direction is the symmetry of the block rule (`New.ParamsCorrespond.symm`: exchange the two spaces). \(\square\)

## References

1. Lean: `New.Data.paramsCorrespond_grid_succ_left`, `New.Data.paramsCorrespond_grid_succ_right`, `New.Data.paramsCorrespond_leftPair` in `src/New/UpperBound/Objects/Parameters.lean`.
