#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
const int N=1e5+777;
struct edge{int v,nxt,w;}e[N*2];
int n,m,cnt,tot,cnt1,st[N],ed[N],len[N],hd[N],pq[N],dep[N],fa[N][20],fo[N],id[N];
ll dis[N],mp[50][50],d1[N],d2[N];
bool has[N];
int find(int x){return x==fo[x]?x:fo[x]=find(fo[x]);}
void add(int x,int y,int z){e[++cnt1].v=y;e[cnt1].nxt=hd[x];hd[x]=cnt1;e[cnt1].w=z;}
void dfs(int u)
{
	for(int i=hd[u];i;i=e[i].nxt)
	if(e[i].v!=fa[u][0])fa[e[i].v][0]=u,dep[e[i].v]=dep[u]+1,dis[e[i].v]=dis[u]+e[i].w,dfs(e[i].v);
}
int lca(int x,int y)
{
	if(dep[x]<dep[y])swap(x,y);
	int t=dep[x]-dep[y];
	for(int i=0;(1<<i)<=t;i++)if(t&(1<<i))x=fa[x][i];
	if(x==y)return x;
	for(int i=19;~i;i--)
	if(fa[x][i]!=fa[y][i])x=fa[x][i],y=fa[y][i];
	return fa[x][0];
}
int main()
{
	scanf("%d%d",&n,&m);
	for(int i=1;i<=n;i++)fo[i]=i;
	for(int i=1,x,y,z,a,b;i<=m;i++)
	{
		scanf("%d%d%d",&x,&y,&z);
		a=find(x),b=find(y);
		if(a!=b)add(x,y,z),add(y,x,z),fo[a]=b;
		else has[x]=has[y]=1,st[++tot]=x,ed[tot]=y,len[tot]=z;
	}
	dfs(1);
	for(int j=1;j<=19;j++)
	for(int i=1;i<=n;i++)
	fa[i][j]=fa[fa[i][j-1]][j-1];
	for(int i=1;i<=n;i++)if(has[i])pq[++cnt]=i,id[i]=cnt;
	for(int i=1;i<=cnt;i++)
	for(int j=1;j<=cnt;j++)
	if(i!=j)
	mp[i][j]=dis[pq[i]]+dis[pq[j]]-2*dis[lca(pq[i],pq[j])];
	for(int i=1;i<=tot;i++)
	mp[id[st[i]]][id[ed[i]]]=mp[id[ed[i]]][id[st[i]]]=min(mp[id[st[i]]][id[ed[i]]],1ll*len[i]);
	for(int k=1;k<=cnt;k++)
	for(int i=1;i<=cnt;i++)
	for(int j=1;j<=cnt;j++)
	if(mp[i][k]+mp[k][j]<mp[i][j])mp[i][j]=mp[i][k]+mp[k][j];
	int Q;scanf("%d",&Q);
	while(Q--)
	{
		int a,b;
		scanf("%d%d",&a,&b);
		ll ans=dis[a]+dis[b]-2*dis[lca(a,b)];
		for(int i=1;i<=cnt;i++)
		d1[i]=dis[a]+dis[pq[i]]-2*dis[lca(a,pq[i])],d2[i]=dis[b]+dis[pq[i]]-2*dis[lca(b,pq[i])];
		for(int i=1;i<=cnt;i++)
		for(int j=1;j<=cnt;j++)
		ans=min(ans,mp[i][j]+d1[i]+d2[j]);
		printf("%lld\n",ans);
	}
}
