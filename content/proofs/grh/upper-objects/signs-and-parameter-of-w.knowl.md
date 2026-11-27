+++
id = "proofs/grh/upper-objects/signs-and-parameter-of-w"
title = "Signs of W_j, doubled target parameter, and entry signs"
kind = "definition"
summary = "The signs at the real places of the spaces W_j, the doubled Harish-Chandra parameter on the row index set, and the sign function used for the grid spaces."
aliases = ["signs of W_j", "entry sign", "doubled target parameter"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.paramW", "New.Data.signsW", "New.Data.entrySign", "New.Data.entrySign_eq_neg_one_pow"]
lean_files = ["src/New/UpperBound/Objects/LabelsAndIndexTypes.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]], \(\mathcal R\) the [[proofs/grh/upper-objects/index-sets-of-the-hermitian-spaces|row index set]] with its basis numbering \(\beta\colon\mathcal R\to\{0,\dots,r-1\}\), and \(\tau\) an infinite place of \(E\) (an element of \(\Phi\)).

**Definition.**

* The **doubled parameter** is \(\lambda_\tau(i)=2\,p_\tau(\beta(i))\) for \(i\in\mathcal R\), where \(p_\tau\) is the [[?lean:New.Data.targetParameter|target parameter]] at \(\tau\): \(p_\tau(a)=k/2-1-a\) for \(a<k-1\) and \(p_\tau(a)=\Delta/2-\kappa_{a+2-k}(\tau)\) for \(a\ge k-1\), with \(\kappa_j\) the [[?lean:New.Data.liftWeight|weight of lift \(j\)]] and \(\Delta/2\) the [[?lean:New.Data.halfGap|half gap]].
* The **signs of \(W_j\)** are \(s_j(i)=-1\) if \(\beta(i)\ge k+j-1\) and \(s_j(i)=+1\) otherwise (\(i\in\mathcal R\), \(j\ge0\)). For \(0\le j\le m\), \(W_j\) has \(k+j-1\) plus signs and \(m-j\) minus signs (recall \(r=k+m-1\)); for \(j>m\) the threshold exceeds every basis number and all \(r\) signs are \(+\).
* The **entry sign** is \(\epsilon(o,j,a)=(-1)^{\,o+a+\min(a\dot-o,\;j)}\) for natural numbers \(o,j,a\), where \(a\dot-o=\max(a-o,0)\).

## Remarks

The Lean definition of \(\epsilon\) is recursive, \(\epsilon(o+1,0,a)=-\epsilon(o,0,a)\), which agrees with the closed formula (for \(j=0\) the minimum is \(0\)); it makes the signs for offset \(o+1\) the negatives of those for \(o\) by definition, as needed for the passage to the opposite space in the [[?lean:New.Data.gridSpace|grid spaces]], where \(o\) is the offset of a node, \(j\) its second coordinate and \(a=n+1-k\) (truncated at \(0\)) for the basis vector with number \(n\).

## References

1. Lean: `New.Data.paramW`, `New.Data.signsW`, `New.Data.entrySign`, `New.Data.entrySign_eq_neg_one_pow` in `src/New/UpperBound/Objects/LabelsAndIndexTypes.lean`.
