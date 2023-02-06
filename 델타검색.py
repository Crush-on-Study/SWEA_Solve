T = int(input())  # 테케 개수 입력
for test_Case in range(T):
    graph = [list(map(int,input().split())) for _ in range(5)] # 그래프 정보 입력
    arr = []  # 토탈값 담아놓을 리스트
    dx = [1,0,-1,0]  # 4방향 탐색
    dy = [0,1,0,-1]

    def search(y,x): # 서칭함수 선언
        tot = 0
        for i in range(4): # 4방향 탐색 루핑
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<5 and 0<=nx<5: # 범위를 벗어나지않는 내에서
                tot+=abs(graph[y][x]-graph[ny][nx]) # 상하좌우 차이값의 절댓값  토탈 구하기

        return tot  # 그 값 반환

    for col in range(5):  # 좌표 서칭해가면서
        for row in range(5):
            a = search(col,row) # search에 넣기
            arr.append(a) # 반환받은 값 arr에 넣기

    print(f"#{test_Case+1} {sum(arr)}")  # 결과값 
