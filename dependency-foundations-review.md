# Foundational dependency review

This report records the first semantic-review snapshot. See the
[second curriculum review](dependency-curriculum-review.md) for subsequent
corrections, current coverage, and learning-path checks.

This follow-up reviews 64 complete prerequisite lists around high-degree concepts
and their immediate foundations. Selection used outgoing dependency counts: smooth
manifold (190 dependents), Lie group (153), vector space (135), principal bundle
(120), Lie algebra and Hilbert space (117 each), and group (103), followed by their
set-theoretic, algebraic, topological, and measure-theoretic inputs.

The review changes 37 prerequisite lists: 52 edges added and 32 removed.
At the end of this stage, the corpus had 10,084 prerequisite edges. Each reviewed list received
`dependency_review_count = 1` and provenance `semantic-foundations-review-v1`.
The generator preserves reviewed lists. No body text or math delimiters changed.

## Review criteria

Prerequisites describe inputs to the canonical definition, including necessary
unlinked notation. Examples, consequences, and optional equivalent descriptions
do not become prerequisites just because they appear before a section heading.
A retained direct edge may be transitively redundant when it names a real input.

The review assumes elementary logic, set membership, and real/complex arithmetic.
The geometry path additionally assumes Euclidean C-infinity calculus and second
countability, for which this corpus has no dedicated canonical entries. These
are explicit entry assumptions, not a claim of a complete curriculum from zero.

## Important corrections

- Metrics precede metric spaces, open balls, and induced topologies.
- Measurable spaces precede measurable sets, measures, and measurable functions.
- Cauchy sequences depend on sequences and metric spaces.
- Lie groups require abstract groups; translations are consequences.
- Topological manifolds precede coordinate charts and smooth manifolds.
- Lie brackets use vector spaces and linearity; vector fields are a realization.
- Inner products explicitly include complex conjugation; Hilbert spaces include norm and completeness.
- Vector bundles explicitly include vector spaces and linear maps.

## Reproducible checks

From the paired engine repository:

```bash
python3 scripts/check_learning_paths.py --report tmp/learning-path-review.json
python3 scripts/audit_dependency_graph.py --profile development --report tmp/dag-development.json
python3 scripts/audit_dependency_graph.py --profile production --report tmp/dag-production.json
```

The path checker verifies all eight paths below and rejects forbidden advanced
ancestors even when the graph remains acyclic. It also reports how many
prerequisites of each endpoint remain unreviewed; checking a path is not a claim
that every other branch in the endpoint’s prerequisite closure has been reviewed.

- Sets to linear maps
- Metric completeness to Hilbert spaces
- Inner products to Hilbert spaces
- Sets to measure spaces
- Measurable spaces to measurable functions
- Topology to Lie groups
- Linear algebra to abstract Lie algebras
- Linear algebra to vector bundles

## Per-concept rationale

[Machine-readable record](dependency-foundations-review.json) includes before/after
lists, review counters, assumptions, path contracts, and excluded ancestors.

### shared-foundations/set

Set membership and elementary logic are entry assumptions. Union, intersection, and power set are subsequent constructions.

### shared-foundations/subset

Containment is defined by membership in two sets; it does not require set operations.

### shared-foundations/ordered-pair

Componentwise equality and the stated Kuratowski realization require sets. Cartesian products and relations use pairs subsequently.

### shared-foundations/cartesian-product

The product is a set of ordered pairs; both constituent notions belong in the dependency list.

### shared-foundations/relation

The definition is a subset of a Cartesian product, including the previously unlinked containment notation.

### shared-foundations/function

A total single-valued relation between sets; images, preimages, and composition are later constructions.

### shared-foundations/binary-operation

A function with domain the Cartesian square; examples of algebraic structures are not prerequisites.

### shared-foundations/power-set

The collection consists of all subsets of a given set; notation in the statement previously produced no inferred prerequisites.

### shared-foundations/indexed-family-of-sets

The family is a set-valued function indexed by a set. Set knowledge is already supplied by the function prerequisite.

### shared-foundations/union

Retain indexed families for the general union formula and explicitly retain sets for the binary definition.

### shared-foundations/intersection

Retain indexed families for the general intersection formula. Union and complement are comparisons rather than required constructions.

### shared-foundations/complement

The complement is specified by membership outside a subset of an ambient set; set difference is an equivalent formulation.

### shared-foundations/preimage

A preimage requires a function and a subset of its codomain. An inverse function is not necessary.

### shared-foundations/sequence

Sequences are functions on natural numbers. The three existing inputs cover the actual definition.

### algebra-groups/semigroup

Associative operation on a set. Monoids and groups add further conditions.

### algebra-groups/monoid

The identity axiom extends a semigroup. Composition appears as an example of a monoid, not as part of its definition.

### algebra-groups/group

Retain the set/operation presentation and its monoid formulation; subgroups and group homomorphisms are downstream.

### algebra-groups/abelian-group

An abelian group is a group satisfying commutativity; vector spaces are examples.

### algebra-rings/ring-axioms

The full axiom statement uses binary operations and an abelian additive group. It does not assume a unit or commutativity of multiplication.

### algebra-rings/ring

Retain operations, additive abelian groups, and the explicit axiom formulation. The repository permits nonunital rings.

### algebra-rings/commutative-ring

A commutative ring adds one identity to the ring axioms. Ideals and spectra are downstream.

### algebra-rings/unital-ring

A unital ring adds a multiplicative identity to a ring; units are defined afterward.

### algebra-rings/unit

An invertible element in a unital ring; no field or group-of-units construction is required.

### algebra-rings/field

