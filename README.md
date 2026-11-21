# CSC 225 — Graph Search: BFS and DFS

**Name:** YOUR NAME HERE

This assignment introduces graph representation and two ways to search a graph: depth-first search (DFS) and breadth-first search (BFS).

## How to complete and submit

1. Open the instructor's GitHub repository and click **Fork** to create a copy in your own GitHub account.
2. **Clone your fork** to your computer (or use GitHub Codespaces if your instructor permits it).
3. Open the project in VS Code. Complete the `TODO` sections in `graph.py`. Leave the provided test cases unchanged.
4. Answer the questions **in this README.md file**, replacing each `YOUR ANSWER HERE` with your response. Use your own words.
5. Run `python main.py` and `python test_graphs.py`. Fix any issues and rerun the tests.
6. Commit and push your changes to **your fork** on GitHub. Verify that both your Python code and README answers appear online.
7. Submit **the URL of your forked GitHub repository** to the assignment on **Blackboard**. Do not submit only a link to the original instructor repository.

> The repository you submit must contain your completed `graph.py` and answered `README.md`. No PDF or separate written worksheet is required. You do not need to open a pull request.

## What you will build

We will work with an **undirected, unweighted graph** stored as an **adjacency list**. Each vertex is a dictionary key, and its neighbors are stored in a list. The graph may contain cycles or disconnected components.

Example:

```python
{
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}
```

For consistent traversal results, **visit neighbors in the order they appear in each list**. Do not sort them.

### Part 1 — Build the graph

Open `graph.py`. Implement:

- `add_vertex(v)`: Create an empty neighbor list for a new vertex; do nothing if it already exists.
- `add_edge(u, v)`: Add both endpoints if needed, then add the undirected connection (`u` to `v` and `v` to `u`). Avoid duplicate neighbors. You may assume `u != v`.

**Guidance:** First check `if v not in self.adj`. Then store a list with `self.adj[v] = []`. For an undirected edge, each endpoint belongs in the other's list.

**Question 1.** Why does adding an undirected edge require updating two adjacency lists?

When we add an edge that is undirected, we need to change two adjacency lists since the edge will go both ways. If there is an edge between u and v, then u must be adjacent to v, and v must be adjacent to u.

**Question 2.** What is one advantage of an adjacency list over an adjacency matrix for a graph with relatively few edges?

For a graph which has fewer edges than vertices, the adjacency list representation will require less memory space than the adjacency matrix since there is no need to represent nonexistent edges.

### Part 2 — Depth-first search (DFS)

Implement `dfs(start)` in `graph.py` using **recursion**. Return a list of vertices in the order they are first visited. You may assume `start` is already in the graph.

Suggested approach:

1. Create an empty `visited` set and an empty `order` list.
2. Define a helper function inside `dfs` that accepts a vertex.
3. Mark the vertex visited and append it to `order`.
4. For each neighbor of that vertex, call the helper if that neighbor has not been visited.
5. Call your helper on `start` and return `order`.

**Question 3.** What prevents DFS from visiting vertices forever when a graph contains a cycle?

The visited set stops DFS from revisiting vertices in a loop. If a vertex is already visited, then DFS does not visit that vertex again.

**Question 4.** Starting at `A` in Graph 1 below, write the DFS visit order. Explain where DFS first needs to backtrack.

DFS order: A, B, D, E, F, C

First backtrack: DFS first backtracks at D because D has no unvisited neighbors. The search returns to B and continues with the next unvisited neighbor.

### Part 3 — Breadth-first search (BFS)

Implement `bfs(start)` in `graph.py` using a **queue** (`collections.deque` is already imported). Return a list of vertices in the order they are removed from the queue. You may assume `start` exists.

Suggested approach:

1. Create `visited`, `order`, and an empty `deque`.
2. Add `start` to the queue and immediately mark it visited.
3. While the queue contains vertices, remove its first vertex with `popleft()` and append it to `order`.
4. Add unvisited neighbors to the back of the queue and mark them visited **when they are added**.
5. Return `order`.

