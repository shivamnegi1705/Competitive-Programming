// Question Link:- https://atcoder.jp/contests/abc180/tasks/abc180_e


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

vc<array<ll,3>> arr;
ll n;
ll ans[18][1<<17];

ll helper(ll a,ll b){
    ll val = abs(arr[a][0]-arr[b][0])+abs(arr[a][1]-arr[b][1]);
    val+=max(arr[a][2]-arr[b][2],0LL);

    return val;
}

ll func(ll i,ll m){
    if(m==((1<<n)-1)){
        return helper(i,0);
    }

    if(ans[i][m]!=-1){
        return ans[i][m];
    }

    ll mex = INT_MAX;
    for(int j=0;j<n;j++){
        if( ((m>>j)&1)==0 ){
            mex = min(mex,helper(i,j)+func(j,m|(1<<j)));
        }
    }
    return ans[i][m] = mex;
}


int main(){
    cin>>n;
    arr.resize(n);
    for(int i=0;i<n;i++){
        int x,y,z;
        cin>>x>>y>>z;
        arr[i] = {x,y,z};
    }
    memset(ans,-1,sizeof(ans));
    ll ans = func(0,1);
    cout<<ans<<endl;
    return 0;
}
