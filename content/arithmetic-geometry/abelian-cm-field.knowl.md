+++
id = "arithmetic-geometry/abelian-cm-field"
title = "Abelian CM field"
kind = "definition"
summary = "A CM field that is Galois over the rational numbers with abelian Galois group."
aliases = ["abelian CM extension of the rationals"]
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["arithmetic-geometry/cm-field", "algebra-fields-galois/galois-extension", "algebra-groups/abelian-group"]
+++

An **abelian CM field** is a [[arithmetic-geometry/cm-field|CM field]] \(E\) such that \(E/\mathbb Q\) is [[algebra-fields-galois/galois-extension|Galois]] and its [[algebra-fields-galois/galois-group|Galois group]] is [[algebra-groups/abelian-group|abelian]]. Every pair of field automorphisms over \(\mathbb Q\) therefore commutes.

## The fifth roots of unity

Let \(\zeta_5\) be a [[algebra-fields-galois/primitive-root-of-unity|primitive fifth root of unity]]. The [[algebra-fields-galois/cyclotomic-extension|cyclotomic field]] \(E=\mathbb Q(\zeta_5)\) has four automorphisms, given by \(\zeta_5\mapsto\zeta_5^a\) for \(a=1,2,3,4\). Composition multiplies the exponents modulo \(5\). Complex conjugation sends \(\zeta_5\) to \(\zeta_5^{-1}\), and its fixed field is the totally real field \(\mathbb Q(\zeta_5+\zeta_5^{-1})=\mathbb Q(\sqrt5)\).
