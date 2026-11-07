# 김동훈 · Android Developer 👋

2017년부터 금융·라이브 커머스·교육 분야의 **Android 앱**을 개발해 왔습니다.\
현재 **한화생명에서 Android 앱을 개발·운영**하며, **공통 UI와 개발 환경을 개선**하고 있습니다.\
개인 브랜드 **Tap Studio**에서는 Android·iOS 앱을 기획부터 출시·운영까지 직접 만듭니다.

<p>
  <img src="assets/badges/android.svg" height="22" alt="Android">
  <img src="assets/badges/kotlin.svg" height="22" alt="Kotlin">
  <img src="assets/badges/compose.svg" height="22" alt="Jetpack Compose">
  <img src="assets/badges/kmp.svg" height="22" alt="Kotlin Multiplatform">
  <img src="assets/badges/swiftui.svg" height="22" alt="SwiftUI">
  <img src="assets/badges/firebase.svg" height="22" alt="Firebase">
</p>

📬 **Contact** · [welcome2c@naver.com](mailto:welcome2c@naver.com)

<!-- activity-stats:start -->
**GitHub 활동** · 전체 기간 작성 커밋 **236** · 생성 PR **76** · 소유 저장소 **32**\
<sub>2026.11.07 집계 · 공개·비공개 합산 · 회사 GitLab 제외</sub>
<!-- activity-stats:end -->

## 실무 경력

### 한화생명

**Android 개발 · 2023.02 ~ 현재**\
대고객 서비스 · 보험설계사 영업지원 앱 · 소크라택스

- **공통 UI:** Compose 디자인 시스템, 다국어·태블릿 컴포넌트와 Catalog를 개발했습니다.
- **앱 기능:** 로그인·인증 SDK 연동과 세금 신고 시뮬레이션을 개발했습니다.
- **운영·개발 환경:** 문서 촬영과 기기 호환성을 개선하고, GitLab CI 기반 AI 코드 리뷰를 구축했습니다.

### 모비두

**Android 개발 · 2021.04 ~ 2023.02**\
소스라이브 · 소스 스튜디오

- 메인·검색 UI, ExoPlayer 영상 재생, SNS 간편 로그인, 실시간 채팅과 구매인증을 개발했습니다.
- Wowza RTMP 기반 모바일 라이브 송출, AppSync GraphQL 기반 방송 제어와 AWS Kinesis 시청 지표 수집을 구현했습니다.

### 한다소프트

**Android 개발 · 2018.12 ~ 2020.10**\
운세의 정석 · 영어신

- Java 앱을 Kotlin으로 전환하고 mVoIP 상담·소켓 통신·인앱 및 PG 결제를 연동했습니다.
- 단어장·사전 데이터를 연동하고 SQLite·Room의 저장·조회 처리를 개선했습니다.

### 쏘피몬 · 투비시스

**Android 개발 · 2017.12 ~ 2018.10**\
트레이딩 · 영어 학습 서비스

- 실시간 시세 차트와 서버 분석 결과를 연결한 트레이딩 기능을 개발했습니다.
- STT 발음 평가, 오디오 분석 시각화와 챗봇 기반 학습 UI를 구현했습니다.

<details open>
<summary><b>한화생명 · 기술 사례와 개선 내용</b></summary>

- **Compose 디자인 시스템** — 공통 컴포넌트와 Catalog를 개발하고, 다국어·태블릿에 대응했습니다.\
  탭 라벨을 글자 수 대신 `TextMeasurer`로 측정한 실제 폭에 맞춰 처리했습니다.
- **공통 UI 안정성 개선** — `ImmutableList` 도입과 안정성 어노테이션 정리, `remember`·리스트 key·스타일 캐싱으로 컴포넌트의 상태와 반복 계산을 개선했습니다.
- **인증 화면·SDK 연동** — Android 앱의 로그인·PIN·생체인증 화면과 등록·변경·실패 시 사용자 흐름을 개발했습니다.\
  OnePass SDK의 중복 요청, 거래 상태 일관성, 인증수단 전환 시 콜백 전달을 개선했습니다.
- **메인 앱·네이티브 전환** — 공동인증서 등록과 보안키패드를 연동하고, 웹 기반 회원가입·인증 흐름을 Kotlin 네이티브로 전환했습니다.\
  인증수단 마이그레이션의 미등록 단말·연속 실패·갱신 예외와 폴더블 입력 레이아웃을 개선했습니다.
