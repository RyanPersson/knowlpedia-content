+++
id = "analytic-number-theory/prime-number"
title = "Prime number"
kind = "definition"
summary = "An integer greater than one whose only positive divisors are one and itself."
aliases = ["rational prime", "prime integer"]
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["shared-foundations/divisibility", "shared-foundations/integers"]
+++

A **prime number** is an [[shared-foundations/integers|integer]] \(p>1\) whose only positive [[shared-foundations/divisibility|divisors]] are \(1\) and \(p\). For instance, \(7\) is prime. The integer \(9\) has the additional divisor \(3\).

## Testing small divisors

If \(n=ab\) with \(1<a\le b\), then \(a\le\sqrt n\). To test whether \(29\) is prime, it suffices to check the primes \(2,3,5\), since every integer greater than one has a prime divisor. None divides \(29\).
