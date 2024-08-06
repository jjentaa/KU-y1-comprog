#include <bits/stdc++.h>

using namespace std;

int canvas_pos[100001], space_ls[100000], summ;
int main(){
    ios_base::sync_with_stdio(0), cin.tie(0);
    int n, m, k, num;
    cin >> n >> m >> k;
    for (int i = 0; i < m; i++) {
        cin >> num;
        canvas_pos[i] = num;
    }
    for (int j=1; j<m; j++){
        space_ls[j-1] = canvas_pos[j]-canvas_pos[j-1]-1;
    }
    
    sort(space_ls, space_ls+m-1);
    
    for(int i=0; i<max(m-k, 0); i++){
        summ+=space_ls[i];
    }
    
    cout<<summ;

    return 0;
}