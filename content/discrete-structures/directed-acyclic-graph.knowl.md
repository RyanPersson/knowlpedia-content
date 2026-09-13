+++
id = "discrete-structures/directed-acyclic-graph"
title = "Directed acyclic graph"
kind = "definition"
summary = "A directed graph containing no directed cycles."
aliases = ["DAG", "acyclic directed graph"]
domains = ["discrete-structures"]
section_mode = "progressive"
prerequisites = ["discrete-structures/directed-graph", "discrete-structures/directed-cycle", "shared-foundations/strict-partial-order"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

A **directed acyclic graph**, or **DAG**, is a [[discrete-structures/directed-graph|directed graph]] with no directed cycle. In particular it has no loop. Reachability by a positive-length directed path is then a strict partial order: concatenation gives transitivity, while acyclicity excludes a path from a vertex to itself.

## Finite and infinite dependency graphs

In a finite DAG, one can successively remove a vertex with no incoming edges, producing an ordering in which every edge points forward. Such a vertex must exist: otherwise repeatedly following incoming edges in the finite set would repeat a vertex and create a cycle.

An infinite DAG can contain an infinite chain. Acyclicity alone therefore does not show that recursive prerequisite expansion terminates at foundational data. That additional claim requires a well-founded dependency relation or an explicit audit of the reachable graph.
