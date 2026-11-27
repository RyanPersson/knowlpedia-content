+++
id = "proofs/grh/upper-objects/lower-chain"
title = "The chain of theta lifts along Y_0, ..., Y_m"
kind = "definition"
summary = "For a tame character theta: the theta lifts from forms on Y_j to forms on Y_{j+1} with the joint harmonic at infinity and the point datum at the finite places, and their composite from forms of principal level on Y_0 to algebraic forms on Y_m."
aliases = ["lower chain", "chain Y_0 to Y_m", "lift along Y_j"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.blockNumber", "New.blockNumber_eq_zero_iff", "New.Data.FormY", "New.Data.harmonicY", "New.Data.datumY", "New.Data.paramsCorrespond_paramY", "New.Data.isArrow_datumY", "New.Data.isArrow_thetaKernelY_datumY", "New.Data.isArrow_swap_thetaKernelY_datumY", "New.Data.liftY", "New.Data.lowerChainUpTo", "New.Data.lowerChain"]
lean_files = ["src/New/UpperBound/Objects/RowChain.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]] and \(\vartheta\) a [[?lean:New.Data.TameChar|tame character]]. Use the [[proofs/grh/upper-objects/spaces-y-and-w|spaces \(Y_j\)]], their [[proofs/grh/upper-objects/grid-nodes|signs and doubled parameters]], and the [[proofs/grh/upper-objects/point-datum-on-y|theta kernel of \((Y_j,Y_{j+1})\), level \(K_{Y_j}(\vartheta)\) and point datum \(\Upsilon_{j+1}\)]].

**Definition.**

* \(\mathcal A(Y_j)\) is the space of [[?lean:New.Space.Form|forms on \(U(Y_j)(\mathbb A)\)]] of the type given by the parameter and signs of \(Y_j\), with the Petersson product.
* The **datum of lift \(j+1\)** is \(\phi_{j+1}\otimes\Upsilon_{j+1}\) on \(\operatorname{Hom}(Y_j,Y_{j+1})\): at infinity the product over the infinite places of the chosen [[?lean:New.jointHarmonic|joint harmonics]] for the parameters and signs of \(Y_j\) and \(Y_{j+1}\) (the splitting character on a space of rank \(n\) has weight \(\lfloor n/2\rfloor-w_{j+1}(\tau)\)), and the point datum at the finite places.
* **Lift \(j+1\)** is the map \(\mathcal A(Y_j)\to\mathcal A(Y_{j+1})\) equal to the index \([K_0:K_{Y_j}(\vartheta)]\) times the [[?lean:New.Space.lift|theta lift]] with this datum.
* The **chain** \(\Theta_\vartheta\) (written \(\iota_\mu\) in the Lean comments) is the composite of the \(m\) lifts, from the [[proofs/grh/upper-objects/target-form|forms of principal level]] on \(Y_0\) to \(\mathcal A(Y_m)\), read as [[?lean:New.AlgForm|algebraic forms]] on the definite group \(U(Y_m)\) of weight \(\mu(Y_m)\) (column numbers \(c^Y_\tau\), determinant exponent \(\ell_m\)).

## Properties

For \(j<m\) the parameters of \(Y_j\) and \(Y_{j+1}\) correspond for the weights \(\operatorname{gw}_{1,j}\) (this is the step in the second coordinate of the grid \(Y\) from \((0,j)\) to \((0,j+1)\), see [[proofs/grh/upper-objects/grid-steps-correspond|steps correspond]]). Consequently the datum of lift \(j+1\) is an [[?lean:New.IsArrow|arrow]] in both directions: every form of the type of \(Y_j\) is of rapid decay and its lift is a form of the type of \(Y_{j+1}\), and for the swapped Weil representation every form of the conjugate type on \(Y_{j+1}\) is of rapid decay and its lift is of the conjugate type on \(Y_j\). The lift maps of the definition are the ordinary theta integrals only for these \(0\le j<m\); in general the Lean `formLift` is defined with projections (by the theorem of the library that a joint harmonic for corresponding parameters gives an edge; cited from another area).

The identification of forms on the definite space \(Y_m\) with algebraic forms uses that the parameter of \(Y_m\) is that of the weight \(\mu(Y_m)\) ([[proofs/grh/upper-objects/point-datum-on-y|see there]]).

## References

1. Lean: `New.Data.liftY`, `New.Data.lowerChain`, `New.Data.isArrow_datumY` in `src/New/UpperBound/Objects/RowChain.lean`.
