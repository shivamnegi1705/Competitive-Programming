// Question Link:- https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/00000000003381cb

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
    // precalculating perfect squares under 10^7
    unordered_map<ll,ll> mapper;
    vc<ll> perfect;
    for(ll i=0;i<3200;i++){
        ll x = i*i;
        if(x<=10000000){
            mapper[x] = 1;
            perfect.pb(x);
        }
        else{
            break;
        }
    }

    ll t;
    cin>>t;
    ll testcase = 1;
    while(t--){
        ll n;
        cin>>n;
        ll arr[n];
        for(int i=0;i<n;i++){
            cin>>arr[i];
        }
        unordered_map<ll,ll> pre;
        ll ans = 0;
        ll s = 0;
        // minimum value present in prefix
        ll min_prev = 10000000;

        for(ll i=0;i<n;i++){
            // s--> sum from 0 to ith position.
            s+=arr[i];
            // if sum from 0 to ith position is a perfect square.
            if(mapper.find(s)!=mapper.end()){
                ans+=1;
            }
            // we need [L,R] = perfect square
            // [0..R]-[0..L] = perfect square
            // [0..R]-perfect square = [0..L]
            // we traverse all the precalculated perfect squares if sum till now - perfect square is less than minimum available prefix we break
            for(ll j=0;j<perfect.size();j++){
                if(pre.find(s-perfect[j])!=pre.end()){
                    ans+=pre[s-perfect[j]];
                }
                if(s-perfect[j]<min_prev){
                    break;
                }
            }
            // update prefix
            pre[s]+=1;
            // update minimum value of prefix.
            min_prev = min(min_prev,s);
        }
        cout<<"Case #"<<testcase<<": "<<ans<<endl;
        testcase++;
    }
    return 0;
}

