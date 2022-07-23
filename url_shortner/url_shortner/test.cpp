#include <bits/stdc++.h>
#define ll long long
#define S set<ll>
#define V vector<ll>
using namespace std;
void dfs(ll i,vector<bool> &vis,vector<V> &adj,V &index)
{
 if(vis[i])
 return;
 index.push_back(i);
 vis[i]=1;
 for(auto j:adj[i])
 dfs(j,vis,adj,index);
}
int main() {
    ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
    
     
      ll t=1;
      //cin>>t;
      while(t--)
      {
       ll n;
       //cin>>n;
       for(ll m=2;m<20;m++)
       {
        for(ll i=1;i<20;i++)
        for(ll j=1;j<20;j++)
        {ll x=((i*m)/__gcd(i,m))-i;
        ll y=((j*m)/__gcd(j,m))-j;
         if(x == y)
         cout<<i<<" "<<j<<"\t";
        }
        cout<<endl<<endl;;
       }
       
      }
    return 0;
}
