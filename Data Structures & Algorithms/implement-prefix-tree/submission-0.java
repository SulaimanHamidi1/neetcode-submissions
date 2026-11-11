class PrefixTree {

    class Node {
        HashMap<Character, Node> map;
        Boolean end;

        Node(){
            map = new HashMap<>();
            end = false;
        }
    }

    Node root;

    public PrefixTree() {
        root = new Node();
    }

    public void insert(String word) {
        Node cur = root;

        for (var c : word.toCharArray()){
            if (!cur.map.containsKey(c)){
                cur.map.put(c, new Node());
            }
            cur = cur.map.get(c);
        }
        cur.end = true;
    }

    public boolean search(String word) {
        Node cur = root;

        for (var c : word.toCharArray()){
            if (!cur.map.containsKey(c)){
                return false;
            }
            cur = cur.map.get(c);
        }
        return cur.end;
    }

    public boolean startsWith(String prefix) {
        Node cur = root;

        for (var c : prefix.toCharArray()){
            if (!cur.map.containsKey(c)) return false;
            cur = cur.map.get(c);
        }
        return true;

    }
}
