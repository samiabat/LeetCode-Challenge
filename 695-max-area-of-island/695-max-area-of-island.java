class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int max = 0;
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[0].length;j++){
                if(grid[i][j]==1){
                    max = Math.max(max,dfs(grid,i,j));
                }
            }
        }
        return max;
    }
    int dfs(int[][] mat,int i, int j){
        if(i<0 || j<0 || i>=mat.length || j>=mat[0].length || mat[i][j]!=1){
            return 0;
        }
        mat[i][j]=0;
        return 1+dfs(mat,i+1,j)+dfs(mat,i-1,j)+dfs(mat,i,j+1)+dfs(mat,i,j-1);
    }
}