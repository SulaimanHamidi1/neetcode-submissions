class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, ArrayList<String>> map = new HashMap<>();

        for (var s : strs){
            char[] arr = s.toCharArray();
            Arrays.sort(arr);
            String sorted = new String(arr);
            
            if (!map.containsKey(sorted)){
                ArrayList<String> list = new ArrayList<>();
                list.add(s);
                map.put(sorted, list); 
            } else {
                map.get(sorted).add(s);
            }
        }

        return new ArrayList<>(map.values());
    }
}
