+++
id = "catalog/categories/topological-rings"
title = "Category of unital topological rings"
kind = "definition"
summary = "Hausdorff unital topological rings and continuous unit-preserving ring maps."
aliases = []
domains = ["catalog", "algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/category", "algebra-rings/unital-ring", "topology/continuous-map"]
dependency_heuristic = "catalog-semantic-review-v1"
dependency_review_count = 1
+++

The **category of unital topological rings** used here consists of unital associative rings equipped with a Hausdorff topology for which addition, additive inversion, and multiplication are continuous. Morphisms are [[topology/continuous-map|continuous maps]] preserving addition, multiplication, and \(1\). Identity maps and compositions preserve all these requirements.

## Convention and comparison

The catalogue key `topological-rings` always uses this unit-preserving convention. Adeles and completions carry their specified topologies; forgetting topology leads to [[catalog/categories/unital-rings|unital rings]].
