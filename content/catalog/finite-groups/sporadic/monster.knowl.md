+++
id = "catalog/finite-groups/sporadic/monster"
title = "Monster group"
kind = "definition"
summary = "The Monster simple group extracted from an explicitly presented Y555 Coxeter quotient."
aliases = ["Monster", "Fischer–Griess group"]
domains = ["catalog", "algebra-groups", "finite-groups"]
section_mode = "progressive"
prerequisites = ["algebra-groups/group-presentation", "algebra-groups/centralizer", "algebra-groups/quotient-group"]
dependency_heuristic = "finite-catalog-semantic-core-v1"
dependency_review_count = 1
+++

Let \(S=\{a\}\cup\{b_i,c_i,d_i,e_i,f_i:1\leq i\leq3\}\), and give these sixteen vertices exactly the edges
\[
a-b_i-c_i-d_i-e_i-f_i\qquad(i=1,2,3).
\]
Define \(G\) on generators \(S\) by the [[algebra-groups/group-presentation|presentation]]
\[
\begin{gathered}
s^2=1\quad(s\in S),\\
(st)^3=1\quad(s,t\text{ adjacent}),\\
(st)^2=1\quad(s\ne t\text{ nonadjacent}),\\
(ab_1c_1ab_2c_2ab_3c_3)^{10}=1.
\end{gathered}
\]
The **Monster group** is
\[
\mathbb M=C_G(a)/\langle a\rangle.
\]
Here \(C_G(a)=\{g\in G:ga=ag\}\) is the [[algebra-groups/centralizer|centralizer]], and the [[algebra-groups/quotient-group|quotient]] identifies elements differing by the central subgroup \(\langle a\rangle\).

## Order and structure

This is a nonabelian finite [[algebra-groups/simple-group|simple group]], with
\[
\begin{aligned}|\mathbb M|&=2^{46}\cdot3^{20}\cdot5^{9}\cdot7^{6}\cdot11^{2}\cdot13^{3}\cdot17\\
&\quad{}\cdot19\cdot23\cdot29\cdot31\cdot41\cdot47\cdot59\cdot71.\end{aligned}
\]
It belongs to the Monster display block of the sporadic groups. This grouping records the ATLAS organization, without asserting a direct embedding into another displayed group.

## Why this construction gives the Monster

The Ivanov–Norton theorem identifies the presented group as
\[
G\cong(H\times H)\rtimes\langle\tau\rangle,
\]
where \(H\) is the Monster simple group and the involution \(\tau\) exchanges the factors. The additional length-nine word raised to the tenth power is the *spider relation*.

The centralizer extraction is an elementary consequence of that theorem. In the abelianization of the presentation, each connected edge identifies its two involution generators. All relators have even word length, so the abelianization is exactly \(C_2\), and \(a\) lies outside \(H\times H\). Every involution outside this base subgroup is conjugate to the factor-swapping involution. Its centralizer is
\[
C_G(\tau)=\operatorname{diag}(H)\times\langle\tau\rangle,
\]
whose quotient by \(\langle\tau\rangle\) is \(H\). Thus the definition selects one Monster, rather than the product of two Monsters in the larger presented group.

## Scope of the construction

The defining graph and relations specify an abstract group without presupposing a Monster representation. The known presentation theorem is separate from geometric conjectures discussed in Allcock’s paper. The displayed spider relation uses the vertices \(b_i,c_i\) on each arm.

## References

1. [ATLAS, Monster group](https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/M/), exact order and prime factorization.
2. John H. Conway, “Y555 and all that,” printed pp. 22–23: the presentation and its proof by Ivanov and Norton. [Publisher preview](https://api.pageplace.de/preview/DT0400.9781139242899_A24435594/preview-9781139242899_A24435594.pdf#page=38).
3. Simon P. Norton, “Constructing the Monster” (1992), pp. 63–76; completion of the presentation proof. [Chapter](https://www.cambridge.org/core/books/abs/groups-combinatorics-and-geometry/constructing-the-monster/B28EB8BF60E87ED875A2F7715E3305A0).
4. Daniel Allcock, “A Monstrous Proposal,” §2, pp. 3–4, diagram and spider relation; §3, remark (7), centralizer description. [Author’s paper](https://web.ma.utexas.edu/users/allcock/research/monstrous.pdf).
