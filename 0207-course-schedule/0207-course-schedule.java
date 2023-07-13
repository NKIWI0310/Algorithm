import java.util.ArrayList;
import java.util.List;

class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        for(int i = 0 ; i < numCourses; i++){
            graph.add(new ArrayList<>());
        }
        
        for(int[] prerequisite : prerequisites){
            int course = prerequisite[0];
            int prerequisiteCourse = prerequisite[1];
            graph.get(course).add(prerequisiteCourse); // index 0 수업을 듣기위해선 index 1이 필요로 함.
        }
        int[] visited = new int[numCourses];
        for(int i = 0 ; i < numCourses; i++){
            if(checkCycle(graph, visited, i)){
                return false;
            }
        }
        return true;
    }
    
    public boolean checkCycle(List<List<Integer>> graph, int[] visited, int check){
        
        if(visited[check] == -1){ //순환감지
            return true;
        }
        if(visited[check] == 1){ //방문감지
            return false;
        }
        
        visited[check] = -1; //방문했으니 -1로 값 설정 
        
        for (int prerequisite : graph.get(check)) {
            if (checkCycle(graph, visited, prerequisite)) {
                return true;
            }
        }
        
        
        visited[check] = 1;
        return false;
        
    }
}


