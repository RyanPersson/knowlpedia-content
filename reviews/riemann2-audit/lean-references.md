# Lean placeholder spellings

Of the 723 distinct Lean names used in placeholders, a qualified source declaration was found directly for 674. Reading the other 49 in context found 35 incorrect names, 11 valid names, including generated fields, and 3 without a single confirmed declaration matching the intended use. A uniquely matching shorthand in the knowl resolver can lead to the intended page even when its Lean spelling needs correction. [Header and resolver checks](structural-checks.md)

## Names to correct

### `New.CMLattice.IsIsogeny`

Use `PeriodPair.IsIsogeny`. The degree predicate belongs to the global PeriodPair namespace. Dot notation on a CM lattice reaches its underlying period pair. [frobenius-congruence-for-theta, line 24](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/frobenius-congruence-for-theta.knowl.md#L24) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/Sigma/Basic.lean#L86) · [Basic.lean:694](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/Sigma/Basic.lean#L694) · [FrobeniusCongruence.lean:152](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/FrobeniusCongruence.lean#L152)

### `New.Exchange.AreMatched`

Use `New.AreMatched`. The partner structure with two support fields and a determinant-character identity is directly in New. [one-exchange, line 19](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-comparison/one-exchange.knowl.md#L19) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/PartnerAlgebra.lean#L76)

### `New.Exchange.areMatched_block`

Use `New.Rows.areMatched_block`. The explicitly qualified Rows lemma pairs the block row and block column. An open Exchange in the caller supplies no Exchange declaration. [one-exchange, line 38](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-comparison/one-exchange.knowl.md#L38) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Exchange/MatchingPartners.lean#L74)

### `New.Exchange.sum_addChar_trace_mul`

Use `New.sum_addChar_trace_mul`. The primitive-character trace sum used in the Fourier transform is the general orthogonality lemma in New. [fourier-transform-of-next-datum, line 39](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-chain/fourier-transform-of-next-datum.knowl.md#L39) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Analysis/FiniteFourier.lean#L114)

### `New.FloorGroups.floorGroup`

Use `New.Shape.Form.floorGroup`. The definition explicitly names _root_.New.Shape.Form.floorGroup. The local export appears inside New.Floors.FloorGroups, which has an additional Floors component. [frames-setting, line 18](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-frames-b/frames-setting.knowl.md#L18) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bruhat/FloorGroups.lean#L176) · [FloorGroups.lean:204](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bruhat/FloorGroups.lean#L204)

### `New.Gf.ofSplitPlace`

Use `New.ofSplitPlace`. The split-place constructor produces an element of Gf and is declared in New. A neighboring map is explicitly named Gf.atPlace. [translated-block-datum, line 47](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-values/translated-block-datum.knowl.md#L47) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Unitary/Defs.lean#L317)

### `New.IsAdmissibleCombination`

Use `New.Seesaw.IsAdmissibleCombination`. The definition explicitly places the condition on finite combinations in New.Seesaw. [chain-datum-as-a-weak-chain-datum, line 24](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/chain-datum-as-a-weak-chain-datum.knowl.md#L24) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/AdmissibleCombinations.lean#L501)

### `New.IsBranchingMap.mul_weylRep`

Use `New.Data.IsBranchingMap.mul_weylRep`. The branching map structure is declared inside New.Data. This field gives the intertwining identity with scalar factor ∏τ z(τ) raised placewise to the branch exponents. [gauge-and-size-of-the-restriction-to-y-m, line 32](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/gauge-and-size-of-the-restriction-to-y-m.knowl.md#L32) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Columns.lean#L681)

### `New.IsBranchingMap.weylNormSq_le`

Use `New.Data.IsBranchingMap.weylNormSq_le`. This generated field of New.Data.IsBranchingMap bounds the squared Weyl norm by exp(x⁷⁰) times the input squared norm. [gauge-and-size-of-the-restriction-to-y-m, line 36](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/gauge-and-size-of-the-restriction-to-y-m.knowl.md#L36) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Columns.lean#L690)

### `New.Space.entireTheta_translate_finiteImage`

Use `New.entireTheta_translate_finiteImage`. The transformation from finite translation by γ to theta shift by −realImage γ is in New. Space is opened for use at line 163. [existence-of-resolution-product-along-tight-frame, line 40](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/existence-of-resolution-product-along-tight-frame.knowl.md#L40) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/ThetaJets.lean#L208)

### `New.Space.exists_finiteImage_approx`

Use `New.exists_finiteImage_approx`. The approximation theorem for finite Heisenberg translates is declared directly in New. Opening Space does not insert it into the declaration name. [resolution-product-integral-values, line 23](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/resolution-product-integral-values.knowl.md#L23) · [standard-data-as-theta-products, line 30](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/standard-data-as-theta-products.knowl.md#L30) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/ThetaJets.lean#L184)

### `New.directDatum`

Use `New.IsSplitLevel.directDatum`. The direct datum is the last-column indicator modulo N in the IsSplitLevel namespace. [direct-lifts-lose-little, line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/direct-lifts-lose-little.knowl.md#L15) · [level-at-n-as-a-mirabolic-group, line 31](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/level-at-n-as-a-mirabolic-group.knowl.md#L31) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftLawsModuloN.lean#L264)

### `New.exists_inclGL_eq`

Use `New.IsSplitLevel.exists_inclGL_eq`. This IsSplitLevel lemma produces an integral invertible representative when the datum is nonzero on both a matrix and its inverse. [level-at-n-as-a-mirabolic-group, line 31](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/level-at-n-as-a-mirabolic-group.knowl.md#L31) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftLawsModuloN.lean#L410)

### `New.exists_short_basis_stdSpace`

Use `New.Space.exists_short_basis_stdSpace`. The short-basis theorem is in New.Space. Its hypotheses include an integer in the different and it controls all archimedean entries of a rational basis. [class-number-bound-for-the-standard-lattice, line 24](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/class-number-bound-for-the-standard-lattice.knowl.md#L24) · [short-forms-span-at-a-free-level, line 23](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/short-forms-span-at-a-free-level.knowl.md#L23) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Reduction/FirstMinimumShortBases.lean#L892)

### `New.finHeisenbergOp_finHeisenbergOp`

Use `New.Space.finHeisenbergOp_finHeisenbergOp`. The finite Heisenberg composition law, including its central character factor, is in New.Space. [expanding-the-gluing, line 38](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/expanding-the-gluing.knowl.md#L38) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/VacuumProjections.lean#L102)

### `New.hecke_transfer_of_pairing`

Use `New.SiegelWeil.hecke_transfer_of_pairing`. The spherical Hecke transfer theorem for paired lifts and its polynomial factor are in New.SiegelWeil. [hecke-transfer-through-the-chain, line 38](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/hecke-transfer-through-the-chain.knowl.md#L38) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Unramified/HeckeTransfer.lean#L495)

### `New.intValuation_natCast_eq_exp_neg_one`

Use `New.Parameters.intValuation_natCast_eq_exp_neg_one`. The value on p at a place over p is a theorem of New.Parameters, with the indicated exclusion of primes dividing q₁d. [properties-of-marked-sets, line 27](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/properties-of-marked-sets.knowl.md#L27) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/PrimeDecomposition.lean#L675)

### `New.integralForms`

Use `New.LevelPlaces.LevelForm.integralForms`. The one-embedding submodule belongs to New.LevelPlaces.LevelForm. The definition of a test form imposes its membership condition at each embedding. [test-form, line 16](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-comparison/test-form.knowl.md#L16) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/AutomorphicForms/PAdicGauge.lean#L738)

### `New.isAdmissibleCombination_schrodingerOp_of_reduction`

Use `New.Seesaw.isAdmissibleCombination_schrodingerOp_of_reduction`. The expansion of a residue-matrix function into vacuum-projected Heisenberg translates is explicitly a Seesaw theorem. [direct-lifts-lose-little, line 27](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/direct-lifts-lose-little.knowl.md#L27) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/AdmissibleCombinations.lean#L842)

### `New.mem_raises_of_standardData`

Use `New.Parameters.mem_raises_of_standardData`. The gauge estimate for standard data at a nonzero scale is in New.Parameters. [direct-lifts-lose-little, line 27](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/direct-lifts-lose-little.knowl.md#L27) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Kernels/ThetaLiftGauge.lean#L298)

### `New.mem_raises_predictedDivisibility`

Use `New.Parameters.mem_raises_predictedDivisibility`. The predicted-divisibility bound on the raise of a theta kernel is in New.Parameters. [one-lift-evaluated-at-a-neighbor, line 37](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/one-lift-evaluated-at-a-neighbor.knowl.md#L37) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Kernels/ThetaLiftGauge.lean#L335)

### `New.mirabolic`

Use `New.IsSplitLevel.mirabolic`. The subgroup of integral matrices fixing the last basis vector modulo N is in New.IsSplitLevel. [level-at-n-as-a-mirabolic-group, line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/level-at-n-as-a-mirabolic-group.knowl.md#L15) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftLawsModuloN.lean#L206)

### `New.mirabolic_fix_upOperator`

Use `New.IsSplitLevel.mirabolic_fix_upOperator`. The lemma that the Up operator preserves mirabolic fixed vectors is in New.IsSplitLevel. [up-operator-preserves-source-forms, line 24](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/up-operator-preserves-source-forms.knowl.md#L24) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftLawsModuloN.lean#L511)

### `New.norm_detCharAt_diagN_anti`

Use `New.IsSplitLevel.norm_detCharAt_diagN_anti`. The determinant-character norm weakly decreases when the twist exponent k increases, independently of the two matrix sizes. The theorem belongs to New.IsSplitLevel. [all-lifts-become-direct, line 25](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/all-lifts-become-direct.knowl.md#L25) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Columns.lean#L341)

### `New.norm_schurJet_jetSeries_le_of_charges`

Use `New.Parameters.norm_schurJet_jetSeries_le_of_charges`. The charged estimate on Schur derivatives of the jet series belongs to New.Parameters. [one-lift-evaluated-at-a-neighbor, line 31](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/one-lift-evaluated-at-a-neighbor.knowl.md#L31) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/Divisibility.lean#L246)

### `New.norm_schur_mulVec_le`

Use `New.Rows.norm_schur_mulVec_le`. The contraction of the maximum norm by the Schur action of an integral matrix is in New.Rows. [short-forms-span-at-a-free-level, line 31](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/short-forms-span-at-a-free-level.knowl.md#L31) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/Dual.lean#L719)

### `New.omega_mem_raises_of_schurJet_le`

Use `New.Parameters.omega_mem_raises_of_schurJet_le`. The theorem that a weighted Schur-jet bound gives a gauge bound after Weil action is in New.Parameters. [one-lift-evaluated-at-a-neighbor, line 27](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/one-lift-evaluated-at-a-neighbor.knowl.md#L27) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Kernels/ThetaLiftGauge.lean#L186)

### `New.omega_projOn`

Use `New.Space.omega_projOn`. The commuting law for the Weil action and the local vacuum projection is in New.Space. [chain-datum-as-a-weak-chain-datum, line 26](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/chain-datum-as-a-weak-chain-datum.knowl.md#L26) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/VacuumProjections.lean#L587)

### `New.poleColumn`

Use `New.Seesaw.poleColumn`. The explicit definition of the pole column is in New.Seesaw. [expanding-the-gluing, line 18](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/expanding-the-gluing.knowl.md#L18) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Columns.lean#L92)

### `New.poleRow`

Use `New.Seesaw.poleRow`. The row with conjugate pole coefficients is explicitly defined in New.Seesaw. [expanding-the-gluing, line 18](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/expanding-the-gluing.knowl.md#L18) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Columns.lean#L98)

### `New.ramified`

Use `New.IsSplitLevel.ramified`. The IsSplitLevel predicate expresses membership in the image of 1 − ρ(x) at each place. At the other places its definition asks that the reduction of x be 1. [up-operator-preserves-source-forms, line 20](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/up-operator-preserves-source-forms.knowl.md#L20) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftLawsModuloN.lean#L222)

### `New.stdLevel.exists_reduceFamily_eq`

Use `New.exists_reduceFamily_eq`. The lifting theorem belongs to New. The function stdLevel.reduceFamily appearing in its conclusion belongs to the opened stdLevel namespace. [block-datum-is-sharp, line 29](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-exchange/block-datum-is-sharp.knowl.md#L29) · [point-lift, line 27](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-comparison/point-lift.knowl.md#L27) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Unitary/CongruenceLevels.lean#L330)

### `New.upOperator`

Use `New.IsSplitLevel.upOperator`. The IsSplitLevel operator sums over residue vectors with unit last entry, weights by the additive character and applies diagonal translation. [setup-at-the-level-prime, line 20](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/setup-at-the-level-prime.knowl.md#L20) · [up-operator-preserves-source-forms, line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/up-operator-preserves-source-forms.knowl.md#L15) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftLawsModuloN.lean#L200)

### `New.weylGauge_deltaForm_le`

Use `New.Rows.weylGauge_deltaForm_le`. The nonarchimedean gauge estimate for a delta form is explicitly qualified Rows within New. [short-forms-span-at-a-free-level, line 21](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/short-forms-span-at-a-free-level.knowl.md#L21) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/AutomorphicForms/PAdicGauge.lean#L252)

### `New.weylNormSq_deltaForm_le`

Use `New.Rows.weylNormSq_deltaForm_le`. The squared Weyl norm estimate for a delta form and its stabilizer factor is explicitly qualified Rows within New. [short-forms-span-at-a-free-level, line 21](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/short-forms-span-at-a-free-level.knowl.md#L21) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/AutomorphicForms/PAdicGauge.lean#L280)

## References needing a choice of declaration

### `New.Derivatives.Divisibility`

The displayed link explicitly names a chapter. New.Derivatives.Divisibility is a module-path prefix. Link the chapter directly. The charged Schur-jet estimate is one input to the divisibility claim. [divisibility-bound, line 35](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/divisibility-bound.knowl.md#L35) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/JetExponent.lean#L1) · [Divisibility.lean:246](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/Divisibility.lean#L246) · [ValuationAtNonSplitPrimes.lean:66](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/ValuationAtNonSplitPrimes.lean#L66) · [ValuationAtNonSplitPrimes.lean:304](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/ValuationAtNonSplitPrimes.lean#L304)

### `New.Filling.covolume_classUnipotent`

Candidate declarations include `New.Filling.lintegral_classCutoff_eq_unipotentCovolume`, `New.Filling.lintegral_classCutoff_eq_measure`. No declaration with this spelling was found. The cutoff-integral identity gives the displayed constant, and the fundamental-domain measure identity identifies it as a covolume. Their hypotheses include a primitive 5040th root and admissibility. [filling-constants, line 35](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-unfolding-b/filling-constants.knowl.md#L35) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/CutoffIntegral.lean#L728) · [CutoffIntegral.lean:324](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/CutoffIntegral.lean#L324) · [Setup.lean:260](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Setup.lean#L260)

### `New.Filling.isCutoff_classCutoff`

Candidate declarations include `New.Filling.tsum_classCutoff_eq_one`, `New.Filling.measurable_classCutoff`. The two ingredients are separate lemmas. Measurability and the sum over the discrete class-unipotent group give the two conditions of IsCutoff with counting measure. The sum lemma requires a primitive 5040th root and admissibility. [class-cutoff, line 31](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-unfolding-b/class-cutoff.knowl.md#L31) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Packing.lean#L134) · [Packing.lean:531](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Packing.lean#L531) · [Basic.lean:70](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/QuotientMeasure/Basic.lean#L70)

## Valid names requiring a scope or field check

### `New.Data.bPlaces`

The b-places are a finite-set field of New.Data, whose declaration begins at line 77. [sparseness-along-powers-of-minus-p, line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/sparseness-along-powers-of-minus-p.knowl.md#L15) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/AdmissibleData.lean#L126)

### `New.Data.piMBar`

New.Data has an integer-of-K field piMBar. The following field states the norm equation with its conjugate. [resolution-forms-of-a-frame, line 14](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/resolution-forms-of-a-frame.knowl.md#L14) · [twelve-space-and-indicator-data, line 14](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/twelve-space-and-indicator-data.knowl.md#L14) · [row-lengths-and-jet-sizes, line 26](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/row-lengths-and-jet-sizes.knowl.md#L26) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/AdmissibleData.lean#L150)

### `New.Data.placeClass_of_mem_bPlaces`

This proof field identifies the place class of each b-place with the class of −1 modulo q₀. [near-pair, line 24](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/near-pair.knowl.md#L24) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/AdmissibleData.lean#L128)

### `New.Data.sparse`

The sparse field supplies the IsSparse proof for the b-places and the cut-off (r + 1 − m)(5r). [sparseness-along-powers-of-minus-p, line 24](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/sparseness-along-powers-of-minus-p.knowl.md#L24) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/AdmissibleData.lean#L134)

### `New.Data.weight`

The weight field sends each infinite place to a natural number. The next field specifies its values on and off the b-places. [degree-near-the-weights, line 14](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/degree-near-the-weights.knowl.md#L14) · [partner-minimum-sum, line 14](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/partner-minimum-sum.knowl.md#L14) · [local-prime-sum, line 14](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/local-prime-sum.knowl.md#L14) · [prime-sum-grouped-by-primes, line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/prime-sum-grouped-by-primes.knowl.md#L15) · [row-lengths-and-jet-sizes, line 20](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/row-lengths-and-jet-sizes.knowl.md#L20) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/AdmissibleData.lean#L136)

### `New.Grading.besselFin`

The source opens New.Space at line 650, closes only Space at 683 and opens Grading at 685. The Bessel subgroup therefore lies in New.Grading. [lattice-bounds-induction-step, line 38](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/lattice-bounds-induction-step.knowl.md#L38) · [shift-maps-lattices, line 35](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/shift-maps-lattices.knowl.md#L35) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/Grading.lean#L688) · [Grading.lean:650](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/Grading.lean#L650) · [Grading.lean:683](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/Grading.lean#L683) · [Grading.lean:685](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/Grading.lean#L685)

### `New.Grading.inclXFin`

The finite-group inclusion is declared in Grading while New remains open. The two namespaces close separately at lines 721 and 723. [glued-level-congruences, line 19](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/glued-level-congruences.knowl.md#L19) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/Grading.lean#L692) · [Grading.lean:683](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/Grading.lean#L683) · [Grading.lean:721](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/Grading.lean#L721) · [Grading.lean:723](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/Grading.lean#L723)

### `New.HasFiniteType.finite_classes`

This generated projection asserts finiteness of the double-coset quotient. The subsequent scoped instance explicitly uses the field. [filling-classes-and-terms, line 33](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-unfolding-b/filling-classes-and-terms.knowl.md#L33) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Hecke/ClassSums.lean#L81)

### `New.frameVector`

The frame vector is defined directly in New. The source closes only Shape at 271 after opening New.Shape at 227. [bessel-length, line 20](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/bessel-length.knowl.md#L20) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bessel/Basic.lean#L277) · [Basic.lean:227](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bessel/Basic.lean#L227) · [Basic.lean:271](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bessel/Basic.lean#L271)

### `New.realFrameGram`

The frame Gram matrix is defined after the partial closing of New.Shape at 271 and before end New at 349. [frame-gram-matrix-of-an-isometry, line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/frame-gram-matrix-of-an-isometry.knowl.md#L15) · [orbital-integral-minors-real, line 19](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-frames-b/orbital-integral-minors-real.knowl.md#L19) · [frame-products-at-infinity, line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-unfolding-b/frame-products-at-infinity.knowl.md#L15) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bessel/Basic.lean#L282) · [Basic.lean:271](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bessel/Basic.lean#L271) · [Basic.lean:349](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bessel/Basic.lean#L349)

### `New.toPoly_schur`

The transpose-substitution formula lies in New. The source opens New.GL at 160 and closes only GL at 323. [integral-values-of-source-forms-as-polynomials, line 23](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/integral-values-of-source-forms-as-polynomials.knowl.md#L23) · [Lean source](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/SchurModule/WeylKernel.lean#L494) · [WeylKernel.lean:160](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/SchurModule/WeylKernel.lean#L160) · [WeylKernel.lean:323](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/SchurModule/WeylKernel.lean#L323) · [WeylKernel.lean:552](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/SchurModule/WeylKernel.lean#L552)
