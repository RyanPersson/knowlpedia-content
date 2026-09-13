+++
id = "shared-foundations/zfc-axioms"
title = "ZFC axioms"
kind = "knowl"
summary = "Standard axioms of set theory: Zermelo-Fraenkel axioms plus the Axiom of Choice."
aliases = ["zfc-axioms", "ZFC axioms"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/zfc-axioms.md"
prerequisites = ["shared-foundations/set", "shared-foundations/first-order-logic"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++


**ZFC** is the classical first-order theory of [[shared-foundations/set|sets]] with equality and membership \(\in\), governed by the following axioms and axiom schemas. Variables range over sets. The logical connectives and quantifiers use [[shared-foundations/first-order-logic|first-order inference rules]].

## Axioms

1. **Extensionality:** \(\forall x\forall y[\forall z(z\in x\Leftrightarrow z\in y)\Rightarrow x=y]\).
2. **Empty set:** \(\exists e\forall z\,(z\notin e)\). Extensionality makes this object unique; write it as \(\varnothing\).
3. **Pairing:** \(\forall a\forall b\exists c\forall z[z\in c\Leftrightarrow(z=a\lor z=b)]\). Write this set as \(\{a,b\}\), with \(\{a\}=\{a,a\}\).
4. **Union:** \(\forall a\exists u\forall z[z\in u\Leftrightarrow\exists x(x\in a\land z\in x)]\).
5. **Power set:** \(\forall a\exists p\forall z[z\in p\Leftrightarrow\forall w(w\in z\Rightarrow w\in a)]\).
6. **Infinity:** there is a set \(I\) with \(\varnothing\in I\) such that \(x\in I\) implies \(x\cup\{x\}\in I\). Here \(x\cup\{x\}\) abbreviates the set whose elements are the elements of \(x\), together with \(x\) itself; pairing and union provide it.
7. **Separation schema:** for each first-order formula \(\phi(z,\mathbf p)\), with the new variable \(b\) not free in \(\phi\), every set \(a\) and every choice of parameter sets \(\mathbf p\) satisfy
\[
\exists b\forall z[z\in b\Leftrightarrow(z\in a\land\phi(z,\mathbf p))].
\]
8. **Replacement schema:** for each formula \(\phi(x,y,\mathbf p)\), if for every \(x\in a\) exactly one \(y\) satisfies \(\phi(x,y,\mathbf p)\), then there is a set \(b\) with
\[
\forall y[y\in b\Leftrightarrow\exists x(x\in a\land\phi(x,y,\mathbf p))].
\]
All parameter choices are quantified; bound variables are chosen to avoid capture.
9. **Foundation:** every nonempty set \(a\) has an element \(x\) sharing no element with \(a\):
\[
\forall a[\exists y(y\in a)\Rightarrow
\exists x(x\in a\land\neg\exists z(z\in x\land z\in a))].
\]
10. **Choice:** for every set \(A\) of pairwise disjoint nonempty sets, there is a set \(C\) meeting each member of \(A\) in exactly one element. In membership notation the conclusion is
\[
\forall x\in A\ \exists u\,[u\in x\land u\in C\land
\forall v((v\in x\land v\in C)\Rightarrow v=u)].
\]
This choice-set form is equivalent, over the other axioms, to the usual choice-function form of the [[shared-foundations/axiom-of-choice|Axiom of Choice]]. Bounded quantifiers such as \(\forall x\in A\) are abbreviations using implication and membership.

## Scope

Separation permits selecting elements from an existing set; it is not unrestricted comprehension. Replacement asserts that a definable single-valued image of a set is a set. The axioms allow constructions such as natural numbers and ordered pairs; those constructions are consequences and explanations, not prerequisites of the axiom statements themselves.

## References

- [Jonathan Pila, Set Theory, Sections 2–7 and 15](https://www.maths.ox.ac.uk/system/files/attachments/SetTheoryHT18.pdf).
