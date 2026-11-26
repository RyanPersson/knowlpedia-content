+++
id = "linear-algebra/gram-schmidt-orthogonalization"
title = "Gram–Schmidt orthogonalization"
kind = "construction"
summary = "Successive orthogonal projections turn an ordered independent family into an orthogonal family with the same partial spans."
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/inner-product-space","linear-algebra/orthogonal-projection","linear-algebra/orthonormal-basis","linear-algebra/orthogonality"]
+++

For an ordered linearly independent family \(v_1,\ldots,v_n\) in a real or complex [[linear-algebra/inner-product-space|inner product space]], **Gram–Schmidt orthogonalization** defines
\[
u_i=v_i-\operatorname{proj}_{\operatorname{span}(v_1,\ldots,v_{i-1})}v_i .
\]
The first [[linear-algebra/orthogonal-projection|projection]] is onto the zero space. Normalization gives the [[linear-algebra/orthonormal-basis|orthonormal basis]] \(u_i/\|u_i\|\) of the span.

## Why the spans agree

Each \(u_i\) is [[linear-algebra/orthogonality|orthogonal]] to the preceding span. It is nonzero since \(v_i\) lies outside that span. The difference \(v_i-u_i\) belongs to the preceding span, so adjoining either vector enlarges it to the same subspace. Induction proves the assertion at every step.
