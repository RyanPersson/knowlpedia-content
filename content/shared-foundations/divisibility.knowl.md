+++
id = "shared-foundations/divisibility"
title = "Divisibility"
kind = "knowl"
summary = "The relation that one integer is an exact multiplicative factor of another."
aliases = ["divides", "divisibility", "divisor"]
domains = ["shared-foundations"]
+++

For [[shared-foundations/integers|integers]] $a$ and $b$, one says that **$a$ divides $b$**, written $a\mid b$, if there exists an integer $c$ such that $b=ac$. Then $a$ is a divisor of $b$, and $b$ is a multiple of $a$.

When $a,b>0$, divisibility can be tested prime by prime: $a\mid b$ exactly when $v_p(a)\le v_p(b)$ for every prime $p$, where $v_p$ denotes the [[shared-foundations/p-adic-valuation|$p$-adic valuation]].
