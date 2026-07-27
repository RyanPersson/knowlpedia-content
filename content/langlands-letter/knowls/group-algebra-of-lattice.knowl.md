+++
id = "langlands-letter/knowls/group-algebra-of-lattice"
title = "Group Algebra of a Lattice and Multiplicative Basis"
kind = "knowl"
summary = "The complex algebra with basis indexed by a lattice and multiplication induced by the lattice addition law."
aliases = ["group-algebra-of-lattice", "Group Algebra of a Lattice and Multiplicative Basis"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/group-algebra-of-lattice.md"
+++

Let $L$ be a free abelian group, called a **lattice**; for example, $L=X^*(T)$.

The **group algebra** $\mathbb C[L]$ is the $\mathbb C$-vector space with basis $\{\xi_\lambda\}_{\lambda\in L}$ and multiplication
$$
\xi_\lambda\cdot \xi_\mu=\xi_{\lambda+\mu}.
$$

When $L=X^*(T)$ is the [[langlands-letter/knowls/maximal-torus-weight-lattice|character lattice]] of a torus, each $t\in T(\mathbb C)$ defines an algebra homomorphism
$$
\mathbb C[L]\longrightarrow\mathbb C,\qquad \xi_\lambda\longmapsto\lambda(t).
$$

## Remarks

**In the letter:** Satake identifies the spherical Hecke algebra with invariants in such a group algebra on a dual lattice.
