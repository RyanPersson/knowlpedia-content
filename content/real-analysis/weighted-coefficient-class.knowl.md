+++
id = "real-analysis/weighted-coefficient-class"
title = "Weighted coefficient class"
kind = "definition"
summary = "A parameter-dependent smooth family controlled derivative by derivative by a spatial weight and specified scale powers."
aliases = ["weighted coefficient bounds"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["asymptotics/uniform-parameter-estimate", "real-analysis/multi-index-notation", "real-analysis/class-ck-map", "real-analysis/real-power", "real-analysis/natural-logarithm"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Fix an open domain \(U\), weights \(0<w(x)\le1\), \(0<\delta(x)\le1\), and a small parameter \(0<\varepsilon<\varepsilon_*<1\). Write \(\Lambda_\varepsilon=1+|\log\varepsilon|\). A smooth family \(f_{\varepsilon,\lambda}(x)\) belongs to the **weighted coefficient class** \(\mathcal C^\alpha(w)\) if for every [[real-analysis/multi-index-notation|multi-index]] \(I\) there are \(C_I,m_I,n_I\ge0\) with
\[
|\partial_x^I f_{\varepsilon,\lambda}(x)|
\le C_I\varepsilon^\alpha\Lambda_\varepsilon^{m_I}
w(x)\delta(x)^{-n_I}.
\]
The constants and exponents are independent of \(\varepsilon,\lambda,x\); the parameter domain is common to all derivative orders. This defines one useful convention for a [[asymptotics/uniform-parameter-estimate|uniform weighted class]], not a universal meaning of that notation.

## What the definition controls

Each derivative bound is an assumption. A bound on \(f\) alone gives no bounds on its derivatives or those of \(f/w\). Additional parameter derivatives can be included by enlarging \(x\); otherwise the label \(\lambda\) is held fixed. Support, periodicity, and smooth extension conditions must be specified separately. The weights themselves need not be smooth.
