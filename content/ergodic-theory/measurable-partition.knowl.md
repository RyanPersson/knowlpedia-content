+++
id = "ergodic-theory/measurable-partition"
title = "Finite measurable partition"
kind = "definition"
summary = "A finite list of measurable cells covering a probability space modulo null sets."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["probability/probability-space", "shared-foundations/partition"]
+++

A **finite measurable partition** \(\mathcal P=\{P_1,\ldots,P_r\}\) of a [[probability/probability-space|probability space]] consists of measurable cells that are disjoint and cover the space modulo null sets. Cells of measure zero may be discarded. The join \(\mathcal P\vee\mathcal Q\) has cells \(P\cap Q\), and \(T^{-1}\mathcal P\) has cells \(T^{-1}P\).

## Orbit names

The joined partition \(\mathcal P^{(n)}=\bigvee_{j=0}^{n-1}T^{-j}\mathcal P\) records the first \(n\) cell labels of an orbit. Its cell \(\mathcal P^{(n)}(x)\) is the set of points with the same first \(n\) labels as \(x\). These finite observations underlie dynamical entropy.
