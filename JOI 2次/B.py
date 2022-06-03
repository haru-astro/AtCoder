h,w = map(int,input().split())
C = [list(input()) for i in range(h)]

queue = []
visited = [] 
visited = [[0 for i in range(w)] for i in range(h)]
ans = 0

queue.append([0,0])
visited[0][0] = 1

dy_dx = [[1,0],[0,1],[-1,0],[0,-1]]
count=0
while len(queue) > 0:
    now = queue.pop(0)
    for k in range(4):
        y = now[0]+dy_dx[k][0]
        x = now[1]+dy_dx[k][1]
        if 0 <= y < h and 0 <= x < w:
            if C[y][x] != now and visited[y][x] == 0:
                visited[y][x] ==1
                count+=1
                queue.append([y,x])
            if y==h-1 and x==w-1:
                ans=count
                exit()
        else:
            ans="-1"
            exit()
 
print(ans)