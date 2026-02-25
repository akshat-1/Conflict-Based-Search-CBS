# Conflict-Based Search (CBS) for Multi-Agent Pathfinding (MAPF)

Conflict-Based Search (CBS) is an **optimal algorithm** for the **multi-agent pathfinding (MAPF)** problem. Unlike traditional A* approaches that treat all agents as a single *joint agent*, CBS decomposes the problem into **multiple single-agent pathfinding problems** constrained by a **high-level search tree**.

---

## Overview of the Two-Level Structure

CBS operates on **two distinct levels** to find an optimal solution:

### 1. High Level (Conflict Tree)

CBS searches a **Constraint Tree (CT)**, which is a **binary tree** where each node represents a set of constraints on agent movements.

- Performs **best-first search**.
- Nodes are ordered by their **total solution cost**.

### 2. Low Level (Single-Agent Search)

For each agent, the low level performs a **fast pathfinding search** under given constraints.

- Typically uses **A***.
- Search state includes **location + time**.

---

## Key Definitions

- **Constraint**  
  A tuple `(a_i, v, t)` that prohibits agent `a_i` from occupying vertex `v` at time `t`.

- **Conflict**  
  A tuple `(a_i, a_j, v, t)` where two agents occupy the same vertex `v` at the same time `t`.

- **Consistent Path**  
  A path for an agent that satisfies **all assigned constraints**.

- **Valid Solution**  
  A set of `k` paths where **no agents conflict** with each other.

---

## The CBS Algorithm

### High-Level Process

The high-level search manages the **Constraint Tree (CT)** and resolves conflicts.

Each CT node **N** contains:

- `N.constraints` – Set of constraints inherited from ancestors plus one new constraint  
- `N.solution` – Set of `k` consistent agent paths  
- `N.cost` – Total solution cost (usually sum-of-costs)

#### Algorithm Steps:

1. **Initialization**  
   - Create a root node with **no constraints**.
   - Compute optimal paths for all agents.
   - Insert the root into the **OPEN list**.

2. **Node Expansion**  
   - Extract the node **P** with the lowest cost.

3. **Validation**  
   - If `P.solution` has **no conflicts**, return it as the **optimal solution**.

4. **Conflict Resolution**  
   - If conflict `(a_i, a_j, v, t)` is found:
     - Create two child nodes:

       **Left Child:** Add constraint `(a_i, v, t)`  
       **Right Child:** Add constraint `(a_j, v, t)`

5. **Low-Level Update**  
   - Re-run low-level search **only for the affected agent**.
   - Update cost and insert new nodes into **OPEN**.

---

### Low-Level Process

The low-level search computes the **shortest valid path** for a single agent.

- **Search Space:** `(k + 1)`-dimensional (space + time)
- **Constraints Handling:**  
  States `(v, t)` violating `(a_i, v, t)` are **discarded**.
- **Tie-Breaking:**  
  Uses a **Conflict Avoidance Table (CAT)** to minimize conflicts with other agents.

---

## Performance and Efficiency

### Advantages:
- Very effective in **bottleneck environments**
- Quickly eliminates conflicting paths

### Drawbacks:
- Performs poorly in **large open spaces**
- Can cause **exponential growth** of the constraint tree

---

## Optimization: Meta-Agent CBS (MA-CBS)

To improve efficiency:

- Agents that conflict **frequently** are **merged into meta-agents**
- Treated as **single composite units**
- Reduces conflict explosion and improves scalability

---

## Summary

CBS provides an **optimal and scalable framework** for MAPF by:
- Decoupling agent planning
- Resolving conflicts incrementally
- Maintaining optimality through constraint-based branching