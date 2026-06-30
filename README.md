# Coding Test Study

Python으로 코딩테스트를 준비하는 저장소입니다.

## 폴더 구조

```
📂 programmers/              # 프로그래머스 문제 풀이
📂 notes/                    # 개념 정리
📂 Python for Data Analysis/ # 책의 챕터별 실습 코드
  └─ 📂 practice/            # 실습 코드 (.py)
```

## 파일 네이밍

```
MMDD_문제이름.py
예) 0619_compare.py

Python for Data Analysis 실습은 챕터 이름으로 저장합니다.
예) `practice/ch02_python_basics.py`
```

## 커밋 컨벤션

공부용 저장소에서 많이 쓰이는 `type: 설명` 형식을 사용합니다.

| 타입 | 사용 시점 | 예시 |
|------|-----------|------|
| `Solve` | 문제 풀이 완료 | `Solve: 두 수 비교하기` |
| `Docs` | 개념 정리 | `Docs: 유클리드 호제법 개념 정리` |
| `Refactor` | 기존 풀이 개선 | `Refactor: 삼항 연산자 개선` |
| `Fix` | 오답 수정 | `Fix: 엣지케이스 오류 수정` |
| `Rename` | 파일명 변경 | `Rename: 날짜_이름 형식으로 통일` |
| `Config` | 설정 파일 | `Config: .gitignore 추가` |

## 작업 흐름

```bash
git pull                         # 다른 기기 작업 내용 받기
# 문제 풀기
git add programmers/MMDD_이름.py
git commit -m "Solve: 문제이름"
git push
```
