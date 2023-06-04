#include <iostream>
#include <queue>
#include <unordered_set>
#include <vector>

void bfs(const std::vector<std::vector<char>>& graph, char start) {
    std::unordered_set<char> visited;
    std::queue<char> queue;
    queue.push(start);
    visited.insert(start);

    while (!queue.empty()) {
        char node = queue.front();
        queue.pop();
        std::cout << node << " ";

        for (char neighbor : graph[node - 'A']) {
            if (visited.find(neighbor) == visited.end()) {
                queue.push(neighbor);
                visited.insert(neighbor);
            }
        }
    }
}

int main() {
    std::vector<std::vector<char>> graph = {
        {'B', 'C'},    // A
        {'A', 'D', 'E'},    // B
        {'A', 'F'},    // C
        {'B'},    // D
        {'B', 'F'},    // E
        {'C', 'E'}    // F
    };
    char start_node = 'A';
    bfs(graph, start_node);

    return 0;
}

