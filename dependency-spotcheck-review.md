# Independent semantic spot checks

Completed a risk-weighted sample of **48 knowls**, with **17 related definitions** checked while resolving findings. Corrected **26 prerequisite lists** and **17 bodies**: 22 edges added, 19 removed. All 65 entries now record a second dependency review. No new knowls were needed.

This follows [the full prerequisite review](dependency-full-review.md). Historical reports and hashes remain intact; the [new machine-readable contract](dependency-spotcheck-review.json) supersedes their reviewed lists for these entries. The contract records exact before/after text, source hashes, reviewer attribution, and eight additional learning paths.

## Selection and method

8 new foundations, 8 highest direct-dependent hubs, 13 repaired-boundary definitions, 12 largest prerequisite removals (ties by dependent count/ID), 7 remaining controls sampled with seed 20260905. Risk-weighted sample; not an estimate of corpus error prevalence.

Three fresh agents reviewed foundations, heavily used concepts, and repaired conceptual boundaries without using the earlier rationales. The parent independently checked removal-heavy definitions and controls, followed direct defining inputs, and integrated the proposals against the complete graph. Separate fresh-agent verification challenged the substantive corrections and covered the remaining removal/control entries, completing fresh-agent coverage of all 48 sampled knowls. Sampling prioritized likely failure points; its findings must not be converted into a corpus-wide error rate.

## Substantive repairs

