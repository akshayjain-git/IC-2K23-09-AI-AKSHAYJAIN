#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <algorithm>
using namespace std;

struct Node {
    int id;
    int g;  // Cost from start
    int h;  // Heuristic cost to goal
    int f;  // g + h

    bool operator>(const Node& other) const {
        return f > other.f;
    }
};

int main() {
    int n, edges;
    cout << "Enter number of nodes: ";
    cin >> n;

    vector<vector<pair<int, int>>> graph(n);

    cout << "Enter number of edges: ";
    cin >> edges;

    cout << "Enter edges (u v cost):\n";
    for (int i = 0; i < edges; i++) {
        int u, v, cost;
        cin >> u >> v >> cost;

        graph[u].push_back({v, cost});
        graph[v].push_back({u, cost});
    }

    vector<int> heuristic(n);

    cout << "Enter heuristic values for each node:\n";
    for (int i = 0; i < n; i++) {
        cout << "h(" << i << ") = ";
        cin >> heuristic[i];
    }

    int start, goal;
    cout << "Enter start node: ";
    cin >> start;

    cout << "Enter goal node: ";
    cin >> goal;

    priority_queue<Node, vector<Node>, greater<Node>> openList;

    vector<int> gCost(n, 1e9);
    vector<int> parent(n, -1);
    vector<bool> visited(n, false);

    gCost[start] = 0;

    openList.push({
        start,
        0,
        heuristic[start],
        heuristic[start]
    });

    while (!openList.empty()) {

        Node current = openList.top();
        openList.pop();

        int u = current.id;

        if (visited[u])
            continue;

        visited[u] = true;

        // Goal reached
        if (u == goal)
            break;

        // Explore neighbors
        for (auto edge : graph[u]) {
            int v = edge.first;
            int cost = edge.second;

            int newG = gCost[u] + cost;

            if (newG < gCost[v]) {
                gCost[v] = newG;
                parent[v] = u;

                int f = newG + heuristic[v];

                openList.push({
                    v,
                    newG,
                    heuristic[v],
                    f
                });
            }
        }
    }

    // If goal was not reached
    if (gCost[goal] == 1e9) {
        cout << "No path found.\n";
        return 0;
    }

    // Reconstruct path
    vector<int> path;

    for (int v = goal; v != -1; v = parent[v])
        path.push_back(v);

    reverse(path.begin(), path.end());

    cout << "\nShortest path using A*:\n";

    for (int node : path)
        cout << node << " ";

    cout << "\nTotal cost = " << gCost[goal] << endl;

    return 0;
}
