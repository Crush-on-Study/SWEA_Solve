T = int(input())  # 테케 입력받고
for test_case in range(1,T+1): # 루핑하고
    arr = [] # 괄호 담을 리스트 선언
    s = input()  # 문자열 입력
    for idx in s:  # 문자열 루핑하면서
        if idx=='(':  # 왼쪽 괄호들 ( , { 들은 append해주고
            arr.append('(') 
        elif idx=='{': 
            arr.append('{')
        elif idx=='}': # 오른쪽 괄호들 만나면 append하지말고 pop시켜서 왼쪽 괄호들 제거
            arr.pop()
        elif idx==')':
            arr.pop()
             
     
    if len(arr)==0: # 리스트가 비어있다면 모두 맞는 짝을 찾은거니까
        print(f"#{test_case} 1") # 1을 출력
    elif len(arr)!=0: # 그렇지않다면
        print(f"#{test_case} 0") # 0을 출력
