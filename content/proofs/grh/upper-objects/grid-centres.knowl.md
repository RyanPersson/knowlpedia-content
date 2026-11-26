+++
id = "proofs/grh/upper-objects/grid-centres"
title = "The centre system of a grid"
kind = "proposition"
summary = "The parameters of all nodes of a grid at one infinite place come from one separated centre system: the stem is the base parameter and the centres are the plus and minus lift weights."
aliases = ["grid centres", "grid blocks"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.gridCentres", "New.Data.gridBlocks", "New.Data.gridBlocks_succ_left", "New.Data.gridBlocks_succ_right", "New.Data.gridBlocks_succ_right_eq_insert_first", "New.Data.gridBlocks_subset", "New.Data.card_stem_gridCentres", "New.Data.isSeparated_gridCentres", "New.Data.entrySign_eq_mul_sign", "New.Data.gridParam_add_lowering", "New.Data.gridSigns_eq_mul_sign", "New.Data.isParam_gridParam", "New.Data.mul_card_gridIndex_add_pow_three_le"]
lean_files = ["src/New/UpperBound/Objects/Parameters.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/upper-objects/grid-nodes|grid nodes]]. Fix an infinite place \(\tau\) and \(z\in\{0,1\}\).

**Definition.** The [[proofs/grh/upper-objects/centre-system|centre system]] \(\mathcal C_{\tau,z}\) of the grid \(z\) has

* centres: for each \(l<m\) an **up** centre \(u_l\) of value \(w_{l+1}\) and length \(t+z\), and a **down** centre \(d_l\) of value \(-w_{l+1}\) and length \(t-z\);
* stem: \(\{\lambda^Y_{\tau,n}+z/2:\ n<r+z\}\) (it has \(r+z\) elements).

The set of centres **present at the node \((i,j)\) with offset \(o\)** is \(B_{o,i,j}=\{u_l:l<i\}\cup\{d_l:o\le l<o+j\}\).

**Proposition.**

1. \(B_{o,i+1,j}=B_{o,i,j}\cup\{u_i\}\); \(B_{o,i,j+1}=B_{o,i,j}\cup\{d_{j+o}\}=B_{o+1,i,j}\cup\{d_o\}\).
2. \(\mathcal C_{\tau,z}\) is separated with bound \(\Delta-t-2\).
3. If \(o+j\le m\), and \(o=0\) or \(i=0\), then the doubled parameter of the node \((i,j)\) with offset \(o\) at \(\tau\) is the parameter \(\lambda_{B_{o,i,j}}\) of \(\mathcal C_{\tau,z}\) with common sign \((-1)^o\), on the index set of the node with its signs.
4. For \(i,j,i',j'\le m\) and nodes of ranks \(N,N'\): \(500(N+N')^3\le\Delta-t-2\).

## Proof

*1.* Immediate from the definition.

*2.* Use the facts (a), (b) on \(\varsigma=\lambda^Y_\tau\) from the proof of the [[proofs/grh/upper-objects/properties-of-grid-nodes|properties of the nodes]], \(k+t+1\le\Delta/2\), \(w_{l+1}\ge\Delta\) and the \(\Delta\)-separation of the weights. In doubled terms the condition to check is \(\lvert y-2c\rvert\ge(\Delta-t-2)+l_c\). Parity: \(t\pm z\equiv r+z\) mod \(2\), and the doubled stem entries \(2\varsigma_n+z\) have parity opposite to \(r+z\) (\(r\) odd). Stem against an up centre: \(2\varsigma_n+z\le k+1\) and \(2w_{l+1}\ge2\Delta\). Stem against a down centre: \(\lvert2\varsigma_n+2w_{l+1}\rvert\ge\Delta\) by (b), and \(\Delta-1\ge\Delta-t-2+t+1\). Block of another centre \(c'\): its doubled entries are within \(t\) of \(2c'\), and \(\lvert2c-2c'\rvert\ge2\Delta\) in all four cases (same kind: weights \(\Delta\) apart; different kinds: \(w+w'\ge2\Delta\)).

*3.* Rank: by the rank formula of the nodes. Entries: adding the lowering (which is \(1\), doubled, exactly when \(z=0\) and \(i+j\) is odd) to the doubled parameter gives \(2\varsigma_n+z\) on the base and the doubled blocks of the centres in \(B_{o,i,j}\). Signs: we must show \(\operatorname{sign}(x)=(-1)^o\operatorname{sgn}_B(y)\) for the doubled entry \(y\). *Counting lemma:* let \(a\le m\) and suppose \(y\le2w_{l+1}\) for all \(l\ge i\), and, for \(l\notin[o,o+j)\), \(y<-2w_{l+1}\iff l<a\). Then the centres outside \(B\) that count for \(y\) are exactly the down centres \(d_l\), \(l<a\), \(l\notin[o,o+j)\); their number plus \(\min(a\dot-o,j)\) is \(a\), so \(\operatorname{sgn}_B(y)=(-1)^{a-\min(a\dot-o,j)}=(-1)^o\epsilon(o,j,a)\). Apply it: for a base entry with number \(n\), take \(a=n+1\dot-k\le m\) (hypotheses by (a), (b)); for an entry of an up block (then \(o=0\)), take \(a=0\), and \(\epsilon(0,j,0)=1\) (the entry lies below the up centres \(l'\ge i\) by \(\Delta\)-separation and above all down centres); for an entry of the down block \(o+l\), take \(a=o\), \(\epsilon(o,j,o)=1\) (it lies below all up centres, and for \(l'\notin[o,o+j)\) it lies below \(-w_{l'+1}\) iff \(l'<o+l\) iff \(l'<o\)). In the last case the hypothesis "\(o=0\) or \(i=0\)" is not needed beyond the up-block case; it ensures that up blocks occur only with \(o=0\).

*4.* \(N,N'\le2n_m\) and \(500(4n_m)^3+t+2\le\Delta\) by the sizes of the data. \(\square\)

## References

1. Lean: `New.Data.gridCentres`, `New.Data.gridBlocks`, `New.Data.isSeparated_gridCentres`, `New.Data.isParam_gridParam` in `src/New/UpperBound/Objects/Parameters.lean`.
