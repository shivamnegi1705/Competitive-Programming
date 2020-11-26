// Question Link:- https://atcoder.jp/contests/abc184/tasks/abc184_d

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

ll a,b,c;
double memo[102][102][102];
const double error = -1000000000;

double func(int i,int j, int k){
    if(i==100 || j==100 || k==100){
        return (i+j+k)-(a+b+c);
    }
    if(fabs(memo[i][j][k]+1)>error){
        return memo[i][j][k];
    }
    double cnt = 0;
    double pre = (i+j+k);
    if(k>0){
        cnt+=(double(k)/pre)*func(i,j,k+1);
    }
    if(i>0){
        cnt+=(double(i)/pre)*func(i+1,j,k);
    }
    if(j>0){
        cnt+=(double(j)/pre)*func(i,j+1,k);
    }
    return memo[i][j][k] = cnt;
}
int main(){
    cin>>a>>b>>c;
    memset(memo,-1,sizeof(memo));
    cout << fixed << setprecision(9)<< func(a,b,c)<<endl;
    return 0;
}

