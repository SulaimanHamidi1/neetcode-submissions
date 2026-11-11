
class LRUCache {

    class Node {
        int key, value;
        Node next, prev;

        Node(int key, int value){
            this.key = key;
            this.value = value;
        }
    }

    private Node head, tail;
    private int capacity;
    private HashMap<Integer, Node> cache;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new HashMap<>();
        this.head = new Node(0, 0);
        this.tail = new Node(0, 0);

        head.next = tail;
        tail.prev = head;
    }
    
    public int get(int key) {
        if (cache.containsKey(key)){
            Node node = cache.get(key);
            
            remove(node);
            append(node);

            return node.value;
        }
        return -1;
    }
    
    public void put(int key, int value) {
        if (cache.containsKey(key)){
            Node node = cache.get(key);
            node.value = value;
            remove(node);
            append(node);
            return;
        }

        cache.put(key, new Node(key, value));
        Node node = cache.get(key);
        append(node);

        if (cache.size() > capacity){
            Node start = head.next;
            remove(start);
            cache.remove(start.key);
        }
    }

    private void remove(Node node) {
        Node prev = node.prev;
        Node next = node.next;
        
        prev.next = next;
        next.prev = prev;
    }

    private void append(Node node) {
        Node prev = tail.prev;
        prev.next = node;
        node.prev = prev;
        node.next = tail;
        tail.prev = node;
    }
}
