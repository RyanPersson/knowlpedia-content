+++
id = "proofs/grh/onelift-comparison/test-form"
title = "Test form of a descent pair"
kind = "definition"
summary = "A form on V that is integral above a prime l and orthogonal to the false lifts for the idempotent of the label X-1 and the kernel of the descent."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.DescentPair.IsTestForm", "New.PadicPlace.ofIso", "New.PadicPlace.\u03b9\u209a_ofIso"]
lean_files = ["src/New/OneLift/TestedForms.lean"]
+++

Let \(O\) be a [[?lean:New.DescentPair|descent pair]] with Weil data, and \(\ell\) a prime. A form \(\Xi\) on \(V\) is a **test form** above \(\ell\) if

1. \(\Xi\) is integral at every embedding \(j\colon\mathbb{C}\to\mathbb{C}_\ell\): all values of \(\Xi\) have [[?lean:New.weylGauge|gauge]] at most \(1\) at \(j\) ([[?lean:New.integralForms|integral forms]]); and
2. \(\Xi\) is [[proofs/grh/onelift-comparison/false-lifts|orthogonal to the false lifts]] for \(e_0=\bigotimes_{w\in M}e_{w}\), where \(e_w\in\mathbb{C}[\mathrm{GL}_r(k_w)]\) is the [[?lean:New.labelIdem|label idempotent]] of the polynomial \(X-1\), and \(Z=\ker\mathcal{D}_O\), the kernel of the [[?lean:New.DescentPair.normalizedDescent|normalized descent]].

For an isomorphism \(\iota\colon\mathbb{C}\simeq\overline{\mathbb{Q}}_\ell\), the associated \(\ell\)-adic place of \(\mathbb{C}\) is \(\iota\) followed by \(\overline{\mathbb{Q}}_\ell\subset\mathbb{C}_\ell\).

## Remarks

For \(W\) of rank one, \(e_0\) is the mean over \(\prod_{w\in M}\mathrm{GL}_1(k_w)\).

## References

1. Lean: `New.DescentPair.IsTestForm`, `New.PadicPlace.ofIso`, `New.PadicPlace.ιₚ_ofIso` in `src/New/OneLift/TestedForms.lean`.
