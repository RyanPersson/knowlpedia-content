+++
id = "posts/module-theory-learning-path"
title = "Modules"
kind = "page"
summary = "Lecture notes on modules over a ring: submodules and quotients, free modules, exact sequences, Hom and tensor products, projective and injective modules, modules over a PID, canonical forms, chain conditions, and semisimplicity."
aliases = ["module-theory-learning-path", "Module theory learning path", "Module theory lecture notes"]
domains = ["posts", "algebra-modules"]
knowls_open = true
learning_path = true
prerequisites = []
dependency_review_count = 0
+++

A module is a vector space whose scalars come from a ring instead of a field. That single change produces a theory that contains linear algebra, the theory of abelian groups, and the theory of ideals as special cases, and it is the language of most of modern algebra.

## Contents

- [0. Background from ring theory](/posts/module-theory-learning-path/#0-background-from-ring-theory)
- [1. Modules](/posts/module-theory-learning-path/#1-modules)
- [2. Submodules, homomorphisms, and quotients](/posts/module-theory-learning-path/#2-submodules-homomorphisms-and-quotients)
- [3. Generators, direct sums, and free modules](/posts/module-theory-learning-path/#3-generators-direct-sums-and-free-modules)
- [4. Torsion](/posts/module-theory-learning-path/#4-torsion)
- [5. Exact sequences](/posts/module-theory-learning-path/#5-exact-sequences)
- [6. Hom and duality](/posts/module-theory-learning-path/#6-hom-and-duality)
- [7. Projective and injective modules](/posts/module-theory-learning-path/#7-projective-and-injective-modules)
- [8. Tensor products](/posts/module-theory-learning-path/#8-tensor-products)
- [9. Algebras](/posts/module-theory-learning-path/#9-algebras)
- [10. Modules over a principal ideal domain](/posts/module-theory-learning-path/#10-modules-over-a-principal-ideal-domain)
- [11. Canonical forms](/posts/module-theory-learning-path/#11-canonical-forms)
- [12. Chain conditions and composition series](/posts/module-theory-learning-path/#12-chain-conditions-and-composition-series)
- [13. Semisimple modules and rings](/posts/module-theory-learning-path/#13-semisimple-modules-and-rings)
- [14. Tools over commutative rings](/posts/module-theory-learning-path/#14-tools-over-commutative-rings)
- [15. Looking ahead: resolutions, Ext, and Tor](/posts/module-theory-learning-path/#15-looking-ahead-resolutions-ext-and-tor)

## Conventions

Throughout, every ring has an identity element \(1\), ring homomorphisms send \(1\) to \(1\), and every module is **unital**: \(1m=m\) for all \(m\). Knowlpedia's general definition of a ring does not require an identity, so several boxes below say "ring" where these notes always mean "ring with identity".

An \(R\)-module is a left \(R\)-module unless right modules are named explicitly. Right modules are needed only for tensor products in Section 8. When \(R\) is commutative, left and right modules are the same thing.

Some constructions need extra hypotheses on \(R\). The module \(\operatorname{Hom}_R(M,N)\), bilinear maps, the tensor product of two left modules, and algebras need \(R\) commutative. Torsion needs an integral domain, and Sections 10 and 11 need a principal ideal domain. Each section states its hypotheses.

The words homomorphism, \(R\)-linear map, and \(R\)-map mean the same thing. The set of homomorphisms from \(M\) to \(N\) is written \(\operatorname{Hom}_R(M,N)\), and \(\operatorname{End}_R(M)=\operatorname{Hom}_R(M,M)\).

## 0. Background from ring theory

The module definitions depend directly on the following ring-theoretic notions. Further background, such as integral domains, polynomial rings, and principal ideal domains, appears where it is first used.

**Background 0.1.** [[algebra-rings/ring|Ring]]

**Background 0.2.** [[algebra-rings/unital-ring|Unital ring]]

**Background 0.3.** [[algebra-rings/commutative-ring|Commutative ring]]

**Background 0.4.** [[algebra-rings/ring-homomorphism|Ring homomorphism]]

**Background 0.5.** [[algebra-rings/ideal|Ideal]]

**Remark.** For a noncommutative ring the three kinds of ideal differ. Left ideals are exactly the submodules of \(R\) viewed as a left module over itself (Section 2), and two-sided ideals are exactly the kernels of ring homomorphisms.

## 1. Modules

A vector space is an abelian group on which a field acts by scalar multiplication. A module is the same structure with the field replaced by an arbitrary ring. Three familiar theories become special cases: vector spaces (modules over a field), abelian groups (modules over \(\mathbb Z\)), and ideals (submodules of a ring over itself).

**Definition 1.1.** [[algebra-modules/module|Module]]

**Remark.** In these notes the axiom \(1m=m\) always holds. Without it, every abelian group with the zero action \(rm=0\) would be a module, which is of no use.

**Elementary consequences.** The axioms give \(0_R\,m=0_M\), \(r\,0_M=0_M\) and \((-r)m=-(rm)=r(-m)\) for all \(r\in R\) and \(m\in M\). For instance, \(0m=(0+0)m=0m+0m\), and cancelling in the group \((M,+)\) gives \(0m=0\). Unlike in a vector space, \(rm=0\) does not force \(r=0\) or \(m=0\): in the \(\mathbb Z\)-module \(\mathbb Z/6\mathbb Z\), \(2\cdot 3=0\).

**Modules as ring homomorphisms.** For each \(r\in R\), the map \(\lambda_r\colon M\to M\), \(m\mapsto rm\), is an endomorphism of the abelian group \((M,+)\), because \(r(m+n)=rm+rn\). The remaining axioms say that
\[
\lambda\colon R\longrightarrow \operatorname{End}_{\mathbb Z}(M),\qquad r\longmapsto\lambda_r,
\]
is a ring homomorphism with \(\lambda_1=\mathrm{id}_M\). Here \(\operatorname{End}_{\mathbb Z}(M)\) is the ring of group endomorphisms of \(M\) under pointwise addition and composition, and \((rs)m=r(sm)\) is the statement \(\lambda_{rs}=\lambda_r\circ\lambda_s\). Conversely, a ring homomorphism \(\varphi\colon R\to\operatorname{End}_{\mathbb Z}(M)\) with \(\varphi(1)=\mathrm{id}_M\) defines a module structure by \(rm=\varphi(r)(m)\). A module structure on an abelian group is therefore the same thing as a ring homomorphism into its endomorphism ring, just as a group action on a set is a homomorphism into its symmetric group.

**Examples.** The following modules recur throughout the notes.

1. Every ring \(R\) is a left module over itself by left multiplication. This is the **left regular module**, also written \({}_RR\).
2. Every abelian group is a \(\mathbb Z\)-module in exactly one way, with \(n\cdot m=m+\cdots+m\) (\(n\) terms) for \(n>0\). Abelian groups and \(\mathbb Z\)-modules are the same thing.
3. A module over a field \(F\) is an \(F\)-vector space.
4. The set \(R^n\) of column vectors is an \(R\)-module under coordinatewise operations, and it is also a left module over the matrix ring \(M_n(R)\) by matrix multiplication.
5. A vector space together with a linear operator is a module over a polynomial ring, as the next two items explain. This example connects module theory to linear algebra, and Section 11 is built on it.

**Background 1.2.** [[algebra-rings/polynomial-ring|Polynomial ring]]

**Definition 1.3.** [[algebra-modules/polynomial-module-from-operator|Polynomial module of an operator]]

Write \(V_T\) for this \(F[x]\)-module. The construction can be reversed. An \(F[x]\)-module \(V\) is an \(F\)-vector space through the action of the constants, and \(T(v)=x\cdot v\) is an \(F\)-linear operator on \(V\). The two constructions are inverse to each other, so an \(F[x]\)-module is the same thing as a vector space with a chosen operator. Submodules of \(V_T\) are the \(T\)-invariant subspaces, and homomorphisms \(V_T\to W_S\) are the linear maps \(u\) with \(uT=Su\).

**Example.** Let \(T\) be the operator on \(F^2\) with \(Te_1=e_2\) and \(Te_2=0\). Then \(x\cdot e_1=e_2\) and \(x^2\cdot e_1=0\), so every element of \(V_T\) has the form \((a+bx)\cdot e_1\). The module \(V_T\) is generated by the single element \(e_1\), and the polynomials that kill \(e_1\) are exactly the multiples of \(x^2\).

**Construction 1.4.** [[algebra-commutative/restriction-of-scalars|Restriction of scalars]]

The box states this for commutative rings, but the construction works for any ring homomorphism \(\varphi\colon R\to S\) with \(\varphi(1)=1\). Every \(F[x]\)-module becomes an \(F\)-vector space by restriction along \(F\hookrightarrow F[x]\). Every \(R\)-module becomes an abelian group by restriction along the unique ring homomorphism \(\mathbb Z\to R\). A ring \(S\) containing \(R\) as a subring is an \(R\)-module, for example \(\mathbb C\) as a real vector space or \(F[x]\) as an \(F\)-vector space with basis \(1,x,x^2,\dots\). An \(R\)-module \(M\) with \(IM=0\) for a two-sided ideal \(I\) is the restriction of a unique \(R/I\)-module along the quotient map \(R\to R/I\).

### Exercises for Section 1

1. Show that \(r\,0=0\) and \((-1)m=-m\) in every module, and give an example of a module in which \(rm=0\) with \(r\neq0\) and \(m\neq0\).
2. Show that an abelian group has exactly one structure of a \(\mathbb Z\)-module.
3. Let \(n\ge1\). Show that a \(\mathbb Z/n\mathbb Z\)-module is the same thing as an abelian group \(M\) with \(nM=0\).
4. Let \(T\) be the operator on \(F^3\) with \(Te_1=e_2\), \(Te_2=e_3\) and \(Te_3=0\). Show that the \(F[x]\)-module \(V_T\) is generated by \(e_1\), and find all of its submodules.
5. Let \(R^{\mathrm{op}}\) be the ring with the same addition as \(R\) and multiplication \(a\ast b=ba\). Show that a right \(R\)-module is the same thing as a left \(R^{\mathrm{op}}\)-module.

## 2. Submodules, homomorphisms, and quotients

The constructions of this section work exactly as for vector spaces or groups: subobjects, structure-preserving maps, kernels and images, quotients, and the isomorphism theorems. The only new requirement is closure under multiplication by every ring element.

**Definition 2.1.** [[algebra-modules/submodule|Submodule]]

**Proposition 2.2.** [[algebra-modules/submodule-criterion|Submodule criterion]]

In practice a one-step test is faster: a subset \(N\subseteq M\) is a submodule if and only if \(N\neq\varnothing\) and \(x+ry\in N\) for all \(x,y\in N\) and \(r\in R\). Conversely, suppose \(N\) is nonempty and closed under \(x+ry\), and pick \(y\in N\). Then \(y+(-1)y=0\in N\), so \(ry=0+ry\in N\) and \(x-y=x+(-1)y\in N\).

**Operations on submodules.** The intersection of any family of submodules is a submodule. The union of two submodules usually is not. The **sum** \(N_1+N_2=\{n_1+n_2:n_i\in N_i\}\) is the smallest submodule containing both. For a subset \(S\subseteq M\), the **submodule generated by \(S\)** is
\[
RS=\{r_1s_1+\cdots+r_ks_k : k\ge0,\ r_i\in R,\ s_i\in S\},
\]
the set of finite \(R\)-linear combinations of elements of \(S\). It is the intersection of all submodules containing \(S\), since \(1\in R\) gives \(S\subseteq RS\). For a single element, \(Rm=\{rm:r\in R\}\).

In the left regular module \({}_RR\), the submodules are exactly the left ideals. For \(R=\mathbb Z\) the submodules are exactly the subgroups, and in \(V_T\) they are the \(T\)-invariant subspaces.

**Definition 2.3.** [[algebra-modules/module-homomorphism|Module homomorphism]]

An **isomorphism** is a bijective homomorphism, and its inverse map is automatically a homomorphism. For \(\mathbb Z\)-modules the homomorphisms are the group homomorphisms, and for vector spaces they are the linear maps. If \(r\) is central in \(R\), for instance when \(R\) is commutative, then \(m\mapsto rm\) is an endomorphism of every module. For noncommutative \(R\), right multiplication \(x\mapsto xa\) is an endomorphism of \({}_RR\) for each \(a\in R\), while left multiplication \(x\mapsto ax\) need not be.

**Definition 2.4.** [[algebra-modules/kernel-module|Kernel]]

**Proposition 2.5.** [[algebra-modules/kernels-are-submodules|Kernels are submodules]]

**Definition 2.6.** [[algebra-modules/image-module|Image]]

More generally, if \(f\colon M\to N\) is a homomorphism, then \(f(M')\) is a submodule of \(N\) for every submodule \(M'\subseteq M\), and \(f^{-1}(N')\) is a submodule of \(M\) for every submodule \(N'\subseteq N\).

**Definition 2.7.** [[algebra-modules/quotient-module|Quotient module]]

Closure under scalars is what makes the action on cosets well defined: if \(m-m'\in N\), then \(rm-rm'=r(m-m')\in N\). The quotient map \(\pi\colon M\to M/N\), \(m\mapsto m+N\), is a surjective homomorphism with kernel \(N\), so every submodule is a kernel.

**Example.** For a left ideal \(I\) of \(R\), the quotient \(R/I\) is a left \(R\)-module generated by \(1+I\). For a monic polynomial \(f\in F[x]\) of degree \(d\), the \(F[x]\)-module \(F[x]/(f)\) has \(F\)-basis \(1,x,\dots,x^{d-1}\), and multiplication by \(x\) is a linear operator on this \(d\)-dimensional space. Section 11 returns to this operator.

**Proposition 2.8.** [[algebra-modules/quotient-module-universal-property|Universal property of quotient modules]]

**Theorem 2.9.** [[algebra-modules/first-isomorphism-theorem-modules|First isomorphism theorem]]

**Proof sketch.** Apply Proposition 2.8 to the submodule \(\ker f\subseteq M\) to obtain \(\bar f\colon M/\ker f\to N\) with \(\bar f(m+\ker f)=f(m)\). Its image is \(\operatorname{im} f\), and it is injective because \(\bar f(m+\ker f)=0\) means \(m\in\ker f\).

**Example.** Let \(c\in F\), and let \(F_c\) be the field \(F\) made into an \(F[x]\)-module by letting \(x\) act as multiplication by \(c\). Evaluation \(p\mapsto p(c)\) is a surjective \(F[x]\)-linear map \(F[x]\to F_c\), because \((xp)(c)=c\,p(c)\). Its kernel is the ideal \((x-c)\), so \(F[x]/(x-c)\cong F_c\) as \(F[x]\)-modules. The module structure matters here: as \(F[x]\)-modules, \(F_c\) and \(F_d\) are not isomorphic when \(c\neq d\), although both are the same one-dimensional vector space.

**Theorem 2.10.** [[algebra-modules/second-isomorphism-theorem-modules|Second isomorphism theorem]]

**Theorem 2.11.** [[algebra-modules/third-isomorphism-theorem-modules|Third isomorphism theorem]]

**Theorem 2.12.** [[algebra-modules/correspondence-theorem-modules|Correspondence theorem]]

**Example.** Let \(n\ge1\). The submodules of the \(\mathbb Z\)-module \(\mathbb Z/n\mathbb Z\) correspond to the subgroups \(d\mathbb Z\) of \(\mathbb Z\) that contain \(n\mathbb Z\), that is, to the positive divisors \(d\) of \(n\). So \(\mathbb Z/n\mathbb Z\) has exactly one submodule for each positive divisor of \(n\).

### Exercises for Section 2

1. Show that the union of two submodules is a submodule if and only if one of them contains the other.
2. (Modular law.) Let \(A\subseteq C\) and \(B\) be submodules of \(M\). Show that \(A+(B\cap C)=(A+B)\cap C\).
3. Use the correspondence theorem to find all submodules of the \(F[x]\)-module \(F[x]/(x^3)\).
4. Let \(c,d\in F\). Show that \(F[x]/(x-c)\cong F[x]/(x-d)\) as \(F[x]\)-modules if and only if \(c=d\).
5. Let \(f\colon M\to N\) be a homomorphism and \(N'\subseteq N\) a submodule. Show that \(f\) induces an injective homomorphism \(M/f^{-1}(N')\to N/N'\).

## 3. Generators, direct sums, and free modules

A vector space has a basis, any two bases have the same size, and every vector space is a direct sum of copies of the field. Over a ring each of these statements fails in general. This section introduces the language for describing how a module is built from smaller pieces, and identifies the modules that do behave like vector spaces: the free modules.

**Definition 3.1.** [[algebra-modules/annihilator-element|Annihilator of an element]]

**Definition 3.2.** [[algebra-modules/cyclic-module|Cyclic module]]

The map \(R\to Rm\), \(r\mapsto rm\), is a surjective homomorphism with kernel \(\operatorname{ann}(m)\), so \(Rm\cong R/\operatorname{ann}(m)\) by the first isomorphism theorem. The cyclic modules are thus exactly the quotients of \({}_RR\) by left ideals, and a cyclic module is determined up to isomorphism by the annihilator of a generator.

**Definition 3.3.** [[algebra-modules/annihilator-module|Annihilator of a module]]

**Definition 3.4.** [[algebra-modules/finitely-generated-module|Finitely generated module]]

**Definition 3.5.** [[algebra-modules/direct-product-modules|Direct product of modules]]

**Definition 3.6.** [[algebra-modules/direct-sum-modules|Direct sum of modules]]

**Proposition 3.7.** [[algebra-modules/direct-sum-universal-property|Direct sum universal property]]

**Internal direct sums.** Let \(N_1,\dots,N_k\) be submodules of \(M\). The map \(N_1\oplus\cdots\oplus N_k\to M\), \((n_1,\dots,n_k)\mapsto n_1+\cdots+n_k\), is a homomorphism. It is an isomorphism if and only if \(N_1+\cdots+N_k=M\) and each \(N_i\) meets the sum of the others only in \(0\). In that case one writes \(M=N_1\oplus\cdots\oplus N_k\) and calls \(M\) the **internal direct sum** of the \(N_i\). For two submodules the condition is \(N_1+N_2=M\) and \(N_1\cap N_2=0\). A submodule \(N\) is a **direct summand** of \(M\) if \(M=N\oplus N'\) for some submodule \(N'\), called a complement of \(N\).

**Warning.** For three or more submodules, pairwise intersections equal to zero are not enough. Three distinct lines through the origin in \(F^2\) meet pairwise in \(0\) and sum to \(F^2\), but their sum is not direct.

Unlike subspaces of a vector space, submodules need not have complements. The only proper nonzero submodule of the \(\mathbb Z\)-module \(\mathbb Z/4\mathbb Z\) is \(2\mathbb Z/4\mathbb Z\), and it has no complement.

**Definition 3.8.** [[algebra-modules/basis-module|Basis of a free module]]

**Definition 3.9.** [[algebra-modules/free-module|Free module]]

**Proposition 3.10.** [[algebra-modules/free-module-universal-property|Free module universal property]]

Every module is a quotient of a free module. Map the free module on any generating set \(S\) of \(M\) onto \(M\) by sending each basis element to the corresponding element of \(S\). A module generated by \(n\) elements is a quotient of \(R^n\).

**Definition 3.11.** [[algebra-modules/rank-module|Rank of a free module]]

**Free modules are not vector spaces.** Even over \(\mathbb Z\), several familiar facts about bases fail.

1. A minimal generating set need not be a basis. The set \(\{2,3\}\) generates \(\mathbb Z\) and no proper subset does, but it is not a basis since \(3\cdot2-2\cdot3=0\).
2. A linearly independent set need not extend to a basis. The set \(\{2\}\) in \(\mathbb Z\) is an example.
3. A submodule of a free module need not be free. Over \(R=\mathbb Z/6\mathbb Z\), the submodule \(3R=\{0,3\}\) of the free module \(R\) has two elements, while every nonzero free \(R\)-module has at least six.
4. A torsion-free module need not be free. In \(\mathbb Q\), any two nonzero elements \(a/b\) and \(c/d\) satisfy \(bc\cdot(a/b)-ad\cdot(c/d)=0\), so a basis would have one element. But \(\mathbb Q\) is not cyclic.
5. Over a noncommutative ring, rank need not be defined. If \(V\) is a vector space of countably infinite dimension and \(R=\operatorname{End}_F(V)\), then \(R\cong R^2\) as left \(R\)-modules.

Over a principal ideal domain, items 3 and 4 are repaired for finitely generated modules (Section 10).

### Exercises for Section 3

1. Show that a left \(R\)-module is cyclic if and only if it is isomorphic to \(R/I\) for some left ideal \(I\).
2. Show that \(\mathbb Q\) is not a finitely generated \(\mathbb Z\)-module.
3. Show that if \(M=N_1\oplus N_2\) internally, then \(M/N_1\cong N_2\).
4. Let \(I\) be a two-sided ideal. Show that \(\operatorname{ann}_R(R/I)=I\), and deduce that \(\mathbb Z/m\mathbb Z\cong\mathbb Z/n\mathbb Z\) for \(m,n\ge0\) only if \(m=n\).
5. Show that a direct summand of a finitely generated module is finitely generated.

## 4. Torsion

In this section \(R\) is an integral domain. Torsion measures how far multiplication by nonzero scalars is from being injective. In \(\mathbb Z\), \(nm=0\) with \(n\neq0\) forces \(m=0\), while in \(\mathbb Z/n\mathbb Z\) every element is killed by \(n\). Over a principal ideal domain, torsion splits every finitely generated module into a free part and a torsion part (Section 10).

**Background 4.1.** [[algebra-rings/integral-domain|Integral domain]]

**Definition 4.2.** [[algebra-modules/torsion-element|Torsion element]]

**Definition 4.3.** [[algebra-modules/torsion-module|Torsion module]]

**Definition 4.4.** [[algebra-modules/torsion-free-module|Torsion-free module]]

**The torsion submodule.** For a module \(M\) over an integral domain, the set of torsion elements
\[
\operatorname{Tor}(M)=\{m\in M: rm=0\text{ for some }r\neq0\}
\]
is a submodule, called the **torsion submodule** of \(M\). The module \(M\) is torsion exactly when \(\operatorname{Tor}(M)=M\) and torsion-free exactly when \(\operatorname{Tor}(M)=0\). The quotient \(M/\operatorname{Tor}(M)\) is always torsion-free, and homomorphisms carry torsion elements to torsion elements. These facts are standard, and the domain hypothesis is essential, as the next warning shows.

**Warning.** Over a ring with zero divisors, the torsion elements need not form a submodule. In \(R=\mathbb Z/6\mathbb Z\) as a module over itself, \(2\) and \(3\) are killed by the nonzero elements \(3\) and \(2\) respectively, but \(2+3=5\) is a unit and kills nothing.

**Example.** Let \(V\) be a vector space of finite dimension \(n\) and \(T\) an operator on \(V\). The \(n^2+1\) operators \(1,T,\dots,T^{n^2}\) lie in the \(n^2\)-dimensional space of operators, so they are linearly dependent. A dependence relation is a nonzero polynomial \(p\) with \(p(T)=0\), and \(p\) kills every element of \(V_T\). So \(V_T\) is a torsion \(F[x]\)-module.

### Exercises for Section 4

1. Show that a submodule of a torsion-free module is torsion-free, and that a direct sum of torsion-free modules is torsion-free.
2. Show that a free module over an integral domain is torsion-free.
3. Let \(M=\bigoplus_{p}\mathbb Z/p\mathbb Z\), the sum over all primes \(p\). Show that \(M\) is a torsion \(\mathbb Z\)-module with \(\operatorname{ann}_{\mathbb Z}(M)=0\). Then show that a finitely generated module over an integral domain is torsion if and only if its annihilator is nonzero.
4. Let \(M\) be torsion-free and \(r\neq0\). Show that \(m\mapsto rm\) is injective. Is it surjective for \(M=\mathbb Z\)? For \(M=\mathbb Q\)?

## 5. Exact sequences

Exact sequences record how a module is assembled from a submodule and a quotient. They are the bookkeeping device of the rest of the course: projective, injective, and flat modules are defined by how they interact with exact sequences.

**Definition 5.1.** [[algebra-modules/exact-sequence-modules|Exact sequence of modules]]

**Definition 5.2.** [[algebra-modules/cokernel-module|Cokernel]]

**Reading exact sequences.** The sequence \(0\to A\xrightarrow{i}B\) is exact if and only if \(i\) is injective, and \(B\xrightarrow{p}C\to0\) is exact if and only if \(p\) is surjective. Every homomorphism \(f\colon M\to N\) sits in an exact sequence
\[
0\to\ker f\to M\xrightarrow{f}N\to\operatorname{coker} f\to0 .
\]

**Definition 5.3.** [[algebra-modules/short-exact-sequence|Short exact sequence]]

The end terms of a short exact sequence do not determine the middle term. The sequences
\[
0\to\mathbb Z\xrightarrow{\;2\;}\mathbb Z\to\mathbb Z/2\to0
\qquad\text{and}\qquad
0\to\mathbb Z\to\mathbb Z\oplus\mathbb Z/2\to\mathbb Z/2\to0,
\]
the second built from the inclusion of the first summand and the projection onto the second, have the same ends. Their middle terms are not isomorphic, since \(\mathbb Z\) has no nonzero element of finite order and \(\mathbb Z\oplus\mathbb Z/2\) does. Classifying the possible middle terms is the extension problem, which Section 15 returns to. The simplest middle term is the direct sum of the ends, and the next two items characterize when this happens.

**Definition 5.4.** [[algebra-modules/split-exact-sequence|Split exact sequence]]

**Lemma 5.5.** [[algebra-modules/splitting-lemma|Splitting lemma]]

**Proof sketch.** Given a retraction \(r\) with \(ri=\mathrm{id}_A\), every \(b\in B\) decomposes as \(b=i(r(b))+(b-i(r(b)))\). The first term lies in \(\operatorname{im} i\) and the second in \(\ker r\). If \(i(a)\in\ker r\), then \(a=r(i(a))=0\), so \(B=\operatorname{im} i\oplus\ker r\) internally, and \(p\) restricts to an isomorphism \(\ker r\to C\). Given a section \(s\), one argues similarly with \(B=\operatorname{im} i\oplus\operatorname{im} s\).

The two lemmas below are the standard diagram-chasing tools, and both are proved by chasing elements around the diagram. The five lemma is stated in an abelian category. For modules, read its objects as \(R\)-modules, its epimorphisms as surjections, and its monomorphisms as injections.

**Lemma 5.6.** [[algebra-homological/snake-lemma|Snake lemma]]

**Lemma 5.7.** [[algebra-homological/five-lemma|Five lemma]]

The case used most often is the **short five lemma**: in a commutative diagram of two short exact sequences, if the two outer vertical maps are isomorphisms, so is the middle one. In the diagram below the rows are short exact and both squares commute:

```tikz-cd
0 \arrow[r] & A \arrow[r] \arrow[d, "\alpha", "\cong"'] & B \arrow[r] \arrow[d, "\beta"] & C \arrow[r] \arrow[d, "\gamma", "\cong"'] & 0 \\
0 \arrow[r] & A' \arrow[r] & B' \arrow[r] & C' \arrow[r] & 0
```

### Exercises for Section 5

1. Show that every short exact sequence \(0\to A\to B\to F\to0\) with \(F\) free splits.
2. Show that \(0\to\mathbb Z\xrightarrow{n}\mathbb Z\to\mathbb Z/n\to0\) does not split for \(n\ge2\). More generally, show that a short exact sequence of abelian groups \(0\to A\to B\to C\to0\) does not split if \(B\) has no nonzero elements of finite order and \(C\) is finite and nonzero.
3. Let \(0\to A\to B\to C\to0\) be a short exact sequence of abelian groups, let \(n\ge1\), and write \(X[n]=\{x\in X:nx=0\}\). Apply the snake lemma to multiplication by \(n\). Show that the result joins \(0\to A[n]\to B[n]\to C[n]\) and \(A/nA\to B/nB\to C/nC\to0\) by a connecting map \(C[n]\to A/nA\) into one exact sequence.
4. Prove the short five lemma directly by a diagram chase.
5. Show that a short exact sequence \(0\to A\xrightarrow{i}B\to C\to0\) splits if and only if \(i(A)\) is a direct summand of \(B\).

## 6. Hom and duality

Homomorphisms between two modules form an abelian group, and an \(R\)-module when \(R\) is commutative. Fixing one argument gives a functor, and this section records how these functors interact with direct sums and exact sequences. In this section, \(R\) is commutative whenever \(\operatorname{Hom}_R(M,N)\) is treated as an \(R\)-module.

**Definition 6.1.** [[algebra-modules/hom-module|Hom module]]

Commutativity is what makes \(rf\) linear: \((rf)(sm)=r\,f(sm)=rs\,f(m)\), while linearity requires \((rf)(sm)=s\,(rf)(m)=sr\,f(m)\). A homomorphism \(u\colon N\to N'\) induces \(u_\ast\colon\operatorname{Hom}_R(M,N)\to\operatorname{Hom}_R(M,N')\), \(f\mapsto u\circ f\). A homomorphism \(v\colon M'\to M\) induces \(v^\ast\colon\operatorname{Hom}_R(M,N)\to\operatorname{Hom}_R(M',N)\), \(f\mapsto f\circ v\), and this reverses the direction of arrows.

**Examples.** The isomorphism \(\operatorname{Hom}_R(R,M)\cong M\) is given by \(f\mapsto f(1)\). For abelian groups:
\[
\operatorname{Hom}_{\mathbb Z}(\mathbb Z/n,M)\cong\{m\in M:nm=0\},\qquad
\operatorname{Hom}_{\mathbb Z}(\mathbb Z/n,\mathbb Z)=0,\qquad
\operatorname{Hom}_{\mathbb Z}(\mathbb Q,\mathbb Z)=0 .
\]

**Proposition 6.2.** [[algebra-modules/hom-sums-to-products|Hom turns sums into products]]

Dually, \(\operatorname{Hom}_R\bigl(M,\prod_i N_i\bigr)\cong\prod_i\operatorname{Hom}_R(M,N_i)\); this is the universal property of the product. In particular \(\operatorname{Hom}_R(R^n,M)\cong M^n\).

**Proposition 6.3.** [[algebra-homological/hom-left-exact|Hom is left exact]]

The functor \(\operatorname{Hom}_R(M,-)\) need not preserve surjections. Apply \(\operatorname{Hom}_{\mathbb Z}(\mathbb Z/2,-)\) to \(0\to\mathbb Z\xrightarrow{2}\mathbb Z\to\mathbb Z/2\to0\). The result is \(0\to0\to0\to\mathbb Z/2\), and the last map is not surjective. Section 7 studies the modules for which these functors are exact.

**Definition 6.4.** [[algebra-modules/dual-module|Dual module]]

For a free module of finite rank, the evaluation map \(M\to M^{\vee\vee}\), \(m\mapsto(\varphi\mapsto\varphi(m))\), is an isomorphism. In general it can fail to be injective or surjective: \((\mathbb Z/n)^\vee=0\) over \(\mathbb Z\), and for an infinite-dimensional vector space the evaluation map is injective but not surjective.

### Exercises for Section 6

1. Show that \(\operatorname{Hom}_{\mathbb Z}(\mathbb Z/m,\mathbb Z/n)\cong\mathbb Z/\gcd(m,n)\).
2. Show that \(\operatorname{Hom}_{\mathbb Z}(\mathbb Q,\mathbb Z)=0\) and \(\operatorname{Hom}_{\mathbb Z}(\mathbb Q,\mathbb Q)\cong\mathbb Q\).
3. For a commutative ring \(R\), an ideal \(I\), and a module \(M\), show that \(\operatorname{Hom}_R(R/I,M)\cong\{m\in M:Im=0\}\).
4. Prove the contravariant form of Proposition 6.3 directly: if \(A\xrightarrow{u}B\xrightarrow{v}C\to0\) is exact, show that the induced maps \(v^\ast\) and \(u^\ast\) on \(\operatorname{Hom}_R(-,N)\) satisfy \(\ker v^\ast=0\) and \(\ker u^\ast=\operatorname{im} v^\ast\).
5. Show that \(M\to M^{\vee\vee}\) is an isomorphism when \(M\) is free of finite rank.

## 7. Projective and injective modules

Free modules are easy to map out of: a homomorphism from a free module is any choice of images of a basis. Projective modules keep the lifting property that this gives, and injective modules have the dual extension property. In terms of Section 6, \(P\) is projective exactly when \(\operatorname{Hom}_R(P,-)\) is exact, and \(E\) is injective exactly when \(\operatorname{Hom}_R(-,E)\) is exact.

**Definition 7.1.** [[algebra-modules/projective-module|Projective module]]

**Proposition 7.2.** [[algebra-modules/projective-summand-of-free|Projective modules are direct summands of free modules]]

**Proof sketch.** Choose a surjection \(\pi\colon F\to P\) from a free module. Projectivity lifts \(\mathrm{id}_P\) to \(s\colon P\to F\) with \(\pi s=\mathrm{id}_P\), so \(F=s(P)\oplus\ker\pi\) by the splitting lemma. Conversely, lift a map from a summand by extending it by zero on the complement and using Proposition 3.10 on the free module.

**Proposition 7.3.** [[algebra-modules/projective-ses-criterion|Projective short exact sequence criterion]]

**Examples.** Free modules are projective, and over a field every module is free and hence projective. A projective module need not be free. For \(R=F\times F\), the ideal \(P=F\times0\) is a direct summand of \(R\), hence projective. It is not free, because \(\dim_F P=1\) while a free \(R\)-module of rank \(n\) has \(F\)-dimension \(2n\). Over \(\mathbb Z\), and more generally over a principal ideal domain, finitely generated projective modules are free (Section 10), and \(\mathbb Z/n\) is not projective for \(n\ge2\).

**Definition 7.4.** [[algebra-modules/injective-module|Injective module]]

**Theorem 7.5.** [[algebra-modules/baers-criterion|Baer's criterion]]

**Injective modules over a principal ideal domain.** An \(R\)-module \(E\) is **divisible** if for every \(m\in E\) and every \(r\neq0\) there is \(m'\in E\) with \(rm'=m\). Over a principal ideal domain, Baer's criterion shows that injective is the same as divisible. A nonzero ideal is \((r)\cong R\), so a homomorphism \(f\colon(r)\to E\) is determined by \(m=f(r)\), which can be any element of \(E\). If \(F\colon R\to E\) extends \(f\), then \(m=F(r)=rF(1)\). Conversely, if \(m=rm'\), then \(F(x)=xm'\) extends \(f\). So every such \(f\) extends exactly when \(E\) is divisible. Thus \(\mathbb Q\) and \(\mathbb Q/\mathbb Z\) are injective \(\mathbb Z\)-modules and \(\mathbb Z\) is not. Every abelian group embeds in an injective one. Write \(A\cong F/K\) with \(F=\bigoplus_{i\in I}\mathbb Z\) free. Then \(A\) embeds in \(\bigl(\bigoplus_{i\in I}\mathbb Q\bigr)/K\), which is divisible because it is a quotient of a divisible group. The same holds over every ring: every module embeds in an injective module.

### Exercises for Section 7

1. Show that a direct sum of modules is projective if and only if every summand is projective.
2. Use Proposition 7.3 to show that \(\mathbb Z/n\) is not a projective \(\mathbb Z\)-module for \(n\ge2\).
3. Show that \(\mathbb Q\) is not a projective \(\mathbb Z\)-module. (Hint: a projective module embeds in a free module, and no nonzero element of a free abelian group is divisible by every positive integer.)
4. Show that a quotient of a divisible abelian group is divisible, and that \(\mathbb Z\) is not an injective \(\mathbb Z\)-module.
5. Show that \(\operatorname{Hom}_R(P,-)\) is exact when \(P\) is projective.

## 8. Tensor products

A bilinear map \(M\times N\to P\) is linear in each variable separately, but it is not a linear map out of the product module. The tensor product is the module that converts bilinear maps into linear ones. The general construction pairs a right \(R\)-module \(M\) with a left \(R\)-module \(N\) and produces an abelian group \(M\otimes_RN\). When \(R\) is commutative, \(M\otimes_RN\) is again an \(R\)-module.

**Definition 8.1.** [[algebra-modules/bilinear-map|Bilinear and balanced maps]]

**Definition 8.2.** [[algebra-modules/tensor-product-universal-property|Universal property of the tensor product]]

**Definition 8.3.** [[algebra-modules/tensor-product|Tensor product of modules]]

**Definition 8.4.** [[algebra-modules/bimodule|Bimodule]]

Bimodules supply the module structure on a tensor product. If \(M\) is an \((S,R)\)-bimodule and \(N\) a left \(R\)-module, then \(M\otimes_RN\) is a left \(S\)-module with \(s(m\otimes n)=(sm)\otimes n\). When \(R\) is commutative, every module is an \((R,R)\)-bimodule with \(rm=mr\), and \(M\otimes_RN\) is an \(R\)-module with \(r(m\otimes n)=(rm)\otimes n=m\otimes(rn)\).

**Working with tensors.** Three points cause most mistakes.

1. Every element of \(M\otimes_RN\) is a finite sum \(\sum_i m_i\otimes n_i\), but in general not a single **pure tensor** \(m\otimes n\). In \(F^2\otimes_FF^2\cong M_2(F)\), the pure tensors correspond to matrices of rank at most one, and \(e_1\otimes e_1+e_2\otimes e_2\) corresponds to the identity matrix.
2. To define a homomorphism out of \(M\otimes_RN\), write down a balanced map on \(M\times N\) and apply the universal property. A formula on pure tensors defines a homomorphism only after this check.
3. Whether \(m\otimes n\) is zero depends on the modules, not only on \(m\) and \(n\). In \(\mathbb Z\otimes_{\mathbb Z}\mathbb Z/2\), the element \(2\otimes1=1\otimes2=0\). In \(2\mathbb Z\otimes_{\mathbb Z}\mathbb Z/2\cong\mathbb Z/2\), the element \(2\otimes1\) is a generator. So tensoring the injection \(2\mathbb Z\hookrightarrow\mathbb Z\) with \(\mathbb Z/2\) gives the zero map \(\mathbb Z/2\to\mathbb Z/2\), which is not injective.

**Computations.** \(R^m\otimes_RR^n\cong R^{mn}\) and \(\mathbb Z/m\otimes_{\mathbb Z}\mathbb Z/n\cong\mathbb Z/\gcd(m,n)\). For any abelian group \(A\), \(\mathbb Z/n\otimes_{\mathbb Z}A\cong A/nA\). Also \(\mathbb Q\otimes_{\mathbb Z}\mathbb Z/n=0\), because
\[
q\otimes x=\tfrac qn\,n\otimes x=\tfrac qn\otimes nx=0 .
\]

**Proposition 8.5.** [[algebra-modules/tensor-preserves-direct-sums|Tensor product preserves direct sums]]

**Proposition 8.6.** [[algebra-homological/tensor-right-exact|Tensor product is right exact]]

**Construction 8.7.** [[algebra-commutative/extension-of-scalars|Extension of scalars]]

**Examples.** Complexification \(\mathbb C\otimes_{\mathbb R}V\) turns a real vector space into a complex one of the same dimension. For a finitely generated abelian group \(A\cong\mathbb Z^r\oplus T\) with \(T\) finite, \(\mathbb Q\otimes_{\mathbb Z}A\cong\mathbb Q^r\): extending scalars to \(\mathbb Q\) kills the torsion and remembers the rank.

**Theorem 8.8.** [[algebra-modules/tensor-hom-adjunction|Tensor–Hom adjunction]]

**Theorem 8.9.** [[algebra-modules/tensor-hom-adjunction-lemma|Tensor–Hom adjunction for bimodules]]

**Proposition 8.10.** [[algebra-modules/tensor-commutes-with-sums|Tensor commutes with direct limits and sums]]

The adjunction explains the exactness properties at once. A left adjoint preserves colimits, and cokernels and direct sums are colimits. This gives Proposition 8.5 and right exactness again. The statement about direct limits can be skipped on a first reading.

**Definition 8.11.** [[algebra-modules/flat-module|Flat module]]

**Proposition 8.12.** [[algebra-modules/projective-implies-flat|Projective implies flat]]

**Examples.** The \(\mathbb Z\)-module \(\mathbb Z/n\) is not flat for \(n\ge2\): tensoring the injection \(\mathbb Z\xrightarrow{n}\mathbb Z\) with \(\mathbb Z/n\) gives the zero map on \(\mathbb Z/n\). The \(\mathbb Z\)-module \(\mathbb Q\) is flat (Section 14) but not projective. Over a principal ideal domain, a module is flat exactly when it is torsion-free.

**Proposition 8.13.** [[algebra-homological/hom-tensor-exactness|Exactness properties of Hom and tensor]]

### Exercises for Section 8

1. Compute \(\mathbb Z/12\otimes_{\mathbb Z}\mathbb Z/18\) and \(\mathbb Q\otimes_{\mathbb Z}(\mathbb Z^2\oplus\mathbb Z/5)\).
2. Show that \(e_1\otimes e_1+e_2\otimes e_2\in F^2\otimes_FF^2\) is not a pure tensor.
3. Show directly from the universal property that \(M\otimes_RR\cong M\) for a right \(R\)-module \(M\).
4. For a commutative ring \(R\) and ideals \(I,J\), show that \(R/I\otimes_RR/J\cong R/(I+J)\).
5. Show that the injection \(2\mathbb Z\hookrightarrow\mathbb Z\) stays injective after tensoring with \(\mathbb Q\), but not after tensoring with \(\mathbb Z/2\).

## 9. Algebras

An algebra over a commutative ring \(R\) is a ring that is also an \(R\)-module, with compatible multiplication. Polynomial rings, matrix rings, and group algebras are examples. Tensor products combine algebras, and three universal constructions build algebras from a module. This section can be read any time after Section 8.

**Definition 9.1.** [[algebra-modules/algebra-over-ring|Algebra over a commutative ring]]

**Definition 9.2.** [[algebra-modules/algebra-homomorphism|Algebra homomorphism]]

**Construction 9.3.** [[algebra-modules/tensor-product-algebras|Tensor product of algebras]]

**Example.** The map \(a\otimes b\mapsto(ab,a\bar b)\) is an isomorphism of rings \(\mathbb C\otimes_{\mathbb R}\mathbb C\cong\mathbb C\times\mathbb C\). Extending scalars can turn a field into a ring with zero divisors.

**Construction 9.4.** [[algebra-modules/tensor-algebra|Tensor algebra]]

**Construction 9.5.** [[algebra-modules/symmetric-algebra|Symmetric algebra]]

**Construction 9.6.** [[algebra-modules/exterior-algebra|Exterior algebra]]

**Determinants.** For \(M=R^n\), the top exterior power \(\bigwedge^nR^n\) is free of rank one with basis \(e_1\wedge\cdots\wedge e_n\). An endomorphism \(\varphi\) of \(R^n\) induces an endomorphism of \(\bigwedge^nR^n\), \(v_1\wedge\cdots\wedge v_n\mapsto\varphi v_1\wedge\cdots\wedge\varphi v_n\), which is multiplication by a scalar. That scalar is \(\det\varphi\). Multiplicativity \(\det(\varphi\psi)=\det\varphi\det\psi\) follows from functoriality, with no computation.

### Exercises for Section 9

1. In \(\bigwedge^2_R(R^2)\), express \((ae_1+be_2)\wedge(ce_1+de_2)\) as a multiple of \(e_1\wedge e_2\).
2. Use universal properties to show that \(\operatorname{Sym}_R(R^n)\cong R[x_1,\dots,x_n]\).
3. Show that \(F[x]\otimes_FF[y]\cong F[x,y]\) as \(F\)-algebras.
4. Show that \(\mathbb C\otimes_{\mathbb R}\mathbb C\cong\mathbb C\times\mathbb C\) as rings.

## 10. Modules over a principal ideal domain

In this section \(R\) is a principal ideal domain (PID). The main examples are \(\mathbb Z\) and \(F[x]\) for a field \(F\). Over a PID, every finitely generated module is a direct sum of cyclic modules, and the cyclic summands can be chosen so that they are unique. For \(R=\mathbb Z\) this classifies finitely generated abelian groups, and for \(R=F[x]\) it gives the canonical forms of Section 11.

**Background 10.1.** [[algebra-rings/euclidean-domain|Euclidean domain]]

**Background 10.2.** [[algebra-rings/pid|Principal ideal domain]]

**Background 10.3.** [[algebra-rings/prime-element|Prime element]]

Recall that in a PID every nonzero prime ideal is maximal, any two elements \(a,b\) have a greatest common divisor \(d\) with \((a,b)=(d)\) and \(d=sa+tb\) for some \(s,t\in R\), and every nonzero nonunit factors uniquely into primes.

**Submodules of free modules.** The first step toward the structure theorem repairs item 3 of the list in Section 3.

**Theorem.** If \(R\) is a PID, then every submodule of \(R^n\) is free of rank at most \(n\).

**Proof sketch.** Induct on \(n\); the case \(n=0\) is trivial. Let \(N\subseteq R^n\) and let \(\pi\colon R^n\to R\) be the last coordinate. The image \(\pi(N)\) is an ideal \((a)\). If \(a=0\), then \(N\subseteq R^{n-1}\) and induction applies. Otherwise \((a)\cong R\) is free, so \(0\to N\cap R^{n-1}\to N\to(a)\to0\) splits (Exercise 1 of Section 5), and \(N\cong(N\cap R^{n-1})\oplus R\). By induction \(N\cap R^{n-1}\) is free of rank at most \(n-1\).

Two consequences follow. A finitely generated projective module \(P\) over a PID is free: a surjection \(R^n\to P\) splits, so \(P\) is isomorphic to a submodule of \(R^n\). And every finitely generated module \(M\) has a **presentation**. Choose generators to get a surjection \(R^n\to M\). Its kernel \(N\) is free with a basis of \(m\le n\) elements. Writing that basis in coordinates gives an \(n\times m\) matrix \(A\) with
\[
M\;\cong\;R^n/A\,R^m=\operatorname{coker}\bigl(A\colon R^m\to R^n\bigr).
\]
The matrix \(A\) is a **presentation matrix** of \(M\). The structure theorem comes from simplifying \(A\) by changes of basis, which the Smith normal form below carries out.

**Theorem 10.4.** [[algebra-modules/structure-theorem-pid|Structure theorem for finitely generated modules over a PID]]

**Theorem 10.5.** [[algebra-modules/elementary-divisor-theorem|Elementary divisor theorem]]

**Proposition 10.6.** [[algebra-modules/chinese-remainder-modules|Chinese remainder theorem for modules]]

Applied with \(M=R\), this gives \(R/(ab)\cong R/(a)\oplus R/(b)\) whenever \(a\) and \(b\) are coprime. Factoring each invariant factor into prime powers therefore converts the invariant-factor form into the elementary-divisor form. Conversely, multiply together the largest prime powers for each prime to get \(d_t\), then the next largest to get \(d_{t-1}\), and so on.

**Corollary 10.7.** [[algebra-modules/fg-torsion-free-pid-free|Finitely generated torsion-free modules over a PID are free]]

**Corollary 10.8.** [[algebra-modules/classification-fg-abelian-groups|Classification of finitely generated abelian groups]]

**Example.** The abelian groups of order \(72=2^3\cdot3^2\) correspond to a partition of the exponent \(3\) (three choices) and a partition of the exponent \(2\) (two choices). In elementary-divisor form and invariant-factor form they are:

| Elementary divisors | Invariant factors |
| --- | --- |
| \(\mathbb Z/8\oplus\mathbb Z/9\) | \(\mathbb Z/72\) |
| \(\mathbb Z/8\oplus\mathbb Z/3\oplus\mathbb Z/3\) | \(\mathbb Z/3\oplus\mathbb Z/24\) |
| \(\mathbb Z/4\oplus\mathbb Z/2\oplus\mathbb Z/9\) | \(\mathbb Z/2\oplus\mathbb Z/36\) |
| \(\mathbb Z/4\oplus\mathbb Z/2\oplus\mathbb Z/3\oplus\mathbb Z/3\) | \(\mathbb Z/6\oplus\mathbb Z/12\) |
| \(\mathbb Z/2\oplus\mathbb Z/2\oplus\mathbb Z/2\oplus\mathbb Z/9\) | \(\mathbb Z/2\oplus\mathbb Z/2\oplus\mathbb Z/18\) |
| \(\mathbb Z/2\oplus\mathbb Z/2\oplus\mathbb Z/2\oplus\mathbb Z/3\oplus\mathbb Z/3\) | \(\mathbb Z/2\oplus\mathbb Z/6\oplus\mathbb Z/6\) |

**Uniqueness.** The free rank \(r\) equals the rank of the free module \(M/\operatorname{Tor}(M)\). For a prime \(p\) and \(k\ge0\), the quotient \(p^kM/p^{k+1}M\) is a vector space over the field \(R/(p)\). Its dimension is \(r\) plus the number of elementary divisors \(p^e\) with \(e>k\). These dimensions are invariants of \(M\), and they determine the exponents of \(p\) that occur. The computation rests on three facts: \(p^k(R/(p^e))/p^{k+1}(R/(p^e))\) is \(R/(p)\) for \(k<e\) and \(0\) otherwise; \(p\) acts invertibly on \(R/(q^e)\) for primes \(q\) not associate to \(p\); and \(p^kR/p^{k+1}R\cong R/(p)\).

**Background 10.9.** [[algebra-modules/matrix-representation|Matrix representation]]

The same formalism applies to free modules of finite rank over any commutative ring: after choosing bases, a homomorphism \(R^m\to R^n\) is an \(n\times m\) matrix, and changing bases replaces \(A\) by \(UAV\) with \(U\) and \(V\) invertible.

**Theorem 10.10.** [[algebra-modules/smith-normal-form-theorem|Smith normal form theorem]]

**Corollary 10.11.** [[algebra-modules/smith-normal-form-invariants|Smith normal form invariants]]

**Computing the Smith normal form.** Over a Euclidean domain, elementary row and column operations suffice. These are swapping two rows, adding a multiple of one row to another, and multiplying a row by a unit, and likewise for columns. Move an entry of smallest size to the corner. Use division with remainder to clear the rest of its row and column, which either succeeds or produces a smaller entry to move to the corner. If the corner entry then fails to divide some other entry, add that entry's row to the first row and continue, which again produces a smaller remainder. Since sizes cannot decrease forever, the corner entry eventually divides every other entry, and the process repeats on the remaining submatrix. Over a general PID, a \(2\times2\) invertible matrix built from \(d=sa+tb\) replaces a pair \(a,b\) by \(d,0\). The invariant factors can also be read off directly: \(d_1d_2\cdots d_k\) is a gcd of all \(k\times k\) minors of \(A\).

**Example.** Over \(\mathbb Z\), take \(A=\begin{pmatrix}2&4\\6&8\end{pmatrix}\). Subtract three times the first row from the second, then twice the first column from the second, then change the sign of the second row:
\[
\begin{pmatrix}2&4\\6&8\end{pmatrix}\to\begin{pmatrix}2&4\\0&-4\end{pmatrix}\to\begin{pmatrix}2&0\\0&-4\end{pmatrix}\to\begin{pmatrix}2&0\\0&4\end{pmatrix}.
\]
Hence \(\mathbb Z^2/A\mathbb Z^2\cong\mathbb Z/2\oplus\mathbb Z/4\). As a check, \(d_1=2\) is the gcd of the entries and \(d_1d_2=8=|\det A|\).

**Proof of the structure theorem.** Take a presentation \(M\cong\operatorname{coker}(A)\) as above and put \(A\) in Smith normal form \(UAV=\operatorname{diag}(d_1,\dots,d_s,0,\dots,0)\). The invertible matrices \(U\) and \(V\) are changes of basis of \(R^n\) and \(R^m\), so they do not change the cokernel up to isomorphism. The cokernel of a diagonal matrix is \(\bigoplus_iR/(d_i)\oplus R^{n-s}\). Summands with \(d_i\) a unit are zero and can be dropped.

### Exercises for Section 10

1. Find the Smith normal form of \(\begin{pmatrix}4&6\\6&9\end{pmatrix}\) over \(\mathbb Z\), and identify the cokernel.
2. List the abelian groups of order \(360\) in invariant-factor and elementary-divisor form.
3. Show that every abelian group of order \(n\) is cyclic if and only if \(n\) is squarefree.
4. Explain why \(\mathbb Q\) shows that the hypothesis "finitely generated" cannot be dropped from Corollary 10.7.
5. Over \(F[x]\), find the invariant factors and the elementary divisors of \(F[x]/(x^2(x-1))\oplus F[x]/(x(x-1)^2)\).
6. Show that a finitely generated module over a PID is indecomposable (not a direct sum of two nonzero submodules) if and only if it is isomorphic to \(R\) or to \(R/(p^e)\) for a prime \(p\) and \(e\ge1\).

## 11. Canonical forms

Let \(V\) be a finite-dimensional vector space over a field \(F\) and \(T\) a linear operator on \(V\). The \(F[x]\)-module \(V_T\) of Definition 1.3 is finitely generated, since any basis generates it, and it is torsion by the example in Section 4. Since \(F[x]\) is a PID, the structure theorem gives
\[
V_T\;\cong\;F[x]/(f_1)\oplus\cdots\oplus F[x]/(f_s),\qquad f_1\mid f_2\mid\cdots\mid f_s,
\]
with each \(f_i\) monic of positive degree. There is no free summand because \(V\) is finite-dimensional. Choosing a good basis of each summand turns this decomposition into a canonical matrix for \(T\).

**Background 11.1.** [[linear-algebra/minimal-polynomial|Minimal polynomial]]

**Background 11.2.** [[linear-algebra/characteristic-polynomial|Characteristic polynomial]]

**Companion matrices.** Let \(f=x^d+a_{d-1}x^{d-1}+\cdots+a_1x+a_0\) be monic. The cyclic module \(F[x]/(f)\) has basis \(1,x,\dots,x^{d-1}\). Multiplication by \(x\) sends each basis vector to the next, except that \(x\cdot x^{d-1}=x^d=-a_0-a_1x-\cdots-a_{d-1}x^{d-1}\). Its matrix in this basis is the **companion matrix**
\[
C(f)=\begin{pmatrix}
0&0&\cdots&0&-a_0\\
1&0&\cdots&0&-a_1\\
0&1&\cdots&0&-a_2\\
\vdots&&\ddots&&\vdots\\
0&0&\cdots&1&-a_{d-1}
\end{pmatrix}.
\]
Both its characteristic polynomial and its minimal polynomial equal \(f\). The minimal polynomial is \(f\) because the annihilator of \(F[x]/(f)\) is \((f)\), and the characteristic polynomial follows by expanding \(\det(xI-C(f))\) along the last column.

**Theorem 11.3.** [[algebra-modules/rational-canonical-form-theorem|Rational canonical form theorem]]

**Corollary 11.4.** [[algebra-modules/rcf-from-structure-theorem|Rational canonical form from the structure theorem]]

**Similarity is isomorphism.** A matrix \(A\in M_n(F)\) makes \(F^n\) into an \(F[x]\)-module \(F^n_A\). An \(F[x]\)-isomorphism \(F^n_A\to F^n_B\) is an invertible matrix \(P\) with \(PA=BP\). The condition \(PA=BP\) says that \(P\) carries the action of \(x\) on \(F^n_A\) to its action on \(F^n_B\), so the square below commutes:

```tikz-cd
F^n \arrow[r, "A"] \arrow[d, "P"', "\cong"] & F^n \arrow[d, "P", "\cong"'] \\
F^n \arrow[r, "B"'] & F^n
```

So \(A\) and \(B\) are similar exactly when \(F^n_A\cong F^n_B\), that is, exactly when they have the same invariant factors and the same rational canonical form. The sequence
\[
0\to F[x]^n\xrightarrow{\;xI-A\;}F[x]^n\to F^n_A\to0
\]
is exact, so \(xI-A\) is a presentation matrix of \(F^n_A\). The invariant factors of \(A\) are therefore the nonunit diagonal entries of the Smith normal form of \(xI-A\) over \(F[x]\).

**Example.** For \(A=\begin{pmatrix}1&1\\0&1\end{pmatrix}\), the matrix \(xI-A=\begin{pmatrix}x-1&-1\\0&x-1\end{pmatrix}\) has a unit entry, so \(d_1=1\) and \(d_2=\det(xI-A)=(x-1)^2\). Thus \(F^2_A\cong F[x]/((x-1)^2)\) is cyclic. For \(A=I\), the Smith normal form is \(\operatorname{diag}(x-1,x-1)\). Both matrices have characteristic polynomial \((x-1)^2\), but their invariant factors differ, so they are not similar.

**Theorem 11.5.** [[linear-algebra/cayley-hamilton-theorem|Cayley–Hamilton theorem]]

**Proof from the rational canonical form.** The characteristic polynomial of \(T\) is the product \(f_1\cdots f_s\) of the characteristic polynomials of the companion blocks. The minimal polynomial is \(f_s\), the largest invariant factor. Hence the minimal polynomial divides the characteristic polynomial, which therefore kills \(T\). The same argument shows that every irreducible factor of the characteristic polynomial divides the minimal polynomial.

**Theorem 11.6.** [[algebra-modules/jordan-canonical-form-theorem|Jordan canonical form theorem]]

**Corollary 11.7.** [[algebra-modules/jcf-from-rcf|Jordan canonical form from rational canonical form]]

**Jordan blocks from elementary divisors.** When the characteristic polynomial splits, the elementary divisors have the form \((x-\lambda)^e\). In the cyclic module \(F[x]/((x-\lambda)^e)\), take the basis
\[
v_1=(x-\lambda)^{e-1},\quad v_2=(x-\lambda)^{e-2},\quad\dots,\quad v_e=1 .
\]
Then \((x-\lambda)v_1=0\) and \((x-\lambda)v_k=v_{k-1}\) for \(k\ge2\), so \(Tv_1=\lambda v_1\) and \(Tv_k=\lambda v_k+v_{k-1}\). The matrix of \(T\) in this basis is the Jordan block \(J_e(\lambda)\). Each elementary divisor contributes one Jordan block.

**Example.** Suppose \(T\) acts on \(\mathbb Q^4\) with invariant factors \(x-1\) and \((x-1)(x^2+1)=x^3-x^2+x-1\). Its rational canonical form is
\[
\begin{pmatrix}1\end{pmatrix}\oplus\begin{pmatrix}0&0&1\\1&0&-1\\0&1&1\end{pmatrix},
\]
with characteristic polynomial \((x-1)^2(x^2+1)\) and minimal polynomial \((x-1)(x^2+1)\). Over \(\mathbb Q\), the factor \(x^2+1\) does not split and there is no Jordan form. Over \(\mathbb C\), the elementary divisors are \(x-1\), \(x-1\), \(x-i\), \(x+i\), so \(T\) is diagonalizable over \(\mathbb C\) with diagonal entries \(1,1,i,-i\).

**Definition 11.8.** [[algebra-modules/diagonalizable|Diagonalizable operator]]

### Exercises for Section 11

1. Find the rational and Jordan canonical forms of \(\begin{pmatrix}2&1\\-1&0\end{pmatrix}\) over \(\mathbb Q\).
2. Show that two \(3\times3\) matrices over \(F\) are similar if and only if they have the same characteristic and minimal polynomials. Show that this fails for \(4\times4\) matrices.
3. Determine the number of similarity classes of \(6\times6\) complex matrices with characteristic polynomial \((x-1)^4(x+1)^2\) and minimal polynomial \((x-1)^2(x+1)\).
4. Use elementary divisors to show that \(T\) is diagonalizable if and only if its minimal polynomial splits into distinct linear factors.
5. Show that every square matrix over a field is similar to its transpose. (Hint: compare the Smith normal forms of \(xI-A\) and \(xI-A^{\mathsf T}\).)

## 12. Chain conditions and composition series

Finite dimension has two module-theoretic substitutes: ascending chains of submodules stabilize (Noetherian), and descending chains stabilize (Artinian). A module with both properties can be broken into simple pieces, and the Jordan–Hölder theorem shows that the pieces are unique. From here on \(R\) is again an arbitrary ring.

**Definition 12.1.** [[algebra-modules/simple-module|Simple module]]

A simple module is generated by each of its nonzero elements: if \(s\neq0\), then \(Rs\) is a nonzero submodule, so \(Rs=S\). Hence \(S\cong R/\mathfrak m\) with \(\mathfrak m=\operatorname{ann}(s)\), and \(\mathfrak m\) is a maximal left ideal by the correspondence theorem.

**Definition 12.2.** [[algebra-modules/noetherian-module|Noetherian module]]

**Definition 12.3.** [[algebra-modules/artinian-module|Artinian module]]

**Chain conditions and exact sequences.** Let \(0\to A\to B\to C\to0\) be exact. Then \(B\) is Noetherian if and only if \(A\) and \(C\) are, and the same holds for Artinian. The key step is a lemma: if \(N\subseteq N'\) are submodules of \(B\) with the same intersection with \(A\) and the same image in \(C\), then \(N=N'\). Consequently finite direct sums of Noetherian modules are Noetherian. If \(R\) is left Noetherian, meaning that \({}_RR\) is Noetherian, then every finitely generated \(R\)-module is Noetherian, being a quotient of some \(R^n\).

**Examples.** The \(\mathbb Z\)-module \(\mathbb Z\) is Noetherian but not Artinian. The **Prüfer group** \(\mathbb Z[1/p]/\mathbb Z\) is Artinian but not Noetherian: its proper submodules are the finite cyclic groups generated by the classes of \(1/p^k\), and they form a single strictly increasing chain.

**Definition 12.4.** [[algebra-modules/composition-series-module|Composition series]]

**Definition 12.5.** [[algebra-modules/length-module|Length of a module]]

**Theorem (Jordan–Hölder for modules).** If \(M\) has a composition series, then any two composition series of \(M\) have the same length, and their simple factors agree up to permutation and isomorphism.

**Proof sketch.** Induct on the shortest length \(n\) of a composition series of \(M\). Let \((M_i)\) and \((N_j)\) be composition series of lengths \(n\) and \(m\). If \(M_{n-1}=N_{m-1}\), apply induction to this submodule. Otherwise \(M_{n-1}+N_{m-1}=M\), because \(M/M_{n-1}\) is simple. With \(K=M_{n-1}\cap N_{m-1}\), the second isomorphism theorem gives \(M/M_{n-1}\cong N_{m-1}/K\) and \(M/N_{m-1}\cong M_{n-1}/K\). The submodule \(K\) has a composition series: the successive quotients of the chain \(K\cap M_0\subseteq K\cap M_1\subseteq\cdots\subseteq K\cap M_n=K\) embed in the simple modules \(M_i/M_{i-1}\), so after repetitions are deleted the chain is a composition series of \(K\). Extending it by \(M_{n-1}\) and by \(N_{m-1}\) gives two composition series of \(M\) with the same factors in a different order, and induction compares each of them with the original series. The argument is the same as for groups.

Length is additive on short exact sequences: \(\ell(B)=\ell(A)+\ell(C)\). For example, \(\ell_{\mathbb Z}(\mathbb Z/n)\) is the number of prime factors of \(n\) counted with multiplicity, and \(\ell_F(V)=\dim V\).

**Proposition 12.6.** [[algebra-modules/artinian-noetherian-finite-length|Artinian and Noetherian implies finite length]]

The converse also holds. In a module of finite length \(\ell\), every strictly increasing or strictly decreasing chain of submodules has at most \(\ell+1\) terms. So a module has finite length if and only if it is both Artinian and Noetherian.

### Exercises for Section 12

1. Write two different composition series of \(\mathbb Z/12\) and compare their factors.
2. Show that \(M\) is Noetherian if and only if every nonempty set of submodules of \(M\) has a maximal element.
3. Show that \(F[x]\) is a Noetherian but not Artinian module over itself, and that \(F[x]/(f)\) has finite length equal to the number of irreducible factors of \(f\) counted with multiplicity.
4. Show that the Prüfer group \(\mathbb Z[1/p]/\mathbb Z\) is Artinian but not Noetherian.
5. Show that length is additive on short exact sequences of finite-length modules.

## 13. Semisimple modules and rings

The best modules are direct sums of simple ones. Vector spaces are of this kind, and so are representations of finite groups in characteristic zero. This section characterizes semisimple modules, classifies the rings over which every module is semisimple, and ends with the uniqueness theorem for decompositions of finite-length modules into indecomposable pieces.

**Schur's lemma.** Let \(S\) and \(S'\) be simple modules and \(f\colon S\to S'\) a homomorphism. Then \(\ker f\) is \(0\) or \(S\), and \(\operatorname{im} f\) is \(0\) or \(S'\). Hence \(f\) is zero or an isomorphism, and \(\operatorname{End}_R(S)\) is a division ring. If \(R\) is an algebra over an algebraically closed field \(k\) and \(S\) is finite-dimensional over \(k\), then \(\operatorname{End}_R(S)=k\): an eigenvalue \(\lambda\) of \(f\) makes \(f-\lambda\) a noninvertible endomorphism, hence zero.

**Definition 13.1.** [[algebra-modules/semisimple-module|Semisimple module]]

**Proposition 13.2.** [[algebra-modules/semisimple-direct-summand|Semisimple iff every submodule is a direct summand]]

A module is semisimple if and only if it is a sum, not necessarily direct, of simple submodules. Submodules and quotients of semisimple modules are semisimple. The \(\mathbb Z\)-module \(\mathbb Z/4\) is not semisimple, since its submodule \(2\mathbb Z/4\) has no complement (Section 3); Exercise 1 treats \(\mathbb Z/n\) in general.

**Definition 13.3.** [[algebra-rings/semisimple-ring|Semisimple ring]]

A semisimple ring is automatically left Artinian. Write \({}_RR\) as a direct sum of simple left ideals. The element \(1\) has only finitely many nonzero components, and they generate \(R\), so only finitely many summands occur and \({}_RR\) has finite length.

**Background 13.4.** [[algebra-rings/division-ring|Division ring]]

**Definition 13.5.** [[algebra-rings/artinian-semisimple-ring|Artinian semisimple ring]]

**Theorem 13.6.** [[algebra-rings/artin-wedderburn-theorem|Artin–Wedderburn theorem]]

Schur's lemma supplies the division rings. If \({}_RR\cong S_1^{n_1}\oplus\cdots\oplus S_t^{n_t}\) with pairwise nonisomorphic simple modules \(S_i\), then
\[
R^{\mathrm{op}}\cong\operatorname{End}_R({}_RR)\cong\prod_iM_{n_i}\bigl(\operatorname{End}_R(S_i)\bigr),
\]
and each \(D_i=\operatorname{End}_R(S_i)\) is a division ring. Since transposition gives \(M_n(D)^{\mathrm{op}}\cong M_n(D^{\mathrm{op}})\), this yields \(R\cong\prod_iM_{n_i}(D_i^{\mathrm{op}})\), and each \(D_i^{\mathrm{op}}\) is again a division ring.

**Background 13.7.** [[algebra-representation-theory/group-algebra|Group algebra]]

A representation of a group \(G\) on a \(k\)-vector space is the same thing as a \(k[G]\)-module.

**Theorem 13.8.** [[algebra-representation-theory/maschkes-theorem|Maschke's theorem]]

So if \(G\) is finite and the characteristic of \(k\) does not divide \(|G|\), then \(k[G]\) is a semisimple ring. Over \(k=\mathbb C\) all the division rings in the Artin–Wedderburn decomposition are \(\mathbb C\), so \(\mathbb C[G]\cong\prod_iM_{n_i}(\mathbb C)\) and \(|G|=\sum_in_i^2\).

**Indecomposable modules.** A nonzero module \(M\) is **indecomposable** if \(M=A\oplus B\) internally forces \(A=0\) or \(B=0\). Simple modules are indecomposable. The \(\mathbb Z\)-modules \(\mathbb Z\) and \(\mathbb Z/p^e\) are indecomposable, but not simple unless the module is \(\mathbb Z/p\). Induction on length shows that every module of finite length is a finite direct sum of indecomposable modules.

**Theorem 13.9.** [[algebra-modules/krull-schmidt-azumaya-theorem|Krull–Schmidt–Azumaya theorem]]

For a finitely generated torsion module over a PID, the indecomposable summands are the cyclic modules \(R/(p^e)\), and the theorem recovers the uniqueness of elementary divisors. The free part \(R^r\) does not have finite length, which is why Section 10 proves uniqueness separately.

### Exercises for Section 13

1. Show that \(\mathbb Z/n\) is a semisimple \(\mathbb Z\)-module if and only if \(n\) is squarefree.
2. Let \(S\) be a simple module and \(D=\operatorname{End}_R(S)\). Show that \(\operatorname{End}_R(S^n)\cong M_n(D)\).
3. Let \(R\) be the ring of upper triangular \(2\times2\) matrices over \(F\). Show that the space \(F^2\) of column vectors is an indecomposable left \(R\)-module that is not simple.
4. Show that \(F[x]/(x^2)\) is not a semisimple ring.
5. For \(G=\mathbb Z/2\) and \(k=\mathbb F_2\), show that \(k[G]\cong k[x]/((x-1)^2)\) is not semisimple, so the hypothesis of Maschke's theorem cannot be dropped.

## 14. Tools over commutative rings

In this section \(R\) is commutative. Localization inverts some elements of \(R\) and lets one study a module near a single prime ideal. Nakayama's lemma is the basic tool for finitely generated modules over local rings.

**Background 14.1.** [[algebra-commutative/multiplicative-set|Multiplicative set]]

**Construction 14.2.** [[algebra-commutative/localization-ring|Localization of a ring]]

**Construction 14.3.** [[algebra-commutative/localization-module|Localization of a module]]

For a prime ideal \(\mathfrak p\), write \(M_{\mathfrak p}=S^{-1}M\) and \(R_{\mathfrak p}=S^{-1}R\) with \(S=R\setminus\mathfrak p\). There is a natural isomorphism \(S^{-1}M\cong S^{-1}R\otimes_RM\). Together with the next proposition, this shows that \(S^{-1}R\) is a flat \(R\)-module. In particular \(\mathbb Q=S^{-1}\mathbb Z\) with \(S=\mathbb Z\setminus\{0\}\) is a flat \(\mathbb Z\)-module.

**Proposition 14.4.** [[algebra-commutative/localization-exact|Exactness of localization]]

**Local properties.** A module \(M\) is zero if and only if \(M_{\mathfrak m}=0\) for every maximal ideal \(\mathfrak m\). Since localization is exact, a homomorphism is injective, surjective, or bijective if and only if it has that property after localizing at every maximal ideal.

**Background 14.5.** [[algebra-commutative/local-ring|Local ring]]

The ring \(R_{\mathfrak p}\) is local, with maximal ideal \(\mathfrak pR_{\mathfrak p}\).

**Lemma 14.6.** [[algebra-commutative/nakayama-lemma|Nakayama's lemma]]

In a local ring \((R,\mathfrak m)\), the Jacobson radical is \(\mathfrak m\), so the lemma applies with \(I=\mathfrak m\): if \(M\) is finitely generated and \(\mathfrak mM=M\), then \(M=0\).

**Minimal generators.** Let \((R,\mathfrak m)\) be local and \(M\) finitely generated. Elements \(m_1,\dots,m_n\) generate \(M\) if and only if their images span the vector space \(M/\mathfrak mM\) over the residue field \(R/\mathfrak m\). For the nontrivial direction, let \(N\) be the submodule they generate. Then \(N+\mathfrak mM=M\), so \(\mathfrak m(M/N)=M/N\), and Nakayama's lemma gives \(M/N=0\). Consequently every minimal generating set of \(M\) has exactly \(\dim_{R/\mathfrak m}M/\mathfrak mM\) elements.

**Proposition 14.7.** [[algebra-modules/fg-projective-locally-free|Finitely generated projective modules are locally free]]

### Exercises for Section 14

1. Show that \(S^{-1}M\cong S^{-1}R\otimes_RM\).
2. Show that \(M=0\) if and only if \(M_{\mathfrak m}=0\) for every maximal ideal \(\mathfrak m\).
3. Let \((R,\mathfrak m)\) be local and \(M,N\) finitely generated. Show that \(M\otimes_RN=0\) implies \(M=0\) or \(N=0\).
4. Let \((R,\mathfrak m)\) be local. Show that a finitely generated projective \(R\)-module is free.

## 15. Looking ahead: resolutions, Ext, and Tor

Hom is only left exact and tensor is only right exact (Sections 6 and 8). Homological algebra measures the failure of exactness with the derived functors Ext and Tor. Every module has a projective resolution, which is built by choosing generators, taking the kernel of the resulting map from a free module, and repeating.

**Definition 15.1.** [[algebra-homological/projective-resolution|Projective resolution]]

**Theorem 15.2.** [[algebra-homological/ext-tor-derived-functors|Ext and Tor as derived functors]]

The functor \(\operatorname{Tor}\) here is unrelated to the torsion submodule \(\operatorname{Tor}(M)\) of Section 4, apart from one link: \(\operatorname{Tor}^{\mathbb Z}_1(\mathbb Q/\mathbb Z,A)\) is the torsion subgroup of \(A\). The splitting results of Sections 5 and 7 have homological meanings. The group \(\operatorname{Ext}^1_R(C,A)\) classifies extensions \(0\to A\to B\to C\to0\), with \(0\) corresponding to the split extension. A module \(P\) is projective if and only if \(\operatorname{Ext}^1_R(P,-)=0\), and a module \(E\) is injective if and only if \(\operatorname{Ext}^1_R(-,E)=0\).

### Exercises for Section 15

1. Use the resolution \(0\to\mathbb Z\xrightarrow{n}\mathbb Z\to\mathbb Z/n\to0\) to show that \(\operatorname{Tor}^{\mathbb Z}_1(\mathbb Z/n,A)\cong\{a\in A:na=0\}\) and \(\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n,A)\cong A/nA\) for every abelian group \(A\).
2. Show that a short exact sequence \(0\to A\to B\to P\to0\) with \(P\) projective splits, and explain this in terms of \(\operatorname{Ext}^1_R(P,A)\).
