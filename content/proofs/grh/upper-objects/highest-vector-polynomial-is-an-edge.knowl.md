+++
id = "proofs/grh/upper-objects/highest-vector-polynomial-is-an-edge"
title = "The polynomial of the highest vector is a product of joint harmonics, hence an edge"
kind = "theorem"
summary = "If a parameter l fits a descent pair, the Fock polynomial of the highest weight vector is the product over the infinite places of staircase products of minors, each a joint harmonic; so its Fock vector is an edge between the discrete series kernels of l and of the parameter of V."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.DescentPair.FitsParams.exists_isJointHarmonic", "New.DescentPair.FitsParams.isEdge", "New.DescentPair.fockPoly_highestVector", "New.DescentPair.FitsParams.isJointHighest_productOfMinors", "New.DescentPair.FitsParams.lowestKType_eq_staircaseWeight", "New.DescentPair.FitsParams.isJointHarmonic_productOfMinors", "New.DescentPair.realPairWeil_fockPoly", "New.DescentPair.fockRowSubst_tensorPoly", "New.fockRowSubst", "New.realPairWeil_one_polyVector", "New.fockRowSubst_fockLetters", "New.realPairWeil_fockLetters"]
lean_files = ["src/New/UpperBound/Objects/AuxiliaryPair.lean"]
proof_status = "outline"
+++

Let \(O\) be a [[proofs/grh/upper-objects/descent-pair|descent pair]], \(l\) a parameter that [[proofs/grh/upper-objects/descent-pair-fitting-parameters|fits \(O\)]], \(l'\) the parameter of \(V\), \(\Pi_w\) the product of minors at \(w\), \(v^+\) the [[?lean:New.highestVector|highest vector]] of the Weyl module of \(O\) for \(l'\), and \(\xi\mapsto P_\xi\) the [[proofs/grh/upper-objects/normalized-descent|Fock polynomial]]. Put \(\gamma_w=\lfloor n/2\rfloor+\operatorname{wt}_w\).

**Theorem.**

1. \(P_{v^+}=\prod_w\Pi_w\), each \(\Pi_w\) written in the Fock variables of the place \(w\). (This needs no hypothesis on \(l\).)
2. For every infinite place \(w\), \(\Pi_w\) is a [[?lean:New.IsJointHarmonic|joint harmonic]] for the standard Fock dual pair of \((V,W)\) with weights \(r_-\) and \(-\gamma_w\) and parameters \(l'_w\) and \(-l_w\); and the lowest \(K\)-type of \(-l_w\) on \(W\) is the [[?lean:New.staircaseWeight|staircase weight]] of \((k^+(w,\cdot),k^-(w,\cdot))\).
3. If \(r\ne\emptyset\), the Fock vector of \(P_{v^+}\) is an [[?lean:New.IsEdge|edge]] from the [[?lean:New.typeKernel|type kernel]] of \((l,s)\) to the type kernel of \((l',1)\), for the real Weil representation with weights \(r_-\) and \(\gamma\).
4. *(Action of the compact group.)* For \(y\in U(V)(\mathbb R)\) and \(\xi\) in the Weyl module, the real Weil representation (weights \(r_-\), any \(\gamma'\)) satisfies \(\omega_\infty(1,y)\,v_{P_{\bar\xi}}=v_{P_{\overline{\rho(y)\xi}}}\), where \(\rho\) is the action through the conjugate matrices by which algebraic forms transform.

## Proof

*4.* With first weight \(r_-\), \((1,y)\) acts on the Fock vector of a polynomial by the substitution \(X_{\tau,i,a}\mapsto\sum_j(y_\tau)_{ji}X_{\tau,j,a}\) for columns \(a\) of sign \(+1\) and \(X_{\tau,i,a}\mapsto\sum_j(y_\tau^{-1})_{ij}X_{\tau,j,a}\) for sign \(-1\); the scalar of the general formula (Lean: `New.realPairWeil_polyVector`, cited) is trivial for this weight. On letter polynomials this is the substitution of \(y^{\mathsf T}\), resp. \(y^{-1}\), in the row variables, so on the polynomial of a tensor \(v\in\mathcal V_{k^+}\otimes\mathcal V_{k^-}\) it is the action of \(S_{k^+}(y)\otimes S_{k^-}(y^{-\mathsf T})\) (Schur matrices). The chosen embedding \(\mathcal V\hookrightarrow\mathcal V_{k^+}\otimes\mathcal V_{k^-}\) intertwines this with the Weyl representation (Lean: `New.MixedCartanEmbedding.intertwines`, cited), and \(\overline{\rho(y)\xi}\) is the image of \(\bar\xi\) under \(y\).

*1.* The embedding sends \(v^+\) to a tensor of two evaluation vectors (Lean: `New.MixedCartanEmbedding.top`, cited), and the letter polynomial of an evaluation vector is a product of powers of leading minors. The row order: the position of \(a\in n\) by decreasing \(l'_w\) is its standard number, and by decreasing \(-l'_w\) the reversed number, because \(l'_w\) is strictly decreasing.

*2.* By the Lean lemma `New.isJointHighest_prod_det_pow_staircaseWeight` (cited) the product of minors is nonzero, harmonic on both sides and highest for rows and columns, with column weight the staircase weight, provided: \(l_w\) is injective (the left gap in the fitted block rule; it makes the numbering within each sign a bijection) and \(l'_w\) is injective (it is a Harish-Chandra parameter), the numbering condition 2 of fitting, no minor is larger than the number of columns of its sign (condition 3), and minors of opposite signs fit into the rows (\(r_++r_-=\lvert r\rvert<\lvert n\rvert\) with condition 3). The row weight is checked to be the lowest \(K\)-type of \(l'_w\) by splitting \(\sum_{1\le i<n}k^-(w,i)\) at the position of the row. Since \(l,l'\) correspond, a joint harmonic \(Q\) for the two lowest \(K\)-types exists (Lean: `ParamsCorrespond.isMatch`, `exists_isJointHarmonic`, cited) and spans the polynomials with these properties (Lean: `IsJointHarmonic.exists_eq_smul_of_row_weight`, cited), so \(\Pi_w=aQ\) with \(a\neq0\); comparing the eigenvalues of the column torus gives the statement on the lowest \(K\)-type of \(-l_w\), and \(\Pi_w\) is a joint harmonic.

*3.* By 1, 2 and the Lean theorem `New.isEdge_of_isJointHarmonic` (a product over the places of joint harmonics gives an edge; cited). \(\square\)

The cited results belong to the theory of discrete series and theta correspondence in `Lib`; this page gives only the assembly performed in the file.

## References

1. Lean: `New.DescentPair.FitsParams.exists_isJointHarmonic`, `New.DescentPair.FitsParams.isEdge`, `New.DescentPair.realPairWeil_fockPoly` in `src/New/UpperBound/Objects/AuxiliaryPair.lean`.
