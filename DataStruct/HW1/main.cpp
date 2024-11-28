#include <iostream>
#include <vector>
using namespace std;

class mazeproblem
{
private:
    vector<vector<int>> data;
public:
    void InsertMaze(int len,int wid);
    void findpath(int len,int wid);
};
void mazeproblem::InsertMaze(int len,int wid){
    //cout<<"input maze data: ";
    for (int row = 0; row < len; row++)
    {
        if (data.size() <= row) data.resize(row + 1);
        for (int col = 0; col < wid; col++)
        {
            if (data[row].size() <= col) data[row].resize(col + 1);
            cin>>data[row][col];
            //cout<<a<<" "<<data[row][col];
        }
    }
}


void mazeproblem::findpath(int len,int wid){
    //char dir[8]={'n','ne','e','se','s','sw','w','nw'};
    int dir[8][2]={{-1,0},{-1,1},{0,1},{1,1},{1,0},{1,-1},{0,-1},{-1,-1}};
    int step=0,branch[8];
    int cp_step=0,right_step=0;
    int cp_mode=0,right_mode=0;
    struct Checkpoint{int x,y,step=0;};
    struct Right{int x,y;};
    struct Been{int x,y;};
    struct Current{int x=0,y=0,mode=0;};
    struct Next{int x,y,count;};

    Checkpoint checkpoint[len*wid];
    Right right[len*wid];
    Been been[len*wid];
    Current current;
    Next next;

    
    //the actual working part idk ffs, fml im gonna kms
    while (1){
        next.count=0;
        for (int i = 0; i < 8; i++){
            branch[i]=0;
            next.x = current.x+dir[i][0];
            next.y = current.y+dir[i][1];
            if(next.x<0 || next.y<0 || next.x>=len || next.y>=wid) continue;

            been[step].x = current.x;
            been[step].y = current.y;
            for (int i = 0; i < step; i++){
                if(next.x==been[i].x && next.y==been[i].x) continue;
            }
            
            if(data[next.x][next.y]==0){
                next.count++;
                branch[i]++;
            }else continue;
            step++;
        }
        if(next.count>1){
            checkpoint[cp_step].x=current.x;
            checkpoint[cp_step].y=current.y;
            checkpoint[cp_step].step=right_step;
            
            cp_step++;
            for (int i=0;i<8;i++){
                if(branch[i]==1){
                    current.x += dir[i][0];
                    current.y += dir[i][1];
                    continue;
                }
            }
        }else if(next.count==1){
            right[right_step].x=current.x;
            right[right_step].y=current.y;
            for (int i=0;i<8;i++){
                if(branch[i]==1){
                    current.x += dir[i][0];
                    current.y += dir[i][1];
                }
            }
            right_step++;
        }else if(next.count==0){
            cp_step--;
            current.x = checkpoint[cp_step-1].x;
            current.y = checkpoint[cp_step-1].y;
            right_step=checkpoint[cp_step-1].step;
        }

        if(current.x==len-1 && current.y==wid-1){
            for (size_t i = 0; i < right_step; i++)
            {
                cout<<"( "<<right[i].x <<","<<right[i].y<< " ), ";
            }
            return;
        }
    }
}

int main(){
    cout<<"input:";
    int amount=0,len=0,wid=0;
    cin>>amount;
    
    for (int i=0;i<amount;i++)
    {
        cin>>len>>wid;
        mazeproblem maze;
        maze.InsertMaze(len,wid);
        maze.findpath(len,wid);
    }
}


//測試用
/*cout<<endl;
    for (int row = 0; row < len; row++)
    {
        for (int col = 0; col < wid; col++)
        {
            cout<<data[row][col]<<" ";
        }
        cout<<endl;
    }
    */