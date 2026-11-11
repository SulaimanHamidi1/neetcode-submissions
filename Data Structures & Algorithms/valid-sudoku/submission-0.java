class Solution {
    public boolean isValidSudoku(char[][] board) {

        Map<Integer, Set<Character>> rows = new HashMap<>();
        Map<Integer, Set<Character>> cols = new HashMap<>();
        Map<String, Set<Character>> squares = new HashMap<>();

        for (int i = 0; i < board.length; i++){
            for (int j = 0; j < board.length; j++){
                char val = board[i][j];
                String squareKey = (i / 3) + "," + (j / 3);

                if (val == '.') continue;
                if (rows.get(i) == null){
                    rows.put(i, new HashSet<>());
                }

                if (cols.get(j) == null){
                    cols.put(j, new HashSet<>());
                }

                if (squares.get(squareKey) == null){
                    squares.put(squareKey, new HashSet<>());
                }

                if (rows.get(i).contains(val) || 
                    cols.get(j).contains(val) || 
                    squares.get(squareKey).contains(val)) return false;

                rows.get(i).add(val);
                cols.get(j).add(val);
                squares.get(squareKey).add(val);
            }
        }

        return true;
    }
}
