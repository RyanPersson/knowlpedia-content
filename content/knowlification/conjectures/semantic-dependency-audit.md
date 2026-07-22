# Semantic dependency audit

## Pass one: conjecture posts

The twelve first-pass posts were compared against the pre-change inventory of 2,140 knowls by ID, title, aliases, summary, and targeted body search. Existing matches were reused even when they lived outside the conjecture's apparent domain; examples include `fiber-bundles/lie-group`, `quantum-foundations/bounded-operator-hilbert`, and `algebra-representation-theory/group-algebra`.

The pass identified 33 missing prerequisite definitions. They cover topology and actions, arithmetic, semialgebraic geometry, Banach/Hilbert geometry, quantum measurement, complex geometry, torsion-free groups, and the triangle-axiom chain. Central objects such as MUB and SIC-POVM remain defined directly in their conjecture pages rather than duplicated as parallel glossary entries.

## Pass two: definitions introduced by pass one

Each new definition was reread for undeclared semantic prerequisites. Eight further knowls were added: initial object, closed manifold, orthogonal complement, orthogonal projection, positive semidefinite operator, holomorphic map, integrable almost-complex structure, and mapping cone. These additions were linked back into the first-pass definitions.

The recursive boundary was then judged using the “smallest sufficient definition” rule. Elementary set-theoretic words and incidental contextual nouns were not expanded into an unbounded glossary. Existing foundational knowls were linked where they materially clarify a definition.

## Link review

The conjecture pages produced 63 candidate links. Every candidate received an accept/reject decision; 28 were applied. A post-application audit found no unreviewed candidate. The definition layer received 22 additional high-confidence links across 19 files. Wrong-sense matches were explicitly rejected, notably algebraic separability versus topological separability, categorical limits versus the inverse limit defining \(\mathbb Z_p\), and categorical endomorphisms versus tangent-bundle endomorphisms.

## Completion criteria

- Every conjecture has an axiom-first source page and linked final page.
- Every essential first-order dependency resolves to a pre-existing or newly created knowl.
- Every essential second-order dependency found during review resolves.
- New knowls appear in both the temporary review index and their permanent domain indexes.
- Candidate decisions are preserved in JSON/JSONL ledgers for reproducibility.
