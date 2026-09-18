import os
import random

# 1. 5개 제휴 업체 데이터
shops = [
    {
        "id": "shop1",
        "name": "한국미인홈케어",
        "tag": "🔥 한국미인홈케어",
        "desc": "서울·경기·인천 전지역 신속 방문! 정성 가득한 테라피 & 릴렉싱 프로그램",
        "price": "100,000원부터~",
        "phone": "0507-1280-3303"
    },
    {
        "id": "shop2",
        "name": "오늘밤테라피",
        "tag": "✨ 오늘밤테라피",
        "desc": "품격 있는 힐링을 선사하는 최고급 오일 프라이빗 방문 테라피 서비스",
        "price": "60,000원부터~",
        "phone": "0507-1280-3223"
    },
    {
        "id": "shop3",
        "name": "주주테라피",
        "tag": "💎 주주테라피",
        "desc": "재방문율 1위! 칼도착 25분 보장, 철저한 위생 관리와 럭셔리 케어",
        "price": "60,000원부터~",
        "phone": "0507-1280-3193"
    },
    {
        "id": "shop4",
        "name": "퀸즈홈테라피",
        "tag": "🌟 퀸즈홈테라피",
        "desc": "전문 힐러들의 맞춤형 VIP 피로회복 특화 프로그램 진행 중",
        "price": "60,000원부터~",
        "phone": "0507-1280-3334"
    },
    {
        "id": "shop5",
        "name": "골든테라피",
        "tag": "👑 골든테라피",
        "desc": "선입금 없는 100% 후불제! 수도권 전지역 평균 25분 내 실시간 도착",
        "price": "110,000원부터~",
        "phone": "0507-1280-3360"
    }
]

