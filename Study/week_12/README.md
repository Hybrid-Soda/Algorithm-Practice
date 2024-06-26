## 백준 2252 - 줄 세우기
- **접근 방식**: 위상 정렬 알고리즘을 사용하여 문제를 해결. 순서가 정해져 있는 작업을 차례로 처리할 때 유용.
- **시간을 줄일 수 있는 요소**: DFS를 사용하여 방문하지 않은 노드를 우선적으로 탐색, 스택을 사용하여 순서를 기록하여 효율적인 정렬 가능.
- **오류가 발생하기 쉬운 부분**: 사이클이 존재할 경우를 처리하지 않음. 실제로는 사이클 체크 로직이 필요.
- **코드의 핵심 부분**: DFS 함수 내에서의 노드 방문과 스택에 노드 추가 로직.

## 백준 5567 - 결혼식
- **접근 방식**: BFS를 사용하여 친구의 친구까지의 거리를 계산.
- **시간을 줄일 수 있는 요소**: 각 노드(사람)에 대해 방문 체크를 하여 중복 탐색을 방지.
- **오류가 발생하기 쉬운 부분**: 배열 인덱스 오류, 친구 수가 0인 경우 처리.
- **코드의 핵심 부분**: BFS 로직과 거리 측정을 위한 dist 배열 관리.

## 백준 11729 - 하노이 탑 이동 순서
- **접근 방식**: 재귀 함수를 사용하여 하노이 탑 문제 해결.
- **시간을 줄일 수 있는 요소**: 재귀의 기저 조건 설정으로 불필요한 호출 제거.
- **오류가 발생하기 쉬운 부분**: 재귀 깊이 초과 가능성.
- **코드의 핵심 부분**: 재귀 호출 구조와 각 단계의 원반 이동 로직.

## 백준 14427 - 수열과 쿼리 15
- **접근 방식**: 우선순위 큐를 사용하여 수열의 각 원소와 인덱스를 관리, 쿼리 처리 시 신속하게 최소값을 갱신.
- **시간을 줄일 수 있는 요소**: 힙(Heap)을 사용하여 최소값을 빠르게 찾아내고 갱신하는 연산 최적화.
- **오류가 발생하기 쉬운 부분**: 쿼리 처리 시 힙의 정합성 유지, 인덱스 오류 주의.
- **코드의 핵심 부분**: 힙 구조를 이용한 최소값 추출 및 갱신 로직.

## 백준 15903 - 카드 합체 놀이
- **접근 방식**: 최소 힙을 사용하여 가장 작은 두 카드를 선택하고 합쳐나가는 방식으로 문제 해결.
- **시간을 줄일 수 있는 요소**: 힙을 사용하여 각 단계에서 최소값을 빠르게 찾음.
- **오류가 발생하기 쉬운 부분**: 힙 연산 중 배열 인덱스 관리.
- **코드의 핵심 부분**: 힙에서 원소를 추출하고 새로운 값을 추가하는 과정.

## 백준 17626 - Four Squares
- **접근 방식**: 동적 프로그래밍을 사용하여 각 수를 표현할 수 있는 최소 제곱수의 합을 찾음.
- **시간을 줄일 수 있는 요소**: 미리 계산된 결과를 배열에 저장하여 재계산 방지.
- **오류가 발생하기 쉬운 부분**: 동적 프로그래밍 배열의 초기값 설정 오류.
- **코드의 핵심 부분**: 동적 프로그래밍 배열을 이용한 최소 제곱수 개수 계산 로직.

## 백준 1197 - 최소 스패닝 트리
- **접근 방식**: 크루스칼 알고리즘을 사용하여 그래프의 최소 스패닝 트리를 찾음.
- **시간을 줄일 수 있는 요소**: 유니온 파인드 자료구조를 이용하여 효율적으로 사이클 생성 여부 판단.
- **오류가 발생하기 쉬운 부분**: 유니온 파인드 구현 시 부모 노드 관리 오류.
- **코드의 핵심 부분**: 간선을 가중치에 따라 정렬하고 유니온 파인드를 통해 최소 스패닝 트리 구성.

## 백준 1799 - 비숍
- **접근 방식**: 백트래킹을 사용하여 비숍을 배치할 수 있는 최대 개수를 탐색.
- **시간을 줄일 수 있는 요소**: 백트래킹 중 가지치기를 통해 불필요한 경로 제거.
- **오류가 발생하기 쉬운 부분**: 대각선 방향의 체크 로직 오류.
- **코드의 핵심 부분**: 대각선 충돌을 체크하는 배열과 백트래킹 로직.

## 백준 1987 - 알파벳
- **접근 방식**: DFS를 사용하여 각 칸을 방문하면서 지나온 칸의 문자를 기록, 최대 이동 거리 계산.
- **시간을 줄일 수 있는 요소**: 방문한 알파벳을 마킹하여 중복 방문 방지.
- **오류가 발생하기 쉬운 부분**: 배열 경계 검사 누락, DFS 재귀 깊이 제어.
- **코드의 핵심 부분**: DFS를 사용한 탐색 및 방문한 알파벳의 체크 로직.

## 백준 1991 - 트리 순회
- **접근 방식**: 재귀 함수를 사용하여 트리의 전위, 중위, 후위 순회를 구현.
- **시간을 줄일 수 있는 요소**: 재귀 호출의 효율적 관리.
- **오류가 발생하기 쉬운 부분**: 재귀 함수의 종료 조건 설정 오류.
- **코드의 핵심 부분**: 트리 구조를 딕셔너리로 구성하고 각 순회 방식에 맞는 재귀 함수 구현.