// Question Link:- https://codeforces.com/contest/1436/problem/D

#include<bits/stdc++.h>
using namespace std;
#pragma GCC optimize ("-O3")
#define ll long long  int
#define all(x) (x).begin(), (x).end()
using ld = long double;
const ll mod = 1000000007;
const ll inf = 1000000000000000000;
const ll rk = 256;
const ld PI = 3.141592653589793;
#define pb push_back
#define mp make_pair
#define vc vector
#define fs first
#define sec second
// #define pq priority_queue
#define lb lower_bound
#define ub upper_bound
#define pll pair<ll,ll>
#define pls pair<ll,string>
#define psl pair<string,ll>
#define plc pair<ll,char>
#define pcl pair<char,ll>
#define pss pair<string,string>
#define all(x) (x).begin(), (x).end()
#define tol(s) transform(s.begin(),s.end(),s.begin(),::tolower);
#define tou(s) transform(s.begin(),s.end(),s.begin(),::toupper);
#define print(a) for(auto j:a) {cout<<j<<",";} cout << "\n";
#define endl '\n'
#define FastIO ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0)
// getting string line
// getline(cin,word);
// -> priority_queue < int > pq; // max_heap
// -> priority_queue < int , vector < int > , greater < int > > pq; // min_heap


ostream & operator << (ostream & os, pair <ll, ll> const& x) {
    os << x.first << "," << x.second;
    return os;
}

template <class T>
ostream & operator << (ostream & os, vector <T> const& x) {
    os << "{ ";
    for(auto& y : x) os << y << " ";
    return os << "}";
}

template <class T>
ostream & operator << (ostream & os, set <T> const& x) {
    os << "{ ";
    for(auto& y : x) os << y << " ";
    return os << "}";
}

template <class Ch, class Tr, class Container>
basic_ostream <Ch, Tr> & operator << (basic_ostream <Ch, Tr> & os, Container const& x) {
    os << "{ ";
    for(auto& y : x) os << y << " ";
    return os << "}";
}

template <class X, class Y>
ostream & operator << (ostream & os, pair <X, Y> const& p) {
    return os << "[ " << p.first << ", " << p.second << "]" ;
}

struct Triplet{
    ll x,y,z;
};

ll modularexpo(ll x,ll n,ll mod){
    ll res = 1;
    while(n>0){
        if(n%2==1){
            res = (res*x)%mod;
        }
        x = (x*x);
        n = n/2;
    }
    return res;
}

const ll mex = 2e5+5;
ll n;
vc<ll> graph[mex];
ll values[mex];


array<ll,3> dfs(ll node){
    // if current node is a leaf
    if(graph[node].size()==0){
        array<ll,3> cur = {1,values[node],values[node]};
        return cur;
    }

    array<ll,3> cur = {0,0,values[node]}; // {number of leaves, max value at leave, subtree sum};
    for(auto child: graph[node]){
        auto temp = dfs(child);
        cur[0]+=temp[0];
        cur[2]+=temp[2];
        cur[1] = max(cur[1],temp[1]);
    }
    ll val = ceil((1.0*cur[2])/cur[0]);
    cur[1] = max(cur[1],val);
    // cout<<node<<" "<<cur<<" "<<val<<endl;
    return cur;

}

int main(){
#ifndef ONLINE_JUDGE
    // for getting input from input.txt
    freopen("input.txt", "r", stdin);
    // for writing output to output.txt
    freopen("output.txt", "w", stdout);
#endif
    cin>>n;
    for(ll i=1;i<n;i++){
        ll x;
        cin>>x;
        x--;
        graph[x].pb(i);
    }
    for(ll i=0;i<n;i++){
        cin>>values[i];
    }
    auto ans = dfs(0);
    cout<<ans[1]<<endl;
    return 0;
}
 