# 2. 서울, 경기, 인천 주요 행정구역 데이터 (1,000여 개 페이지 확장 기반)
all_regions = [
    # --- 서울시 25개 구 ---
    {"sido": "seoul", "sido_name": "서울", "path": "jongrogu", "name": "종로구", "dongs": [{"name": "사직동", "path": "sajikdong"}, {"name": "삼청동", "path": "samcheongdong"}, {"name": "부암동", "path": "buamdong"}, {"name": "평창동", "path": "pyeongchangdong"}, {"name": "무악동", "path": "muakdong"}, {"name": "교남동", "path": "gyonamdong"}, {"name": "가회동", "path": "gahoedong"}, {"name": "종로동", "path": "jongrodong"}, {"name": "이화동", "path": "ihwadong"}, {"name": "창신동", "path": "changsindong"}, {"name": "숭인동", "path": "sungindong"}]},
    {"sido": "seoul", "sido_name": "서울", "path": "junggu", "name": "중구", "dongs": [{"name": "소공동", "path": "sogongdong"}, {"name": "회현동", "path": "hoehyeondong"}, {"name": "명동", "path": "myeongdong"}, {"name": "필동", "path": "pildong"}, {"name": "장충동", "path": "jangchungdong"}, {"name": "광희동", "path": "gwanghuidong"}, {"name": "을지로동", "path": "euljirodong"}, {"name": "신당동", "path": "sindangdong"}, {"name": "황학동", "path": "hwanghakdong"}, {"name": "중림동", "path": "jungrimdong"}]},
    {"sido": "seoul", "sido_name": "서울", "path": "yongsangu", "name": "용산구", "dongs": [{"name": "후암동", "path": "huamdong"}, {"name": "용산동", "path": "yongsandong"}, {"name": "남영동", "path": "namyeongdong"}, {"name": "원효로동", "path": "wonhyorodong"}, {"name": "효창동", "path": "hyochangdong"}, {"name": "용문동", "path": "yongmundong"}, {"name": "이촌동", "path": "ichondong"}, {"name": "이태원동", "path": "itaewondong"}, {"name": "한남동", "path": "hannamdong"}, {"name": "보광동", "path": "bogwangdong"}]},
    {"sido": "seoul", "sido_name": "서울", "path": "seongdonggu", "name": "성동구", "dongs": [{"name": "왕십리동", "path": "wangsipridong"}, {"name": "마장동", "path": "majangdong"}, {"name": "사근동", "path": "sageundong"}, {"name": "행당동", "path": "haengdangdong"}, {"name": "응봉동", "path": "eungbongdong"}, {"name": "금호동", "path": "geumhodong"}, {"name": "옥수동", "path": "oksudong"}, {"name": "성수동", "path": "seongsudong"}, {"name": "송정동", "path": "songjeongdong"}, {"name": "용답동", "path": "yongdapdong"}]},
    {"sido": "seoul", "sido_name": "서울", "path": "gwangjingu", "name": "광진구", "dongs": [{"name": "중곡동", "path": "junggokdong"}, {"name": "능동", "path": "neungdong"}, {"name": "구의동", "path": "guuidong"}, {"name": "광장동", "path": "gwangjangdong"}, {"name": "자양동", "path": "jayangdong"}, {"name": "화양동", "path": "hwayangdong"}, {"name": "군자동", "path": "gunjadong"}]},
    {"sido": "seoul", "sido_name": "서울", "path": "dongdaemungu", "name": "동대문구", "dongs": [{"name": "용신동", "path": "yongsindong"}, {"name": "제기동", "path": "jegidong"}, {"name": "전농동", "path": "jeonnongdong"}, {"name": "답십리동", "path": "dapsipridong"}, {"name": "장안동", "path": "jangandong"}, {"name": "청량리동", "path": "cheongryangridong"}, {"name": "회기동", "path": "hoegidong"}, {"name": "휘경동", "path": "hwigyeongdong"}, {"name": "이문동", "path": "imundong"}]},
    {"sido": "seoul", "sido_name": "서울", "path": "jungnanggu", "name": "중랑구", "dongs": [{"name": "면목동", "path": "myeonmokdong"}, {"name": "상봉동", "path": "sangbongdong"}, {"name": "중화동", "path": "junghwadong"}, {"name": "묵동", "path": "mukdong"}, {"name": "망우동", "path": "mangudong"}, {"name": "신내동", "path": "sinnaedong"}]},
    {"sido": "seoul", "sido_name": "서울", "path": "seongbukgu", "name": "성북구", "dongs": [{"name": "성북동", "path": "seongbukdong"}, {"name": "삼선동", "path": "samseondong"}, {"name": "동선동", "path": "dongseondong"}, {"name": "돈암동", "path": "donamdong"}, {"name": "안암동", "path": "anamdong"}, {"name": "보문동", "path": "bomundong"}, {"name": "정릉동", "path": "jeongreungdong"}, {"name": "길음동", "path": "gileumdong"}, {"name": "종암동", "path": "jongamdong"}, {"name": "월곡동", "path": "wolgokdong"}, {"name": "장위동", "path": "jangwidong"}, {"name": "석관동", "path": "seokgwandong"}]},
    {"sido": "seoul", "sido_name": "서울", "path": "gangbukgu", "name": "강북구", "dongs": [{"name": "삼양동", "path": "samyangdong"}, {"name": "미아동", "path": "miadong"}, {"name": "송중동", "path": "songjungdong"}, {"name": "송천동", "path": "songcheondong"}, {"name": "수유동", "path": "suyudong"}, {"name": "번동", "path": "beondong"}, {"name": "우이동", "path": "uidong"}, {"name": "인수동", "path": "insudong"}]},
    {"sido": "seoul", "sido_name": "서울", "path": "dobonggu", "name": "도봉구", "dongs": [{"name": "창동", "path": "changdong"}, {"name": "도봉동", "path": "dobongdong"}, {"name": "방학동", "path": "banghakdong"}, {"name": "쌍문동", "path": "ssangmundong"}]},
    {"sido": "seoul", "sido_name": "서울", "path": "nowongu", "name": "노원구", "dongs": [{"name": "월계동", "path": "wolgyedong"}, {"name": "공릉동", "path": "gongreungdong"}, {"name": "하계동", "path": "hagyedong"}, {"name": "중계동", "path": "junggyedong"}, {"name": "상계동", "path": "sanggyedong"}]},
    {"sido": "seoul", "sido_name": "서울", "path": "eunpyeonggu", "name": "은평구", "dongs": [{"name": "녹번동", "path": "nokbeondong"}, {"name": "불광동", "path": "bulgwangdong"}, {"name": "갈현동", "path": "galhyeondong"}, {"name": "구산동", "path": "gusandong"}, {"name": "대조동", "path": "daejodong"}, {"name": "응암동", "path": "eungamdong"}, {"name": "신사동", "path": "sinsadong"}, {"name": "증산동", "path": "jeungsandong"}, {"name": "수색동", "path": "susaekdong"}, {"name": "진관동", "path": "jingwandong"}]},
    {"sido": "seoul", "sido_name": "서울", "path": "seodaemungu", "name": "서대문구", "dongs": [{"name": "천연동", "path": "cheonyeondong"}, {"name": "홍제동", "path": "hongjedong"}, {"name": "홍은동", "path": "hongeundong"}, {"name": "남가좌동", "path": "namgajwadong"}, {"name": "북가좌동", "path": "bukgajwadong"}, {"name": "신촌동", "path": "sinchondong"}, {"name": "연희동", "path": "yeonhuidong"}]},
    {"sido": "seoul", "sido_name": "서울", "path": "mapogu", "name": "마포구", "dongs": [{"name": "공덕동", "path": "gongdeokdong"}, {"name": "아현동", "path": "ahyeondong"}, {"name": "도화동", "path": "dohwadong"}, {"name": "서교동", "path": "seogyodong"}, {"name": "합정동", "path": "hapjeongdong"}, {"name": "망원동", "path": "mangwondong"}, {"name": "연남동", "path": "yeonnamdong"}, {"name": "성산동", "path": "seongsandong"}, {"name": "상암동", "path": "sangamdong"}]},
    {"sido": "seoul", "sido_name": "서울", "path": "yangcheongu", "name": "양천구", "dongs": [{"name": "목동", "path": "mokdong"}, {"name": "신월동", "path": "sinwoldong"}, {"name": "신정동", "path": "sinjeongdong"}]},
    {"sido": "seoul", "sido_name": "서울", "path": "gangseogu", "name": "강서구", "dongs": [{"name": "염창동", "path": "yeomchangdong"}, {"name": "등촌동", "path": "deungchondong"}, {"name": "화곡동", "path": "hwagokdong"}, {"name": "가양동", "path": "gayangdong"}, {"name": "발산동", "path": "balsandong"}, {"name": "공항동", "path": "gonghangdong"}, {"name": "방화동", "path": "banghwadong"}]},
    {"sido": "seoul", "sido_name": "서울", "path": "gurogu", "name": "구로구", "dongs": [{"name": "신도림동", "path": "sindorimdong"}, {"name": "구로동", "path": "gurodong"}, {"name": "고척동", "path": "gocheokdong"}, {"name": "개봉동", "path": "gaebongdong"}, {"name": "오류동", "path": "oryudong"}, {"name": "항동", "path": "hangdong"}]},
    {"sido": "seoul", "sido_name": "서울", "path": "geumcheongu", "name": "금천구", "dongs": [{"name": "가산동", "path": "gasandong"}, {"name": "독산동", "path": "doksandong"}, {"name": "시흥동", "path": "siheungdong"}]},
    {"sido": "seoul", "sido_name": "서울", "path": "yeongdeungpogu", "name": "영등포구", "dongs": [{"name": "영등포동", "path": "yeongdeungpodong"}, {"name": "여의동", "path": "yeouidong"}, {"name": "당산동", "path": "dangsandong"}, {"name": "문래동", "path": "munraedong"}, {"name": "양평동", "path": "yangpyeongdong"}, {"name": "신길동", "path": "singildong"}, {"name": "대림동", "path": "daerimdong"}]},
    {"sido": "seoul", "sido_name": "서울", "path": "dongjakgu", "name": "동작구", "dongs": [{"name": "노량진동", "path": "noryangjindong"}, {"name": "상도동", "path": "sangdodong"}, {"name": "흑석동", "path": "heukseokdong"}, {"name": "사당동", "path": "sadangdong"}, {"name": "대방동", "path": "daebangdong"}, {"name": "신대방동", "path": "sindaebangdong"}]},
    {"sido": "seoul", "sido_name": "서울", "path": "gwanakgu", "name": "관악구", "dongs": [{"name": "보라매동", "path": "boramaedong"}, {"name": "은천동", "path": "euncheondong"}, {"name": "성현동", "path": "seonghyeondong"}, {"name": "낙성대동", "path": "nakseongdaedong"}, {"name": "신림동", "path": "sinlimdong"}, {"name": "서원동", "path": "seowondong"}, {"name": "신사동", "path": "sinsadong"}]},
    {"sido": "seoul", "sido_name": "서울", "path": "seochogu", "name": "서초구", "dongs": [{"name": "서초동", "path": "seochodong"}, {"name": "잠원동", "path": "jamwondong"}, {"name": "반포동", "path": "banpodong"}, {"name": "방배동", "path": "bangbaedong"}, {"name": "양재동", "path": "yangjaedong"}, {"name": "내곡동", "path": "naegokdong"}]},
    {"sido": "seoul", "sido_name": "서울", "path": "gangnamgu", "name": "강남구", "dongs": [{"name": "신사동", "path": "sinsadong"}, {"name": "논현동", "path": "nonhyeondong"}, {"name": "압구정동", "path": "apgujeongdong"}, {"name": "청담동", "path": "cheongdamdong"}, {"name": "삼성동", "path": "samseongdong"}, {"name": "역삼동", "path": "yeoksamdong"}, {"name": "대치동", "path": "daechidong"}, {"name": "도곡동", "path": "dogokdong"}, {"name": "개포동", "path": "gaepodong"}, {"name": "수서동", "path": "suseodong"}]},
    {"sido": "seoul", "sido_name": "서울", "path": "songpagu", "name": "송파구", "dongs": [{"name": "풍납동", "path": "pungnapdong"}, {"name": "잠실동", "path": "jamsildong"}, {"name": "삼전동", "path": "samjeondong"}, {"name": "석촌동", "path": "seokchondong"}, {"name": "송파동", "path": "songpadong"}, {"name": "방이동", "path": "bangidong"}, {"name": "문정동", "path": "munjeongdong"}, {"name": "가락동", "path": "ganakdong"}, {"name": "거여동", "path": "geoyeodong"}, {"name": "마천동", "path": "macheondong"}]},
    {"sido": "seoul", "sido_name": "서울", "path": "gangdonggu", "name": "강동구", "dongs": [{"name": "명일동", "path": "myeongildong"}, {"name": "고덕동", "path": "godeokdong"}, {"name": "암사동", "path": "amsadong"}, {"name": "천호동", "path": "cheonhodong"}, {"name": "성내동", "path": "seongnaedong"}, {"name": "둔촌동", "path": "dunchondong"}, {"name": "길동", "path": "gildong"}]},
    # --- 경기도 및 인천 주요 지역 ---
    {"sido": "gyeonggi", "sido_name": "경기", "path": "suwon_paldal", "name": "수원시 팔달구", "dongs": [{"name": "인계동", "path": "ingyedong"}, {"name": "우만동", "path": "umandong"}, {"name": "지동", "path": "jidong"}, {"name": "매산동", "path": "maesandong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "seongnam_bundang", "name": "성남시 분당구", "dongs": [{"name": "서현동", "path": "seohyeondong"}, {"name": "정자동", "path": "jeongjadong"}, {"name": "수내동", "path": "sunaedong"}, {"name": "야탑동", "path": "yatapdong"}]},
    {"sido": "incheon", "sido_name": "인천", "path": "yeonsugu", "name": "연수구", "dongs": [{"name": "송도동", "path": "songdodong"}, {"name": "연수동", "path": "yeonsudong"}, {"name": "동춘동", "path": "dongchundong"}]}
]

# 3. '출장'과 '마사지'가 절대 붙어있지 않도록 분산 배치된 순차 패턴 정의
title_patterns = [
    "{loc_title} 출장 전문 스웨디시 마사지 추천 {shop_name} | 케어힐즈",
    "{loc_title} 타이 출장 테라피 및 마사지 안내 {shop_name} | 케어힐즈",
    "{loc_title} 아로마 출장 케어 전문 마사지 샵 {shop_name} | 케어힐즈",
    "{loc_title} 방문 출장 감성 홈케어 마사지 {shop_name} | 케어힐즈",
    "{loc_title} 힐링 출장 테라피 코스 마사지 {shop_name} | 케어힐즈"
]

desc_patterns = [
    "{loc_title} 지역에서 이용 가능한 출장 전문 매장 {shop_name} 제휴 안내. 선입금 없는 후불제 홈케어 마사지 코스 및 가격표 정보.",
    "{loc_title} 맞춤형 방문 출장 프로그램 운영 중인 {shop_name} 안내. 안전한 후불제 시스템으로 이용하는 전문 마사지 정보.",
    "{loc_title} 전 지역 출장 케어 서비스 {shop_name} 제휴 페이지. 신뢰할 수 있는 후불제 아로마 및 타이 마사지 안내.",
    "{loc_title} 감성 충전 출장 홈케어 전문 {shop_name} 방문 안내. 부담 없는 후불제로 즐기는 프리미엄 마사지 코스 모음."
]

# HTML 템플릿
html_template = """<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<title>{shop_title}</title>
<meta name="description" content="{shop_desc}">
<meta name="robots" content="index,follow">
<link rel="canonical" href="{shop_url}">
<style>
:root{{--p:#1a3a5c;--a:#c9a84c;--bg:#f8f9fb;--bg2:#fff;--txt:#1a2332;--muted:#5a6a7e;--bdr:#dde3ec;--hd:#fff;--ft:#1a2332;--shadow:0 2px 12px rgba(26,58,92,.10);}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:var(--bg);color:var(--txt);font-family:'Pretendard',-apple-system,'Malgun Gothic',sans-serif;line-height:1.6}}
a{{color:inherit;text-decoration:none}}
.cm2-hd{{background:var(--hd);border-bottom:2px solid var(--p);position:sticky;top:0;z-index:100;box-shadow:0 2px 8px rgba(0,0,0,.07)}}
.cm2-hd-inner{{max-width:1100px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;height:62px;padding:0 20px}}
.cm2-logo{{display:flex;align-items:center;gap:10px}}
.cm2-logo-mark{{width:38px;height:38px;background:var(--p);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:900;font-size:16px}}
.cm2-logo-text{{font-size:16px;font-weight:800;color:var(--p)}}
.cm2-logo-sub{{font-size:10px;color:var(--muted);font-weight:400}}
.cm2-tel{{background:var(--a);color:#fff;padding:8px 18px;border-radius:6px;font-weight:700;font-size:14px}}
.cm2-bc{{background:#fff;border-bottom:1px solid var(--bdr);padding:10px 20px}}
.cm2-bc-inner{{max-width:1100px;margin:0 auto;font-size:12px;color:var(--muted)}}
.cm2-bc-inner a{{color:var(--p)}}
.cm2-sec{{padding:44px 20px}}
.cm2-sec-inner{{max-width:1100px;margin:0 auto}}
.cm2-shop{{background:#fff;border:1.5px solid var(--bdr);border-radius:12px;overflow:hidden;box-shadow:var(--shadow)}}
.cm2-shop-body{{padding:24px}}
.cm2-shop-hd{{display:flex;justify-content:space-between;align-items:flex-start;gap:8px;margin-bottom:12px}}
.cm2-shop-name{{font-size:22px;font-weight:800;color:var(--txt)}}
.cm2-shop-rating{{font-size:12px;background:#fff9ee;border:1px solid #e8c87a;color:#8a6000;padding:3px 10px;border-radius:4px;font-weight:700}}
.cm2-shop-tags{{display:flex;flex-wrap:wrap;gap:5px;margin-bottom:14px}}
.cm2-tag{{font-size:11px;padding:3px 10px;border-radius:4px;background:#eef3fa;color:var(--p);font-weight:600}}
.cm2-shop-intro{{font-size:15px;color:var(--muted);line-height:1.6;margin-bottom:16px}}
.cm2-courses{{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:20px}}
.cm2-course{{background:var(--bg);border:1px solid var(--bdr);border-radius:6px;padding:10px 14px;font-size:13px;flex:1;min-width:140px}}
.cm2-course strong{{display:block;font-weight:700;color:var(--txt);margin-bottom:2px}}
.cm2-shop-ft{{display:flex;justify-content:space-between;align-items:center;padding-top:16px;border-top:1px solid var(--bdr)}}
.cm2-price-label{{font-size:12px;color:var(--muted)}}
.cm2-price-val{{font-size:18px;font-weight:800;color:var(--p)}}
.cm2-call{{background:var(--a);color:#fff;padding:12px 24px;border-radius:6px;font-weight:700;font-size:14px}}
.cm2-ft{{background:var(--ft);padding:40px 20px;color:#8fa4be;font-size:12px;line-height:1.8;margin-top:40px}}
.cm2-ft-brand{{font-size:18px;font-weight:800;color:#fff;margin-bottom:6px}}
.cm2-ft-brand span{{font-size:11px;color:var(--a);display:block;font-weight:400;letter-spacing:1px;margin-top:2px}}
@media(max-width:768px){{.cm2-tel{{display:none}}.cm2-shop-ft{{flex-direction:column;gap:12px;align-items:stretch}}.cm2-call{{text-align:center}}}}
</style>
</head>
<body>

<header class="cm2-hd">
  <div class="cm2-hd-inner">
    <a href="https://careheals.netlify.app/" class="cm2-logo">
      <div class="cm2-logo-mark">CH</div>
      <div><div class="cm2-logo-text">케어힐즈</div><div class="cm2-logo-sub">CAREHEALS</div></div>
    </a>
    <div class="cm2-hd-right">
      <a href="tel:{shop_phone}" class="cm2-tel">📞 {shop_phone}</a>
    </div>
  </div>
</header>

<nav class="cm2-bc">
  <div class="cm2-bc-inner">
    <a href="https://careheals.netlify.app/">케어힐즈</a> › 
    <a href="https://careheals.netlify.app/{sido_path}/">{sido_name}</a> › 
    <a href="https://careheals.netlify.app/{sido_path}/{gu_path}/">{gu_name}</a> › 
    {current_dong} {shop_name}
  </div>
</nav>

<section class="cm2-sec">
  <div class="cm2-sec-inner" style="max-width:780px">
    <div class="cm2-shop">
      <div class="cm2-shop-body">
        <div class="cm2-shop-hd">
          <div class="cm2-shop-name">{shop_tag}</div>
          <div class="cm2-shop-rating">★ 4.8 (128건)</div>
        </div>
        <div class="cm2-shop-tags">
          <span class="cm2-tag">프리미엄전문</span>
          <span class="cm2-tag">여성/남성 관리사</span>
          <span class="cm2-tag">카드결제 가능</span>
          <span class="cm2-tag">선입금 없음</span>
          <span class="cm2-tag">실시간 방문</span>
        </div>
        <p class="cm2-shop-intro">{shop_desc}</p>
        
        <div class="cm2-courses">
          <div class="cm2-course"><strong>아로마 테라피</strong><span>60분 · {shop_price}</span></div>
          <div class="cm2-course"><strong>스웨디시 코스</strong><span>90분 · 120,000원</span></div>
        </div>
        
        <div class="cm2-shop-ft">
          <div>
            <span class="cm2-price-label">이용 요금 </span>
            <span class="cm2-price-val">{shop_price}</span>
          </div>
          <a href="tel:{shop_phone}" class="cm2-call">📞 {shop_phone} 예약 문의</a>
        </div>
      </div>
    </div>
  </div>
</section>

<footer class="cm2-ft">
  <div class="cm2-ft-inner">
    <div class="cm2-ft-brand">케어힐즈<span>CAREHEALS</span></div>
    <p>수도권 출장 프리미엄 아로마 마사지 업체 지도. 내 위치 근처 방문마사지를 찾아보세요.</p>
    <p>대표번호: {shop_phone} · 운영시간: 매일 19:00 ~ 익일 05:00</p>
    <p style="margin-top:16px; color:#4a6a8a">© 2026 케어힐즈. All rights reserved.</p>
  </div>
</footer>

</body>
</html>
"""

# 4. 1000개 이상의 페이지 순차적 자동 생성 루프
sitemap_urls = []
global_index = 0

for reg in all_regions:
    sido_path = reg["sido"]
    sido_name = reg["sido_name"]
    gu_path = reg["path"]
    gu_name = reg["name"]
    
    # 각 동별 순회 생성 (동마다 5개 샵 = 대량 페이지 확장)
    for dong in reg["dongs"]:
        dong_dir = f"{sido_path}/{gu_path}/{dong['path']}"
        
        for shop in shops:
            shop_dir = f"{dong_dir}/{shop['id']}"
            os.makedirs(shop_dir, exist_ok=True)
            
            # 순차 패턴 적용 ('출장'과 '마사지'가 절대 붙어있지 않음)
            t_pattern = title_patterns[global_index % len(title_patterns)]
            d_pattern = desc_patterns[global_index % len(desc_patterns)]
            global_index += 1
            
            loc_title = f"{gu_name} {dong['name']}"
            shop_title_str = t_pattern.format(loc_title=loc_title, shop_name=shop["name"])
            shop_desc_str = d_pattern.format(loc_title=loc_title, shop_name=shop["name"])
            shop_url = f"https://careheals.netlify.app/{sido_path}/{gu_path}/{dong['path']}/{shop['id']}/"
            
            file_path = f"{shop_dir}/index.html"
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(html_template.format(
                    shop_title=shop_title_str,
                    shop_desc=shop_desc_str,
                    shop_url=shop_url,
                    shop_name=shop["name"],
                    shop_tag=shop["tag"],
                    shop_desc_text=shop["desc"],
                    shop_price=shop["price"],
                    shop_phone=shop["phone"],
                    sido_path=sido_path,
                    sido_name=sido_name,
                    gu_path=gu_path,
                    gu_name=gu_name,
                    current_dong=dong["name"]
                ))
            sitemap_urls.append(shop_url)

print(f"✨ 총 {len(sitemap_urls)}개의 고유 페이지가 순차 조합 패턴으로 생성되었습니다!")