+++
id = "proofs/grh/onelift-values/factorial-classes-span-schwartz-bruhat"
title = "Indicators of classes modulo i! span the Schwartz-Bruhat functions"
kind = "lemma"
summary = "A subspace of functions on finite adelic vectors that contains, for every point, the indicator of its class modulo i! at a set S of places for all large i, contains every Schwartz-Bruhat function of the components at S."
aliases = ["factorial idele", "factorial box"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.factorialIdele", "New.factorialBox", "New.mem_of_nested_cosets", "New.IsSchwartzBruhat.eventually_const", "New.IsSchwartzBruhat.mem_of_eventually_coset", "New.antitone_factorialBox", "New.isOpen_factorialBox"]
lean_files = ["src/New/OneLift/FalseLifts/BottomOfTower.lean"]
proof_status = "full"
+++

Let \(E\) be a number field, \(\mathbb{A}_f\) its ring of
[[catalog/arithmetic/adeles-number-field-finite|finite adeles]], \(\widehat{\mathcal O}\subset\mathbb{A}_f\)
the integral adeles, \(S\) a set of finite places of \(E\) and \(m\) a finite index set. For \(i\ge 0\) the
integer \(i!\) is a finite idele (the **factorial idele**). The **factorial box** \(B_i\subset\mathbb{A}_f^m\)
is the subgroup of the vectors \(x\) with \(x_v\in i!\,\mathcal{O}_v^m\) for all \(v\in S\). The boxes are
open and decrease: \(B_j\subset B_i\) for \(i\le j\), because \(i!\mid j!\). The class of \(x\) modulo \(i!\)
at \(S\) is \(x+B_i\).

A function \(\Psi\colon\mathbb{A}_f^m\to\mathbb{C}\) is
[[harmonic-analysis/schwartz-bruhat-space-adeles|Schwartz–Bruhat]] *above \(S\)* (Lean:
[[?lean:New.IsSchwartzBruhat|`IsSchwartzBruhat S`]]) if it is locally constant, depends only on the
components at \(S\), and the projections to the components at \(S\) of the points of its support lie in a
compact set.

**Lemma.** Let \(P\) be a complex vector subspace of the space of functions \(\mathbb{A}_f^m\to\mathbb{C}\).
Suppose that for every \(x\) there is \(i_0\) such that the indicator function of \(x+B_i\) lies in \(P\)
for all \(i\ge i_0\). Then \(P\) contains every function that is Schwartz–Bruhat above \(S\).

## Proof

*Step 1 (local constancy at scale \(i!\)).* Let \(\Psi\) be Schwartz–Bruhat above \(S\) and \(x\) a point.
The function \(u\mapsto\Psi(u+x_S)\), with \(x_S\) the part of \(x\) at \(S\), is locally constant, so it is
constant on a neighbourhood of \(0\). The integral lattice \(\widehat{\mathcal O}^m\) is compact and the
multiples \(N\widehat{\mathcal O}^m\) shrink to \(0\), so some \(N\ge1\) has
\(\Psi(Nu+x_S)=\Psi(x_S)\) for all \(u\in\widehat{\mathcal O}^m\). For \(i\ge N\) we have \(N\mid i!\); if
\(y-x\in B_i\) then the part at \(S\) of \(y-x\) is \(i!\,u=N\cdot(i!/N)u\) with \(u\) integral, hence
\(\Psi(y)=\Psi(y_S)=\Psi(x_S)=\Psi(x)\). Thus \(\Psi\) is constant on \(x+B_i\) for all large \(i\).

*Step 2 (a finite cover).* By hypothesis and Step 1 choose for each \(x\) an integer \(i(x)\) such that the
indicator of \(x+B_{i(x)}\) lies in \(P\) and \(\Psi\) is constant on \(x+B_{i(x)}\). The open sets
\(x+B_{i(x)}\) cover the compact set \(C\) containing the \(S\)-parts of the support, so finitely many of
them, for \(x\in F\), cover \(C\). If \(\Psi(y)\ne0\) then \(y_S\in C\) lies in some \(x+B_{i(x)}\), and
\(y-y_S\in B_{i(x)}\) (it vanishes at \(S\)), so \(y\in x+B_{i(x)}\).

*Step 3 (nested cosets).* We claim: if \(U_0\supset U_1\supset\cdots\) are subgroups of an abelian group,
\(F\) is a finite set, \(i\colon F\to\mathbb{N}\), a function \(\Psi\) is constant on each \(x+U_{i(x)}\),
\(x\in F\), and vanishes off their union, and \(P\) contains the indicators \(\mathbf 1_{x+U_{i(x)}}\), then
\(\Psi\in P\). Induct on \(\lvert F\rvert\), the empty case being \(\Psi=0\). Otherwise pick \(a\in F\) with
\(i(a)\) minimal, so that \(a+U_{i(a)}\) is a largest coset, and let
\(\Psi_1=\Psi-\Psi(a)\mathbf 1_{a+U_{i(a)}}\). For \(x\in F\setminus\{a\}\) the coset \(x+U_{i(x)}\) is
contained in \(a+U_{i(a)}\) or disjoint from it (as \(U_{i(x)}\subset U_{i(a)}\)), so \(\Psi_1\) is constant
on it; and \(\Psi_1\) vanishes on \(a+U_{i(a)}\), so it is supported in the union over \(F\setminus\{a\}\).
By induction \(\Psi_1\in P\), hence \(\Psi\in P\).

Applying Step 3 to \(U_i=B_i\) and the data of Step 2 gives \(\Psi\in P\). \(\blacksquare\)

## References

1. Lean: `New.IsSchwartzBruhat.mem_of_eventually_coset`, `New.mem_of_nested_cosets`, `New.IsSchwartzBruhat.eventually_const` in `src/New/OneLift/FalseLifts/BottomOfTower.lean`.
