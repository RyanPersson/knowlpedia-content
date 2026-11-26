+++
id = "proofs/grh/upper-objects/chain-datum-and-composite-lift"
title = "Chain datum and composite lift"
kind = "definition"
summary = "A chain datum for a twist is a finitely supported coefficient function on tuples of translations, integral away from the twist and bounded, whose glued tensor is jointly invariant; the composite lift is the chain of double lifts with the glued tensor as data, restricted to Y_m."
aliases = ["chain datum", "composite lift", "weak chain datum", "glued tensor", "glued vacuum"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.gluedDoubleLiftDatum", "New.Data.admissibleTranslations", "New.Data.supportedTranslations", "New.Data.ChainTensor", "New.Data.ChainTensor.IsInvariant", "New.Data.gluedVacuum", "New.Data.plainTensor", "New.Data.gluedTensor", "New.Data.IsChainDatum", "New.Data.IsChainDatum.mem_admissibleTranslations", "New.Data.chainOfTensor", "New.Data.compositeLift", "New.Data.IsWeakChainDatum", "New.Seesaw.doubleLiftGluing", "New.Seesaw.poleColumn", "New.Seesaw.poleRow"]
lean_files = ["src/New/UpperBound/Objects/Columns.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]], \(\vartheta\) a [[?lean:New.Data.Twist|twist]] with set of ramified places \(Q\) and \(q=\prod_{w\in Q}q_w\) the product of their norms. Use the [[proofs/grh/upper-objects/lift-kernels-of-the-chain|kernels \(k_j(\vartheta)\), data spaces \(\mathcal S_j\), tuples of translations \(x\) and translated vacua \(\Phi_j(x)\)]], the [[proofs/grh/upper-objects/level-places-of-the-data|places \(P_N\) and levels \(K_{X_j}\)]], and \(m=2\varrho+2\).

**Definition.**

1. *(Gluing.)* For a finite set \(P\) of places, a prime \(N\) and \(y\in((\mathbb Z/N)^P)^{n'}\), the **pole column** is the adelic \(n'\times n^+\) matrix with last column \(-y/N\) (at the places of \(P\)) and zero elsewhere, and the **pole row** is the \(m^+\times n'\) matrix with last row \(-\overline{y/N}\) and zero elsewhere. The **gluing** of a double lift is the endomorphism \(\mathrm{Glue}=\sum_{y}\varrho(\text{pole column}_y)\otimes\varrho(\text{pole row}_y)\) of the tensor product of the two finite data spaces (\(\varrho\) the finite Heisenberg operators). For the double lift \(X_{2i}\to X_{2i+1}\to X_{2i+2}\) it is taken with \(P=P_N\), acting on \(\mathcal S_{2i}\otimes\mathcal S_{2i+1}\).
2. *(Tensors.)* A **chain tensor** is an element of \(\bigotimes_{i\le\varrho}(\mathcal S_{2i}\otimes\mathcal S_{2i+1})\). It is **invariant** for \(\vartheta\) if it is fixed by \(\bigotimes_i\omega_{2i}(b_{2i},b_{2i+1})\otimes\omega_{2i+1}(b_{2i+1},b_{2i+2})\) for all tuples \(b_j\in K_{X_j}\) with \(b_m=1\). For a tuple of translations \(x\): the **glued vacuum** is \(\bigotimes_i\mathrm{Glue}\big(\Phi_{2i}(x)\otimes\Phi_{2i+1}(x)\big)\). For a finitely supported \(\Psi\): the **plain tensor** is \(\varphi^\flat=\sum_x\Psi(x)\bigotimes_i\Phi_{2i}(x)\otimes\Phi_{2i+1}(x)\), and the **glued tensor** is \(\varphi^{\mathrm{ch}}=\sum_x\Psi(x)\cdot(\text{glued vacuum of }x)\).
3. *(Chain datum.)* \(\Psi\) is a **chain datum for \(\vartheta\)** if
   * for every \(x\) in the support of \(\Psi\) and every \(j\): \(\bar\pi_M\,x_j\) is integral at every finite place not dividing \(q\), and \(x_j\) vanishes at every finite place not dividing \(Mq\);
   * every value \(\Psi(x)\) is [[?lean:New.Seesaw.integralAway|integral away from \(q\)]];
   * if \(Q=\emptyset\): \(\sum_x\lvert\sigma(\Psi(x))\rvert\le M^{3fm\,n_m^2}\) for every field automorphism \(\sigma\) of \(\mathbb C\);
   * the glued tensor \(\varphi^{\mathrm{ch}}\) is invariant for \(\vartheta\).
4. *(Composite lift.)* For a source form \(\varphi\), the **composite lift** is
\[
\operatorname{res}_Y\Big(\text{chain of }\varrho+1\text{ double lifts with data }\varphi^{\mathrm{ch}},\text{ applied to }\varphi\Big),
\]
a form on \(Y_m\); here the [[proofs/grh/upper-objects/chain-of-lifts|chain of double lifts]] is extended linearly to chain tensors and \(\operatorname{res}_Y\) is the [[proofs/grh/upper-objects/branching-map-and-restriction-to-y|restriction to \(Y_m\)]]. (It is defined for any tame character \(\vartheta\) and any \(\Psi\).)
5. *(Weak chain datum.)* \(\Psi\) is a **weak chain datum for \(\vartheta\)** if: for \(x\) in its support, \(\bar\pi_Mx_j\) is integral at the places not dividing \(qN\); the values are integral away from \(q\); if \(Q=\emptyset\) then \(\sum_x\lvert\sigma(\Psi(x))\rvert\le\exp(x^{60})\) for all \(\sigma\) (here \(x\) in the exponent is the scale of the data); and \(\sum_x\Psi(x)\otimes\bigotimes_{j<m}\Phi_j(x)\) is [[proofs/grh/upper-objects/jointly-invariant-combination|jointly invariant]] for the kernels \(k_j(\vartheta)\) and the levels \(K_{X_j}\) (coefficients \(L_x=\Psi(x)\cdot\mathrm{id}\)).

## Remarks

A weak chain datum has no gluing, its translations need not vanish anywhere and may have simple poles above \(N\). For a chain datum both \(\varphi^\flat\) and the expansion of \(\mathrm{Glue}\,\varphi^\flat\) are of this form, and the composite lift is then a [[proofs/grh/upper-objects/lift-kernels-of-the-chain|restricted chain]] ([[?lean:New.Data.IsChainDatum.exists_isWeakChainDatum_compositeLift_eq|proved in another area]]). The seesaw identity expresses the chain \(Y_0\to Y_m\) composed with the Poincaré series through the composite lift of a chain datum.

## References

1. Lean: `New.Data.IsChainDatum`, `New.Data.compositeLift`, `New.Data.gluedTensor`, `New.Data.IsWeakChainDatum`, `New.Seesaw.doubleLiftGluing` in `src/New/UpperBound/Objects/Columns.lean`.
