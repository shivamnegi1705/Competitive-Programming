// Question Link:- https://codeforces.com/contest/1461/problem/D

#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#pragma GCC optimize ("-O3")
#define ll long long  int
#define all(x) (x).begin(), (x).end()
using ld = long double;
const ll mod = 1000000007;
const ll inf = 1e9;
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

vector<ll> arr,pre;
ll n,m;
map<ll,ll> mapper;

void func(ll l,ll r){
    if(l>r){
        return ;
    }
    mapper[pre[r]-pre[l]+arr[l]] = 1;
    if(l==r){
        return ;
    }
    ll a = arr[l];
    ll b = arr[r];
    ll k = (a+b)/2;
    ll ind = upper_bound(all(arr),k)-arr.begin();
    ind--;
    if(ind!=r){
        func(l,ind);
    }
    func(ind+1,r);
}

int main(){
#ifndef ONLINE_JUDGE
    // for getting input from input.txt
    freopen("input.txt", "r", stdin);
    // for writing output to output.txt
    freopen("output.txt", "w", stdout);
#endif
    ll t;
    cin>>t;
    while(t--){
        arr.clear();
        pre.clear();
        mapper.clear();
        cin>>n>>m;
        for(ll i=0;i<n;i++){
            ll x;
            cin>>x;
            arr.pb(x);
        }
        sort(all(arr));
        pre.pb(arr[0]);
        for(ll i=1;i<n;i++){
            pre.pb(pre.back()+arr[i]);
        }
        func(0,n-1);
        while(m--){
            ll x;
            cin>>x;
            if(mapper[x]==1){
                cout<<"Yes"<<endl;
            }
            else{
                cout<<"No"<<endl;
            }
        }
    }
    return 0;
}
