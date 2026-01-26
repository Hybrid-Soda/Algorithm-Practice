import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public class Graph {
    private void dfs(boolean[] visited, List<List<Integer>> graph, int now) {

        if (!visited[now]) {
            visited[now] = true;
        }

        for (int next: graph.get(now)) {
            dfs(visited, graph, next);
        }
    }

    private void dfsStack(List<List<Integer>> graph, int start, int node) {
        boolean[] visited = new boolean[node+1];
        Deque<Integer> stack = new ArrayDeque<>();

        stack.push(start);

        while (!stack.isEmpty()) {
            int now = stack.pop();

            if (!visited[now]) {
                visited[now] = true;
                List<Integer> adj = graph.get(now);
                for (int i = adj.size() - 1; i >= 0; i--) {
                    stack.push(adj.get(i));
                }
            }
        }
    }
}
