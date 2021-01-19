// Question Link:- https://codeforces.com/contest/1474/problem/C

#include<bits/stdc++.h>
#define endl '\n'
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<int> arr(2*n);
        for(int i=0;i<2*n;i++){
            cin>>arr[i];
        }
        sort(arr.begin(),arr.end());
        vector<vector<int>> moves;
        int final = -1;
        int i = 0;
        while (i<2*n-1 && final==-1){
            moves.clear();
            int target = arr.back()+arr[i];
            map<int,int> mapper;
            for(auto j: arr){
                mapper[j]++;
            }
            bool flag = true;
            while(mapper.size()!=0 && flag==true){
                auto it = *mapper.rbegin();
                int last = it.first;
                mapper[last]--;
                if(mapper[last]==0){
                    mapper.erase(last);
                }
                auto ind = mapper.lower_bound(target-last);
                if(ind!=mapper.end()){
                    auto temp = *ind;
                    int val = temp.first;
                    if(val==target-last){
                        mapper[val]--;
                        if(mapper[val]==0){
                            mapper.erase(val);
                        }
                        moves.push_back({last,val});
                        target = max(last,val);
                    }
                    else{
                        flag = false;
                    }
                }
                else{
                    flag = false;
                }
            }
            if(flag==true){
                final = arr.back()+arr[i];
                break;
            }
            i++;
        }
        if(final==-1){
            cout<<"NO"<<endl;
        }
        else{
            cout<<"YES"<<endl;
            cout<<final<<endl;
            for(auto i:moves){
                cout<<i[0]<<" "<<i[1]<<endl;
            }
        }
    }
    return 0;
}