**Question 5.** Why should BFS mark a neighbor visited when it is **enqueued**, rather than waiting until it is removed from the queue?

The BFS algorithm needs to mark a neighbor as visited when it gets queued so that it doesn’t get added to the queue again. If it waits until it gets dequeued, then the same vertex may be added to the queue by many neighbors.

**Question 6.** Starting at `A` in Graph 1, write the BFS visit order and list the queue contents immediately after processing `A` and immediately after processing `B`.

BFS order: A, B, C, D, E, F
After processing A, the queue contains: [B, C]
After processing B, the queue contains: [C, D, E]

### Part 4 — Test your code

Run these commands in the project folder:

```bash
python main.py
python test_graphs.py
```

On some computers, use `python3` instead of `python`.

`main.py` builds these graphs, and `test_graphs.py` checks the results. The expected orders assume neighbors are stored in the order the edges were added.

**Graph 1** (branching graph with a cycle):

```text
A--B   A--C   B--D   B--E   C--F   E--F
```

**Graph 2** (diamond):

```text
0--1   0--2   1--3   2--3
```

**Graph 3** (disconnected; `Z` is isolated):

```text
A--B   B--C   X--Y   Z
```

| Test | Start | Expected DFS | Expected BFS |
|---|---|---|---|
| Graph 1 | `A` | `A, B, D, E, F, C` | `A, B, C, D, E, F` |
| Graph 2 | `0` | `0, 1, 3, 2` | `0, 1, 2, 3` |
| Graph 3 | `A` | `A, B, C` | `A, B, C` |
| Graph 3 | `Z` | `Z` | `Z` |

Tests also check neighbor lists and duplicate-edge handling. **Do not modify `test_graphs.py` to make the tests pass.**

**Question 7.** Why do searches starting at `A` in Graph 3 not visit `X`, `Y`, or `Z`?

Searches that begin from A in Graph 3 will never visit X, Y, and Z as they belong to different disconnected components of the graph. There is no way to reach those vertices from A.

**Question 8.** Suppose every edge has the same cost. Which search is useful for finding a path with the fewest edges from a starting vertex: DFS or BFS? Why?

BFS can be used to find the path with the least number of edges when each edge has equal costs. BFS visits vertices in levels, hence it is used to get the shortest path in terms of number of edges.

**Question 9.** After your program works, describe one difference between the orders produced by DFS and BFS on Graph 1.

A difference between them is that DFS will go as far down as it can before backtracking to give an ordering of A, B, D, E, F, C whereas BFS will visit vertices level-by-level, giving an ordering of A, B, C, D, E, F. This means that BFS visits C much earlier than DFS.

### Part 5 — Optional visualization (not graded)

Run:

```bash
python visualize.py
```

This writes `example_graph.dot` using only standard Python. If you have the separate **Graphviz** application installed, you can render it with:

```bash
dot -Tpng example_graph.dot -o example_graph.png
```

Graphviz is **not required** for grading. Do not spend time installing it until BFS and DFS work.

## Files

| File | Purpose |
|---|---|
| `graph.py` | **Edit this:** implement the graph and searches |
| `README.md` | **Edit this:** answer Questions 1–9 |
| `main.py` | Provided examples; run to see results |
| `test_graphs.py` | Provided checks; do not modify |
| `visualize.py` | Optional DOT export |
| `.gitignore` | Excludes generated files |

## Final submission checklist

- [ ] All `TODO` methods in `graph.py` are complete.
- [ ] `python test_graphs.py` reports `All tests passed!`.
- [ ] Questions 1–9 are answered in this `README.md`.
- [ ] My changes are committed and pushed to **my fork**.
- [ ] I submitted the URL of **my fork** in Blackboard.

---

*Source acknowledgment: Graph search topics adapted from the instructor-provided Chapter 22 lecture slides, © 2022 Pearson Education, Inc. The programming prompts, examples, and code structure are prepared for this assignment.*
