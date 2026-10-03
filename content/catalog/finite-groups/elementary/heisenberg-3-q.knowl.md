+++
id = "catalog/finite-groups/elementary/heisenberg-3-q"
title = "Finite Heisenberg group H_3(F_q)"
kind = "definition"
summary = "Triples over F_q with a bilinear central term in the multiplication."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["algebra-groups/group", "algebra-fields-galois/finite-field"]
dependency_heuristic = "finite-elementary-semantic-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(q=p^f\), with \(p\) prime and \(f\geq1\) an integer, and let \(\mathbb F_q\) be the [[algebra-fields-galois/finite-field|field of order \(q\)]]. The **finite Heisenberg group \(H_3(\mathbb F_q)\)** is \(\mathbb F_q^3\times\mathbb F_q^3\times\mathbb F_q\), with multiplication
\[
(x,y,z)(x',y',z')=(x+x',y+y',z+z'+x\cdot y'),
\]
where \(x\cdot y'\) is the usual coordinate dot product. This formula works in every characteristic.

## Order and group law

The order is \(q^7\), the identity is \((0,0,0)\), and the inverse of \((x,y,z)\) is \((-x,-y,-z+x\cdot y)\). Bilinearity of the dot product verifies associativity.

## Center and nonsimplicity

Using \([g,h]=ghg^{-1}h^{-1}\), the commutator is
\[
[(x,y,z),(x',y',z')]=(0,0,x\cdot y'-x'\cdot y).
\]
The center is exactly \(\{(0,0,z):z\in\mathbb F_q\}\): commuting with every \((x',y',0)\) forces both \(x=0\) and \(y=0\). It is nontrivial and proper, so the group is not simple. The displayed commutators fill the center; consequently the group is nonabelian of nilpotency class two.