The commutative-ring and unit prerequisites together provide the unital inverse condition. Ideals are equivalent characterizations.

### linear-algebra/vector-space

The statement supplies the complete vector-space axioms using a field, set, and functions. Linear maps and eigenvalues are downstream.

### linear-algebra/linear-map

A function between vector spaces preserving the two operations. Operator theory is a specialization.

### linear-algebra/inner-product

The displayed conjugate-symmetry axiom uses complex conjugation, absent from the original link-only list. Norms and orthogonality are constructions from the product.

### linear-algebra/inner-product-space

Retain a vector space and chosen inner product. Completeness is not required until Hilbert spaces.

### linear-algebra/norm

The explicit norm axioms require a vector space and scalar absolute value. A metric is induced afterward.

### linear-algebra/hilbert-space

The definition requires an inner product, the induced norm, and metric completeness. Banach spaces are a consequence, not an input.

### topology/topology

The closure axioms use a power set, arbitrary unions, and finite intersections. Open sets are the members selected by this structure.

### topology/topological-space

An ordered pair of a set and its topology; later constructions are not prerequisites.

### topology/open-set

Membership in the topology defines openness. Interior and closure are derived operations and must not precede open sets.

### topology/neighborhood

A neighborhood contains an open set around a point. Metric balls and interior provide examples or equivalent descriptions.

### topology/continuous-map

The function/preimage/open-set condition and the underlying spaces provide the full definition.

### topology/metric

A metric is a distance function satisfying three axioms. Balls and induced topology are constructed from it.

### topology/metric-space

The pair consists of a set and a metric. Its topological structure and open balls are consequences.

### topology/open-ball

The inequality d(x,y)<r requires a metric space. Being open and forming a topological basis are subsequent properties.

### topology/metric-induced-topology

This constructs a topology from metric balls. The basis characterization is useful but not needed before the construction.

### topology/cauchy-sequence

The epsilon condition is stated for a sequence in a metric space. Completeness and convergence are not prerequisites for Cauchyness.

### topology/convergent-sequence

The general definition uses neighborhoods. Metric convergence and uniqueness in Hausdorff spaces are special cases.

### topology/complete-metric-space

Completeness quantifies over Cauchy sequences and demands a limit inside the metric space.

### measure-theory/sigma-algebra

The definition uses subsets of a power set, relative complements, and countable sequences/unions. Neither measures nor measurable functions are inputs.

### measure-theory/measurable-space

A set with a sigma-algebra exists before measures or measurable functions are introduced.

### measure-theory/measurable-set

Membership in the specified sigma-algebra defines measurability. Functions and measures use this notion afterward.

### measure-theory/measurable-function

Both measurable spaces and their measurable sets are necessary to state the preimage condition; they were missing from the heuristic list.

### measure-theory/measure

Countable additivity is a condition on a function on measurable sets. Null sets require a measure and cannot be an input to it.

### measure-theory/measure-space

A measurable space together with a measure; almost-everywhere statements are later notions.

### topology/homeomorphism

The definition requires topological spaces and a bijective continuous function with continuous inverse. Compactness and connectedness are preserved properties.

### topology/topological-manifold

The base definition is topological and Hausdorff. A smooth manifold is a stronger structure, not an input. Second countability and Euclidean space are explicit background assumptions in this review.

### fiber-bundles/smooth-chart-coordinate-chart

A chart is a homeomorphism between suitable open sets. Comparing two charts to form a transition map occurs afterward.

### fiber-bundles/coordinate-transition-map

The transition is the composition of one chart with the inverse of another. Smooth compatibility is a property of this map.

### fiber-bundles/smooth-atlas

A covering by charts with smooth coordinate changes; maximal atlases and smooth manifolds are built later. Euclidean C-infinity calculus is assumed.

### fiber-bundles/smooth-compatibility-of-charts-and-atlases

The entry covers both chart and atlas compatibility. Its core specifies smooth coordinate changes directly; it need not depend on manifold diffeomorphisms.

### fiber-bundles/maximal-smooth-atlas

Maximality is a condition on a smooth atlas relative to compatibility of charts. A chosen smooth structure is introduced afterward.

### fiber-bundles/smooth-structure

The maximal-atlas definition and compatible-atlas formulation cover the entry without requiring the resulting smooth manifold.

### fiber-bundles/smooth-manifold

Restore the underlying topological manifold, alongside the existing smooth atlas data. Lie groups and tangent bundles are examples or subsequent constructions.

### fiber-bundles/smooth-map

A map between smooth manifolds is tested in coordinate charts. Its differential and pullbacks are subsequent constructions. Euclidean C-infinity calculus is assumed.

### fiber-bundles/lie-group

Restore the abstract group required by the definition. Translations and their diffeomorphism property follow from smooth group operations.

### fiber-bundles/lie-bracket

A bracket is an alternating bilinear operation satisfying Jacobi; linearity in each argument is sufficient. Vector fields and Lie groups are realizations of the abstract operation.

### lie-groups/lie-algebra

A vector space with a specified Lie bracket. The bracket entry is now abstract and no longer imports differential geometry into this definition.

### fiber-bundles/local-trivialization

The definition uses a bundle and a diffeomorphism to a local product. Transition functions, equivariant versions, and constructions from sections are downstream.

### fiber-bundles/vector-bundle

Restore the linear algebra behind vector fibers and fiberwise linear isomorphisms. Tangent bundles and connection theory are examples or later constructions.

### fiber-bundles/principal-g-bundle

The statement requires a surjective submersion and group action in addition to smooth local products. Connections and holonomy remain downstream.
