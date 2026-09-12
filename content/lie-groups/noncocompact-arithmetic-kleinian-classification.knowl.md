+++
id = "lie-groups/noncocompact-arithmetic-kleinian-classification"
title = "Noncocompact arithmetic Kleinian groups"
kind = "theorem"
summary = "Every noncocompact arithmetic Kleinian group is commensurable up to conjugacy with a Bianchi group."
aliases = []
domains = ["lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/arithmetic-kleinian-group", "lie-groups/uniform-lattice", "algebra-groups/bianchi-group", "algebra-groups/commensurable-subgroups", "algebra-rings/split-quaternion-algebra"]
+++

Let \(\Gamma\le\operatorname{PSL}_2(\mathbb C)\) be an [[lie-groups/arithmetic-kleinian-group|arithmetic Kleinian group]]. Then \(\Gamma\backslash\mathbb H^3\) is noncompact if and only if \(\Gamma\) is [[algebra-groups/commensurable-subgroups|commensurable up to conjugacy]] with a [[algebra-groups/bianchi-group|Bianchi group]] \(\operatorname{PSL}_2(\mathcal O_K)\) for an imaginary quadratic field \(K\).

Finite covolume is built into the arithmetic class used here. The statement does not apply to an arbitrary discrete group merely because some of its matrices have algebraic entries.

## Why imaginary quadratic fields appear

The noncompact arithmetic case has split quaternion algebra \(M_2(K)\). A split algebra cannot be ramified at a real place, so the required real-place ramification forces \(K\) to have no real embeddings. Exactly one complex pair then makes \([K:\mathbb Q]=2\).

Orders in that split algebra give the same commensurability class as \(M_2(\mathcal O_K)\). Conversely, finite-index passage and conjugacy preserve compactness or noncompactness of these finite-volume quotients.

## What the result does not assert

Commensurability is weaker than equality or conjugacy of the full groups. It does not identify all the groups in one class with a single Bianchi group.

## References

1. F. W. Gehring, C. Maclachlan, G. J. Martin, and A. W. Reid, *Arithmeticity, discreteness and volume*, Transactions of the AMS 349 (1997). [Author-hosted paper](https://math.rice.edu/~ar99/ADV.pdf), §4 and the split-algebra criterion used in the proof of Lemma 9.6.
2. D. D. Long, C. Maclachlan, and A. W. Reid, *Arithmetic Fuchsian Groups of Genus Zero*, §3.1, p. 5 of the linked version: Kleinian construction and compactness criterion. [Author-hosted paper](https://math.rice.edu/~ar99/genus0_final.pdf).
