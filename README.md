# 👋 안녕하세요, 김동훈(DONGHOON KIM)입니다!
**Android 앱 개발자** · *"상상을 현실로 만드는 즐거움"*

<p align="left">
  <img src="https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white" />
  <img src="https://img.shields.io/badge/Kotlin-7F52FF?style=for-the-badge&logo=kotlin&logoColor=white" />
  <img src="https://img.shields.io/badge/Jetpack_Compose-4285F4?style=for-the-badge&logo=jetpackcompose&logoColor=white" />
  <img src="https://img.shields.io/badge/iOS-000000?style=for-the-badge&logo=ios&logoColor=white" />
  <img src="https://img.shields.io/badge/SwiftUI-FF3008?style=for-the-badge&logo=swift&logoColor=white" />
  <img src="https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black" />
</p>

> **"상상하던 아이디어가 화면 속에서 살아 움직일 때 가장 큰 에너지를 얻습니다."**  
> 단순한 코딩을 넘어 누군가에게 실제 도움이 되는 서비스를 직접 기획, 설계, 개발 및 출시하여 운영하는 라이프사이클 전체를 사랑하는 안드로이드 개발자입니다.

---

## 📬 Contact & Channels

- **📧 Email** | welcome2c@naver.com
- **💻 GitHub** | [github.com/welcome2c](https://github.com/welcome2c)
- **🎨 Brand** | **Tap Studio** (1인 기획/개발/운영 브랜드)
- **🛠 Main Tech** | `Android (Kotlin)` · `Jetpack Compose` · `Kotlin Multiplatform (KMP)` · `iOS (SwiftUI)` · `Firebase AI`

---

## ⚡ 한 줄 소개

- **다양한 도메인 경험**: 2017년부터 AI(STT·챗봇·트레이딩), 라이브 커머스, 금융/보험 등 트렌디하고 고도화된 안드로이드 앱 서비스를 개발해 왔습니다.
- **전문성과 실행력**: 현재 한화생명에서 **인증·보안 도메인 및 모바일 디자인 시스템** 개발을 담당하고 있으며, 퇴근 후에는 개인 브랜드 **'Tap Studio'**를 통해 생성형 AI 기술을 결합한 9종 이상의 앱을 기획부터 출시, 결제, 운영까지 독립적으로 완결했습니다.
- **혁신과 생산성 개선**: 레거시 **Java ➔ Kotlin**, **Web ➔ Native**, **Fragment ➔ Compose** 전환 프로젝트를 모두 경험했으며, 사내에 **Claude 기반 AI 자동 코드 리뷰 파이프라인**을 직접 구축하는 등 개발 생산성 및 인프라 개선에 깊은 관심을 가지고 실천하고 있습니다.

---

## 🛠 Tech Stack

### 🤖 Mobile Client
- **Languages** | `Kotlin`, `Java`, `Swift`, `JavaScript / Node.js`
- **Android Core** | `Jetpack Compose` · `Coroutines / Flow` · `Hilt (DI)` · `Jetpack Navigation` · `Room` · `DataStore` · `Paging3` · `WorkManager`
- **System & Media** | `CameraX` · `ML Kit (DocumentScanner)` · `Custom IME (InputMethodService)` · `Adaptive Layout (폴더블/태블릿 대응)` · `Foreground Service` · `ExoPlayer2`
- **Cross-platform / iOS** | `Kotlin Multiplatform (KMP)` · `Compose Multiplatform` · `SwiftUI` · `Combine` · `SwiftData` · `WidgetKit` · `ActivityKit`

### 🌐 Network & Security
- **Network** | `Retrofit` · `OkHttp` · `Ktor` · `kotlinx.serialization` · `소켓 통신` · `AWS AppSync (GraphQL)` · `AWS Kinesis` · `Wowza`
- **Security & Auth** | `간편인증 (PIN/생체인증)` · `공동인증서` · `통합인증` · `OnePass / 베스트핀 마이그레이션` · `보안키패드 (mTransKey)` · `Firebase App Check`

### ⚙ DevOps & Backend
- **Backend / Infra** | `Firebase (Firestore, Remote Config, Crashlytics)` · `Firebase AI Logic (Gemini)` · `Cloud Functions (Node.js)` · `GCP` · `AWS`
- **CI/CD** | `GitHub Actions` · `fastlane` · `GitLab CI` · `Detekt` · **Claude AI 코드 리뷰 파이프라인 직접 구축**

---

## 🏢 Work Experience

<details>
<summary><b>🏢 한화생명 (Hanwha Life) · Android 앱 개발 (2023.02 ~ 재직 중)</b></summary>
<br>

> **대고객 및 대FP(보험설계사) 서비스의 인증·보안 도메인과 디자인 시스템 개발을 총괄하고, 사내 개발 생산성 개선을 위한 자동화 인프라를 구축했습니다.**

#### 1. 📱 영업지원시스템(보험설계사 FP) 앱 — Jetpack Compose 100% 신규 구축
- **Compose 단일 스택 아키텍처**: 신규 영업지원 시스템을 Jetpack Compose 기반으로 설계하고 구축.
- **인증 시스템**: FP 로그인 및 통합 인증수단 (**OnePass**) 등록/설정 화면 전담 설계 및 개발.
- **Adaptive Layout 디자인 시스템**: 폴더블폰 및 태블릿에 최적화된 반응형 모바일 디자인 시스템 컴포넌트 설계 및 적용.
  - 다국어 텍스트 라벨 생략(`ellipsis`) 시 `TextMeasurer`를 활용해 폰트 크기 및 실제 픽셀 너비를 동적으로 측정·반영하는 고성능 커스텀 Tab 개발.
- **멀티 모듈 구조화**: 디자인 시스템, 공통 Core 라이브러리, 보안 모듈을 완전히 분리하여 코드 재사용성을 극대화하고 빌드 속도 개선.
- **스마트 전자서명**: **CameraX + ML Kit DocumentScanner**를 연동하여 안정적인 전자청약(eApp) 문서 스캐닝 및 촬영 기능 구현.
- **🛠 트러블슈팅 & 성능 개선**
  - **Android 15 대응**: 16KB 페이지 사이즈 적용 단말의 호환성을 위해 사전 분석 및 빌드 최적화 완료.
  - **Foreground Service 안정화**: 문서 스캔 도중 OS에 의해 앱 프로세스가 강제 종료되는 현상을 방지하기 위해 Foreground Service 기반 보완 설계를 적용하여 작성 중인 전자청약 유실율 0% 달성.
  - **WebView 버전 가드 구축**: Remote Config를 통해 기기의 System WebView 최소 사양을 검증하고, 미달 단말 진입 시 자동 업데이트 모달을 제공해 웹뷰 기반 화면의 안정성 확보.
  - **공통 UI 코드 최적화**: 핀/생체인증 에러 처리 공통 컴포넌트화를 통해 반복 코드 **화면당 약 90줄 감축**, 매직 스트링 제거 및 리팩터링 주도.

#### 2. 🛡 한화생명 메인 앱 — 인증·보안 도메인 고도화 및 운영
- **핵심 모듈 전담**: 로그인, 간편인증(PIN/지문), 공동인증서 등록 및 **통합인증** 고도화 (누적 **500+ 커밋** 수행).
- **네이티브 전환**: 기존 하이브리드 웹 뷰 기반의 회원가입/인증 플로우를 **Full-Native(Kotlin)**로 성공적으로 마이그레이션하여 사용자 이탈율 감소 및 진입 속도 대폭 개선.
- **인증 마이그레이션**: 원패스/베스트핀 무중단 통합인증 데이터 마이그레이션을 안전하게 설계. 미등록 단말, 연속 인증 실패, 만료 인증서 갱신 누락 등 복잡한 예외 처리 플로우 설계.
- **보안 모듈 연동**: mTransKey 보안 가상 키패드 등 금융 필수 보안 솔루션을 Compose UI 생태계와 매끄럽게 결합.
- **🛠 트러블슈팅 & 성능 개선**
  - **폴더블 레이아웃 최적화**: 갤럭시 폴드 등 접힘/펼침 상태 변화 시 핀 번호 입력 레이아웃이 잘리는 이슈를 반응형 ConstraintLayout 구조로 재설계하여 완벽히 해결.
  - **무중단 동기화 예외 방어**: 구버전 원패스 미등록 유저가 병행 운영 구간에 진입 시 발생하는 크래시 원인을 식별하고 대체 플로우를 구축해 크래시 발생율 최소화.

#### 3. 📊 소크라택스 (SocraTax) 앱 개발
- 종합소득세 신고 시뮬레이션 및 맞춤형 절세 가이드 기능 개발.
- 신규 기능 구현 및 레거시 버그 핫픽스로 전반적인 앱 신뢰도 제어.

#### 4. 🤖 [차별화 포인트] 사내 AI 자동 코드 리뷰 CI/CD 파이프라인 구축
- **배경**: 팀 내 신속하고 정확한 피드백 루프를 만들고자 스스로 기획하여 구축.
- **파이프라인 설계**: GitHub Actions 및 GitLab CI에 **Claude API**를 연동하여 자동 코드 리뷰어 도입.
- **비용 최적화**: 커밋 메시지에 기재된 트리거 태그(`[review]` = 경량/빠른 리뷰, `[review-deep]` = 상위 Claude 모델을 통한 깊이 있는 로직 검증)에 따라 API 호출 모델과 프롬프트를 분기하여 운영 비용 대폭 절감.
- **협업 연동**: 코드 리뷰 결과를 **GitHub Commit Discussions API**를 통해 소스코드의 실제 변경 라인에 인라인 코멘트로 자동 게시하고, **Slack Block Kit**으로 실시간 요약 알림 발송.
- **안정성 강화**: diff parsing 시 발생하던 헤더 유실 버그 및 인라인 코멘트 행 번호 환각(Hallucination) 현상을 정규식 파싱 가드로 정밀하게 제어하여 사내 실무 환경에 완벽 적용.
</details>

<details>
<summary><b>🏢 모비두 (Mobidoo / Sauce Live) · Android 앱 개발 (2021.04 ~ 2023.02)</b></summary>
<br>

> **자사 실시간 라이브 커머스 서비스인 '소스라이브' 및 판매자용 '송출용 앱(Sauce Studio)'의 핵심 기능을 전담 개발했습니다.**

- **소스라이브 2.1v 고도화** *(2022.04 ~ 2022.12)*
  - 메인/검색 화면의 대대적인 UI/UX 개선 및 코드 구조 리팩터링.
  - 실시간 채팅 성능 개선을 위해 **웹소켓 통신 레이어 고도화** 및 구매인증 기능 개발.
- **소스라이브 2.0v 메이저 리뉴얼** *(2021.09 ~ 2021.11)*
  - **ExoPlayer2** 커스터마이징을 통한 고성능 미디어 플레이어 전면 개발.
  - SNS 연동(카카오, 네이버, 페이스북) 간편 로그인 통합 구축.
  - **AWS Kinesis**를 연동한 미디어 시청 지표 및 실시간 데이터 수집 수립.
  - **AWS AppSync** 인프라를 사용해 서버리스 환경에서의 실시간 방송 메타데이터 구독(Subscription) 및 채팅 시스템 구축.
- **소스 스튜디오 (Sauce Studio 송출 앱)** *(2021.04 ~ 2021.06)*
  - 판매자를 위한 **Wowza RTMP 엔진 연동 모바일 라이브 송출 기능** 개발.
  - AWS AppSync GraphQL 기반 실시간 채팅 차단, 방송 상태 제어 기능 구현.
</details>

<details>
<summary><b>🏢 한다소프트 (Handasoft) · Android 앱 개발 (2018.12 ~ 2020.10)</b></summary>
<br>

> **누적 100만 이상의 영어 학습 플랫폼 및 운세 서비스를 Modern Stack으로 전환하고 유지보수를 담당했습니다.**

- **운세의 정석 메이저 리뉴얼** *(2019.10 ~ 2020.08)*
  - 기존 **Java 기반 프로젝트를 Kotlin으로 100% 마이그레이션**하여 코드베이스 현대화.
  - 1:1 실시간 상담을 위한 **mVoIP 통화 솔루션 및 소켓 통신 모듈** 개발.
  - In-App Purchase 및 다양한 PG 결제 모듈(선불/후불) 연동.
- **영어신 플랫폼 리뉴얼** *(2018.12 ~ 2019.04)*
  - 사용자 커스텀 단어장 기능 구축 및 외부 사전 **크롤링 기반 자동 단어 뜻 입력** 엔진 구현.
  - Local DB(SQLite/Room) 대용량 트랜잭션 튜닝을 통해 단어장 저장/로드 **성능 300% 이상 개선**.
</details>

<details>
<summary><b>🏢 쏘피몬 & 투비시스 · Android 앱 개발 (2017.12 ~ 2018.10)</b></summary>
<br>

- **코인 트레이딩 앱 개발 (쏘피몬)**
  - **MPAndroidChart**를 커스텀하여 실시간 자산 시세 및 변동 추이 가속화 구현.
  - AI 서버 연동 매수/매도 시그널 분석 및 자동 매매 기능 구현.
- **삼성영어 / LG U+ / YBM 시연용 앱 개발 (투비시스)**
  - 기기 마이크 기반 **STT (Speech-to-Text) 기술 연동 영어 발음 평가** 및 오디오 분석 시각화 피드백 시스템 구축.
  - **AI 챗봇 엔진 서버**와 연동한 시나리오 기반 대화형 주니어 영어 학습 인터페이스 구현.
</details>

---

## 🚀 1인 브랜드 사이드 프로젝트 — Tap Studio
> **기획부터 UI/UX 디자인, 클라이언트 개발, 서버리스 인프라 구축, 수익화(구독/인앱), 배포 및 스토어 운영까지 모든 과정을 혼자 완결해 오고 있습니다.**  
> **공통 스택**: `Kotlin` · `Compose` · `Hilt` · `Flow` · `Firebase` · `AdMob` · `Play Billing` — *AI 기능이 있는 앱은 **Firebase AI Logic (Gemini)** 사용*  
> [➔ Google Play에서 탭 스튜디오 앱 전체보기](https://play.google.com/store/search?q=%ED%85%9D+%EC%8A%A4%ED%8A%AC%EB%94%94%EC%98%A4&c=apps)

| 프로젝트 명 | 플랫폼 | 한 줄 설명 | 활용 기술 및 차별점 | 스토어 링크 |
|:---|:---|:---|:---|:---|
| **🌦 Weather Cast** | AOS / iOS | 날씨 기반 옷차림 추천 | 기상청 공공데이터 API · Kakao API · Gemini 코디 · 홈 위젯 | [Google Play](https://play.google.com/store/search?q=Weather+Cast+%ED%85%9D+%EC%8A%A4%ED%8A%AC%EB%94%94%EC%98%A4&c=apps) / [App Store](https://apps.apple.com/kr/search?term=Weather+Cast+%ED%85%9D+%EC%8A%A4%ED%8A%AC%EB%94%94%EC%98%A4) |
| **🔮 Astro AI** | AOS | AI 기반 운세·타로 상담 | 타로 로컬 데이터(JSON) · Gemini 해석 · Room 히스토리 | [Google Play](https://play.google.com/store/apps/details?id=com.tapstudio.astroai) |
| **👟 Pixel Walker RPG** | AOS / iOS | 만보기 기반 RPG 게임 | 걸음 센서(StepCounter) · Firestore · WidgetKit/ActivityKit · fastlane | [Google Play](https://play.google.com/store/search?q=Pixel+Walker+RPG+%ED%85%9D+%EC%8A%A4%ED%8A%AC%EB%94%94%EC%98%A4&c=apps) / [App Store](https://apps.apple.com/kr/search?term=Pixel+Walker+RPG+%ED%85%9D+%EC%8A%A4%ED%8A%AC%EB%94%94%EC%98%A4) |
| **🐱 Meow Bow** | AOS | 귀여운 강아지·고양이 사진 구경 | TheCatAPI / TheDogAPI 외부 REST(Retrofit) | [Google Play](https://play.google.com/store/apps/details?id=com.tapstudio.meowbow) |
| **📸 Voda** | AOS | 스크린샷 기반 미디어 검색 | 스크린샷 미디어 인덱싱 · **Gemini 이미지 분석** · RTDN 구독 | [Google Play](https://play.google.com/store/apps/details?id=com.tapstudio.voda) |
| **⌨ Gemiboard** | AOS | AI 기반 스마트 키보드 | Custom InputMethodService · **천지인 한글 오토마타 직접 구현** · Gemini 글 교정 | [Google Play](https://play.google.com/store/apps/details?id=com.tapstudio.gemiboard) |
| **🍹 Cocktail Wiki** | AOS | 칵테일 레시피·정보 위키 | 로컬 데이터(JSON) · Gemini 챗 · Room 즐겨찾기 | [Google Play](https://play.google.com/store/apps/details?id=com.tapstudio.cocktail) |
| **🎯 Pick It** | AOS | 결정 장애를 위한 메뉴 선택 룰렛 | 로컬 룰렛 · Room 히스토리 | [Google Play](https://play.google.com/store/search?q=PickIt+%ED%85%9D+%EC%8A%A4%ED%8A%AC%EB%94%94%EC%98%A4&c=apps) |
| **🧠 Pop Quiz Daily** | AOS / iOS | 매일 풀어보는 상식 퀴즈 | **Kotlin Multiplatform(공유)** · Room KMP · GitLive Firebase | [Google Play](https://play.google.com/store/apps/details?id=com.tapstudio.popquizdaily) / [App Store](https://apps.apple.com/kr/search?term=Pop+Quiz+Daily+%ED%85%9D+%EC%8A%A4%ED%8A%AC%EB%94%94%EC%98%A4) |
| **📦 CrossPromoSDK** | SDK | 자체 앱 교차 홍보 SDK | JitPack 배포 · AOS/iOS/Firestore 공통 | [GitHub](https://github.com/welcome2c) |

<details>
<summary><b>🛠️ 개인 프로젝트 핵심 트러블슈팅 (운영 중 실제 해결)</b></summary>
<br>

- **🔐 Gemini API 키 APK 노출 제거** — 클라이언트 내장 키가 APK 디컴파일로 유출될 수 있는 구조를 **Firebase AI Logic + App Check로 전면 이관**해 키를 클라이언트에서 완전 제거. 다수 앱 일괄 적용
- **R8 릴리즈 빌드 차단 해결** — Firebase AI SDK가 유발하는 `okhttp3.internal.Util` missing class 경고로 막힌 릴리즈 빌드를 R8 규칙으로 해결
- **GCP API 키 Android 앱 제한(403) 대응** — 앱 서명 제한 정책 충돌을 SDK 제거➔REST 전환➔Firebase AI Logic 이관으로 정리
- **한글 IME 오토마타 직접 구현 (Gemiboard)** — 천지인 복합 모음(ㅘ/ㅙ/ㅝ/ㅞ) 미입력 버그, IME 스위처 누락 등 키보드 코어 로직 직접 디버깅
- **방치형 RPG 라이브 이슈 (Pixel Walker)** — EXP `Int32` 오버플로우, 백그라운드 일일 퀘스트 집계 누락, 익명 로그인 실패 시 크래시 등 신속 핫픽스
- **구독 결제 안정화 (Voda)** — 익명 사용자 RTDN 지원 및 구독 상태 동기화 race condition 해결
</details>

---

## 🏆 강점 요약 (Core Strengths)

- **🥇 압도적인 실행력과 책임감** - 기획부터 디자인, 풀스택 개발, 출시 및 스토어 운영까지 1인 사이드 프로젝트 9종을 마켓에 론칭하고 매끄럽게 유지관리해 온 강인한 오너십을 갖고 있습니다.
- **🏗 모던 아키텍처 및 레거시 리팩터링 스페셜리스트** - Java ➔ Kotlin 마이그레이션, Fragment ➔ Jetpack Compose 단일 액티비티 설계, 멀티 모듈 및 UDF 단방향 데이터 흐름을 구축해 본 탄탄한 아키텍처 역량을 보유하고 있습니다.
- **📱 플랫폼 경계를 넘나드는 확장성** - 안드로이드 네이티브를 주력으로 하면서도 Kotlin Multiplatform(KMP), iOS SwiftUI, Firebase/Cloud Functions 백엔드까지 넓은 풀스택 커버리지를 활용해 모바일 생태계를 종합적으로 다룹니다.
- **💡 자발적인 개발 생산성 극대화** - 사내에 Claude 연동 AI 자동 코드 리뷰 파이프라인을 직접 구축하고 트러블슈팅하여 동료들과 팀 전체의 코드 퀄리티와 비즈니스 효율을 극대화하는 것에 깊은 만족과 열정을 느낍니다.

---
<sub>© 2026 김동훈 (welcome2c · Tap Studio) · 본 이력서의 무단 전재·복제를 금합니다.</sub>
