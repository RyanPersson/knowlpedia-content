+++
id = "proofs/grh/upper-objects/grid-nodes"
title = "Index sets, signs and parameters of the nodes of the two grids"
kind = "definition"
summary = "For the two grids of unitary groups Y and Y-tilde, with an offset for the triangles: the index set, the signs at the real places and the doubled Harish-Chandra parameter of each node, and the weights of the steps; in particular the signs and parameter of Y_j."
aliases = ["grid index", "grid signs", "grid parameter", "grid weight", "signs of Y_j", "parameter of Y_j"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.GridIndex", "New.Data.gridNumber", "New.Data.gridBlockEquiv", "New.Data.gridSigns", "New.Data.gridParam", "New.Data.gridParam_false", "New.Data.gridParam_true", "New.Data.neg_gridParam_true", "New.Data.signsY", "New.Data.paramY", "New.Data.gridWeight", "New.Data.gridHarmonic", "New.Data.gridDiagEquiv"]
lean_files = ["src/New/UpperBound/Objects/Parameters.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]]: \(m\) even, \(r\) odd, \(k=r+1-m\), \(t=5r\) odd, gap \(\Delta\), and for an infinite place \(\tau\) the centres \(w_l=\kappa_l(\tau)\) ([[?lean:New.Data.liftWeight|lift weights]]) and the [[?lean:New.Data.targetParameter|target parameter]] \(\lambda^Y_\tau=([k-1];-\kappa_{1/2},-\kappa_{3/2},\dots)\), entries numbered from \(0\). Let \(\mathcal R\) be the [[proofs/grh/upper-objects/index-sets-of-the-hermitian-spaces|row index set]] with numbering \(\beta\), and \(\epsilon(o,j,a)=(-1)^{o+a+\min(a\dot-o,j)}\) the [[proofs/grh/upper-objects/signs-and-parameter-of-w|entry sign]]. A flag \(z\in\{0,1\}\) selects the grid: \(z=0\) for \(Y\), \(z=1\) for \(\tilde Y\).

**Definition.** Let \(i,j,o\ge0\) (\(o\) is the *offset*; the grids are \(o=0\), the triangles are \(i=0\)).

* **Index set of the node \((i,j)\)**: a base \(\mathcal R\) (for \(z=1\): \(\mathcal R\sqcup\{\ast\}\), the extra point having number \(r\)), followed by \(i\) blocks of length \(t+z\) (*first kind*) and \(j\) blocks of length \(t-z\) (*second kind*). A splitting of the index set into base numbers \(n<r+z\), positions \((l,b)\) of first-kind blocks (\(l<i\), \(b<t+z\)) and positions \((l,b)\) of second-kind blocks (\(l<j\), \(b<t-z\)) is fixed; except at the node \((0,0)\) this splitting is an arbitrary bijection.
* **Signs** (with offset \(o\)): the base index with number \(n\) has the sign \(\epsilon(o,j,\,n+1\dot-k)\); all indices in added blocks have the sign \(+1\).
* **Doubled parameter** at \(\tau\) (with offset \(o\)): let \(y\) be \(2\lambda^Y_{\tau,n}\) at the base index \(n\); \(2w_{l+1}+t-1-2b\) at \((l,b)\) of the first kind; \(-2w_{l+1+o}+t-1-2z-2b\) at \((l,b)\) of the second kind. The parameter is \(y+1\) if \(z=1\); and for \(z=0\) it is \(y-1\) if \(i+j\) is odd and \(y\) otherwise.
* **\(Y_j\)**: the signs and the doubled parameter of \(Y_j\) are those of the node \((0,j)\) of grid \(Y\) with offset \(0\), on the index set \(\mathcal R\sqcup j\) blocks of length \(t\).
* **Weight of a step**: for a flag \(c\), \(l\ge0\) and a node with \(N\) indices, \(\operatorname{gw}_{c,l}(\tau)=\lfloor N/2\rfloor-w_{l+1}(\tau)\) if \(c=1\) and \(\lceil N/2\rceil-w_{l+1}(\tau)\) if \(c=0\).

So for \(z=0\), \(o=0\) the node \((i,j)\) is the space \(Y^i_j\) with twice its parameter: \(2\lambda^Y\) on the base, blocks of length \(t\) centred at \(w_l\) (\(1\le l\le i\)) and at \(-w_l\) (\(1\le l\le j\)), all lowered by \(1\) if \(i+j\) is odd. For \(z=1\), \(o=0\) the node \((i,j)\) is the space \(\tilde Y^j_i\) with *minus* twice its parameter, so that one formula serves both grids: the doubled parameter of \(\tilde Y^j_i\) is \(-2\lambda^Y-1\) on the base with rising blocks of length \(t+1\) centred at \(-w_l\) (\(l\le i\)) and of length \(t-1\) centred at \(w_l\) (\(l\le j\)).

## Remarks

The Lean text also fixes, for each pair of nodes and each step, a product over the infinite places of chosen [[?lean:New.jointHarmonic|joint harmonic polynomials]] (`gridHarmonic`), and for each \(j\) a bijection between the index set of \(\tilde Y\) at \((j,j)\) and that of \(Y\) at \((j,j)\) plus one point, matching the signs (`gridDiagEquiv`; see [[proofs/grh/upper-objects/properties-of-grid-nodes|properties of the nodes]]).

## References

1. Lean: `New.Data.GridIndex`, `New.Data.gridSigns`, `New.Data.gridParam`, `New.Data.signsY`, `New.Data.paramY`, `New.Data.gridWeight` in `src/New/UpperBound/Objects/Parameters.lean`.
