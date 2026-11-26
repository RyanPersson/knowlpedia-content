+++
id = "proofs/grh/upper-objects/good-idempotent"
title = "The group of the chosen places and the good idempotent e_0"
kind = "definition"
summary = "The finite group G-bar, a product of GL_r over the residue fields at the chosen places, and the central idempotent e_0 of its group algebra, the sum of the label idempotents over the good families."
aliases = ["good idempotent", "e_0", "chosen GL", "good families of labels"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.chosenPlace", "New.Data.chosenGL", "New.Data.goodTupleFamilies", "New.Data.mem_goodTupleFamilies", "New.Data.e₀", "New.Data.isCentralProj_e₀"]
lean_files = ["src/New/UpperBound/Objects/LabelsAndIndexTypes.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]] with level primes \(p_0,p_1\), field \(E\), rank \(r\) and [[proofs/grh/upper-objects/index-sets-of-the-hermitian-spaces|row index set]] \(\mathcal R\) (\(\lvert\mathcal R\rvert=r\)). For \(i\in\{0,1\}\) let \(C_i\) be the finite set of [[?lean:New.Data.ChosenPlace|chosen places above \(p_i\)]]: the finite places of \(E\) dividing both \(p_i\) and \(\pi_M\). Put \(C=C_0\sqcup C_1\) and let \(\mathbb F_w\) be the residue field at \(w\).

**Definition.** The **group of the chosen places** is the finite group
\[
\bar G=\prod_{w\in C}\mathrm{GL}_{\mathcal R}(\mathbb F_w).
\]
A family \(c=(c_w)_{w\in C}\) of polynomials \(c_w\in\mathbb F_w[X]\) is a **good family** if for each \(i\in\{0,1\}\) the tuple \((c_w)_{w\in C_i}\) is a [[proofs/grh/upper-objects/good-tuple-of-labels|good tuple]] for \(M=q_2\) and degree \(r\); that is, every \(c_w\) is a label of degree \(r\) without roots in \(\mathbb F_w\) that are \(q_2\)-th roots of unity, and above each of \(p_0\), \(p_1\) at least one \(c_w\) is primitive. Here \(q_2=q_2(s)\) is the [[?lean:New.Parameters.q₂|integer \(q_2\)]] at the tower exponent \(s\) of \(D\).

The **good idempotent** is the element of the [[?c:group algebra|group algebra]] \(\mathbb C[\bar G]\)
\[
e_0=\sum_{c\ \mathrm{good}}e_c,\qquad e_c=\bigotimes_{w\in C}e_{c_w},
\]
where \(e_{c_w}\in\mathbb C[\mathrm{GL}_{\mathcal R}(\mathbb F_w)]\) is the [[?lean:New.labelIdem|idempotent of the label]] \(c_w\) and the pure tensor is formed in \(\mathbb C[\bar G]=\bigotimes_w\mathbb C[\mathrm{GL}_{\mathcal R}(\mathbb F_w)]\) ([[?lean:New.tupleIdem|tuple idempotent]]).

## Properties

\(e_0\) is a central idempotent of \(\mathbb C[\bar G]\) whose coefficient function is a class function (hence it is self-adjoint). This is the general fact that a sum of tuple idempotents over a set of tuples of labels is a central projection, [[?lean:New.isCentralProj_sum_tupleIdem|proved with the label idempotents]]; it rests on the orthogonality of the idempotents of distinct labels.

## References

1. Lean: `New.Data.chosenGL`, `New.Data.goodTupleFamilies`, `New.Data.e₀`, `New.Data.isCentralProj_e₀` in `src/New/UpperBound/Objects/LabelsAndIndexTypes.lean`.
