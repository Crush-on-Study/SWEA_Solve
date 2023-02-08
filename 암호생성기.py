from collections import deque
for test_case in range(1,11): # 테케 10개니까
    a = int(input()) # 테케 번호 입력하고
    q = deque(list(map(int,input().split()))) # 데큐에 숫자들 집어넣고
    idx = 1 # 얘는 이제 1~5를 돌려줄 변수
    while q: # 큐가 비어있지 않다면
        if (idx+5)%5==0: # idx==5를 겨냥한 것
            check = q.popleft()-5 # 큐 가장 앞에 있는 애를 꺼내서 5을 차감하고
            q.append(check) # 맨 뒤로 보내
        else: # idx가 1~4라면
            check = q.popleft()-((idx+5)%5) # 큐 가장 앞에 있는 애를 꺼내서 루핑
            q.append(check) # 맨 뒤로 보내
        idx+=1
        if q[-1] <= 0: # 근데 그게 0이면 이제 멈춰!
            q[-1] = 0
            print(f"#{test_case} {' '.join(map(str,q))}")
            break
 
# 핵심은 (idx+5)%5
