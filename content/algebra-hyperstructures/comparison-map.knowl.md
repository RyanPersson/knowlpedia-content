+++
id = "algebra-hyperstructures/comparison-map"
title = "Comparison map for semirings, hyperrings, and blueprints"
kind = "comparison"
summary = "A guide to the functors and non-equivalences among semirings, hyperstructures, tracts, and ordered blueprints."
aliases = ["hyperstructure comparison map", "semiring hyperfield blueprint comparison"]
domains = ["algebra-hyperstructures", "algebra-rings", "algebraic-geometry-foundations"]
section_mode = "progressive"
+++

The standard coefficient structures in tropical and matroid geometry are connected by functors, not by a blanket chain of equivalences.

- Commutative monoids and commutative [[algebra-rings/semiring|semirings]] embed fully faithfully into [[algebraic-geometry-foundations/blueprint|blueprints]].
- Blueprints embed into [[algebraic-geometry-foundations/ordered-blueprint|ordered blueprints]] by replacing each equality with inequalities in both directions.
- [[algebraic-geometry-foundations/hyperrings-as-ordered-blueprints|Hyperrings embed fully faithfully into ordered blueprints]] by encoding \(a\in b\boxplus c\) as \(a\leq b+c\).
- Fields, [[algebra-hyperstructures/partial-field|partial fields]],
  [[algebra-hyperstructures/hyperfield|hyperfields]], and
  [[algebra-hyperstructures/partial-hyperfield|partial hyperfields]] have
  associated [[algebra-hyperstructures/tract|tracts]]; the first three also
  have canonical [[algebra-hyperstructures/pasture|pasture]] avatars.
- Tracts admit ordered-blueprint avatars, but the comparison with ordered blueprints is not an equivalence on the whole categories.

## Tropical objects: same carrier, different addition

The [[algebra-rings/tropical-semifield|tropical semifield]] and the [[algebra-hyperstructures/tropical-hyperfield|tropical hyperfield]] can use the same underlying set and multiplication. Their additions differ: the semifield has single-valued idempotent addition, whereas equal summands in the hyperfield produce a whole lower interval (with the direction depending on max-plus or min-plus convention). See [[algebra-hyperstructures/tropical-hyperfield-versus-semifield|the direct comparison]].

More generally, idempotent semifields correspond to
[[algebra-groups/lattice-ordered-abelian-group|lattice-ordered abelian
groups]] after adjoining a bottom element.
[[algebra-hyperstructures/valuative-hyperfield|Valuative hyperfields]]
instead use a **totally** ordered abelian group and replace tied joins by a
multivalued lower interval. These are related constructions, not equivalent
categories of coefficient objects.

## A safe reading rule

An embedding says that the source can be represented faithfully inside the target; it does not say every target object comes from the source. An adjunction supplies universal comparison maps; it does not by itself supply an equivalence. Claims of equivalence apply only to explicitly described essential images or restricted subcategories.

## References

- Matthew Baker and Oliver Lorscheid, [*The moduli space of matroids*, Theorem 2.21](https://arxiv.org/abs/1809.03542).
- Oliver Lorscheid, [*A unifying approach to tropicalization*](https://arxiv.org/abs/1508.07949).
