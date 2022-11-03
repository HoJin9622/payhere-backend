# :money_with_wings: 페이헤이

소비내역을 기록/관리하는 서버

## :scroll: 목차

- [:money_with_wings: 페이헤이](#money_with_wings-페이헤이)
  - [:scroll: 목차](#scroll-목차)
  - [:notebook_with_decorative_cover: 프로젝트 요구사항](#notebook_with_decorative_cover-프로젝트-요구사항)
  - [:whale: Development(Docker)](#whale-developmentdocker)
  - [:mag_right: Development(Poetry)](#mag_right-developmentpoetry)
  - [:pencil2: Commit Message Convention](#pencil2-commit-message-convention)
  - [:closed_book: API Docs](#closed_book-api-docs)

## :notebook_with_decorative_cover: 프로젝트 요구사항

1. 고객은 이메일과 비밀번호 입력을 통해서 회원 가입을 할 수 있습니다.
2. 고객은 회원 가입이후, 로그인과 로그아웃을 할 수 있습니다.
3. 고객은 로그인 이후 가계부 관련 아래의 행동을 할 수 있습니다.
   - 가계부에 오늘 사용한 돈의 금액과 관련된 메모를 남길 수 있습니다.
   - 가계부에서 수정을 원하는 내역은 금액과 메모를 수정 할 수 있습니다.
   - 가계부에서 삭제를 원하는 내역은 삭제 할 수 있습니다.
   - 삭제한 내역은 언제든지 다시 복구 할 수 있어야 한다.
   - 가계부에서 이제까지 기록한 가계부 리스트를 볼 수 있습니다.
   - 가계부에서 상세한 세부 내역을 볼 수 있습니다.
4. 로그인하지 않은 고객은 가계부 내역에 대한 접근 제한 처리가 되어야 합니다.

## :whale: Development(Docker)

```bash
# Application Run
docker-compose up
```

## :mag_right: Development(Poetry)

```bash
# 가상환경 진입
poetry shell

# 관련 패키지 설치
poetry install

# Application Run
python manage.py runserver
```

## :pencil2: Commit Message Convention

- feat: 기능 추가, 삭제, 변경(or ✨ emoji) - 제품 코드 수정 발생
- fix: 버그 수정(or 🐛 emoji) - 제품 코드 수정 발생
- docs: 문서 추가, 삭제, 변경(or 📝 emoji) - 코드 수정 없음
- style: 코드 형식, 정렬, 주석 등의 변경, eg; 세미콜론 추가(or 💎 emoji) - 제품 코드 수정 발생, 하지만 동작에 영향을 주는 변경은 없음
- refactor: 코드 리펙토링, eg. renaming a variable(or ♻️ emoji) - 제품코드 수정 발생
- test: 테스트 코드 추가, 삭제, 변경 등(or 🧪 emoji) - 제품 코드 수정 없음. 테스트 코드에 관련된 모든 변경에 해당
- chore: 위에 해당하지 않는 모든 변경(or 🧹 emoji), eg. 빌드 스크립트 수정, 패키지 배포 설정 변경 - 코드 수정 없음

위 규칙에 맞게 커밋메시지를 작성한다.

## :closed_book: API Docs
