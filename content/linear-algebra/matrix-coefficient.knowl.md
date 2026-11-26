+++
id = "linear-algebra/matrix-coefficient"
title = "Matrix coefficient of a representation"
kind = "definition"
summary = "Evaluate a linear functional on a translated vector."
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["algebra-representation-theory/group-representation", "linear-algebra/linear-functional"]
+++

Given a [[algebra-representation-theory/group-representation|representation]] \(\pi:G\to\mathrm{GL}(V)\), \(v\in V\) and a [[linear-algebra/linear-functional|linear functional]] \(\lambda\in V^*\), a **matrix coefficient** is the function \(g\mapsto\lambda(\pi(g)v)\).

## References

- [Lib/Weil/Periods/BesselIntegral.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/BesselIntegral.lean)
