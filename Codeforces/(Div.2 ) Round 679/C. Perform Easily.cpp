// Question Link:- https://codeforces.com/contest/1435/problem/C

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



int main(){
#ifndef ONLINE_JUDGE
    // for getting input from input.txt
    freopen("input.txt", "r", stdin);
    // for writing output to output.txt
    freopen("output.txt", "w", stdout);
#endif
    ll arr[6];
    for(ll i=0;i<6;i++){
        cin>>arr[i];
    }
    ll n;
    cin>>n;
    ll brr[n];
    for(ll i=0;i<n;i++){
        cin>>brr[i];
    }
    vc<pll> diff;
    for(ll i=0;i<6;i++){
        for(ll j=0;j<n;j++){
            diff.pb({brr[j]-arr[i],j});
        }
    }
    sort(all(diff));
    ll cnt = 0;
    map<ll,ll> d;
    ll ans = LLONG_MAX;
    ll l=0,r=0;
    while (r<diff.size()){
        while(cnt<n && r<diff.size()){
            if(d[diff[r].second]==0){
                d[diff[r].second]++;
                cnt++;
            }
            else{
                d[diff[r].second]+=1;
            }
            r++;
        }

        while(cnt>=n){
            if(cnt>=n){
                ans = min(ans,diff[r-1].first-diff[l].first);
            }
            d[diff[l].second]-=1;
            if(d[diff[l].second]==0){
                cnt-=1;
            }
            l+=1;
        }
    }
    cout<<ans<<endl;
    return 0;
}
 
