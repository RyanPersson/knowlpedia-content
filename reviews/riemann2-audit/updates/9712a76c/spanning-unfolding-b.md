# spanning-unfolding-b

All 89 knowls and their chapter narrative were checked. Of 7 earlier findings, 0 are resolved, 3 are partly addressed and 4 remain open. This review adds 53 findings. [Author’s report](https://github.com/RyanPersson/knowlpedia/blob/12cc7330341b6b4fb72c78b91a659e67e82a4b18/docs/riemann2/reports/spanning-unfolding-b.md)

[Review overview](README.md) · [Status of earlier findings](response-ledger.tsv) · [New findings](findings.tsv)

<a name="page-spanning-unfolding-b"></a>

## Unfolding II: the filling data, terms and their links, and the moment bounds

Added · page · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b.knowl.md) · [Moments.lean:567](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Moments.lean#L567)

All 89 child knowls are linked and every such target resolves. The orientation of the two cutoff factors and the numerical constants b⁻¹², 1 + 9b⁻⁴ and 5b⁻⁴ agree with the source.

<a name="new-spanning-unfolding-b-1"></a>

**New finding · high · The whole-group moment bound needs positive type and an identity bound.** For arbitrary admissible filling data the displayed conclusion has two additional analytic hypotheses. For β(s) the singleton second moment, the theorem takes a realization β(a⁻¹b) = ⟪u(a),u(b)⟫ and β(1) ≤ 2 dim_S, as well as Weil data on E. Mentioning a sieve for positive-type functions does not establish either hypothesis for β. They are proved later for a unitary amplitude-block realization in Moments.lean:571–577. State the conditional bound with its two assumptions and Weil data. When the operator realization is introduced, explain how it supplies them. [Knowl, line 52](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b.knowl.md#L52) · [MomentBounds.lean:441](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/MomentBounds.lean#L441)

<a name="new-spanning-unfolding-b-2"></a>

**New finding · high · An amplitude-block realization must be unitary for equivariance and the total bound.** The chapter quantifies over an arbitrary representation, but the intertwining identity explicitly assumes that ρ preserves the chosen inner product. Its proof moves ρ across inner products. The whole-group Hilbert–Schmidt bound at line 567 and the good-forms theorem at line 1230 need the same assumption. Averaging the inner product on a finite group would change P\* and the specified blocks. Introduce a finite-dimensional unitary ρ with respect to the inner product used for P\*, assume admissibility and the requisite field data, and distinguish the block identities that hold before unitarity is imposed. [Knowl, line 56](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b.knowl.md#L56) · [Moments.lean:347](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Moments.lean#L347)

<a name="new-spanning-unfolding-b-3"></a>

**New finding · medium · A threshold for norm-one pairs alone does not give a cell rank.** The definition also requires the j-th leading minor to be nonzero and j to be the top rank exactly when the discriminant is nonzero. For example an isometry scaling the isotropic frame by 2, its dual by 1/2, and fixing the middle has a norm-one pair at z and at no earlier index. Its leading minor of size ϱ is zero since it preserves the isotropic span. The flag threshold therefore fails the cell-rank test. Describe all three tests for a proposed rank j, including one common norm-one coefficient for all a ≥ j. [Knowl, line 36](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b.knowl.md#L36) · [Terms.lean:114](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Terms.lean#L114)

<a name="new-spanning-unfolding-b-4"></a>

**New finding · medium · The quotient identification with the positive space is linear.** The equivalence directly following the graph-isometry statement can be read as identifying the quotient with its inherited Hermitian form. At γ = 1 the quotient is A⊥/A and contains z of norm −N, whereas z⁺ has norm +N. The cited theorem identifies the kernel and range of a linear map. The isometry statement concerns the source and target obtained by exchanging coordinates of the link pair. Describe the induced E-linear bijection from the quotient, and reserve preservation of the positive form for the link isometry. [Knowl, line 40](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b.knowl.md#L40) · [Link.lean:727](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Link.lean#L727)

<a name="new-spanning-unfolding-b-5"></a>

**New finding · medium · Unipotent invariance holds for leading principal minors.** The chapter says that minors are invariant on both sides. The minor theorem controls the top-left principal minor of each order. Adding an earlier column to a later one preserves these minors but can alter other entries and minors. The cell-stability deduction uses only the leading ones. Specify the leading principal minors of the frame Gram matrix. [Knowl, line 40](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b.knowl.md#L40) · [FloorGroups.lean:702](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bruhat/FloorGroups.lean#L702)

<a name="new-spanning-unfolding-b-6"></a>

**New finding · medium · The flag direct sum and rank formula need a primitive root hypothesis.** For a bare CM field the cited result does not give disjointness or the dimension formula. An existing cell rank and a zero discriminant give the ordinary sum at line 673. The disjointness at line 690 and rank formula at line 710 both assume a primitive 5040th root in E. With the zero-based frame of this chapter, the first j frame vectors span e₀ through eⱼ₋₁, so writing A_{≤j} without a definition also gives the wrong first summand at j = 0 on the usual inclusive reading. Assume the primitive root here and define the flag summand as the span of the first j vectors, empty for j = 0. A standing Weil-data hypothesis would also supply the root if its scope is made explicit. [Knowl, line 44](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b.knowl.md#L44) · [TermStructure.lean:710](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/TermStructure.lean#L710)

<a name="new-spanning-unfolding-b-7"></a>

**New finding · medium · Off-subgroup terms and remaining terms agree only after summation.** The excluded cosets in AvoidsScalarCosets are ζR̄₀ for nonidentity integral global norm-one ζ. The condition permits R̄₀ itself. For admissible data containing the requisite primitive root, the theorem identifies amplitude sums over each block. Terms outside both the Bessel subgroup and the remaining set with disagreeing characters have total amplitude zero by cancellation (lines 524–538). Disjointness of the cosets alone does not eliminate those terms individually. Specify the nonidentity global scalars, then say that at each allowed residue the off-Bessel amplitude sum equals the sum over the remaining terms by character cancellation. [Knowl, line 48](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b.knowl.md#L48) · [SquareExpansion.lean:519](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/SquareExpansion.lean#L519)

<a name="new-spanning-unfolding-b-8"></a>

**New finding · medium · Scalar cosets overlap the non-open part of the proposed partition.** Every scalar-coset element is non-open. In particular the identity lies in both categories. MomentBounds.lean:217–220 separates scalar cosets from their complement inside the full-fixer estimate. Only when a maximizing fixer omits a place does the proof split its elements into open and non-open parts (lines 477–510). Reading the three listed classes as a partition double counts. Describe the two cases for the maximizing set of places, with the scalar split in the full-fixer case and the open/non-open split in the proper case. [Knowl, line 52](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b.knowl.md#L52) · [SquareExpansion.lean:271](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/SquareExpansion.lean#L271)

<a name="new-spanning-unfolding-b-9"></a>

**New finding · medium · The first operator estimate uses an undefined residue set and a zero extension.** Ωᵢ appears without a definition. The sum is over residues agreeing with some member of R̄₀ in the other level-prime coordinate, and those residues need not belong to R̄₀. The immediately preceding sentence defines rψ only as a representation of R̄₀, so the difference in the displayed sum also needs its values outside that subgroup (zero by Moments.lean:169). Set Ωᵢ = {s ∈ Ḡ : there exists t ∈ R̄₀ with sᵢ₊₁ = tᵢ₊₁}, with the index modulo two, and extend rψ by zero on the complement of R̄₀. [Knowl, line 58](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b.knowl.md#L58) · [Moments.lean:446](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Moments.lean#L446)

<a name="new-spanning-unfolding-b-10"></a>

**New finding · medium · Near-isometry is a lower mean-square estimate over subspaces.** The unqualified conclusion “almost an isometry with error 5b⁻⁴” suggests uniform two-sided control on vector norms. The statement bounds ‖ρ(e₀)P pr_U‖²_HS below by dim U − 5b⁻⁴ dim_S for every source subspace U. The allowance scales with the full source dimension, so this estimate can tolerate a kernel on a small subspace. The precise coefficient bound on each idempotent complement is Re((1−gᵢ)(1)) ≤ b⁻⁸/2. Describe the one-sided mean-square conclusion, and give the subspace estimate and coefficient threshold so that the error scale is unambiguous. [Knowl, line 60](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b.knowl.md#L60) · [Moments.lean:1230](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Moments.lean#L1230)

<a name="new-spanning-unfolding-b-11"></a>

**New finding · low · Strong approximation reaches the reduced unipotent subgroup.** “Every reduction” has an ambient group already named, the full residue group. The equivalence for a fixed class c says that the attained residues are exactly the reductions of integral unipotent elements. A residue outside that subgroup cannot have the stated lift. Say that at each class the rational unipotent terms reach every element of the reduced unipotent subgroup, with the prescribed character. [Knowl, line 32](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b.knowl.md#L32) · [BesselLevelStructure.lean:878](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselLevelStructure.lean#L878)

<a name="new-spanning-unfolding-b-12"></a>

**New finding · low · The singleton moment equals the squared Hilbert–Schmidt norm.** The link text states that the norms themselves are second moments. The normalization proved in Lean is ‖P_s‖²_HS = secondMoment({s}). The adjacent display indeed uses squares. Write “its squared Hilbert–Schmidt norm is the second moment at s.” [Knowl, line 56](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b.knowl.md#L56) · [Moments.lean:137](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Moments.lean#L137)

<a name="page-amplitude-blocks"></a>

## Maps with amplitude blocks

Added · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/amplitude-blocks.knowl.md) · [Moments.lean:92](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Moments.lean#L92)

The defining pairing has the correct argument order and class/coordinate indices. The identification of that pairing with a matrix entry reverses the complex conjugation.

<a name="new-amplitude-blocks-1"></a>

**New finding · medium · Conjugate the amplitude when reading off the Gram matrix.** With the stated convention the row-x, column-y coefficient is ⟨e_x,P_s e_y⟩ = overline(A_xy)/ν. The formula ⟨P_s e_y,e_x⟩ = A_xy/ν is correct for the reverse pairing. Calling it the matrix entry contradicts both the next clause and the source. The summary at line 5 makes the same identification. Keep the definition’s pairing unchanged. In the summary and remark describe the blocks as entrywise conjugates of the normalized amplitudes, and write the row-x, column-y coefficient with e_x in the first slot. [Knowl, line 22](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/amplitude-blocks.knowl.md#L22) · [Moments.lean:86](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Moments.lean#L86)

<a name="page-avoiding-scalar-cosets"></a>

## Sets avoiding the scalar cosets of the reduced Bessel group

Added · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/avoiding-scalar-cosets.knowl.md) · [SquareExpansion.lean:329](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/SquareExpansion.lean#L329)

The avoidance quantifier correctly ranges over global integral norm-one elements. Kronecker applies because conjugation in the CM field gives absolute value one at every embedding.

<a name="new-avoiding-scalar-cosets-1"></a>

**New finding · low · Distinguish the adelic membership test from a group coset.** For an arbitrary integral finite adele ζ the displayed predicate can be empty. If ζ is zero modulo even one chosen place, the corresponding matrix on the right is singular and no element of the residue group satisfies it. A group coset of the reduced Bessel subgroup is always nonempty. Describe the formula as a membership predicate for general integral adeles. It is a group coset when all chosen residues are units, as they are for the global scalars in the avoidance condition. [Knowl, line 14](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/avoiding-scalar-cosets.knowl.md#L14) · [Climbing.lean:280](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Climbing.lean#L280)

<a name="page-bessel-groups-in-the-lattice-basis"></a>

## Bessel groups under the change to the lattice basis

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/bessel-groups-in-the-lattice-basis.knowl.md) · [BesselLevelStructure.lean:101](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselLevelStructure.lean#L101)

The change of basis and its inverse preserve the level filtration. The description of H as an image and its conjugation of rational unipotents agree with the finite-adelic lemmas.

<a name="new-bessel-groups-in-the-lattice-basis-1"></a>

**New finding · low · Distinguish the base field of the rational unitary group from its matrix coefficient field.** The inclusion formula calls η a rational point of U(X₀)(E). In the linked definition of classes the source unitary group is defined over E⁺. Its rational points are the E-matrices η satisfying η\*η=1, whereas base change of that algebraic group to the CM field E splits it. Write η ∈ U(X₀)(E⁺) and, if desired, identify these points with the unitary matrices over E. Apply the finite embedding to η on the right of the formula. [Knowl, line 18](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/bessel-groups-in-the-lattice-basis.knowl.md#L18) · [BesselLevelStructure.lean:148](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselLevelStructure.lean#L148)

<a name="page-bessel-subgroup-reductions-reached-by-rational-terms"></a>

## Reductions of the Bessel subgroup are reached by rational terms

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/bessel-subgroup-reductions-reached-by-rational-terms.knowl.md) · [BesselLevelStructure.lean:895](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselLevelStructure.lean#L895)

The rational unipotent approximation and the order of the two factors of the principal-level correction agree with the proof. The double-coset step requires its rational factor in the group defining the classes.

<a name="new-bessel-subgroup-reductions-reached-by-rational-terms-1"></a>

**New finding · medium · Use the rational group that actually defines the double cosets.** The decomposition of g is written with η ∈ U(X₀)(E). The class representatives are for the left action of U(X₀)(E⁺), as specified in the class definition and the cited Lean theorem. An arbitrary E-point after scalar extension need not be unitary for the CM involution and cannot be used for the claimed rational extension. In g=ηg_d a take η ∈ U(X₀)(E⁺), represented by a matrix over E with η\*η=1. Read its product with g_d through its finite embedding. [Knowl, line 19](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/bessel-subgroup-reductions-reached-by-rational-terms.knowl.md#L19) · [BesselLevelStructure.lean:893](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselLevelStructure.lean#L893)

<a name="page-bessel-subgroup-terms-in-principal-level"></a>

## Rational elements of the Bessel subgroup in the principal level are unipotent

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/bessel-subgroup-terms-in-principal-level.knowl.md) · [BesselLevelStructure.lean:831](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselLevelStructure.lean#L831)

The level factorization isolates g_c⁻¹ηg_d in the source level. Equality of classes and the free stabilizer then force the rational H-factor to be the identity.

<a name="new-bessel-subgroup-terms-in-principal-level-1"></a>

**New finding · medium · Freeness is asserted for points over the wrong base field.** The argument writes η ∈ U(X₀)(E) on line 19 and states the trivial-stabilizer hypothesis for δ ∈ U(X₀)(E) on line 25. The filling datum supplies this hypothesis for U(X₀)(E⁺), embedded at the finite places. The nominal E-points of the scalar-extended algebraic group form a larger split group. Use U(X₀)(E⁺) in both lines and, if needed, describe it as the group of E-matrices satisfying η\*η=1. [Knowl, line 25](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/bessel-subgroup-terms-in-principal-level.knowl.md#L25) · [BesselLevelStructure.lean:825](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselLevelStructure.lean#L825)

<a name="page-bessel-translate"></a>

## The twisted translation operators of the reduced Bessel group

Added · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/bessel-translate.knowl.md) · [Moments.lean:159](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Moments.lean#L159)

The conjugated matrix defining rψ is correct, including its class and coordinate order. Its support assertion and the representation property have different hypotheses.

<a name="new-bessel-translate-1"></a>

**New finding · medium · Add the hypotheses for the twisted translations to form a unitary representation.** The definition starts with an arbitrary filling datum. The vanishing off the reduced Bessel group holds at that generality. The identity, multiplication and adjoint lemmas used for the representation additionally assume admissibility and a primitive 5040th root of unity in E. Keep the vanishing unconditional and explicitly qualify the unitary representation assertion by those two hypotheses. [Knowl, line 22](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/bessel-translate.knowl.md#L22) · [Moments.lean:239](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Moments.lean#L239)

<a name="page-bessel-translate-is-a-unitary-representation"></a>

## The twisted translations form a unitary representation of the reduced Bessel group

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/bessel-translate-is-a-unitary-representation.knowl.md) · [Moments.lean:207](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Moments.lean#L207)

The proof correctly evaluates the matrix product with entrywise conjugation, distinguishes left multiplication by a subgroup element, and uses s⁻¹ in the trace. The body supplies the restriction missing in the summary.

<a name="new-bessel-translate-is-a-unitary-representation-1"></a>

**New finding · low · Restrict multiplicativity in the summary to the reduced Bessel group.** The zero extension is described as multiplicative without a domain restriction. For s outside the subgroup both r(s) and r(s⁻¹) vanish, whereas r(ss⁻¹) is the identity. Part 3 already gives the precise statement. Say that the restriction to the reduced Bessel group is multiplicative, or state the version for a left factor in that subgroup. [Knowl, line 5](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/bessel-translate-is-a-unitary-representation.knowl.md#L5) · [Moments.lean:207](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Moments.lean#L207)

<a name="page-blocks-of-the-bessel-subgroup"></a>

## Blocks of the Bessel subgroup

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/blocks-of-the-bessel-subgroup.knowl.md) · [SquareExpansion.lean:434](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/SquareExpansion.lean#L434)

The body gives the inverse finite unipotent character, the tensor product action, the vanishing blocks, and the conjugated entry N̄ⱼₖ with residue st⁻¹ in the correct order.

<a name="new-blocks-of-the-bessel-subgroup-1"></a>

**New finding · low · Qualify the block and translation laws in the summary.** A full block containing a subgroup term is νM, while blocks with no subgroup term vanish. The right-translation formula that compares two blocks of the same set T also requires membership in T to be invariant under right multiplication by δ⁻¹ (lines 489–497 of the source). Stability alone concerns rational unipotents. State that matching full blocks are νM, empty blocks are zero, and the comparison for a fixed stable T assumes Tδ⁻¹ = T. [Knowl, line 5](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/blocks-of-the-bessel-subgroup.knowl.md#L5) · [SquareExpansion.lean:434](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/SquareExpansion.lean#L434)

<a name="page-cell-rank-of-a-term"></a>

## Cell rank of a term

Added · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/cell-rank-of-a-term.knowl.md) · [Terms.lean:114](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Terms.lean#L114)

The page uses one common norm-one multiplier for all indices from j onward, requires the j-th leading minor to be nonzero and correctly treats the vacuous flag condition at j = ϱ+1.

<a name="new-cell-rank-of-a-term-1"></a>

**New finding · low · Define the isotropic space in the cell-rank formula.** The dimension formula introduces A without defining it. Taking the span of the entire frame, which also contains z, would already give the wrong dimension for the identity isometry. Define A as the span of e₀, …, eᵨ₋₁ immediately before the formula. [Knowl, line 30](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/cell-rank-of-a-term.knowl.md#L30) · [TermStructure.lean:710](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/TermStructure.lean#L710)

<a name="page-common-link"></a>

## Common link of two isometries

Added · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/common-link.knowl.md) · [Terms.lean:64](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Terms.lean#L64)

The body specifies the intersection with both kernels of the z row and the projection of the first middle vector to its X₀ coordinates. The separate link form for a filling datum also has the correct minus sign on its second block.

<a name="new-common-link-1"></a>

**New finding · medium · Project the first middle vector in the common-link summary.** The summary identifies the output with the first vector itself. For two identity isometries over the reals with middle Gram matrix ((1,1),(1,2)), the diagonal pair with both vectors (2,−1) satisfies both z-orthogonality tests. It projects to 2 in X₀, although (2,0) is not z-orthogonal. The body gives the correct definition on line 18. Call each element of the common link the X₀-coordinate projection of the first vector in a qualifying pair. [Knowl, line 5](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/common-link.knowl.md#L5) · [Terms.lean:64](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Terms.lean#L64)

<a name="page-expansion-of-the-squares"></a>

## Expansion of the squares

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/expansion-of-the-squares.knowl.md) · [SquareExpansion.lean:559](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/SquareExpansion.lean#L559)

The link sum uses cut amplitudes with no ν⁻², while the ordinary moment includes ν⁻². The cut estimate and remaining-term estimate each cost at most b⁻²⁰ times the square root of the identity moment after taking square roots.

<a name="new-expansion-of-the-squares-1"></a>

**New finding · low · Name the ambient space for the link sum.** “All subspaces” leaves the index Λ unspecified. The link lives in two copies of the middle-coordinate space, which includes the distinguished z coordinate. The linked subspace of X₀ used elsewhere in the area is a different object. Specify all E-linear subspaces of (E^(κ ⊔ {z}))² and link the term “link” to its definition. [Knowl, line 23](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/expansion-of-the-squares.knowl.md#L23) · [Size.lean:82](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/Size.lean#L82)

<a name="page-filling-amplitude"></a>

## Bessel kernel, amplitude of a term and amplitude sums

Existing chapter knowl · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/filling-amplitude.knowl.md) · [Setup.lean:669](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Setup.lean#L669)

The second Bessel factor is conjugated, and the product of cutoffs is converted from extended nonnegative reals for the Bochner integral. Both full and cut functions really are continuous in BesselSystem.besselFn.

<a name="new-filling-amplitude-1"></a>

**New finding · medium · Square the normalized block when passing to the second moment.** The normalized amplitude A_T/ν is a complex vector. The contribution of the block (c,s,c′) to the second moment for T is the real number ‖A_T‖²/ν². For disjoint sets of terms, the moment of the union can include cross terms. For the full uncut family, Moments.lean:92 identifies the normalized amplitude with pairings whose conjugates are the operator matrix entries. Call A_T/ν the normalized amplitude block and give its second-moment contribution as ‖A_T‖²/ν². Reserve the pairing identity for the full, uncut family satisfying HasAmplitudeBlocks. [Knowl, line 34](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/filling-amplitude.knowl.md#L34) · [Size.lean:71](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/Size.lean#L71)

<a name="page-finite-head-weight"></a>

## Weight of a head at the finite places

Added · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/finite-head-weight.knowl.md) · [BesselLevelStructure.lean:354](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselLevelStructure.lean#L354)

The initial products, the zero for nonintegral D even at K=0, and the reciprocal Haar factor agree with the definition. For i=0 the empty product is one.

<a name="new-finite-head-weight-1"></a>

**New finding · low · The parenthetical description leaves out defining semilocal-field conditions.** A locally compact ring with a volume-one compact open subring need not be a SemilocalField in the source. For example, a nonzero finite field with the discrete topology and normalized counting measure satisfies this description and has no topologically nilpotent unit. The cited class requires such an integral unit and a valuation-pair condition. Introduce just the features used by the formula with “write O for its volume-one compact open subring”, or include the other conditions when presenting the parenthesis as a definition. [Knowl, line 14](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/finite-head-weight.knowl.md#L14) · [LocalFactors.lean:348](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Adeles/LocalFactors.lean#L348)

<a name="page-flags-of-a-term-and-the-cell-rank"></a>

## Flags of a term and the cell rank

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/flags-of-a-term-and-the-cell-rank.knowl.md) · [TermStructure.lean:710](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/TermStructure.lean#L710)

The trailing-coordinate matching and norm identity place the shared vector in both isotropic spans. A vector supported below j contradicts the nonzero j-th minor, and the common-vector lemma then gives both disjointness assertions under the stated assumptions.

<a name="new-flags-of-a-term-and-the-cell-rank-1"></a>

**New finding · low · The cell-rank summary omits the field hypothesis in item 2.** The summary presents the direct decompositions and j + dim I = ϱ for every agreeing term of discriminant zero. Item 2 and the named TermStructure results assume a primitive 5040-th root of unity in E. Item 1 alone gives ordinary sums. Qualify the summary of the direct decompositions and rank identity with the field hypothesis used in item 2. [Knowl, line 5](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/flags-of-a-term-and-the-cell-rank.knowl.md#L5) · [TermStructure.lean:710](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/TermStructure.lean#L710)

<a name="page-frame-complement-and-linked-subspace"></a>

## The frame complement modulo the common isotropic space is the linked subspace

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/frame-complement-and-linked-subspace.knowl.md) · [TermStructure.lean:216](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/TermStructure.lean#L216)

The link relation kills both auxiliary coordinates on the frame complement, and surjectivity lifts every vector in the linked subspace. The kernel and the radical of the frame sum both equal Iγ.

<a name="new-frame-complement-and-linked-subspace-1"></a>

**New finding · low · The isometry is induced on the quotient.** The summary calls the projection from the entire complement an isometry. It preserves the Hermitian form but has kernel Iγ. For γ = 1 that kernel is the whole positive-dimensional isotropic span A. The title and numbered theorem give the correct quotient interpretation. Describe the projection as form-preserving and surjective, and say that it induces an isometry after quotienting by Iγ. [Knowl, line 5](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/frame-complement-and-linked-subspace.knowl.md#L5) · [TermStructure.lean:245](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/TermStructure.lean#L245)

<a name="page-hilbert-schmidt-norms-of-the-blocks"></a>

## Hilbert–Schmidt norms of the translated Gram operators

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/hilbert-schmidt-norms-of-the-blocks.knowl.md) · [Moments.lean:137](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Moments.lean#L137)

The scalar normalization, subtraction of the Bessel-subgroup contribution, and squared Hilbert–Schmidt identities all agree. Absolute squares make the result insensitive to a conjugation omitted when the proof names matrix entries.

<a name="new-hilbert-schmidt-norms-of-the-blocks-1"></a>

**New finding · medium · Distinguish the two basis pairings from the operator matrix entries.** The proof calls ⟨P_s e_y,e_x⟩ and ⟨rψ(s)e_y,e_x⟩ the row-x, column-y entries. With the conjugate-first inner product these pairings are the conjugates of the entries. Part (3) therefore describes the matrix of rψ(s) differently from its explicit defining matrix. The resulting squared norms still agree. Give the two entries as the conjugates of A/ν and A_S/ν, respectively, or compute directly with the displayed pairings and explain that taking absolute squares permits this. [Knowl, line 24](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/hilbert-schmidt-norms-of-the-blocks.knowl.md#L24) · [Moments.lean:162](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Moments.lean#L162)

<a name="page-isotropic-complement-maps-onto-positive-space"></a>

## The isotropic complement modulo the common isotropic space is the positive space

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/isotropic-complement-maps-onto-positive-space.knowl.md) · [Link.lean:727](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Link.lean#L727)

The vanishing of both middle projections on the orthogonal complement identifies the kernel with A ∩ γA. Surjectivity follows since every link pair lifts to the complement and its source ranges over P.

<a name="new-isotropic-complement-maps-onto-positive-space-1"></a>

**New finding · low · Specify the structure preserved by the quotient identification.** The title identifies the quotient with a named positive Hermitian space. The proof gives an E-linear isomorphism. For γ = 1 the class of z_N has value −N in A⊥/A, but its image z⁺ has value N in P. Say in the title or summary that the quotient is E-linearly isomorphic to P, and qualify the isomorphism in the last sentence of the theorem. [Knowl, line 3](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/isotropic-complement-maps-onto-positive-space.knowl.md#L3) · [Link.lean:727](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Link.lean#L727)

<a name="page-lattice-middle-form-is-unimodular"></a>

## The form in the lattice basis is unimodular

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/lattice-middle-form-is-unimodular.knowl.md) · [BesselLevelStructure.lean:368](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselLevelStructure.lean#L368)

The displayed two-by-two inverse multiplies to the identity, and the complementary block is the identity. These facts give integral inverses under the hypotheses in the body.

<a name="new-lattice-middle-form-is-unimodular-1"></a>

**New finding · low · The summary drops the star-fixity hypothesis on N.** Containing N in a subring suffices for integrality of the inverse but does not imply that the matrix is Hermitian. With A=R=ℤ\[i\] and N=i its last diagonal entry −i is not fixed by conjugation. The body includes the necessary hypothesis. Say “for N fixed by the involution, over every subring containing N”, or specialize the summary to the natural-number parameter of a filling datum. [Knowl, line 5](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/lattice-middle-form-is-unimodular.knowl.md#L5) · [BesselLevelStructure.lean:368](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselLevelStructure.lean#L368)

<a name="new-lattice-middle-form-is-unimodular-2"></a>

**New finding · low · Three indexed Lean declarations are absent from the page.** The front matter also assigns frameImage_one_mulVec, frameImage_mulVec and exists_star_vecMul_eq to this page. Neither the proof nor references explain the two frame identities or the representation of a prescribed row as v\*J. Source-based lookup therefore points three independent statements to a proof of the middle-block inverse. Move those names to pages giving their statements, or add a short separate paragraph stating the frame-coordinate formulas and the representation v=star(ℓJ⁻¹) for a prescribed row ℓ. [Knowl, line 10](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/lattice-middle-form-is-unimodular.knowl.md#L10) · [BesselLevelStructure.lean:397](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselLevelStructure.lean#L397)

<a name="page-link-is-graph-of-link-isometry"></a>

## The link is the graph of the link isometry

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/link-is-graph-of-link-isometry.knowl.md) · [Link.lean:735](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Link.lean#L735)

The converse graph implication uses a link pair with prescribed source, then both source and target determine the original middle pair. This also establishes the equivalence between equal subspaces and equal isometries.

<a name="new-link-is-graph-of-link-isometry-1"></a>

**New finding · low · State which coordinates turn the link into a graph.** The summary reads as a graph in the original pair (p₁,p₂). Lean tests Υ(src p) = tgt p, and src and tgt exchange the z-coordinates of p₁ and p₂. The raw pair need not satisfy Υ(p₁) = p₂ under the coordinate identification with P. Describe the link as the graph in (src p, tgt p) coordinates after exchanging the two z-coordinates. The displayed theorem already gives the right test. [Knowl, line 5](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/link-is-graph-of-link-isometry.knowl.md#L5) · [Link.lean:735](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Link.lean#L735)

<a name="page-link-isometry-on-the-moved-frame"></a>

## The link isometry on combinations of the moved frame

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/link-isometry-on-the-moved-frame.knowl.md) · [Link.lean:805](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Link.lean#L805)

The last frame product gives y_z = −c′/N and the preimage has last coefficient cρ. Comparing the two positive norms yields the stated factors N and N², and injectivity gives the frame-span criterion when c′ = 0.

<a name="new-link-isometry-on-the-moved-frame-1"></a>

**New finding · medium · Give the link isometry its positive-space input.** The summary applies Υ to the moved-frame combination y in V. The input in Lean is Πγ(y) = y₀ + cρ z⁺ in P. For γ = 1 and the combination y = e₀, the ambient vector is nonzero and its input to Υ is zero. State that Υ sends the positive-space projection y₀ + cρ z⁺ of the combination to −(c′/N)z⁺, as in part 1. [Knowl, line 5](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/link-isometry-on-the-moved-frame.knowl.md#L5) · [Link.lean:807](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Link.lean#L807)

<a name="page-near-term"></a>

## Near term

Added · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/near-term.knowl.md) · [Terms.lean:130](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Terms.lean#L130)

The boxed witness, the left action by the inverse of the archimedean image, and the Bessel-length threshold agree with the definitions of IsNear, boxedPoints and InCut.

<a name="new-near-term-1"></a>

**New finding · low · Qualify the chosen residue set for an arbitrary filling datum.** Nearness is defined for every filling datum. The source uses a choice of set and proves it is a residue domain under admissibility at Box.lean:145. The page assumes it is a residue domain even in the unrestricted definition, while the linked class-cutoff page explicitly records the fallback. Refer to the fixed set D used to define reduced points, and say that admissibility ensures D is a residue domain. [Knowl, line 14](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/near-term.knowl.md#L14) · [Box.lean:200](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/Box.lean#L200)

<a name="page-non-open-elements-carry-little"></a>

## Elements that are not open carry a small part of a positive type sum

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/non-open-elements-carry-little.knowl.md) · [MomentBounds.lean:399](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/MomentBounds.lean#L399)

The two stabilizer tests agree with the component action at w and its inverse adjoint at the conjugate place. The determinant sieve gives qˡ√(qʳ) ≤ b⁶ᵏ, and the union over l &lt. N gives the claimed b⁻⁴ bound, including the vacuous test for the empty minor.

<a name="new-non-open-elements-carry-little-1"></a>

**New finding · low · Extend the test vector to all frame coordinates.** The determinant-sieve vector v has l coordinates, with l &lt. N. A FrameVector at w has n coordinates. The stabilizer identity uses the vector v extended by zeros to the rest of the frame. This extension is injective, so the resulting vector is nonzero for each v under test. Write ṽ = (v,0,…,0) in the full frame and use (false,ṽ) and (true,ṽ) for the two stabilizers. The first l frame columns still send v to ev. [Knowl, line 35](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/non-open-elements-carry-little.knowl.md#L35) · [MomentBounds.lean:366](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/MomentBounds.lean#L366)

<a name="page-norm-identity-for-combinations-of-the-moved-frame"></a>

## Norm identity for combinations of the moved frame

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/norm-identity-for-combinations-of-the-moved-frame.knowl.md) · [Terms.lean:284](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Terms.lean#L284)

Evaluation against z gives −N t_z = D. Preservation of the form yields the independent term N²|Φ_v(y_ϱ)|² in the norm identity, and vanishing of the sum at one place kills every X₀-coordinate by injectivity.

<a name="new-norm-identity-for-combinations-of-the-moved-frame-1"></a>

**New finding · low · Distinguish the original frame coefficient in the norm summary.** “Its z-coefficient” reads as the ambient coordinate t_z of the moved vector, which is already determined by its product D with z. The squared X₀ length also depends on the input coefficient y_ϱ multiplying γz. The formula in the body makes the distinction correctly. Identify the two inputs as the product of the moved vector with z and the coefficient of γz in its moved-frame expansion. [Knowl, line 5](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/norm-identity-for-combinations-of-the-moved-frame.knowl.md#L5) · [Terms.lean:245](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Terms.lean#L245)

<a name="new-norm-identity-for-combinations-of-the-moved-frame-2"></a>

**New finding · low · Give the frame multiplication and cancellation lemmas an owner that states them.** The final three Lean declarations in the header concern multiplication of frame images, invariance under right multiplication by a frame-fixing unipotent and cancellation by an inverse. This page gives none of those statements. The packing-of-frames knowl cites the cancellation lemma, so resolving that citation by this header leads to a norm identity without the required result. Move the three names to the same-frame-image page, which uses the cancellation identity, and state the multiplication, right-invariance and cancellation identities there. [Knowl, line 10](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/norm-identity-for-combinations-of-the-moved-frame.knowl.md#L10) · [Terms.lean:167](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Terms.lean#L167)

<a name="page-positive-space-and-link-maps"></a>

## The positive space and the source and target maps of a link

Added · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/positive-space-and-link-maps.knowl.md) · [Link.lean:397](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Link.lean#L397)

The source takes its X₀ component from the first middle vector and its z component from the second. The target reverses the choices, making the pair recoverable, and positivity at an infinite place establishes anisotropy.

<a name="new-positive-space-and-link-maps-1"></a>

**New finding · low · Give the general definition of the registered isotropic span.** This definition page registers isotropicSpan in its Lean metadata. Its bullet gives A, A ∩ γA and (A + γA)⊥, but does not tell a reader what isotropicSpan M means for the arbitrary matrix M accepted in Lean. Introduce isotropicSpan M as the span of the columns M e_a for a &lt; ρ, then identify its specializations at 1 and γ with A and γA. [Knowl, line 25](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/positive-space-and-link-maps.knowl.md#L25) · [Link.lean:378](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Link.lean#L378)

<a name="page-positive-type-function-is-largest-at-the-identity"></a>

## A function of positive type is largest at the identity

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/positive-type-function-is-largest-at-the-identity.knowl.md) · [SquareExpansion.lean:75](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/SquareExpansion.lean#L75)

The theorem and proof use the full Gram identity, giving the common squared norm β(1) even when β(1) = 0. No finiteness assumption on the group is needed.

<a name="new-positive-type-function-is-largest-at-the-identity-1"></a>

**New finding · low · State the translation-invariance condition on the Gram matrix.** Being given by inner products of group-indexed vectors alone does not imply the bound. For G = {1,s}, u₁ = 1 and uₛ = 2 in ℂ, the coefficient β(g) = ⟨u₁,u_g⟩ has β(s) = 2 &gt; 1 = β(1). Line 15 has the condition the summary omits. Say that the Gram entries satisfy ⟨uₐ,u_b⟩ = β(a⁻¹b) for every a,b. [Knowl, line 5](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/positive-type-function-is-largest-at-the-identity.knowl.md#L5) · [SquareExpansion.lean:77](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/SquareExpansion.lean#L77)

<a name="new-positive-type-function-is-largest-at-the-identity-2"></a>

**New finding · low · Remove or document the unrelated subgroup-sum declaration.** New.sum_subgroup_filter is a separate equality reindexing a finite sum over a subgroup as a filtered sum over the ambient group. It appears only in the front matter and plays no part in the statement or the Cauchy–Schwarz proof, so a declaration lookup points to a page that never states it. Move the declaration mapping to a knowl explaining the subgroup-sum step in MomentBounds.lean (lines 496 and 505), or add its actual identity as a separate item. [Knowl, line 10](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/positive-type-function-is-largest-at-the-identity.knowl.md#L10) · [SquareExpansion.lean:87](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/SquareExpansion.lean#L87)

<a name="page-principal-level-is-congruence-subgroup"></a>

## The principal level is the congruence subgroup modulo M

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/principal-level-is-congruence-subgroup.knowl.md) · [BesselLevelStructure.lean:633](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselLevelStructure.lean#L633)

The two reductions, modulo a chosen place and its conjugate, suffice to detect divisibility by M. The displayed conjugate-reduction formula and the final principal-level criterion agree with Lean.

<a name="new-principal-level-is-congruence-subgroup-1"></a>

**New finding · medium · Transposing the isometry relation introduces an extra transpose on k.** From k\*J=Jk⁻¹ and Jᵀ=J, the left side after transposition is J(k\*)ᵀ=J conjugate(k). The intermediate displayed identity instead writes J times the transpose of the overbar of k and identifies that with entrywise conjugation. For a nonsymmetric matrix the extra transpose changes the entries at the chosen place. Use J_w·(((k\*)ᵀ) mod w)=((k⁻¹)ᵀ mod w)·J_w and explicitly set (k\*)ᵀ=conjugate(k). Keep the subscripted reduced matrix distinct from this conjugation. [Knowl, line 29](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/principal-level-is-congruence-subgroup.knowl.md#L29) · [BesselLevelStructure.lean:550](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselLevelStructure.lean#L550)

<a name="page-remaining-terms"></a>

## Remaining terms

Added · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/remaining-terms.knowl.md) · [TermStructure.lean:830](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/TermStructure.lean#L830)

The union correctly includes every nonzero-discriminant isometry, regardless of character agreement. The remark needs the stable-set and arithmetic assumptions of the vanishing result it cites.

<a name="new-remaining-terms-1"></a>

**New finding · medium · Character disagreement gives vanishing for a stable sum.** The remark suggests that each disagreeing term contributes zero and has been removed. The cited theorem gives zero for the amplitude sum over a bi-unipotent-stable set consisting entirely of disagreeing terms, for an admissible filling over a field with a primitive 5040-th root. In the off-Bessel comparison only the disagreeing subset outside Γ\* is discarded this way; Γ\* retains every nonzero-discriminant element. State that the sum over that stable disagreeing subset vanishes under the two arithmetic hypotheses, and distinguish it from the nonzero-discriminant branch of Γ\*. [Knowl, line 22](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/remaining-terms.knowl.md#L22) · [Climbing.lean:584](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Climbing.lean#L584)

<a name="page-remaining-terms-stable-and-complement"></a>

## The remaining terms are stable, and their complement among agreeing terms

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/remaining-terms-stable-and-complement.knowl.md) · [TermStructure.lean:843](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/TermStructure.lean#L843)

Bi-unipotent stability follows from invariance of discriminant, agreement and the dimension of the common span. At rank zero the flags vanish, while the converse uses the separately stated field hypothesis.

<a name="new-remaining-terms-stable-and-complement-1"></a>

**New finding · low · The summary omits the field hypothesis on the converse.** The summary asserts that every agreeing term outside Γ\* has a norm-one pair from index zero. The source theorem and item 4 assume E contains a primitive 5040-th root. Stability and the forward implication have no such assumption. Add the field qualifier specifically to the converse in the summary. [Knowl, line 5](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/remaining-terms-stable-and-complement.knowl.md#L5) · [TermStructure.lean:885](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/TermStructure.lean#L885)

<a name="page-second-moment-near-the-bessel-subgroup"></a>

## The second moment near the Bessel subgroup

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/second-moment-near-the-bessel-subgroup.knowl.md) · [SquareExpansion.lean:644](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/SquareExpansion.lean#L644)

The prime comparison, positive meet bound, admissibility estimate, and squaring justify b⁻¹² for the amplitude second moment. The operator interpretation needs the missing normalization below.

<a name="new-second-moment-near-the-bessel-subgroup-1"></a>

**New finding · medium · Divide both operator blocks by the unipotent covolume.** The remark identifies Pₛ with the conjugated raw amplitude sum. Its block is the conjugate of A_all/ν, and the corresponding block of rψ(s) is the conjugate of A_Bessel/ν. Using the raw blocks makes the squared Hilbert–Schmidt sum ν² times the second moment defined earlier. Write (Pₛ)ₓᵧ = conjugate(A_all(c,s,c′)ᵢⱼ/ν) and give the same denominator for rψ(s). [Knowl, line 42](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/second-moment-near-the-bessel-subgroup.knowl.md#L42) · [Moments.lean:419](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Moments.lean#L419)

<a name="page-second-moment-off-the-reduced-bessel-group"></a>

## Second moments over residues outside the reduced Bessel group

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/second-moment-off-the-reduced-bessel-group.knowl.md) · [MomentBounds.lean:75](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/MomentBounds.lean#L75)

The singleton formula exchanges finite sums over classes and residues. Splitting the amplitude by the rational Bessel subgroup gives identical full and complementary blocks outside its reduced image before squaring.

<a name="new-second-moment-off-the-reduced-bessel-group-1"></a>

**New finding · low · Identify the covolume in the second-moment formula.** The normalization is written ν⁻² at the first occurrence of the formula, but this page does not identify ν. The source identifies it with the positive unipotent covolume, which is already tabulated in this chapter under the notation cov_U. Set ν equal to the unipotent covolume and link the filling-constants page at this formula. [Knowl, line 15](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/second-moment-off-the-reduced-bessel-group.knowl.md#L15) · [Size.lean:71](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/RemainingTerms/Size.lean#L71)

<a name="page-second-moment-over-a-full-fixer"></a>

## The second moment over residues fixing a vector at every place above the first level prime

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/second-moment-over-a-full-fixer.knowl.md) · [MomentBounds.lean:202](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/MomentBounds.lean#L202)

The f labeled places (w,εw) are distinct even if the conjugate choice varies. Their contribution gives meetNorm ≥ p₀ᶠ, and the one-link bound and expansion yield the stated T/2 estimate outside all scalar cosets.

<a name="new-second-moment-over-a-full-fixer-1"></a>

**New finding · medium · Fix the vector family before summing over residues.** The summary can be read as summing all residues for which there exists some nonzero fixed vector at each place. The theorem fixes one family d first and sums over its common stabilizer. Taking the union over all d can enlarge the sum, and the proof gives no estimate for that union. The body has the correct order. State that for any prescribed family of nonzero frame vectors, one above each chosen place, the bound holds for the residues fixing that family. [Knowl, line 5](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/second-moment-over-a-full-fixer.knowl.md#L5) · [MomentBounds.lean:203](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/MomentBounds.lean#L203)

<a name="page-second-moment-over-open-elements-of-a-fixer"></a>

## The second moment over the open elements of a fixer

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/second-moment-over-open-elements-of-a-fixer.knowl.md) · [MomentBounds.lean:264](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/MomentBounds.lean#L264)

The main term bounds the unnormalized link sum by (1 + b⁻⁴)Tν² for the cut side on nonzero discriminants. The square-root expansion restores the full-side moment and gives the claimed (1 + 4b⁻⁴)T.

<a name="new-second-moment-over-open-elements-of-a-fixer-1"></a>

**New finding · low · Use the unconditional numerical part of the full-fixer bound.** The referenced page places its numerical “moreover” clause after the extra assumption β(s) ≤ 2 dim_S for all s. The open-fixer lemma has no such assumption. Lean uses a separate numerical lemma requiring only admissibility and |Q| ≤ f. Cite that numerical lemma explicitly, or deduce b^(5kf) M_id ≤ T directly from b^(11kf) M_id ≤ M_main and |Q| ≤ f. The linked full-fixer page can state this consequence before its pointwise hypothesis. [Knowl, line 22](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/second-moment-over-open-elements-of-a-fixer.knowl.md#L22) · [MomentBounds.lean:113](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/MomentBounds.lean#L113)

<a name="page-second-moment-over-the-whole-group"></a>

## The second moment over the whole residue group

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/second-moment-over-the-whole-group.knowl.md) · [MomentBounds.lean:441](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/MomentBounds.lean#L441)

Maximizing over all vector families and subsets gives the stabilizer fraction F⁻¹ by changing one unused coordinate, and (1−x)(1+9x)−(1+4x) = x(4−9x) completes the absorption. A maximizing family exists because every residue field admits a nonzero vector in the nonempty frame.

<a name="new-second-moment-over-the-whole-group-1"></a>

**New finding · low · Use unitarity in the positive-type realization.** The operator remark attributes positive type to a matrix coefficient on Hilbert–Schmidt operators. The cited application uses a unitary representation ρ and a diagonal coefficient. An arbitrary involution whose matrix has rows (1, 1) and (0, −1) and P equal to the identity gives squared Hilbert–Schmidt norm 3 at the involution and 2 at the identity, which violates the positive-type bound. Specify that ρ is unitary and use the vectors Tₐ = ρ(a)PP\*ρ(a)\*. Their Hilbert–Schmidt Gram matrix equals β(a⁻¹b). [Knowl, line 45](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/second-moment-over-the-whole-group.knowl.md#L45) · [Moments.lean:567](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Moments.lean#L567)

<a name="page-second-moments-of-the-poincare-operators"></a>

## Second moments of the operators P\* s P

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/second-moments-of-the-poincare-operators.knowl.md) · [Moments.lean:567](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Moments.lean#L567)

The three inequalities and constants agree after indexing Ω by the prime on which elements agree. The positive-type argument uses unitarity of ρ, as the formal statement and the body explicitly require.

<a name="new-second-moments-of-the-poincare-operators-1"></a>

**New finding · low · Include the additional assumptions for the global moment estimate in the summary.** The summary presents the global (1+9b⁻⁴) estimate for any pair with amplitude blocks. The source assumes Weil data and unitarity of ρ. In particular the positive-type Gram computation uses unitarity. Part 3 gives these assumptions correctly. State that the global sum bound holds with Weil data and unitary ρ, or omit that estimate from the short summary. [Knowl, line 5](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/second-moments-of-the-poincare-operators.knowl.md#L5) · [Moments.lean:567](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Moments.lean#L567)

<a name="page-spaces-of-the-two-frames"></a>

## Spaces attached to the two frames of a term

Added · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/spaces-of-the-two-frames.knowl.md) · [TermStructure.lean:82](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/TermStructure.lean#L82)

Both frame orthogonality tests use the same isotropic complement, with vanishing auxiliary coordinates of y and γ⁻¹y. The linked-space test and the rank claim for the two invertible matrices used here agree with the source.

<a name="new-spaces-of-the-two-frames-1"></a>

**New finding · low · The flag definition also applies to singular matrices.** The definition page introduces the flag only for invertible M. The owned definition flagSpan, its membership test and the zero flag accept every matrix. For instance M = 0 and j &gt; 0 gives a well-defined zero flag, where the dimension assertion would fail. Define the span for every M, then state the dimension j for invertible M, including the two cases used here. [Knowl, line 17](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/spaces-of-the-two-frames.knowl.md#L17) · [TermStructure.lean:492](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/TermStructure.lean#L492)

<a name="page-square-sum-of-the-induced-character"></a>

## The conjugation mean of the unipotent character has square sum at most two

Added · outline · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/square-sum-of-the-induced-character.knowl.md) · [Moments.lean:991](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Moments.lean#L991)

The theorem uses the unnormalized square sum of the normalized conjugation mean, with bound 2. The averaging, disjoint-coset and rank arguments match, but the outline leaves out two inputs used at the local character comparison and the factor of two.

<a name="new-square-sum-of-the-induced-character-1"></a>

**New finding · medium · Cite the independent volume lower bound that yields the constant two.** The cited mass estimate reaches μ(K_T)μ(K_T(M))(μ(K_T)+2⁻ⁿ). The next inequality requires μ(K_T) ≥ 2⁻ⁿ for the filling datum’s specific Haar measure. Lean obtains this from Frames/FiniteDepth.lean:63 using the estimate on nonunits in Frames/FixedLines.lean:105. Without that input the resulting square-sum bound after cancellation is 1+2⁻ⁿ/μ(K_T), not 2. After the mass estimate, explicitly invoke the lower bound for the local integral group and its condition that T consists of chosen places and their conjugates. In passing to step 5, one may also state that the compact open congruence subgroup has positive finite measure. [Knowl, line 27](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/square-sum-of-the-induced-character.knowl.md#L27) · [Moments.lean:952](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Moments.lean#L952)

<a name="new-square-sum-of-the-induced-character-2"></a>

**New finding · low · Identify the additive character used to compare the local and reduced values.** The proof introduces ψ in the definition of χ_M and then concludes its value on a global unipotent lift is ψ_U(k). Reduction and lifting determine the support and coset, but equality of the two character values also uses the filling datum’s compatibility with the global character, invoked in Moments.lean:808. Identify ψ as the local character of the filling datum and cite IsFillingData.psi_simpleRootSum_eq_unipotentChar for ψ(σ(k_T)/M) = ψ_U(k) on the integral lift. [Knowl, line 25](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/square-sum-of-the-induced-character.knowl.md#L25) · [GlobalToLocal.lean:534](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/GlobalToLocal.lean#L534)

<a name="page-vanishing-of-the-term-discriminant"></a>

## The discriminant vanishes exactly when the two frames share a vector

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/vanishing-of-the-term-discriminant.knowl.md) · [Link.lean:929](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Link.lean#L929)

For singular Z a nonzero kernel vector produces a shared frame combination. When Z is invertible, the last adjugate column has last entry Dρ, and any shared combination has coefficient vector proportional to that column, giving the converse to the norm test.

<a name="new-vanishing-of-the-term-discriminant-1"></a>

**New finding · low · Name the intersection of the frame spans in the title.** Sharing a listed frame vector is stronger than having a nonzero intersection of the spans. For γ = −I the two frames f and −f have no vector in common as lists over the CM field, but their spans agree and the discriminant vanishes. Use “The discriminant vanishes exactly when the frame spans meet nontrivially.” The existing summary and theorem already specify the intersection. [Knowl, line 3](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/vanishing-of-the-term-discriminant.knowl.md#L3) · [Link.lean:929](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Link.lean#L929)

<a name="page-bessel-function-under-unipotent-translation"></a>

## Transformation of the Bessel function under rational unipotent elements

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/bessel-function-under-unipotent-translation.knowl.md) · [BesselLevelStructure.lean:308](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselLevelStructure.lean#L308)

The rescaled archimedean components stay block unitriangular. Multiplying the local transformation laws gives the same scalar on every full or cut coordinate, and the rational specialization is the inverse of the finite character.

<a name="page-bounds-for-near-terms"></a>

## Bounds for the frame products of near terms

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/bounds-for-near-terms.knowl.md) · [Terms.lean:541](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Terms.lean#L541)

The box estimate and the change of frame give 60n + 2·37n = 134n. Bounding the determinant by l! terms gives 2(l+134nl) ≤ 270n² for every l ≤ n, including the empty minor.

<a name="page-box-partition-of-unity"></a>

## Box partition of unity for a class

Existing chapter knowl · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/box-partition-of-unity.knowl.md) · [Setup.lean:434](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Setup.lean#L434)

The support bound is the local radius b²⁷ times the Bessel length. The orbit identity permits any nonnegative weight summing to one on each right coset of the frame fixer, and the stated invariance has the same left action as Lean.

<a name="page-characters-agree"></a>

## Terms whose unipotent characters agree

Added · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/characters-agree.knowl.md) · [Terms.lean:135](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Terms.lean#L135)

Writing u′ = γ⁻¹uγ in the intertwining equation gives precisely the stated intersection of the two rational unipotent groups. The comparison is of the finite character after embedding those two elements.

<a name="page-class-basis"></a>

## Basis of the lattice of a class

Added · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/class-basis.knowl.md) · [BesselLevelStructure.lean:158](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselLevelStructure.lean#L158)

Both expressions for the matrix of the class basis, B_c=ĝ_c B=B h_c, give exactly the stated B_c⁻¹γB_d. Requiring the matrix and its inverse to be integral matches the translated stabilizer.

<a name="page-class-coordinates"></a>

## Coordinates of the lattice of a class

Added · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/class-coordinates.knowl.md) · [Terms.lean:94](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Terms.lean#L94)

The class coordinate matrix is the inverse of the finite-adelic class basis. The written X₀-coordinate formula has the middle inclusion on the left of the inverse representative, and the congruence of Gram matrices has the same orientation as the source.

<a name="page-class-cutoff"></a>

## Class cutoff and reduced points

Revised · construction · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/class-cutoff.knowl.md) · [Setup.lean:648](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Setup.lean#L648)

The product separates the class-specific cutoff for the frame fixer from the shared reduced indicator. The ratio of the two basis scales in each upper triangular coordinate agrees with ratTriangle. The two choices occur before any admissibility assumption.

<a name="prior-class-cutoff-1"></a>

**Partly addressed · medium · State the hypotheses for the full-group cutoff.** The new reference names the actual orbit-sum theorem. Its two assumptions, a primitive 5040th root of unity in E and admissibility of S, are still missing from the remark. The selected residue domain alone does not supply the box partition used in the proof. [Knowl, line 31](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/class-cutoff.knowl.md#L31) · [Packing.lean:134](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Packing.lean#L134)

<a name="page-class-unipotent-discrete"></a>

## Discreteness of the class unipotent groups and existence of cutoffs

Existing chapter knowl · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/class-unipotent-discrete.knowl.md) · [Setup.lean:569](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Setup.lean#L569)

The compact-set argument bounds each rational matrix entry simultaneously at the finite and infinite places. For the full family of complex matrices the target is locally compact, and injectivity of the rational embedding lets the cutoff sum be transported from the discrete image.

<a name="page-common-link-by-link-isometries"></a>

## The common link in terms of link isometries

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/common-link-by-link-isometries.knowl.md) · [TermStructure.lean:311](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/TermStructure.lean#L311)

The source/target identification interchanges the two auxiliary coordinates. Requiring both to vanish identifies the common link with the restricted intersection of the graphs, and the dimension inequality follows inside the first graph of dimension κ+1.

<a name="page-discriminant-and-link-on-the-big-cell"></a>

## Discriminant and link on the big cell

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/discriminant-and-link-on-the-big-cell.knowl.md) · [Link.lean:277](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Link.lean#L277)

The formulas at BigCell.lean:48 and :64 give p₁ = σ_mid p₂, Dρ = d and Dρ₊₁ = dt, hence the discriminant d d̄(t t̄ − N²) including the empty product at ρ = 0. The equality test for two links recovers exactly the equality of the middle blocks.

<a name="page-eichler-map-in-bessel-unipotent-group"></a>

## Eichler maps in the Bessel unipotent group

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/eichler-map-in-bessel-unipotent-group.knowl.md) · [BesselLevelStructure.lean:411](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselLevelStructure.lean#L411)

Expanding the two rank-one corrections gives the stated root sum, including the final column z. The same support argument removes the entries on and below the block diagonal and covers both endpoints of the cut.

<a name="page-equivariance-of-maps-with-amplitude-blocks"></a>

## Equivariance of maps with amplitude blocks under the reduced Bessel group

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/equivariance-of-maps-with-amplitude-blocks.knowl.md) · [Moments.lean:298](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Moments.lean#L298)

Following the term over (d,t⁻¹,d′) gives N_jk in rψ(t)e_(d,j) and its conjugate in the first argument of the pairing. The proof uses unitarity of ρ for intertwining and for left equivariance, matching the source.

<a name="page-filling-admissible"></a>

## Admissible filling datum (standing hypotheses)

Revised · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/filling-admissible.knowl.md) · [Setup.lean:501](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Setup.lean#L501)

The nine numbered conditions reproduce the eleven Lean fields by grouping related conditions. The two index inequalities have the correct direction, including the convention that infinite relative index is zero.

<a name="prior-filling-admissible-1"></a>

**Partly addressed · low · Condition 6 also involves the rank-r mass and the local degrees.** The new Lean link resolves uniquely to unfolding A’s scaled-siegel-constant-bound. Condition 6 also compares the rank-r mass with the local degrees: its ratio has degree × mass_r × unipotentOrder in the denominator. Describe condition 9 specifically as the scaled Siegel bound involving the covolume and open-cell factors. [Knowl, line 35](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/filling-admissible.knowl.md#L35) · [FillingAdmissible.lean:604](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/FillingAdmissible.lean#L604)

<a name="page-filling-classes-and-terms"></a>

## Classes, terms over a block, and the unipotent groups of a class

Revised · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/filling-classes-and-terms.knowl.md) · [Setup.lean:382](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Setup.lean#L382)

The classes are double cosets for the level on the definite group. A rational term requires both membership of the conjugated finite component in the integral stabilizer and its specified residue. The signs in the frame discriminant agree with frameDisc.

<a name="page-filling-constants"></a>

## Constants of a filling datum

Revised · notation · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/filling-constants.knowl.md) · [Setup.lean:260](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Setup.lean#L260)

The frame product, unipotent exponent, Siegel normalization and main and identity second moments agree with the definitions. Positivity of the explicit unipotent constant holds for arbitrary filling data.

<a name="prior-filling-constants-1"></a>

**Partly addressed · medium · Qualify the interpretation as a covolume.** The replacement reference now names the correct integral theorem. Its geometric interpretation still needs admissibility, a primitive 5040th root in E, and the product of the specified Bessel Haar measures for the unipotent integral. [Knowl, line 35](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/filling-constants.knowl.md#L35) · [CutoffIntegral.lean:728](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/CutoffIntegral.lean#L728)

<a name="page-filling-data"></a>

## Filling data

Revised · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/filling-data.knowl.md) · [Setup.lean:58](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Setup.lean#L58)

The size conditions, ordered pair of level primes, and product indexing the Bessel coordinates agree with the structure. The replacement of the broken final link by New.Data.filling has the unique owner spanning-core/filling-data-of-admissible-data.

<a name="prior-filling-data-1"></a>

**Still open · high · The lattice change of basis does not exist over every ring.** The universal lattice matrix has distinguished block ((0,−1),(−1,−N)). In characteristic N this block is nonsingular while the rational middle form is singular. Give the integral matrix over general rings, and state the displayed basis change over the finite adèles, where π and N are units. [Knowl, line 51](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/filling-data.knowl.md#L51) · [Basic.lean:599](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/Basic.lean#L599)

<a name="page-filling-level-and-reduction"></a>

## Lattice stabiliser, reduction and principal level of a filling datum

Revised · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/filling-level-and-reduction.knowl.md) · [Setup.lean:211](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Setup.lean#L211)

The principal level is the kernel inside the lattice stabilizer embedded back into the full finite group. The reduced image of a subgroup correctly takes its intersection with the stabilizer before applying simultaneous reduction.

<a name="page-filling-unitary-groups"></a>

## Unitary groups of a filling datum and the maps between them

Revised · construction · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/filling-unitary-groups.knowl.md) · [Setup.lean:333](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Setup.lean#L333)

The finite change of coordinates is conjugation by the inverse lattice basis on the left. At an infinite place the displayed diagonal scales give the stated Gram identity, and the newly indexed basisScale_ne_zero is proved in Setup.

<a name="prior-filling-unitary-groups-1"></a>

**Still open · medium · A ring map of unitary groups must respect the involutions.** The final sentence still asserts functoriality for arbitrary ring maps. Preserving the entries of J suffices for the Gram matrix, but an induced map on unitary groups also requires compatibility with the involutions. An identity ring map from complex conjugation to trivial involution already fails on a diagonal coordinate i. [Knowl, line 47](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/filling-unitary-groups.knowl.md#L47) · [CongruenceSubgroups.lean:351](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Groups/CongruenceSubgroups.lean#L351)

<a name="page-frame-products-at-infinity"></a>

## Frame products of a rational term at the infinite places

Existing chapter knowl · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/frame-products-at-infinity.knowl.md) · [Setup.lean:707](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Setup.lean#L707)

The displayed minor identity applies to any finite indexing map, including repetitions and the empty family. Pulling out one scale from each row and column gives precisely one factor of 1/N per index.

<a name="prior-frame-products-at-infinity-1"></a>

**Still open · low · Group the denominator inside the product in the proof.** The theorem statement groups the factors correctly. The proof still places a single unparenthesized /N after the product. Write N^(−|m|) times the product of the powers of κ to display the denominator contributed by every row. [Knowl, line 28](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/frame-products-at-infinity.knowl.md#L28) · [Setup.lean:710](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Setup.lean#L710)

<a name="page-frame-products-of-terms-are-integral"></a>

## Frame products of terms are algebraic integers

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/frame-products-of-terms-are-integral.knowl.md) · [Terms.lean:618](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Terms.lean#L618)

The base change alters the distinguished X₀ basis vector and fixes each frame column. This gives C_c F = F and its adjoint identity, so integrality of the lattice Gram and of the translated term proves integrality of every rational frame product.

<a name="page-freeness-in-small-rank"></a>

## Freeness of the level in rank at most k

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/freeness-in-small-rank.knowl.md) · [BesselLevelStructure.lean:925](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselLevelStructure.lean#L925)

The strict norm-product inequality follows from the two factors in \[E:ℚ\]=2f and k⁴&lt;k¹⁰≤pᵢ. The primitive root supplies the auxiliary nontriviality of the infinite-place set used by the cited freeness criterion.

<a name="page-good-forms-near-isometry"></a>

## Good forms: the projected map is nearly an isometry

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/good-forms-near-isometry.knowl.md) · [Moments.lean:1230](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Moments.lean#L1230)

The one-prime trace and remainder estimates give 2b⁻⁴D_X. The two commuting factors lose at most 4b⁻⁴D_X, which combines with the initial b⁻⁴ loss to give the stated additive error for every subspace.

<a name="page-link-and-cells-are-invariant-under-the-unipotent-group"></a>

## Links, discriminants and cells are invariant under the Bessel unipotent group

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/link-and-cells-are-invariant-under-the-unipotent-group.knowl.md) · [Link.lean:254](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Link.lean#L254)

The bijection of witnesses preserves the two middle blocks on the zero-dual-block locus. The three cell conditions are separately invariant: occurrence by inversion and left multiplication, the indexed leading minor by FloorGroups.lean:702, and the discriminant by its last two minors.

<a name="page-link-in-coordinates"></a>

## The link of an isometry in coordinates

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/link-in-coordinates.knowl.md) · [Link.lean:104](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Link.lean#L104)

The kernel condition gives vanishing dual coordinates for both t and γ⁻¹t. In the reverse direction t = γ(a,p₂,0) has middle block p₁ and zero dual block, so it is an admissible witness over the stated commutative ring.

<a name="page-link-is-its-own-orthogonal-complement"></a>

## The link is its own orthogonal complement

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/link-is-its-own-orthogonal-complement.knowl.md) · [Link.lean:778](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Link.lean#L778)

The difference of the two middle-form pairings becomes the difference of the two positive pairings after the z-coordinates are crossed. Surjectivity of the target gives a test vector realizing the discrepancy, whose positive norm must vanish, proving the reverse inclusion.

<a name="page-link-isometry"></a>

## Link isometry

Added · construction · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/link-isometry.knowl.md) · [Link.lean:658](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Link.lean#L658)

The link isometry is tgt composed with the inverse of src restricted to the link. Bijectivity of both maps justifies the unique choice of a link pair for each source and ensures that the resulting linear equivalence is invertible.

<a name="page-norm-one-pairs-at-infinite-places"></a>

## Norm-one pairs pass to the infinite places

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/norm-one-pairs-at-infinite-places.knowl.md) · [Terms.lean:397](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Terms.lean#L397)

The local coefficient multiplier is the scale at the leading frame index divided by the scale at each coordinate. It preserves the leading pair and vanishing above it under the archimedean diagonal conjugation.

<a name="page-norm-one-pairs-under-inversion-and-unipotent-multiplication"></a>

## Norm-one pairs under inversion and unipotent multiplication

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/norm-one-pairs-under-inversion-and-unipotent-multiplication.knowl.md) · [Link.lean:144](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Link.lean#L144)

Inversion exchanges the two coefficient vectors and uses the conjugate norm-one scalar. The upper-unitriangular change from WittTheorem.lean:598 fixes the last specified coefficient, and the descending construction has a vacuous initial condition at j = ρ + 1.

<a name="page-rank-of-the-link"></a>

## The link has rank k + 1

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/rank-of-the-link.knowl.md) · [Link.lean:616](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Link.lean#L616)

With d = dim(A ∩ γA), the span A + γA has dimension 2ρ − d and the kernel of the map from its perpendicular to the link has dimension d, yielding dim L = r − 2ρ = k + 1. Equality of the two pullbacks of the positive form and anisotropy give injectivity of both maps, hence bijectivity.

<a name="page-rank-of-the-linked-subspace"></a>

## Rank of the linked subspace

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/rank-of-the-linked-subspace.knowl.md) · [TermStructure.lean:466](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/TermStructure.lean#L466)

The two frames are disjoint for nonzero discriminant, yielding dim X₀^γ + 1 = κ. In the zero-discriminant cell the norm-one pair forces the second auxiliary coordinate to vanish along the link, giving X₀^γ = X₀.

<a name="page-rational-unipotent-terms-reach-all-reductions"></a>

## Rational unipotent terms reach every reduction of the unipotent group

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/rational-unipotent-terms-reach-all-reductions.knowl.md) · [BesselLevelStructure.lean:878](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselLevelStructure.lean#L878)

Taking x=h_c u h_c⁻¹ and y=h_c in strong approximation yields u⁻¹h_c⁻¹(u₀)_fin h_c on the required side of the coset. The two directions of the assertion about residues then follow with the same class at either end.

<a name="page-real-gram-discriminant-of-a-term"></a>

## The real Gram discriminant of a rational term

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/real-gram-discriminant-of-a-term.knowl.md) · [Terms.lean:352](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Terms.lean#L352)

The last squared frame scale is 1/N, so the product for the penultimate minor is N times the full product. After squaring, this gives the required N² on the rational minor and the stated square of the full scale.

<a name="page-reduced-unipotent-character"></a>

## The unipotent character on the residue group and its conjugation mean

Added · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/reduced-unipotent-character.knowl.md) · [Moments.lean:728](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Moments.lean#L728)

The chosen lift, zero extension and conjugating average match the definitions. Equality on level cosets makes the choice independent and right translation of the averaging variable proves class invariance.

<a name="page-remainder-against-a-central-idempotent"></a>

## The remainder against a central idempotent of one factor

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/remainder-against-a-central-idempotent.knowl.md) · [Moments.lean:607](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Moments.lean#L607)

The opposite-prime support condition ensures sφ_i(t) stays in Ω for s in the reduced Bessel group. Inverting the variable correctly turns the source’s convolution contraction into the right-convolution bound, yielding b⁻¹²D_X.

<a name="page-residues-near-the-reduced-bessel-group"></a>

## Residues that agree with the reduced Bessel group above one level prime

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/residues-near-the-reduced-bessel-group.knowl.md) · [SquareExpansion.lean:612](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/SquareExpansion.lean#L612)

The fixed first frame vector gives both the vanishing minors and a meeting vector at each chosen place and its conjugate, supplying pᵢ^(2f). The scalar comparison uses the global norm-one condition and the rank-one freeness result with the stated hypotheses.

<a name="page-scalar-isometry"></a>

## Scalar isometry

Added · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/scalar-isometry.knowl.md) · [SquareExpansion.lean:39](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/SquareExpansion.lean#L39)

The inverse and action on another isometry are ζ̄I and ζ̄g. The computation over a commutative ring with involution works for the stated arbitrary square matrix J.

<a name="page-second-moment-over-the-scalar-cosets"></a>

## The scalar cosets carry a small part of the second moment

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/second-moment-over-the-scalar-cosets.knowl.md) · [MomentBounds.lean:151](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/MomentBounds.lean#L151)

The scalar count uses residue tuples at both sets of f chosen places, giving p₀ᶠp₁ᶠ = Mᶠ possibilities. The proof only needs an upper bound on this count, so multiple descriptions of the same residue do not inflate its contribution.

<a name="page-self-duality-of-integral-adeles"></a>

## Self-duality of the integral adeles for the self-dual character

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/self-duality-of-integral-adeles.knowl.md) · [BesselLevelStructure.lean:572](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselLevelStructure.lean#L572)

The cited additive-character duality tests every element d of the different. With d=rϖ and x=−a/ϖ its test becomes integrality of −ra, and r=1 gives precisely the claimed annihilator.

<a name="page-strong-approximation-for-bessel-unipotent-group"></a>

## Strong approximation for the Bessel unipotent group

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/strong-approximation-for-bessel-unipotent-group.knowl.md) · [BesselLevelStructure.lean:702](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselLevelStructure.lean#L702)

The induction multiplies the next floor on the left. Skew parameters are approximated via t−conj(t), which hits each skew β at t=β/2, and the open neighborhood in the second assertion has the conjugating factors in the correct order.

<a name="page-tail-scale-inequalities"></a>

## Inequalities for the tail scale

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/tail-scale-inequalities.knowl.md) · [Terms.lean:484](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Terms.lean#L484)

Substituting n = ϱ+1 gives kf/4 ≥ 128000 n⁹f, which suffices for the advertised powers. The fourth-power identity also gives τ⁴⁴ = b^(11kf), the exponent in the admissibility bound.

<a name="page-term-discriminant-is-totally-positive-or-zero"></a>

## The discriminant of a term is totally positive or zero

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/term-discriminant-is-totally-positive-or-zero.knowl.md) · [Terms.lean:338](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Terms.lean#L338)

The adjugate supplies a coefficient vector even when the frame-product matrix is singular. The norm identity then gives nonnegativity at each place, and the embedding is injective, so a nonzero discriminant is strictly positive at every place.

<a name="page-term-discriminant-norm-and-pair-count-scale"></a>

## Norm of the discriminant of a term and the pair count scale

Added · notation · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/term-discriminant-norm-and-pair-count-scale.knowl.md) · [Terms.lean:126](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Terms.lean#L126)

The product uses one absolute value for each infinite place, without squaring it. The counting scale has the reduced Bessel group order and the number of classes in the numerator, N^(kf) in the denominator, and is strictly positive.

<a name="page-terms-compose-like-a-groupoid"></a>

## Terms over blocks compose like a groupoid

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/terms-compose-like-a-groupoid.knowl.md) · [BesselLevelStructure.lean:187](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselLevelStructure.lean#L187)

The common class representative cancels in the stated order when multiplying terms. The quotient criterion takes k⁻¹ times the translated rational matrix on the left, as in the source.

<a name="page-terms-of-cell-rank-zero-are-scalar-multiples-of-the-bessel-subgroup"></a>

## Terms with norm-one pairs from index zero are scalar multiples of the Bessel subgroup

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/terms-of-cell-rank-zero-are-scalar-multiples-of-the-bessel-subgroup.knowl.md) · [SquareExpansion.lean:195](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/SquareExpansion.lean#L195)

The flag argument uses one common global ζ at every index. Its first diagonal entry is integral in the class coordinates, and division by the corresponding integral scalar isometry produces the stated residue coset.

<a name="page-terms-off-the-bessel-subgroup-reduce-to-remaining-terms"></a>

## Terms off the Bessel subgroup reduce to the remaining terms

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/terms-off-the-bessel-subgroup-reduce-to-remaining-terms.knowl.md) · [SquareExpansion.lean:519](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/SquareExpansion.lean#L519)

The source and translation both separate the stable disagreeing terms, which have zero total amplitude, from the agreeing nonremaining terms, which cannot occur over the chosen residue. This proves the block equality for either side.

<a name="page-terms-with-the-same-frame-image"></a>

## Terms with the same image of the frame

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/terms-with-the-same-frame-image.knowl.md) · [Terms.lean:599](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Terms.lean#L599)

The source gives r⁻¹r′ in the reduced Bessel group, yielding a left coset. For equal residues the composed term runs from c′ to d with identity residue, and the frame-fixing Bessel condition gives c′ = d and membership in the required integral unipotent subgroup.

<a name="page-trace-against-a-small-central-idempotent"></a>

## Trace of the twisted translations against a small central idempotent

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/trace-against-a-small-central-idempotent.knowl.md) · [Moments.lean:1033](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Moments.lean#L1033)

The coefficient identity follows by evaluating x²=x at the identity and using the inverse-conjugate character relation. Conjugacy invariance and injectivity of the single-prime embedding justify the restriction of the square sum, giving the claimed b⁻⁴D_X.

<a name="page-trace-of-the-twisted-translations"></a>

## Trace of the twisted translations

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/trace-of-the-twisted-translations.knowl.md) · [Moments.lean:751](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Moments.lean#L751)

The small-rank freeness argument applies because the integral H component reduces to the identity at each chosen place over the specified prime. Using the right unipotent translate in the inverse block yields ψ_U(k) with the stated sign, and the absence of a unipotent lift gives zero.

<a name="page-unipotent-character-agreement-stability"></a>

## Unipotent character, agreeing residues, stable sets and terms of a link

Revised · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/unipotent-character-agreement-stability.knowl.md) · [Setup.lean:741](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Setup.lean#L741)

The minus sign in the shifted finite character, the level M, and the relation between the two reductions in Agrees match Lean. The underlying finite character is trivial on integral adèles and has the stated positive-exponent trace on rational inputs.

<a name="prior-unipotent-character-agreement-stability-1"></a>

**Still open · medium · Multiplicativity on the Bessel subgroup is not exclusive.** The root-sum lemma proves multiplicativity on the Bessel subgroup. It also holds on the scalar subgroup {I,−I}, where every simple-root entry vanishes and −I does not fix the frame as required for the Bessel subgroup. Remove “only”. [Knowl, line 27](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/unipotent-character-agreement-stability.knowl.md#L27) · [FloorGroups.lean:912](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bruhat/FloorGroups.lean#L912)

<a name="page-unipotent-character-at-infinity"></a>

## The unipotent character at the infinite places

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/unipotent-character-at-infinity.knowl.md) · [BesselLevelStructure.lean:263](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselLevelStructure.lean#L263)

The adjacent frame scales have ratio 1/κ_v even at the final frame vector. With z=−σ/(Mϖ) the archimedean exponent is −4πi Re(z_v), and triviality on the diagonal gives the conjugate finite character.

<a name="page-unipotent-character-on-level-cosets"></a>

## The unipotent character is constant on cosets of the principal level

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/unipotent-character-on-level-cosets.knowl.md) · [BesselLevelStructure.lean:775](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselLevelStructure.lean#L775)

For k=u⁻¹h⁻¹vh the equality vh=huk gives σ(v)=σ(u)+σ(k). Off-diagonal divisibility by M kills the extra factor under the normalized self-dual character and yields the stated rational wave product.

<a name="page-unipotent-group-acts-on-the-structure-of-a-term"></a>

## The unipotent group and the structure of a term

Added · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/spanning-unfolding-b/unipotent-group-acts-on-the-structure-of-a-term.knowl.md) · [TermStructure.lean:795](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/TermStructure.lean#L795)

Left multiplication by the first unipotent factor transports the common isotropic span, and the second factor preserves A. Additivity of the simple-root sum on the rational Bessel unipotents gives conjugation invariance of the finite character and hence both directions of character agreement.
