#include<bits/stdc++.h>
#define endl '\n'
using namespace std;
const int MAX_N = 1e5+2;
int a[MAX_N];
int ar[MAX_N];
pair<int,int> ar2[MAX_N];
int used[MAX_N];
void solve()
{
    int n;
    int num;
    cin>>n;
    for(int i=0; i<n; i++)
    {
        used[i] = 0;
    }
    for(int i=0; i<n; i++)
    {
        cin>>a[i];
        ar[i] = a[i];
    }
    sort(ar,ar+n); /// the optimal wait times
    long long ans = 0;
    for(int i=0; i<n; i++)
    {
        ans+=((long long)ar[i]*(n-i));
    }
    int ptr = 0;
    for(int i=0; i<n; i++)
    {
        if(a[i] == ar[i])
        {
            used[i] = 1; /// the student stays in his original place
        }
        else
        {
            ar2[ptr++] = {a[i],i};
        }
    }
    sort(ar2,ar2+ptr);
    int idx = 0;
    cout<<ans<<endl;
    for(int i=0; i<n; i++)
    {
        if(used[i] == 1) cout<<i+1<<" ";
        else
        {
            cout<<ar2[idx++].second+1<<" ";
        }
    }
    cout<<endl;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int T;
    cin>>T;
    for(int test_number=1; test_number<=T; test_number++)
    {
        solve();
    }
}