- **화면 생명주기 문제 해결** — navigation result와 콜백의 saved state 직렬화 크래시를 수정하고, 결과 전달을 메모리 상태로 분리했습니다.
- **기기·운영 환경 대응** — 문서 촬영·DocumentScanner 경로에 Foreground Service를 연결하고, 16 KB 페이지 크기 호환성과 Remote Config 기반 WebView 최소 버전 확인을 적용했습니다.
- **개발 도구 구축** — GitLab CI에 Claude 기반 AI 코드 리뷰를 최초 구축했습니다.\
  초기 모델 분기, diff 헤더 보존, 코멘트 대상 파일·행 검증과 Slack 알림을 개발했습니다.
- **소크라택스** — 종합소득세 신고 시뮬레이션·절세 가이드 개발과 유지보수를 진행했습니다.

</details>

## 출시한 앱 · Tap Studio

기획·UI/UX·클라이언트·Firebase 백엔드·결제와 광고·스토어 운영까지 직접 진행합니다.

### 오늘뭐입지 · WeatherCast

**Android / iOS** · 날씨와 외출 시간에 맞는 옷차림 추천 앱입니다.\
현재·시간별·주간 날씨와 체감 설정을 반영한 옷차림, AI 코디와 홈 화면 위젯을 제공합니다.

- **개발·운영:** 캐시 우선 날씨 표시, 대기질 재시도와 측정 시각 기반 이전 값 표시를 개선했습니다.\
  위젯 이미지 복구를 Android의 `WorkManager`, iOS의 백그라운드 전송으로 보완했습니다.
