# Git·GitHub 연습 규칙

## Issue

- 계층: 전체 Tracking Issue → Feature Issue → Task Issue
- Feature: 사용자가 확인할 수 있는 기능 단위
- Task: 한 사람이 한 Branch와 한 PR로 끝낼 수 있는 작업 단위
- Type: `Feature`, `Task`, `Bug` 중 하나를 선택합니다.
- Label: 작업 영역만 선택합니다. 예: `frontend`, `backend`, `docs`, `qa`
- 담당자, Milestone, 상위 Issue를 지정한 뒤 작업합니다.

## Branch

- 형식: `type/이슈번호-영역-영어-작업명`
- Frontend 예시: `feat/12-frontend-task-form`
- Backend 예시: `feat/13-backend-task-api`
- 연동 예시: `fix/14-integration-task-flow`
- 작업 Branch는 최신 `dev`에서 만듭니다.
- Frontend와 Backend 작업은 서로 다른 Task와 Branch로 진행합니다.

## Commit

Conventional Commits를 사용합니다. type과 scope는 영어, 제목과 본문은 한국어로 작성합니다. scope는 생략할 수 없습니다.

```text
feat(frontend): 할 일 입력 폼 추가

빈 입력 검증과 등록 버튼을 구현했습니다.
```

사용할 type은 `feat`, `fix`, `refactor`, `docs`, `test`, `style`, `chore`입니다.

사용할 scope는 다음과 같습니다.

- `frontend`: `frontend/` 변경
- `backend`: `backend/` 변경
- `database`: Database와 Migration 변경
- `ai`: AI Prompt, Mock AI, AI 연동 변경
- `docs`: 문서만 변경
- `design`: 디자인 시스템과 디자인 산출물 변경
- `qa`: 테스트와 QA 변경
- `integration`: Frontend·Backend 연동 변경
- `common`: 공통 설정과 저장소 전체 변경

Frontend와 Backend 변경은 각각 별도 Commit으로 작성합니다. 한 PR에 두 영역을 함께 넣지 않으며, 연동이 필요하면 별도 Integration Task와 PR을 만듭니다.

## Pull Request

- base: `dev`
- 제목: `[영역] type: 한국어 제목`
- Frontend 제목 예시: `[FE] feat: 할 일 입력 화면 추가`
- Backend 제목 예시: `[BE] feat: 할 일 등록 API 추가`
- 본문: 한국어
- 관련 Issue: `Closes #이슈번호`
- Review와 테스트를 통과한 뒤 Squash and merge

`main`에는 일반 작업 Branch를 직접 Merge하지 않습니다. 최종본을 반영할 때만 `dev → main` PR을 만듭니다.

## Project Board

- `Todo`: 시작 전
- `In Progress`: Branch를 만든 뒤
- `In Review`: PR을 만든 뒤
- `Done`: Merge와 Issue 종료를 확인한 뒤

## 이름 규칙

- Python 파일·함수·변수: `snake_case`
- Python class: `PascalCase`
- JavaScript 파일: `kebab-case`
- JavaScript 함수·변수: `camelCase`
- 상수: `UPPER_SNAKE_CASE`
- HTML·CSS class: `kebab-case`
- 디렉터리: 소문자 단어

## 공통 편집기 설정

- 저장소의 `.editorconfig`와 `.vscode/` 설정을 사용합니다.
- 추천 확장 프로그램 설치 알림이 나오면 팀 공통 확장만 설치합니다.
