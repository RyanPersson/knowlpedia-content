+++
id = "langlands/root-number"
title = "Root number"
kind = "definition"
summary = "The unit-modulus constant in a normalized local or global L-function functional equation."
aliases = ["local root number", "global root number", "sign of the functional equation"]
domains = ["langlands", "number-theory"]
prerequisites = ["langlands-letter/knowls/euler-product-and-local-factor", "langlands-letter/knowls/contragredient-representation"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

After an
[[langlands-letter/knowls/euler-product-and-local-factor|\(L\)-function]] has
been completed and normalized so that its functional
equation relates \(s\) to \(1-s\), its **global root number** is the
unit-modulus constant \(w\) in

\[
\Lambda(s)=w\,\Lambda(1-s,\text{dual data}).
\]

Here “dual data” means the appropriate
[[langlands-letter/knowls/contragredient-representation|contragredient]]
parameter or representation. For self-dual data with the usual reality
conditions, \(w\in\{+1,-1\}\) and
is often called the **sign of the functional equation**.  Without self-duality
the root number can be any complex number of absolute value one.

## Local root numbers

For a local
[[langlands/weil-deligne-representation|Weil–Deligne representation]] \(V\)
and additive [[algebra-representation-theory/character|character]] \(\psi\),
the local root number is the unit-modulus normalization of the
[[langlands/local-epsilon-factor|epsilon factor]] at the central point,

\[
w(V,\psi)=
\frac{\varepsilon(1/2,V,\psi)}
{|\varepsilon(1/2,V,\psi)|}.
\]

For global data and compatible choices, the global root number is the product
of the local root numbers.  Almost every local factor equals \(1\).

## Convention warning

The central point may be written \(1/2\), \(0\), or another shifted value,
depending on whether the L-function is in analytic, motivic, or unitary
normalization.  Local root numbers can also change with the additive
character; the global product is choice-independent after the standard global
compatibility is imposed.

## References

1. Pierre Deligne, “Les constantes des équations fonctionnelles des fonctions
   \(L\),” in *Modular Functions of One Variable II*, Lecture Notes in
   Mathematics 349, Springer, 1973, 501–597.
2. John Tate, “Number theoretic background,” in *Automorphic Forms,
   Representations and L-Functions*, Proceedings of Symposia in Pure
   Mathematics 33, part 2, 1979.
