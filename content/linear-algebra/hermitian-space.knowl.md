+++
id = "linear-algebra/hermitian-space"
title = "Hermitian space over a field with involution"
kind = "definition"
summary = "A vector space with a nondegenerate conjugate-symmetric sesquilinear form."
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/vector-space", "algebra-fields-galois/field-automorphism"]
+++

Let \(E\) be a field with an [[algebra-fields-galois/field-involution|involution]] \(a\mapsto\bar a\). A **Hermitian space** is a finite-dimensional [[linear-algebra/vector-space|vector space]] \(V/E\) with a form \(h:V\times V\to E\) additive in each variable, satisfying \(h(au,bv)=\bar a b\,h(u,v)\), \(h(v,u)=\overline{h(u,v)}\), and \(h(u,V)=0\Rightarrow u=0\).

## A unitary group

The unitary group consists of the \(E\)-linear automorphisms \(g\) for which \(h(gu,gv)=h(u,v)\). At a complex place a positive definite \(h\) gives an [[linear-algebra/inner-product-space|inner product space]]. Mixed signatures also occur.
