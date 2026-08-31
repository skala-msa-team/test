# Git·GitHub 연습 규칙

## Branch

- 형식: `type/이슈번호-영어-작업명`
- 예시: `feat/12-task-form`
- 작업 Branch는 최신 `dev`에서 만듭니다.

## Commit

Conventional Commits를 사용합니다. type은 영어, 제목과 본문은 한국어로 작성합니다.

```text
feat: 할 일 입력 폼 추가

빈 입력 검증과 등록 버튼을 구현했습니다.
```

사용할 type은 `feat`, `fix`, `refactor`, `docs`, `test`, `style`, `chore`입니다.

## Pull Request

- base: `dev`
- 제목: `[영역] type: 한국어 제목`
- 본문: 한국어
- 관련 Issue: `Closes #이슈번호`
- Review와 테스트를 통과한 뒤 Squash and merge

`main`에는 일반 작업 Branch를 직접 Merge하지 않습니다. 최종본을 반영할 때만 `dev → main` PR을 만듭니다.