- Restored defining inputs: sections for differential forms, subspace topology for irreducibility, determinants and bases for matrix groups, connectedness for connected Lie groups, subgroup/immersion definitions, Euclidean pairing for conjugates, subgroup generation for commutators, and closed forms for symplectic manifolds.
- Corrected the conceptual order to Euclidean holomorphic map → complex atlas → complex manifold, and horizontal subbundle → Ehresmann connection → horizontal lift → parallel transport. Removed contextual specializations and consequences from these prerequisite lists.
- Generalized the Lie-bracket primitive to arbitrary fields, retaining alternation and the characteristic-2 distinction. The distinction agrees with [Elkies’s Lie algebra course notes](https://people.math.harvard.edu/~elkies/M222.23/).
- Preserved the unital algebra-over-ring convention while defining possibly nonunital involutive and Banach algebras from vector spaces and associative bilinear multiplication. The C*-algebra prerequisite path now supports its stated nonunital examples.
- Corrected both Fenchel-conjugate codomains: the permitted input identically +infinity gives conjugate identically -infinity. Qualified the convex-function assertion consistently.
- Added the missing section additivity to the connection definition through real bilinearity. Made Leibniz an axiom on the operation rather than assume the connection it defines.
- Corrected positive-direction holonomy for the stated convention ∇ = d + A dθ to exp(−2πA), by solving s′ + As = 0.
- Defined arbitrary Ehresmann transport on its actual open domain; full-fiber invertibility requires global lifts in both directions. General complex line transport need not be a phase. The local-domain/completeness distinction is also treated in [Kolář–Michor–Slovák, §§9.8–9.10](https://www.mat.univie.ac.at/~michor/kmsbookh.pdf).
- Stated n ≥ 2 in cyclic-group exactness counterexamples, and finite rank where a Hom direct-sum identification requires it.

Two later suggestions were declined: adding smooth-map directly to vector-field would duplicate a prerequisite already supplied transitively, and adding Fell topology to unitary-dual would recreate the direct cycle. The unitary-dual wording was clarified, but the initial proposal’s claim of a reversed Fell-topology theorem was not accepted: its informal wording could be read correctly with the other representation as neighborhood center.

A useful transport counterexample is the horizontal ODE y′ = −y³ over a product bundle above the real line. Its time-one map y ↦ y/√(1+2y²) exists for every real initial value but has image (−1/√2, 1/√2). This demonstrates why forward existence alone does not establish surjectivity.

## Validation

| Check | Result |
| --- | --- |
| Development graph | 3,509 nodes; 10,938 edges; zero cycles, missing targets or invalid sources |
| Production graph | 3,499 nodes; 10,912 edges; zero cycles, missing targets or invalid sources |
| Learning paths | 47 pass; all prerequisite closures have review metadata |
| Python tests | 124 pass |
| Graph model and browser suites | Pass, including subjects, components, navigation and responsive layouts |
| Corrected rendered graph views | 17 pass, including mobile; no browser or math errors |
| Targeted HTML scan | 510 pages and fragments across both profiles; zero rendering issues |
| Full builds and whitespace checks | Both profiles/repositories pass |

Visually inspected the desktop flat-connection graph, mobile parallel-transport sheet, subject overview, component detail, and the expanded example displaying the corrected negative holonomy sign. Existing long formulas use their internal horizontal scrolling; graph labels truncate long titles while the selected entry shows the full title. The persistent preview is [available here](http://100.69.17.72:8016/graph/), service `devserver-knowlpedia-graph-iteration`, port 8016.

The compiler still reports existing duplicate-alias warnings. This review does not certify every mathematical statement in the corpus. Before benchmark comparison, freeze both versions and compare the same production corpus and task set, with semantic quality reported separately from graph structure and rendering.

## Entry ledger

| Knowl | Stratum | Resolution |
| --- | --- | --- |
| [shared-foundations/finite-permutation](content/shared-foundations/finite-permutation.knowl.md) | foundations | confirmed; related prerequisite corrections incorporated where noted |
| [shared-foundations/permutation-sign](content/shared-foundations/permutation-sign.knowl.md) | foundations | corrected |
| [algebraic-geometry-foundations/regular-local-ring](content/algebraic-geometry-foundations/regular-local-ring.knowl.md) | foundations | confirmed; related prerequisite corrections incorporated where noted |
| [algebraic-geometry-foundations/regular-scheme](content/algebraic-geometry-foundations/regular-scheme.knowl.md) | foundations | corrected |
| [algebraic-geometry-foundations/geometric-fiber](content/algebraic-geometry-foundations/geometric-fiber.knowl.md) | foundations | corrected |
| [differential-geometry/differentiable-flow](content/differential-geometry/differentiable-flow.knowl.md) | foundations | confirmed; related prerequisite corrections incorporated where noted |
| [fiber-bundles/unit-tangent-bundle](content/fiber-bundles/unit-tangent-bundle.knowl.md) | foundations | corrected |
| [differential-geometry/geodesic](content/differential-geometry/geodesic.knowl.md) | foundations | confirmed; related prerequisite corrections incorporated where noted |
| [fiber-bundles/smooth-manifold](content/fiber-bundles/smooth-manifold.knowl.md) | hubs | confirmed; related prerequisite corrections incorporated where noted |
| [linear-algebra/vector-space](content/linear-algebra/vector-space.knowl.md) | hubs | confirmed; related prerequisite corrections incorporated where noted |
| [fiber-bundles/lie-group](content/fiber-bundles/lie-group.knowl.md) | hubs | confirmed; related prerequisite corrections incorporated where noted |
| [linear-algebra/hilbert-space](content/linear-algebra/hilbert-space.knowl.md) | hubs | confirmed; related prerequisite corrections incorporated where noted |
| [lie-groups/lie-algebra](content/lie-groups/lie-algebra.knowl.md) | hubs | confirmed; related prerequisite corrections incorporated where noted |
| [fiber-bundles/principal-g-bundle](content/fiber-bundles/principal-g-bundle.knowl.md) | hubs | confirmed; related prerequisite corrections incorporated where noted |
| [algebra-groups/group](content/algebra-groups/group.knowl.md) | hubs | confirmed; related prerequisite corrections incorporated where noted |
| [operator-algebras/cstar-algebra](content/operator-algebras/cstar-algebra.knowl.md) | hubs | confirmed; related prerequisite corrections incorporated where noted |
| [fiber-bundles/lie-bracket](content/fiber-bundles/lie-bracket.knowl.md) | follow-up | corrected |
| [algebra-modules/algebra-over-ring](content/algebra-modules/algebra-over-ring.knowl.md) | follow-up | confirmed; related prerequisite corrections incorporated where noted |
| [operator-algebras/involutive-algebra](content/operator-algebras/involutive-algebra.knowl.md) | follow-up | corrected |
| [functional-analysis/banach-algebra](content/functional-analysis/banach-algebra.knowl.md) | follow-up | corrected |
| [algebra-category-theory/category](content/algebra-category-theory/category.knowl.md) | repairs | confirmed; related prerequisite corrections incorporated where noted |
| [algebra-category-theory/morphism](content/algebra-category-theory/morphism.knowl.md) | repairs | confirmed; related prerequisite corrections incorporated where noted |
| [differential-geometry/complex-atlas](content/differential-geometry/complex-atlas.knowl.md) | repairs | corrected |
| [differential-geometry/holomorphic-map](content/differential-geometry/holomorphic-map.knowl.md) | repairs | corrected |
| [differential-geometry/complex-manifold](content/differential-geometry/complex-manifold.knowl.md) | repairs | confirmed; related prerequisite corrections incorporated where noted |
| [algebra-modules/tensor-product](content/algebra-modules/tensor-product.knowl.md) | repairs | confirmed; related prerequisite corrections incorporated where noted |
| [algebra-modules/tensor-product-universal-property](content/algebra-modules/tensor-product-universal-property.knowl.md) | repairs | confirmed; related prerequisite corrections incorporated where noted |
| [algebra-modules/smith-normal-form-invariants](content/algebra-modules/smith-normal-form-invariants.knowl.md) | repairs | confirmed; related prerequisite corrections incorporated where noted |
| [algebra-modules/smith-normal-form-theorem](content/algebra-modules/smith-normal-form-theorem.knowl.md) | repairs | corrected |
| [algebraic-geometry-foundations/site](content/algebraic-geometry-foundations/site.knowl.md) | repairs | confirmed; related prerequisite corrections incorporated where noted |
| [algebraic-geometry-foundations/covering-family](content/algebraic-geometry-foundations/covering-family.knowl.md) | repairs | confirmed; related prerequisite corrections incorporated where noted |
| [harmonic-analysis/unitary-dual](content/harmonic-analysis/unitary-dual.knowl.md) | repairs | corrected |
| [harmonic-analysis/fell-topology](content/harmonic-analysis/fell-topology.knowl.md) | repairs | confirmed; related prerequisite corrections incorporated where noted |
| [fiber-bundles/differential-k-form](content/fiber-bundles/differential-k-form.knowl.md) | removals | corrected |
| [lie-groups/simply-connected-lie-group](content/lie-groups/simply-connected-lie-group.knowl.md) | removals | confirmed; related prerequisite corrections incorporated where noted |
| [lie-groups/smooth-action-lie-group](content/lie-groups/smooth-action-lie-group.knowl.md) | removals | confirmed; related prerequisite corrections incorporated where noted |
| [topology/irreducible-space](content/topology/irreducible-space.knowl.md) | removals | corrected |
| [algebra-fields-galois/cyclotomic-extension](content/algebra-fields-galois/cyclotomic-extension.knowl.md) | removals | confirmed; related prerequisite corrections incorporated where noted |
| [algebra-modules/module](content/algebra-modules/module.knowl.md) | removals | confirmed; related prerequisite corrections incorporated where noted |
| [fiber-bundles/vector-field](content/fiber-bundles/vector-field.knowl.md) | removals | confirmed; related prerequisite corrections incorporated where noted |
| [convex-analysis/legendre-fenchel-transform](content/convex-analysis/legendre-fenchel-transform.knowl.md) | removals | corrected |
| [algebra-category-theory/coproduct](content/algebra-category-theory/coproduct.knowl.md) | removals | confirmed; related prerequisite corrections incorporated where noted |
| [convex-analysis/minkowski-function-gauge-of-a-set](content/convex-analysis/minkowski-function-gauge-of-a-set.knowl.md) | removals | confirmed; related prerequisite corrections incorporated where noted |
| [lie-groups/special-linear-group](content/lie-groups/special-linear-group.knowl.md) | removals | corrected |
| [fiber-bundles/flat-vector-bundle-connection](content/fiber-bundles/flat-vector-bundle-connection.knowl.md) | removals | corrected |
| [linear-algebra/eigenspace](content/linear-algebra/eigenspace.knowl.md) | control | confirmed; related prerequisite corrections incorporated where noted |
| [differential-geometry/dolbeault-complex](content/differential-geometry/dolbeault-complex.knowl.md) | control | confirmed; related prerequisite corrections incorporated where noted |
| [algebra-homological/hom-tensor-exactness](content/algebra-homological/hom-tensor-exactness.knowl.md) | control | corrected |
| [probability/moment-generating-function](content/probability/moment-generating-function.knowl.md) | control | confirmed; related prerequisite corrections incorporated where noted |
| [lie-groups/type-i-locally-compact-group](content/lie-groups/type-i-locally-compact-group.knowl.md) | control | corrected |
| [lie-groups/commutator-subgroup-of-a-lie-group](content/lie-groups/commutator-subgroup-of-a-lie-group.knowl.md) | control | corrected |
| [differential-geometry/symplectic-lie-group-action](content/differential-geometry/symplectic-lie-group-action.knowl.md) | control | confirmed; related prerequisite corrections incorporated where noted |
| [convex-analysis/convex-conjugate-fenchel](content/convex-analysis/convex-conjugate-fenchel.knowl.md) | follow-up | corrected |
| [lie-groups/connected-lie-group](content/lie-groups/connected-lie-group.knowl.md) | follow-up | corrected |
| [lie-groups/general-linear-group](content/lie-groups/general-linear-group.knowl.md) | follow-up | corrected |
| [lie-groups/lie-subgroup](content/lie-groups/lie-subgroup.knowl.md) | follow-up | corrected |
| [lie-groups/closed-subgroup-lie-group](content/lie-groups/closed-subgroup-lie-group.knowl.md) | follow-up | corrected |
| [fiber-bundles/connection-on-a-vector-bundle](content/fiber-bundles/connection-on-a-vector-bundle.knowl.md) | follow-up | corrected |
| [differential-geometry/symplectic-manifold](content/differential-geometry/symplectic-manifold.knowl.md) | follow-up | corrected |
| [algebra-homological/hom-left-exact](content/algebra-homological/hom-left-exact.knowl.md) | follow-up | corrected |
| [algebra-homological/tensor-right-exact](content/algebra-homological/tensor-right-exact.knowl.md) | follow-up | corrected |
| [fiber-bundles/parallel-transport](content/fiber-bundles/parallel-transport.knowl.md) | follow-up | corrected |
| [fiber-bundles/ehresmann-connection](content/fiber-bundles/ehresmann-connection.knowl.md) | follow-up | corrected |
| [fiber-bundles/horizontal-lift-of-a-curve](content/fiber-bundles/horizontal-lift-of-a-curve.knowl.md) | follow-up | corrected |
| [fiber-bundles/leibniz-rule-for-a-connection](content/fiber-bundles/leibniz-rule-for-a-connection.knowl.md) | follow-up | corrected |
