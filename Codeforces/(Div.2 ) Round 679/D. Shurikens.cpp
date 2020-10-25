// Question Link:- https://codeforces.com/contest/1435/problem/D

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
    ll n;
    cin>>n;
    vc<pair<char,ll>> query;
    set<ll> avail;
    vc<pll> arr;
    vc<ll> values;
    char x;
    ll y;
    for(ll i=0;i<2*n;i++){
        cin>>x;
        if(x=='+'){
            query.pb({x,0});
            avail.insert(i);
        }
        else{
            cin>>y;
            query.pb({x,y});
            arr.pb({y,i});
        }
        values.pb(-1);
    }
    sort(all(arr));
    ll f = 1;
    vc<ll> ans;
    for(auto i: arr){
        auto it = avail.lower_bound(i.second);
        if(it==avail.end()){
            it--;
            if(*it < i.second){
                ll idx = *it;
                values[idx] = i.first;
                avail.erase(it);
            }
            else{
                f = 0;
                break;
            }
            
        }
        else{
            it--;
            ll idx = *it;
            values[idx] = i.first;
            avail.erase(it);
        }
    }
    if(f==0){
        cout<<"NO"<<endl;
        return 0;
    }
    priority_queue < ll , vector < ll > , greater < ll > > pq;
    for(ll i=0;i<2*n;i++){
        if(query[i].first=='+'){
            pq.push(values[i]);
            ans.pb(values[i]);
        }
        else{
            if(pq.size()==0){
                cout<<"NO"<<endl;
                return 0;
            }
            else{
                ll val = pq.top();
                pq.pop();
                if(val!=query[i].second){
                    cout<<"NO"<<endl;
                    return 0;
                }
            }
        }

    }
    cout<<"YES"<<endl;
    for(auto i:ans){
        cout<<i<<" ";
    }

    return 0;
}
 
