# Profile assets

[← 프로필로 돌아가기](../README.md)

프로필 배너와 프로젝트 커버는 이 저장소에서 관리하는 SVG입니다. 외부 폰트, 스크립트, 원격 이미지 요청 없이 표시되며 라이트·다크 테마를 각각 제공합니다. 배너에는 좁은 화면용 버전도 있습니다.

## 다시 생성하기

```sh
python3 scripts/generate_assets.py
```

Python 표준 라이브러리만 사용합니다. 앱 아이콘은 SVG 안에 포함되며 원본은 `assets/apps/`에 보관합니다.

## 앱 이미지 출처

기술 배지의 로고는 [Simple Icons](https://github.com/simple-icons/simple-icons)에서 가져와 로컬 SVG로 구성했습니다. 배지는 외부 이미지 서비스에 의존하지 않고 저장소에서 직접 제공합니다.

기존 앱 아이콘은 공개 스토어 자료를 사용했습니다. 2026-10-30에 확인한 이미지이며, 앱 업데이트에 따라 실제 화면이 달라질 수 있습니다.

## 프로필의 스토어 스크린샷

2026-11-03에 9개 앱의 Google Play·App Store 갤러리 12개를 확인하고, 등록된 스크린샷 70장을 모두 가져왔습니다.
시작 화면을 포함해 스토어에 표시된 순서를 유지하며, 장수 제한이나 선별은 하지 않습니다.
앱 설명 아래의 접힌 드롭다운에서 스토어별로 구분해 볼 수 있으며 이미지 내용과 비율은 변경하지 않았습니다.
출처 URL·원래 순번·파일 크기·SHA-256은 [이미지 출처 목록](../assets/apps/store-screenshots.json)에 기록했습니다.

- **오늘뭐입지 · WeatherCast** — [Google Play](https://play.google.com/store/apps/details?id=kr.dev.hoony.weathercast) 7장 · [App Store](https://apps.apple.com/kr/app/id6758431684) 5장
- **Pixel Walker RPG** — [Google Play](https://play.google.com/store/apps/details?id=kr.dev.hoony.pixelwalkerrpg) 5장 · [App Store](https://apps.apple.com/kr/app/id6760536041) 4장
- **Pop Quiz Daily · 팝 퀴즈 데일리** — [Google Play](https://play.google.com/store/apps/details?id=kr.dev.hoony.popquizdaily) 6장 · [App Store](https://apps.apple.com/kr/app/id6759132499) 6장
- **GemiBoard · 제미보드** — [Google Play](https://play.google.com/store/apps/details?id=kr.dev.hoony.gemiboard) 8장
- **Astro AI** — [Google Play](https://play.google.com/store/apps/details?id=kr.dev.hoony.astroai) 8장
- **Voda** — [Google Play](https://play.google.com/store/apps/details?id=kr.dev.hoony.voda) 4장
- **멍냥이는 힐링이야 · Meow Bow** — [Google Play](https://play.google.com/store/apps/details?id=kr.dev.hoony.meowbow) 6장
- **칵테일 위키 · Cocktail Wiki** — [Google Play](https://play.google.com/store/apps/details?id=kr.dev.hoony.cocktailwiki) 5장
- **PickIt · 픽잇** — [Google Play](https://play.google.com/store/apps/details?id=kr.dev.hoony.pickit) 6장

Astro AI는 스토어 직접 조회가 404를 반환해 공개 스토어 페이지 기록의 전체 이미지 목록 8장을 사용했습니다.
나머지 갤러리는 Google Play 공개 페이지 또는 App Store 공개 조회 API의 전체 목록을 사용했습니다.