- **기술:** Kotlin · Compose · SwiftUI · WidgetKit · Firebase AI Logic
- **출시:** [Google Play](https://play.google.com/store/apps/details?id=kr.dev.hoony.weathercast) · [App Store](https://apps.apple.com/kr/app/id6758431684)

<details>
<summary><b>실제 앱 화면 · Google Play / App Store</b></summary>

<p><b>Google Play</b></p>

<p>
<img src="assets/apps/weathercast-google-play-1.png" width="200" loading="lazy" alt="오늘뭐입지 · WeatherCast Google Play 공개 스크린샷 1"> <img src="assets/apps/weathercast-google-play-2.png" width="200" loading="lazy" alt="오늘뭐입지 · WeatherCast Google Play 공개 스크린샷 2"> <img src="assets/apps/weathercast-google-play-3.png" width="200" loading="lazy" alt="오늘뭐입지 · WeatherCast Google Play 공개 스크린샷 3"> <img src="assets/apps/weathercast-google-play-4.png" width="200" loading="lazy" alt="오늘뭐입지 · WeatherCast Google Play 공개 스크린샷 4"> <img src="assets/apps/weathercast-google-play-5.png" width="200" loading="lazy" alt="오늘뭐입지 · WeatherCast Google Play 공개 스크린샷 5"> <img src="assets/apps/weathercast-google-play-6.png" width="200" loading="lazy" alt="오늘뭐입지 · WeatherCast Google Play 공개 스크린샷 6"> <img src="assets/apps/weathercast-google-play-7.png" width="200" loading="lazy" alt="오늘뭐입지 · WeatherCast Google Play 공개 스크린샷 7">
</p>

<p><b>App Store</b></p>

<p>
<img src="assets/apps/weathercast-store-1.jpg" width="200" loading="lazy" alt="오늘뭐입지 · WeatherCast App Store 공개 스크린샷 1"> <img src="assets/apps/weathercast-store-2.jpg" width="200" loading="lazy" alt="오늘뭐입지 · WeatherCast App Store 공개 스크린샷 2"> <img src="assets/apps/weathercast-store-3.jpg" width="200" loading="lazy" alt="오늘뭐입지 · WeatherCast App Store 공개 스크린샷 3"> <img src="assets/apps/weathercast-store-4.jpg" width="200" loading="lazy" alt="오늘뭐입지 · WeatherCast App Store 공개 스크린샷 4"> <img src="assets/apps/weathercast-store-5.jpg" width="200" loading="lazy" alt="오늘뭐입지 · WeatherCast App Store 공개 스크린샷 5">
</p>

</details>

### Pixel Walker RPG

**Android / iOS** · 실제 걸음 수를 탐험과 캐릭터 성장으로 연결한 만보기 RPG입니다.\
전투·직업 성장·장비 수집과 강화, 보스 도전과 일일 퀘스트를 제공합니다.

- **개발·운영:** 걸음 수를 게임 진행과 퀘스트에 연결했습니다.\
  iOS의 백그라운드 걸음 수 반영 누락과 퀘스트 중복 집계를 수정했습니다.
- **기술:** Kotlin · Compose · SwiftUI · 걸음 센서 · Firebase · 위젯
- **출시:** [Google Play](https://play.google.com/store/apps/details?id=kr.dev.hoony.pixelwalkerrpg) · [App Store](https://apps.apple.com/kr/app/id6760536041)

<details>
<summary><b>실제 앱 화면 · Google Play / App Store</b></summary>

<p><b>Google Play</b></p>

<p>
<img src="assets/apps/pixel-walker-google-play-1.png" width="200" loading="lazy" alt="Pixel Walker RPG Google Play 공개 스크린샷 1"> <img src="assets/apps/pixel-walker-google-play-2.png" width="200" loading="lazy" alt="Pixel Walker RPG Google Play 공개 스크린샷 2"> <img src="assets/apps/pixel-walker-google-play-3.png" width="200" loading="lazy" alt="Pixel Walker RPG Google Play 공개 스크린샷 3"> <img src="assets/apps/pixel-walker-google-play-4.png" width="200" loading="lazy" alt="Pixel Walker RPG Google Play 공개 스크린샷 4"> <img src="assets/apps/pixel-walker-google-play-5.png" width="200" loading="lazy" alt="Pixel Walker RPG Google Play 공개 스크린샷 5">
</p>

<p><b>App Store</b></p>

<p>
<img src="assets/apps/pixel-walker-store-1.jpg" width="200" loading="lazy" alt="Pixel Walker RPG App Store 공개 스크린샷 1"> <img src="assets/apps/pixel-walker-store-2.jpg" width="200" loading="lazy" alt="Pixel Walker RPG App Store 공개 스크린샷 2"> <img src="assets/apps/pixel-walker-store-3.jpg" width="200" loading="lazy" alt="Pixel Walker RPG App Store 공개 스크린샷 3"> <img src="assets/apps/pixel-walker-store-4.jpg" width="200" loading="lazy" alt="Pixel Walker RPG App Store 공개 스크린샷 4">
</p>

</details>

### GemiBoard · 제미보드

**Android** · 입력 중인 문장을 교정·변환·번역하는 AI 키보드입니다.\
두벌식·천지인 입력과 테마, 격식체·일상체 등 상황에 맞는 문장 변환을 제공합니다.

- **개발·운영:** `InputMethodService`와 한글 오토마타를 구현했습니다.\
  천지인 복합 모음·연속 탭·타임아웃 처리를 입력 시퀀스 테스트로 검증할 수 있게 구성했습니다.
- **기술:** Kotlin · Compose · InputMethodService · 한글 오토마타 · Gemini
- **출시:** [Google Play](https://play.google.com/store/apps/details?id=kr.dev.hoony.gemiboard)

<details>
<summary><b>실제 앱 화면 · Google Play</b></summary>

<p>
<img src="assets/apps/gemiboard-store-1.jpg" width="200" loading="lazy" alt="GemiBoard · 제미보드 Google Play 공개 스크린샷 1"> <img src="assets/apps/gemiboard-store-2.jpg" width="200" loading="lazy" alt="GemiBoard · 제미보드 Google Play 공개 스크린샷 2"> <img src="assets/apps/gemiboard-store-3.jpg" width="200" loading="lazy" alt="GemiBoard · 제미보드 Google Play 공개 스크린샷 3"> <img src="assets/apps/gemiboard-store-4.jpg" width="200" loading="lazy" alt="GemiBoard · 제미보드 Google Play 공개 스크린샷 4"> <img src="assets/apps/gemiboard-store-5.jpg" width="200" loading="lazy" alt="GemiBoard · 제미보드 Google Play 공개 스크린샷 5"> <img src="assets/apps/gemiboard-store-6.jpg" width="200" loading="lazy" alt="GemiBoard · 제미보드 Google Play 공개 스크린샷 6"> <img src="assets/apps/gemiboard-store-7.jpg" width="200" loading="lazy" alt="GemiBoard · 제미보드 Google Play 공개 스크린샷 7"> <img src="assets/apps/gemiboard-store-8.jpg" width="200" loading="lazy" alt="GemiBoard · 제미보드 Google Play 공개 스크린샷 8">
</p>

</details>

### Pop Quiz Daily · 팝 퀴즈 데일리

**Android / iOS** · 매일 여러 분야의 상식을 풀고 해설로 복습하는 퀴즈 앱입니다.\
오늘의 퀴즈·오답 노트·스트릭·배지와 활동 캘린더, 생존 모드와 정답률 통계를 제공합니다.

- **개발·운영:** `commonMain`에서 화면·상태·데이터 계층을 공유하고 플랫폼별 기능을 분리했습니다.\
  Room 기반 기록과 GitLive Firebase, Koin을 공통 코드에 구성했습니다.
- **기술:** Kotlin Multiplatform · Compose Multiplatform · Room · Koin · Firebase
- **출시:** [Google Play](https://play.google.com/store/apps/details?id=kr.dev.hoony.popquizdaily) · [App Store](https://apps.apple.com/kr/app/id6759132499)

<details>
<summary><b>실제 앱 화면 · Google Play / App Store</b></summary>

<p><b>Google Play</b></p>

<p>
<img src="assets/apps/pop-quiz-daily-google-play-1.png" width="200" loading="lazy" alt="Pop Quiz Daily · 팝 퀴즈 데일리 Google Play 공개 스크린샷 1"> <img src="assets/apps/pop-quiz-daily-google-play-2.png" width="200" loading="lazy" alt="Pop Quiz Daily · 팝 퀴즈 데일리 Google Play 공개 스크린샷 2"> <img src="assets/apps/pop-quiz-daily-google-play-3.png" width="200" loading="lazy" alt="Pop Quiz Daily · 팝 퀴즈 데일리 Google Play 공개 스크린샷 3"> <img src="assets/apps/pop-quiz-daily-google-play-4.png" width="200" loading="lazy" alt="Pop Quiz Daily · 팝 퀴즈 데일리 Google Play 공개 스크린샷 4"> <img src="assets/apps/pop-quiz-daily-google-play-5.png" width="200" loading="lazy" alt="Pop Quiz Daily · 팝 퀴즈 데일리 Google Play 공개 스크린샷 5"> <img src="assets/apps/pop-quiz-daily-google-play-6.png" width="200" loading="lazy" alt="Pop Quiz Daily · 팝 퀴즈 데일리 Google Play 공개 스크린샷 6">
</p>

<p><b>App Store</b></p>

<p>
<img src="assets/apps/pop-quiz-daily-store-1.jpg" width="200" loading="lazy" alt="Pop Quiz Daily · 팝 퀴즈 데일리 App Store 공개 스크린샷 1"> <img src="assets/apps/pop-quiz-daily-store-2.jpg" width="200" loading="lazy" alt="Pop Quiz Daily · 팝 퀴즈 데일리 App Store 공개 스크린샷 2"> <img src="assets/apps/pop-quiz-daily-store-3.jpg" width="200" loading="lazy" alt="Pop Quiz Daily · 팝 퀴즈 데일리 App Store 공개 스크린샷 3"> <img src="assets/apps/pop-quiz-daily-store-4.jpg" width="200" loading="lazy" alt="Pop Quiz Daily · 팝 퀴즈 데일리 App Store 공개 스크린샷 4"> <img src="assets/apps/pop-quiz-daily-store-5.jpg" width="200" loading="lazy" alt="Pop Quiz Daily · 팝 퀴즈 데일리 App Store 공개 스크린샷 5"> <img src="assets/apps/pop-quiz-daily-store-6.jpg" width="200" loading="lazy" alt="Pop Quiz Daily · 팝 퀴즈 데일리 App Store 공개 스크린샷 6">
</p>

</details>

### Astro AI

**Android** · 사용자의 고민과 상황에 맞춰 AI가 타로를 해석하는 운세·상담 앱입니다.\
오늘의 운세, 연애·금전·이직 등 주제별 3카드 리딩, 78장 타로 도감과 상담 기록을 제공합니다.

- **개발:** Gemini 기반 상담과 로컬 타로 데이터를 연결하고, 상담 기록과 Google Drive 백업 기능을 구성했습니다.
- **출시:** [Google Play](https://play.google.com/store/apps/details?id=kr.dev.hoony.astroai)

<details>
<summary><b>실제 앱 화면 · Google Play</b></summary>

<p>
<img src="assets/apps/astro-ai-store-1.jpg" width="200" loading="lazy" alt="Astro AI Google Play 공개 스크린샷 1"> <img src="assets/apps/astro-ai-store-2.jpg" width="200" loading="lazy" alt="Astro AI Google Play 공개 스크린샷 2"> <img src="assets/apps/astro-ai-store-3.jpg" width="200" loading="lazy" alt="Astro AI Google Play 공개 스크린샷 3"> <img src="assets/apps/astro-ai-store-4.jpg" width="200" loading="lazy" alt="Astro AI Google Play 공개 스크린샷 4"> <img src="assets/apps/astro-ai-store-5.jpg" width="200" loading="lazy" alt="Astro AI Google Play 공개 스크린샷 5"> <img src="assets/apps/astro-ai-store-6.jpg" width="200" loading="lazy" alt="Astro AI Google Play 공개 스크린샷 6"> <img src="assets/apps/astro-ai-store-7.jpg" width="200" loading="lazy" alt="Astro AI Google Play 공개 스크린샷 7"> <img src="assets/apps/astro-ai-store-8.jpg" width="200" loading="lazy" alt="Astro AI Google Play 공개 스크린샷 8">
</p>

</details>

### Voda

**Android** · 스크린샷 속 상품·장소·텍스트를 AI로 분석하고 검색으로 이어주는 앱입니다.\
다른 앱 위에 분석 결과를 표시하고, 감지 대상 앱 선택·분석 기록·Google Drive 백업과 복원을 제공합니다.

- **개발:** 스크린샷 감지와 오버레이, AI 이미지 분석과 구독을 연동했습니다.\
  분석 결과를 Room에 저장하고 이미지 축소·압축을 적용해 기록을 관리합니다.
- **기술:** Kotlin · Compose · Hilt · Room · Gemini
- **출시:** [Google Play](https://play.google.com/store/apps/details?id=kr.dev.hoony.voda)

<details>
<summary><b>실제 앱 화면 · Google Play</b></summary>

<p>
<img src="assets/apps/voda-store-1.png" width="200" loading="lazy" alt="Voda Google Play 공개 스크린샷 1"> <img src="assets/apps/voda-store-2.png" width="200" loading="lazy" alt="Voda Google Play 공개 스크린샷 2"> <img src="assets/apps/voda-store-3.png" width="200" loading="lazy" alt="Voda Google Play 공개 스크린샷 3"> <img src="assets/apps/voda-store-4.png" width="200" loading="lazy" alt="Voda Google Play 공개 스크린샷 4">
</p>

</details>

### 멍냥이는 힐링이야 · Meow Bow

**Android** · 강아지·고양이 사진을 감상하고 사진과 품종을 수집하는 앱입니다.\
사진 저장·공유, 품종 도감과 수집률, 카메라·앨범 사진의 AI 품종 분석을 제공합니다.

- **개발:** 외부 REST API 사진 탐색과 AI 이미지 분석을 연동했습니다.\
  Room 기반 보관함과 Google Drive 백업·복원을 구성했습니다.
- **기술:** Kotlin · Compose · Hilt · Room · Retrofit · Firebase AI
- **출시:** [Google Play](https://play.google.com/store/apps/details?id=kr.dev.hoony.meowbow)

<details>
<summary><b>실제 앱 화면 · Google Play</b></summary>

<p>
<img src="assets/apps/meow-bow-store-1.png" width="200" loading="lazy" alt="멍냥이는 힐링이야 · Meow Bow Google Play 공개 스크린샷 1"> <img src="assets/apps/meow-bow-store-2.png" width="200" loading="lazy" alt="멍냥이는 힐링이야 · Meow Bow Google Play 공개 스크린샷 2"> <img src="assets/apps/meow-bow-store-3.png" width="200" loading="lazy" alt="멍냥이는 힐링이야 · Meow Bow Google Play 공개 스크린샷 3"> <img src="assets/apps/meow-bow-store-4.png" width="200" loading="lazy" alt="멍냥이는 힐링이야 · Meow Bow Google Play 공개 스크린샷 4"> <img src="assets/apps/meow-bow-store-5.png" width="200" loading="lazy" alt="멍냥이는 힐링이야 · Meow Bow Google Play 공개 스크린샷 5"> <img src="assets/apps/meow-bow-store-6.png" width="200" loading="lazy" alt="멍냥이는 힐링이야 · Meow Bow Google Play 공개 스크린샷 6">
</p>

</details>

### 칵테일 위키 · Cocktail Wiki

**Android** · 재료와 취향에 맞는 칵테일·무알콜 음료 레시피를 찾는 앱입니다.\
보유 재료·잔·카테고리 검색, AI 바텐더와의 대화, 즐겨찾기와 Google Drive 백업·복원을 제공합니다.

- **개발:** 레시피 API와 AI 바텐더를 연동하고, Room 기반 즐겨찾기와 백업 기능을 구성했습니다.
- **기술:** Kotlin · Compose · Hilt · Room · Retrofit · Firebase AI
- **출시:** [Google Play](https://play.google.com/store/apps/details?id=kr.dev.hoony.cocktailwiki)

<details>
<summary><b>실제 앱 화면 · Google Play</b></summary>

<p>
<img src="assets/apps/cocktail-wiki-store-1.png" width="200" loading="lazy" alt="칵테일 위키 · Cocktail Wiki Google Play 공개 스크린샷 1"> <img src="assets/apps/cocktail-wiki-store-2.png" width="200" loading="lazy" alt="칵테일 위키 · Cocktail Wiki Google Play 공개 스크린샷 2"> <img src="assets/apps/cocktail-wiki-store-3.png" width="200" loading="lazy" alt="칵테일 위키 · Cocktail Wiki Google Play 공개 스크린샷 3"> <img src="assets/apps/cocktail-wiki-store-4.png" width="200" loading="lazy" alt="칵테일 위키 · Cocktail Wiki Google Play 공개 스크린샷 4"> <img src="assets/apps/cocktail-wiki-store-5.png" width="200" loading="lazy" alt="칵테일 위키 · Cocktail Wiki Google Play 공개 스크린샷 5">
</p>

</details>

### PickIt · 픽잇

**Android** · 메뉴 후보와 추첨 비중을 직접 정해 돌리는 메뉴 결정 룰렛 앱입니다.\
여러 룰렛과 테마, 재료·최근 메뉴 제외, 식사 기록·캘린더·통계, 위젯과 바로가기를 제공합니다.

- **개발:** 추첨 결과와 확정·실제 식사 기록을 구분하고, 메뉴·재료 필터와 Google Drive 백업·복원을 구현했습니다.
- **기술:** Kotlin · Compose · Hilt · Room · DataStore
- **출시:** [Google Play](https://play.google.com/store/apps/details?id=kr.dev.hoony.pickit)

<details>
<summary><b>실제 앱 화면 · Google Play</b></summary>

<p>
<img src="assets/apps/pickit-store-1.png" width="200" loading="lazy" alt="PickIt · 픽잇 Google Play 공개 스크린샷 1"> <img src="assets/apps/pickit-store-2.png" width="200" loading="lazy" alt="PickIt · 픽잇 Google Play 공개 스크린샷 2"> <img src="assets/apps/pickit-store-3.png" width="200" loading="lazy" alt="PickIt · 픽잇 Google Play 공개 스크린샷 3"> <img src="assets/apps/pickit-store-4.png" width="200" loading="lazy" alt="PickIt · 픽잇 Google Play 공개 스크린샷 4"> <img src="assets/apps/pickit-store-5.png" width="200" loading="lazy" alt="PickIt · 픽잇 Google Play 공개 스크린샷 5"> <img src="assets/apps/pickit-store-6.png" width="200" loading="lazy" alt="PickIt · 픽잇 Google Play 공개 스크린샷 6">
</p>

</details>

## 기술 스택

- **Android:** Kotlin · Java · Jetpack Compose · Coroutines / Flow · Hilt · Room · DataStore · WorkManager
- **iOS·멀티플랫폼:** SwiftUI · Kotlin Multiplatform · Compose Multiplatform · Koin · WidgetKit · ActivityKit
- **백엔드·AI:** Firebase · Firestore · Remote Config · Cloud Functions · Firebase AI Logic · App Check
- **개발·배포:** GitLab CI · GitHub Actions · fastlane · Detekt · AI 코드 리뷰

---

**김동훈 · DevHoony · Tap Studio** · [welcome2c@naver.com](mailto:welcome2c@naver.com)
