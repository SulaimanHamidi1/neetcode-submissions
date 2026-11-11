class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        
        for (String s : strs){
            int len = s.length();
            sb.append(len).append("#").append(s);
        }

        return sb.toString();
    }

    public List<String> decode(String str) {
        List<String> lst = new ArrayList<>();
        int i = 0;

        while (i < str.length()){
            int j = i;

            while (str.charAt(j) != '#'){
                j++;
            }

            int len = Integer.parseInt(str.substring(i, j));
            i = j + 1;
            j = i + len;
            lst.add(str.substring(i, j));
            i = j;
        }

        return lst;
    }
}
