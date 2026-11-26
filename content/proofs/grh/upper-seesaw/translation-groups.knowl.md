+++
id = "proofs/grh/upper-seesaw/translation-groups"
title = "Groups of translations with denominators away from q"
kind = "definition"
summary = "Finite adelic vectors that become integral, at every place not dividing q, after multiplication by given finite adeles."
aliases = ["weighted translations", "translations with denominator d away from q"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Seesaw.weightedTranslations", "New.Seesaw.translations"]
lean_files = ["src/New/UpperBound/Seesaw/AdmissibleCombinations.lean"]
+++

Let \(E\) be a [[?c:Number field|number field]] with ring of
[[?c:Finite adele ring of a number field|finite adeles]] \(\mathbb{A}_{E,f}\), let \(\iota\) be a
finite index set, \(q\) a natural number and \(d=(d_i)_{i\in\iota}\) a family of finite adeles. The
**group of weighted translations** is the additive subgroup
\[
T_q(d)=\bigl\{\,x\in\mathbb{A}_{E,f}^{\iota}\;:\; \lvert d_i\,x_i\rvert_w\le 1\ \text{for all } i\in\iota \text{ and all finite places } w\nmid q\,\bigr\}
\]
of \(\mathbb{A}_{E,f}^{\iota}\). Here \(w\nmid q\) means that \(q\) does not lie in the prime ideal
of \(w\), and \(\lvert\cdot\rvert_w\) is the absolute value of the component at \(w\). There is no
condition at the places dividing \(q\).

For a single finite adele \(d\) the **group of translations with denominator \(d\) away from \(q\)**
is \(T_q^{\iota}(d)=T_q\bigl((d)_{i\in\iota}\bigr)\).

## Remarks

These groups index the translates of the vacuum vector that may occur in an
[[proofs/grh/upper-seesaw/admissible-combination|admissible combination]]: a vector
\(x\in T_q^{\iota}(d)\) gives the translate \(\varrho_f(x)v_0\) by the
[[?lean:New.Space.finHeisenbergOp|finite Heisenberg operator]].

## References

1. Lean: `New.Seesaw.weightedTranslations`, `New.Seesaw.translations` in `src/New/UpperBound/Seesaw/AdmissibleCombinations.lean`.
