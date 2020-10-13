// Question Link:- https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class Solution {
public:
    
    int find(int v,vector<int> &parent){
        if(v==parent[v]){
            return v;
        }
        return parent[v] = find(parent[v],parent);
    }
    
    int unions(int a,int b,vector<int> &parent,vector<int> &size){
        int p1 = find(a,parent);
        int p2 =find(b,parent);
        if(p1==p2){
            return -1;
        }
        if(size[p1]>size[p2]){
            size[p1]+=size[p2];
            size[p2] = 0;
            parent[p2] = p1;
        }
        else{
            size[p2]+=size[p1];
            size[p1] = 0;
            parent[p1] = p2;
        }
        return 0;
    }
    
    int comp(vector<int> &arr){
        
        vector<int> ans = arr;
        for(int i=0;i<arr.size();i++){
            ans[i] = find(arr[i],arr);
        }
        
        int cnt = ans[0];
        for(auto i:ans){
            if(cnt!=i){
                return -1;
            }
        }
        return 1;
    }
    
    int maxNumEdgesToRemove(int n, vector<vector<int>>& edges) {
        int ans = edges.size();
        vector<int> parent(n,0),size(n,0);
        for(int i=0;i<edges.size();i++){
            edges[i][1]-=1;
            edges[i][2]-=1;
        }
        for(int i=0;i<n;i++){
            parent[i] = i;
            size[i] = 1;
        }
        
        // process common edge
        for(int i=0;i<edges.size();i++){
            if(edges[i][0]==3){
                ans+=unions(edges[i][1],edges[i][2],parent,size);
            }
        }
        
        vector<int> arr(n,0);
        vector<int> help(n,0);
        for(int i=0;i<n;i++){
            arr[i] = parent[i];
            help[i] = size[i];
        }
        for(int i=0;i<edges.size();i++){
            if(edges[i][0]==2){
                ans+=unions(edges[i][1],edges[i][2],arr,help);
            }
        }
        int f = comp(arr);
        if(f==-1){
            return -1;
        }
        
        
        arr = parent;
        help = size;
        for(int i=0;i<edges.size();i++){
            if(edges[i][0]==1){
                ans+=unions(edges[i][1],edges[i][2],arr,help);
            }
        }
        f = comp(arr);
        if(f==-1){
            return -1;
        }
        
        return edges.size()-ans;
        
    }
};
