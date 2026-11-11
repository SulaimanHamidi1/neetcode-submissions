/*
Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    HashMap<Node, Node> oldToNew = new HashMap<>();

    public Node cloneGraph(Node node) {    
        return (node != null) ? dfs(node) : null;
    }

    public Node dfs(Node cur){
        if (oldToNew.containsKey(cur)){
            return oldToNew.get(cur);
        }

        Node copy = new Node(cur.val);
        oldToNew.put(cur, copy);

        for (var nei : cur.neighbors){
            copy.neighbors.add(dfs(nei));
        }
        return copy;
    }
}