+++
id = "asymptotics/leading-order"
title = "Leading order"
kind = "definition"
summary = "The first nonvanishing contribution in an ordered asymptotic expansion."
aliases = []
domains = ["asymptotics"]
section_mode = "progressive"
prerequisites = ["asymptotics/asymptotic-scale", "asymptotics/leading-term"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++


If a function has [[asymptotics/leading-term|leading term]] \(a_k\phi_k\) in an asymptotic expansion, its **leading order** is the comparison scale \(\phi_k\), up to a nonzero constant factor. Thus a leading term \(3\varepsilon^2\) has order \(\varepsilon^2\). The limiting variable and the chosen [[asymptotics/asymptotic-scale|scale]] are part of the statement.

## Cancellations change the order

If two quantities of order \(\varepsilon\) have equal leading coefficients, their difference may have order \(\varepsilon^2\) or smaller. An upper bound \(f=O(\varepsilon)\) alone does not establish a nonzero leading term.
