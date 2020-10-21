// Question Link:-  https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08/0000000000386edd
// Solution for 13pts.


#include<bits/stdc++.h>
#define ll long long int
#define ld long double
#define pi pair<int,int>
#define all(x) x.begin(), x.end()
#define allr(x) x.rbegin(), x.rend()
#define sz(x) ((int)x.size())
#define ln(x) ((int)x.length())
#define mp make_pair
#define pb push_back
#define ff first
#define ss second
#define endl '\n'
#define dbg(x) cout<<#x<<": "<<x<<endl
#define clr(x,v) memset(x, v, sizeof(x))
#define FASTIO ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
using namespace std;
const double eps = 1e-7;
const double PI = acos(-1.0);
const ll mod = 1e9 + 7;
const int MAXN = 1e6 + 5;

void cp()
{
    int n, a, b;
    cin >> n >> a >> b;
    vector<vector<int>> adj(n + 1);
    for(int i = 1; i <= n - 1; i++)
    {
        int u;
        cin >> u;
        adj[u].pb(i + 1);
    }

    ld total_ways = (n * 1.0) * (n * 1.0);
    ld ans = 0;
    for(int i = 1; i <= n; i++)
    {
        ld me = 0;
        ld pa = 0, pb = 0;
        queue<pi> q;
        q.push({i, 0});
        vector<bool> vis(n + 1, false);
        while(!q.empty())
        {
            pi node = q.front();
            q.pop();
            int u = node.ff;
            int d = node.ss;
            vis[u] = true;
            if(d % a == 0)
                pa++;
            if(d % b == 0)
                pb++;
            for(int v : adj[u])
            {
                if(!vis[v])
                    q.push({v, d + 1}), vis[v] = true;
            }
        }
        me = pa * n + pb * n - pa * pb;
        me /= total_ways;
        ans += me;
    }

    cout << setprecision(7) << fixed << ans + eps;
}

int main()
{
    FASTIO;
    int t;
    t = 1;
    cin >> t;
    for(int i = 1; i <= t; i++)
    {
        cout << "Case #" << i << ": ";
        cp();
        cout << endl;
    }
    return 0;
}
