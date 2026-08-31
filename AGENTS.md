# AGENTS.md

## 목적

이 저장소는 초보 개발자의 GitHub 협업 연습용 팀 할 일 보드입니다.

## 수정 범위

- Frontend: `frontend/`
- Backend: `backend/`
- 협업 문서: `README.md`, `CONTRIBUTING.md`, `.github/`

## 실행과 테스트

- Backend 실행: `python3 backend/app.py`
- Frontend 실행: `python3 -m http.server 5173 --directory frontend`
- 테스트: `python3 -m unittest discover -s backend -p "test_*.py"`

## 작업 규칙

- 작업은 Issue 하나, Branch 하나, PR 하나로 진행합니다.
- 작업 Branch는 최신 `dev`에서 만듭니다.
- Commit은 반드시 `type(scope): 한국어 제목` 형식으로 작성합니다.
- Frontend scope는 `frontend`, Backend scope는 `backend`를 사용합니다.
- Frontend와 Backend는 Task, Branch, Commit, PR을 분리합니다.
- 한 PR에서 `frontend/`와 `backend/`를 함께 수정하지 않습니다.
- 두 영역의 연동은 `integration` scope의 별도 Task와 PR로 진행합니다.
- API 경로와 JSON 필드를 변경하면 Frontend와 Backend를 함께 확인합니다.
- 비밀정보와 `.env` 파일을 Commit하지 않습니다.
- 변경 후 관련 테스트를 실행합니다.
