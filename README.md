# :money_with_wings: 페이헤이

소비내역을 기록/관리하는 서버

## :scroll: 목차

- [:money_with_wings: 페이헤이](#money_with_wings-페이헤이)
  - [:scroll: 목차](#scroll-목차)
  - [:notebook_with_decorative_cover: 프로젝트 요구사항](#notebook_with_decorative_cover-프로젝트-요구사항)
  - [:whale: Development(Docker)](#whale-developmentdocker)
  - [:mag_right: Development(Poetry)](#mag_right-developmentpoetry)
  - [:pencil2: Commit Message Convention](#pencil2-commit-message-convention)
  - [:chart_with_upwards_trend: Git Flow / Branch Information](#chart_with_upwards_trend-git-flow--branch-information)
  - [:closed_book: API Docs](#closed_book-api-docs)
    - [회원가입](#회원가입)
    - [로그인](#로그인)
    - [토큰 재발급](#토큰-재발급)
    - [가계부 내역 확인](#가계부-내역-확인)
    - [가계부 내역 기록](#가계부-내역-기록)
    - [가계부 내역의 세부 내용](#가계부-내역의-세부-내용)
    - [가계부 내역 수정](#가계부-내역-수정)
    - [가계부 내역 삭제](#가계부-내역-삭제)
    - [가계부 내역 복구](#가계부-내역-복구)

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

## :chart_with_upwards_trend: Git Flow / Branch Information

```
- main: 제품으로 출시 될 수 있는 브랜치입니다.
- develop: 다음 출시 버전을 개발합니다.
- feature: 다가오는 배포(release)를 위한 새 기능(feature)을 개발합니다.
- release: 새로운 제품 출시 준비를 지원합니다.
- hotfix: 핫픽스는 현재 출시된 제품에 문제가 생겨서 즉각 대응해야하는 상황에서 필요합니다.
```

## :closed_book: API Docs

### 회원가입

- Method: POST
- URL: api/v1/users/signup/
- Description: 회원가입을 진행합니다.
- Request Example
  ```json
  {
    "email": "test1@gmail.com", // required
    "password": "qwer1234!", // required
    "username": "test1" // required
  }
  ```
- Response Example
  ```json
  {
    "ok": true
  }
  ```

### 로그인

- Method: POST
- URL: api/v1/users/login/
- Description: 유저 이메일을 검증 후 JWT를 반환합니다.
- Request Example
  ```json
  {
    "email": "test1@gmail.com", // required
    "password": "qwer1234!" // required
  }
  ```
- Response Example
  ```json
  {
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2NzYyMjMwMywiaWF0IjoxNjY3NTM1OTAzLCJqdGkiOiIyZWFlMjkxNjM4NGM0ZTM0ODZhMWNkZWRkZGE2YjM2YSIsInVzZXJfaWQiOjF9.v0BdSHzqN_uV14qX8cxLreOv1JLg1SM4i420lkl57xg",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY3NTM2MjAzLCJpYXQiOjE2Njc1MzU5MDMsImp0aSI6Ijk4NzJjMDg4YzFmMjRlNGY5NjJmZGZmZWM1NjVhN2MwIiwidXNlcl9pZCI6MX0.e-hiZIYBfL5ibTq_IUYbm-1molzLhoLsTxfA_E3Do14"
  }
  ```

### 토큰 재발급

- Method: POST
- URL: api/v1/users/token/refresh/
- Description: refresh token을 확인 후 access token을 반환합니다.
- Request Example
  ```json
  {
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2NzYyMjMwMywiaWF0IjoxNjY3NTM1OTAzLCJqdGkiOiIyZWFlMjkxNjM4NGM0ZTM0ODZhMWNkZWRkZGE2YjM2YSIsInVzZXJfaWQiOjF9.v0BdSHzqN_uV14qX8cxLreOv1JLg1SM4i420lkl57xg" // required
  }
  ```
- Response Example
  ```json
  {
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY3NTM2MjkxLCJpYXQiOjE2Njc1MzU5MDMsImp0aSI6ImU1ZWI4NjcyODRkMzRiZjVhNGZkYjBjYTI2NDJkODU5IiwidXNlcl9pZCI6MX0.9mq-i5hnPJhxTxpjracgnOFHwcVxTUa1LCY9yvGJ3uA"
  }
  ```

### 가계부 내역 확인

- Method: GET
- URL: api/v1/households/
- Description: 자신의 가계부 내역을 확인합니다.
- Header: `Authorization: Bearer {access token}`
- Response Example
  ```json
  [
    {
      "id": 2,
      "amount": 35000,
      "memo": "고깃집",
      "created_at": "2022-11-03T19:47:45.434960+09:00"
    },
    {
      "id": 3,
      "amount": 20000,
      "memo": "",
      "created_at": "2022-11-03T19:48:12.478745+09:00"
    },
    {
      "id": 4,
      "amount": 5000,
      "memo": "편의점",
      "created_at": "2022-11-03T19:48:44.092476+09:00"
    }
  ]
  ```

### 가계부 내역 기록

- Method: POST
- URL: api/v1/households/
- Description: 자신의 가계부 내역을 기록합니다.
- Header: `Authorization: Bearer {access token}`
- Request Example
  ```json
  {
    "amount": 9000, // required
    "memo": "미용실" // optional
  }
  ```
- Response Example
  ```json
  {
    "ok": true
  }
  ```

### 가계부 내역의 세부 내용

- Method: GET
- URL: api/v1/households/{pk}/
- Description: 자신의 가계부 내역의 세부 내역을 확인합니다.
- Header: `Authorization: Bearer {access token}`
- Response Example
  ```json
  {
    "id": 2,
    "amount": 35000,
    "memo": "",
    "created_at": "2022-11-03T19:47:45.434960+09:00"
  }
  ```

### 가계부 내역 수정

- Method: PATCH
- URL: api/v1/households/{pk}/
- Description: 자신의 가계부 내역을 수정합니다.
- Header: `Authorization: Bearer {access token}`
- Request Example
  ```json
  {
    "amount": 9000, // optional
    "memo": "미용실" // optional
  }
  ```
- Response Example
  ```json
  {
    "ok": true
  }
  ```

### 가계부 내역 삭제

- Method: POST
- URL: api/v1/households/{pk}/inactive/
- Description: 자신의 가계부 내역을 삭제합니다.
- Header: `Authorization: Bearer {access token}`
- Response Example
  ```json
  {
    "ok": true
  }
  ```

### 가계부 내역 복구

- Method: POST
- URL: api/v1/households/{pk}/active/
- Description: 자신의 가계부 내역을 복구합니다.
- Header: `Authorization: Bearer {access token}`
- Response Example
  ```json
  {
    "ok": true
  }
  ```
