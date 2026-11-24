+++
id = "analytic-number-theory/square-root-bound"
title = "Square-root bound"
kind = "definition"
summary = "An error bound on the scale of √x, often allowing logarithms or an arbitrarily small power of x."
aliases = ["square-root exponent", "exponent 1/2"]
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["asymptotics/big-o"]
+++

A **square-root bound** controls the error in a quantity of scale \(x\) by about \(\sqrt{x}=x^{1/2}\). A precise version often used in number theory is \(E(x)=O_\varepsilon(x^{1/2+\varepsilon})\) for every \(\varepsilon>0\). In this [[asymptotics/big-o|big-O notation]] the constant may depend on \(\varepsilon\). A one-sided bound only asserts \(E(x)\le C_\varepsilon x^{1/2+\varepsilon}\).

## Balancing two errors

For \(m>0\), the expression \(m+x/m\) has minimum \(2\sqrt{x}\) at \(m=\sqrt{x}\). For \(x\ge1\), the integer \(m=\lceil\sqrt{x}\rceil\) satisfies \(m\le\sqrt{x}+1\) and \(x/m\le\sqrt{x}\). The same choice therefore gives \(m+x/m\le2\sqrt{x}+1\).
