+++
id = "asymptotics/concentration-scale"
title = "Concentration scale"
kind = "definition"
summary = "A shrinking spatial length used to locate the region occupied by a family of profiles."
aliases = []
domains = ["asymptotics"]
section_mode = "progressive"
prerequisites = ["shared-foundations/function", "real-analysis/limit-of-a-function-at-a-point", "shared-foundations/support-of-a-function"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A positive [[shared-foundations/function|function]] \(L(\varepsilon)\to0\) is a **concentration scale** for a profile family
\[
u_\varepsilon(x)=A(\varepsilon)V\left(\frac{x-x_\varepsilon}{L(\varepsilon)}\right).
\]
For a fixed compactly supported \(V\), the [[shared-foundations/support-of-a-function|support]] lies in \(x_\varepsilon+L(\varepsilon)\operatorname{supp}V\). Thus \(L\) specifies a spatial length; \(A\) specifies amplitude, and \(x_\varepsilon\) specifies the center.

## Multiple lengths

Different directions may have different lengths \(L_i\). A parameter \(q\) with transverse length \(q^{1/2}\) is not itself that physical length. Concentration can coexist with a bounded or vanishing integral norm, as the [[real-analysis/concentrating-profile-norms|profile norm scaling]] makes explicit.
