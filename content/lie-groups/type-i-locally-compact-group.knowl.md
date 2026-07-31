+++
id = "lie-groups/type-i-locally-compact-group"
title = "Type I locally compact group"
kind = "definition"
summary = "A locally compact group is type I when its full group C*-algebra is a type I C*-algebra."
aliases = ["type I group", "postliminal group"]
domains = ["lie-groups", "harmonic-analysis", "operator-algebras"]
section_mode = "progressive"
+++

A [[topology/locally-compact-group|locally compact group]] \(G\) is a **type I
locally compact group** if its [[operator-algebras/full-group-cstar-algebra|full group \(C^*\)-algebra]] \(C^*(G)\) is a
[[operator-algebras/type-i-cstar-algebra|type I \(C^*\)-algebra]]. Equivalently,
every [[operator-algebras/factorial-representation|factor representation]] of
\(G\) generates a [[operator-algebras/type-i-factor|type I factor]], or every
factor representation is a Hilbert-space multiple of an irreducible
representation [Bekka–de la Harpe, §6.D].
The definition itself does not require second countability, but separability
or second-countability hypotheses are normally added when using measurable
disintegration over the [[harmonic-analysis/unitary-dual|unitary dual]].

## Representation-theoretic consequence

For a second-countable type I group, the unitary dual has the standard Borel
regularity needed for decomposition theory, and unitary representations admit
essentially unique direct-integral decompositions into irreducibles with
multiplicity data. Without the type I hypothesis, central decomposition into
factor representations remains available in suitable separable settings, but
those factors need not be irreducible multiples and decomposition into
irreducibles need not give a workable measurable classification
[Folland, §7.4].

## Examples and non-examples

Abelian and compact locally compact groups are type I. Connected nilpotent Lie
groups and the standard classes of
[[lie-groups/real-reductive-lie-group|real reductive Lie groups]] are major
noncompact examples. In contrast, the [[algebra-groups/free-group|free group]] on two generators, with the
discrete topology, is not type I; more generally, a countable discrete group
is type I exactly when it is virtually abelian
[Bekka–de la Harpe, §8.B and Theorem 8.F.3].
These examples show that amenability alone does not characterize the type I
property.

## Conventions and scope

**Warning.** “Type I group” refers to the full group \(C^*\)-algebra, not to
the [[operator-algebras/group-von-neumann-algebra|group von Neumann algebra]] of the
[[harmonic-analysis/regular-representations-locally-compact-group|regular representation]]. The latter can have a different Murray–von Neumann type. Nor
is the reduced group \(C^*\)-algebra an interchangeable replacement in the
definition.

## References

1. Jacques Dixmier, *\(C^*\)-Algebras*, North-Holland Mathematical Library 15, North-Holland, 1977. [Publisher record](https://www.sciencedirect.com/bookseries/north-holland-mathematical-library/vol/15/suppl/C). Relevant: §§9.1 and 13.9 on type I algebras and representations, and §18.8 on unitary representations and disintegration.
2. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: §7.4 on type I groups and direct-integral decomposition.
3. Bachir Bekka and Pierre de la Harpe, *Unitary Representations of Groups, Duals, and Characters*, Mathematical Surveys and Monographs 250, American Mathematical Society, 2020. [AMS record](https://bookstore.ams.org/SURV/250). Relevant: §6.D on type I representations, §8.B on type I groups, and Theorem 8.F.3 on discrete groups.
