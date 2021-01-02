// Question Link:- https://atcoder.jp/contests/abc187/tasks/abc187_c

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

ll modularexpo(ll a , ll n, ll mod)
{
    ll result = 1;
 
    while(n)
    {
        if(n & 1) result = (result * a) % mod;
 
        n >>= 1;
        a = (a * a) % mod;
    }
 
    return result;
}



int main(){

    ll n;
    cin>>n;
    vc<string> arr(n);
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    string ans;
    map<string,bool> mapper;
    for(auto x: arr){
        string temp = x;
        if(x.front()!='!'){
            reverse(all(x));
            x+='!';
            reverse(all(x));
            if(mapper.count(x)){
                ans = temp;
            }
        }
        else{
            reverse(all(x));
            x.pop_back();
            reverse(all(x));
            if(mapper.count(x))
                ans = x;
        }
        mapper[temp] = 1;
    }
    if(ans.empty()){
        cout<<"satisfiable\n";
    }
    else{
        cout<<ans<<endl;
    }
    return 0;
}

