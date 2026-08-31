# GitHub 협업 연습용 팀 할 일 보드

Issue, Branch, Commit, Pull Request, Review, Merge와 Project Board를 연습하기 위한 작은 Python·JavaScript 프로젝트입니다.

## Branch 역할

- `main`: 최종 완성본
- `dev`: 작업 Branch 병합용
- 작업 Branch: 최신 `dev`에서 생성

## 실행 방법

터미널 1에서 Backend를 실행합니다.

```bash
python3 backend/app.py
```

터미널 2에서 Frontend를 실행합니다.

```bash
python3 -m http.server 5173 --directory frontend
```

브라우저에서 `http://localhost:5173`을 엽니다.

## 테스트

```bash
python3 -m unittest discover -s backend -p "test_*.py"
```

## 연습 순서

1. 본인에게 배정된 Issue를 확인합니다.
2. 최신 `dev`에서 Issue 번호가 포함된 Branch를 만듭니다.
3. 개발하고 테스트합니다.
4. Conventional Commits 형식으로 Commit합니다.
5. `dev`를 base로 PR을 만듭니다.
6. 다른 팀원의 Review를 받은 뒤 Merge합니다.
7. Project 상태를 Done으로 변경합니다.

자세한 규칙은 [CONTRIBUTING.md](CONTRIBUTING.md)를 확인합니다.

