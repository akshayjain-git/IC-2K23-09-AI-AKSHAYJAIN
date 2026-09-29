#include <iostream>
#include <vector>
#include <queue>
using namespace std;

struct Node {
    int vertex;
    int heuristic;

    bool operator>(const Node& other) const {
        return heuristic > other.heuristic;
    }
};

void bestFirstSearch(vector<vector<int>>& graph,
                     vector<int>& heuristic,
                     int start, int goal) {

    priority_queue<Node, vector<Node>, greater<Node>> pq;

    vector<bool> visited(graph.size(), false);
    vector<int> parent(graph.size(), -1);

    pq.push({start, heuristic[start]});

    while (!pq.empty()) {

        Node current = pq.top();
        pq.pop();

        int u = current.vertex;

        if (visited[u])
            continue;

        visited[u] = true;

        cout << "Visited: " << u << endl;

        // Goal reached
        if (u == goal) {
            cout << "Goal found!\n";
            break;
        }

        // Add neighboring nodes
        for (int v : graph[u]) {
            if (!visited[v]) {
                parent[v] = u;
                pq.push({v, heuristic[v]});
            }
        }
    }

    if (!visited[goal]) {
        cout << "Goal not found.\n";
        return;
    }

    // Construct path
    vector<int> path;

    for (int v = goal; v != -1; v = parent[v])
        path.push_back(v);

    cout << "\nPath: ";

    for (int i = path.size() - 1; i >= 0; i--)
        cout << path[i] << " ";

    cout << endl;
}

int main() {

    int n, edges;

    cout << "Enter number of nodes: ";
    cin >> n;

    vector<vector<int>> graph(n);

    cout << "Enter number of edges: ";
    cin >> edges;

    cout << "Enter edges (u v):\n";

    for (int i = 0; i < edges; i++) {
        int u, v;
        cin >> u >> v;

        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    vector<int> heuristic(n);

    cout << "Enter heuristic values:\n";

    for (int i = 0; i < n; i++) {
        cout << "h(" << i << ") = ";
        cin >> heuristic[i];
    }

    int start, goal;

    cout << "Enter start node: ";
    cin >> start;

    cout << "Enter goal node: ";
    cin >> goal;

    bestFirstSearch(graph, heuristic, start, goal);

    return 0;
}
