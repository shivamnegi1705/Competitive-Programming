// Question Link:- https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d40bb

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

ll n,k,p;
ll mat[55][55];
ll pre[55][55];
ll dp[55][1710];

// i--> stack number
// rem --> number of remaining plates to pick.
ll func(ll i,ll rem){

    // if we have traversed all the stacks 
    // or we have selected p plates then we cannot choose more.
    if(i==n || rem==0){
        return 0;
    }

    // if this state is already been calculated.
    if(dp[i][rem]!=-1){
        return dp[i][rem];
    }

    // incl--> will store max ans.
    ll incl = 0;
    for(ll j=0;j<k;j++){
        // taking 1st j+1 elements from the stack if possible
        if(j+1<=rem){
            incl = max(incl,pre[i][j]+func(i+1,rem-j-1));
        }
        // if we cannot choose j+1 plates from this stack change stack.
        else{
            incl = max(incl,func(i+1,rem));
        }
    }
    // choose none of the plates from this stack.
    incl = max(incl,func(i+1,rem));

    // set dp for this state with max ans.
    return dp[i][rem] = incl;
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
    ll testcase = 1;
    while(t--){
        cin>>n>>k>>p;

        // initialize DP
        memset(dp,-1,sizeof(dp));
        for(ll i=0;i<n;i++){
            for(ll j=0;j<k;j++){
                cin>>mat[i][j];
                pre[i][j] = mat[i][j];
            }
        }

        for(ll i=0;i<n;i++){
            for(ll j=1;j<k;j++){
                pre[i][j]+= pre[i][j-1];
            }
        }

        cout<<"Case #"<<testcase<<": "<<func(0,p)<<endl;
        testcase++;
    }
    return 0;
}
