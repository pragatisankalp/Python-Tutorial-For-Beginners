#include <bits/stdc++.h>
using namespace std;
void dfs(int s,vector<vector<int>> &adj,vector<bool> &vis){
    vis[s]=true;
    for(auto &it : adj[s]){
        if(vis[it]==false) dfs(it,adj,vis);
    }
}
int main() {
    int n;cin>>n;
    vector<pair<int,int>> points(n);
    for(int i=0;i<n;i++){
    cin>>points[i].first>>points[i].second;
    }
     
    
    vector<vector<int>> adj(n);
    for(int i=0;i<n;i++){
        for(int j=i+1;j<n;j++){
            if(points[i].first==points[j].first || points[i].second==points[j].second){
                adj[i].push_back(j);
                adj[j].push_back(i);
            }
        }
    }
    int cnt=0;
    vector<bool> vis(n,0);
    for(int i=0;i<n;i++){
        if(vis[i]==false){
            cnt++;
            dfs(i,adj,vis);
            
        }
    }
    cout<<cnt-1;
    
}