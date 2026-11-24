+++
id = "analytic-number-theory/galois-character"
title = "Character of an abelian number field"
kind = "definition"
summary = "A one-dimensional complex character of the finite Galois group of an abelian extension."
aliases = ["Galois character", "characters of a field"]
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/galois-group", "algebra-groups/group-homomorphism"]
+++

For a finite abelian extension \(E/\mathbb Q\), a **complex Galois character** is a [[algebra-groups/group-homomorphism|homomorphism]] from its [[algebra-fields-galois/galois-group|Galois group]] to the nonzero complex numbers, \(\chi:\operatorname{Gal}(E/\mathbb Q)\to\mathbb C^\times\). Its argument is an automorphism of \(E\). At an unramified prime \(p\), the associated prime weight is \(\chi(\operatorname{Frob}_p)\), the value at the [[algebra-fields-galois/frobenius-unramified|Frobenius element]].

## A two-element example

For \(E=\mathbb Q(i)\), the [[algebra-fields-galois/galois-group|Galois group]] consists of the identity and complex conjugation. The nontrivial character takes the values \(1,-1\). At an odd prime it gives \(1\) when the prime splits in \(E\) and \(-1\) when it is [[arithmetic-geometry/inert-prime|inert]]. These are the values of the nonprincipal [[analytic-number-theory/dirichlet-character|Dirichlet character]] modulo \(4\).
