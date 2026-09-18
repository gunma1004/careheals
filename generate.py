import os

# 1. 서울, 경기, 인천 전체 행정구역 데이터 구조화 (구/시 단위 목록 포함)
region_data = {
    "seoul": {
        "name": "서울",
        "full_name": "서울특별시",
        "districts": [
            {"gu": "jongrogu", "gu_name": "종로구", "dongs": [{"name": "사직동", "path": "sajikdong"}, {"name": "삼청동", "path": "samcheongdong"}, {"name": "종로동", "path": "jongrodong"}]},
            {"gu": "junggu", "gu_name": "중구", "dongs": [{"name": "소공동", "path": "sogongdong"}, {"name": "명동", "path": "myeongdong"}, {"name": "을지로동", "path": "euljirodong"}]},
            {"gu": "yongsangu", "gu_name": "용산구", "dongs": [{"name": "후암동", "path": "huamdong"}, {"name": "이태원동", "path": "itaewondong"}, {"name": "한남동", "path": "hannamdong"}]},
            {"gu": "seongdonggu", "gu_name": "성동구", "dongs": [{"name": "왕십리동", "path": "wangsipridong"}, {"name": "성수동", "path": "seongsudong"}, {"name": "옥수동", "path": "oksudong"}]},
            {"gu": "gwangjingu", "gu_name": "광진구", "dongs": [{"name": "화양동", "path": "hwayangdong"}, {"name": "구의동", "path": "guuidong"}, {"name": "자양동", "path": "jayangdong"}]},
            {"gu": "dongdaemungu", "gu_name": "동대문구", "dongs": [{"name": "회기동", "path": "hoegidong"}, {"name": "청량리동", "path": "cheongryangridong"}, {"name": "장안동", "path": "jangandong"}]},
            {"gu": "jungnanggu", "gu_name": "중랑구", "dongs": [{"name": "면목동", "path": "myeonmokdong"}, {"name": "상봉동", "path": "sangbongdong"}, {"name": "중화동", "path": "junghwadong"}]},
            {"gu": "seongbukgu", "gu_name": "성북구", "dongs": [{"name": "돈암동", "path": "donamdong"}, {"name": "안암동", "path": "anamdong"}, {"name": "길음동", "path": "gileumdong"}]},
            {"gu": "gangbukgu", "gu_name": "강북구", "dongs": [{"name": "미아동", "path": "miadong"}, {"name": "수유동", "path": "suyudong"}, {"name": "번동", "path": "beondong"}]},
            {"gu": "dobonggu", "gu_name": "도봉구", "dongs": [{"name": "쌍문동", "path": "ssangmundong"}, {"name": "창동", "path": "changdong"}, {"name": "방학동", "path": "banghakdong"}]},
            {"gu": "nowongu", "gu_name": "노원구", "dongs": [{"name": "상계동", "path": "sanggyedong"}, {"name": "중계동", "path": "junggyedong"}, {"name": "하계동", "path": "hagyedong"}]},
            {"gu": "eunpyeonggu", "gu_name": "은평구", "dongs": [{"name": "불광동", "path": "bulgwangdong"}, {"name": "응암동", "path": "eungamdong"}, {"name": "연신내동", "path": "yeonsinnaedong"}]},
            {"gu": "seodaemungu", "gu_name": "서대문구", "dongs": [{"name": "신촌동", "path": "sinchondong"}, {"name": "홍제동", "path": "hongjedong"}, {"name": "연희동", "path": "yeonhuidong"}]},
            {"gu": "mapogu", "gu_name": "마포구", "dongs": [{"name": "서교동", "path": "seogyodong"}, {"name": "합정동", "path": "hapjeongdong"}, {"name": "연남동", "path": "yeonnamdong"}, {"name": "공덕동", "path": "gongdeokdong"}]},
            {"gu": "yangcheongu", "gu_name": "양천구", "dongs": [{"name": "목동", "path": "mokdong"}, {"name": "신정동", "path": "sinjeongdong"}, {"name": "신월동", "path": "sinwoldong"}]},
            {"gu": "gangseogu", "gu_name": "강서구", "dongs": [{"name": "화곡동", "path": "hwagokdong"}, {"name": "등촌동", "path": "deungchondong"}, {"name": "발산동", "path": "balsandong"}]},
            {"gu": "gurogu", "gu_name": "구로구", "dongs": [{"name": "구로동", "path": "gurodong"}, {"name": "신도림동", "path": "sindorimdong"}, {"name": "개봉동", "path": "gaebongdong"}]},
            {"gu": "geumcheongu", "gu_name": "금천구", "dongs": [{"name": "가산동", "path": "gasandong"}, {"name": "독산동", "path": "doksandong"}, {"name": "시흥동", "path": "siheungdong"}]},
            {"gu": "yeongdeungpogu", "gu_name": "영등포구", "dongs": [{"name": "여의도동", "path": "yeouidong"}, {"name": "영등포동", "path": "yeongdeungpodong"}, {"name": "당산동", "path": "dangsandong"}]},
            {"gu": "dongjakgu", "gu_name": "동작구", "dongs": [{"name": "노량진동", "path": "noryangjindong"}, {"name": "사당동", "path": "sadangdong"}, {"name": "상도동", "path": "sangdodong"}]},
            {"gu": "gwanakgu", "gu_name": "관악구", "dongs": [{"name": "신림동", "path": "sinlimdong"}, {"name": "봉천동", "path": "bongcheondong"}, {"name": "남현동", "path": "namhyeondong"}]},
            {"gu": "seochogu", "gu_name": "서초구", "dongs": [{"name": "서초동", "path": "seochodong"}, {"name": "반포동", "path": "banpodong"}, {"name": "방배동", "path": "bangbaedong"}, {"name": "양재동", "path": "yangjaedong"}]},
            {"gu": "gangnamgu", "gu_name": "강남구", "dongs": [{"name": "신사동", "path": "sinsadong"}, {"name": "논현동", "path": "nonhyeondong"}, {"name": "삼성동", "path": "samseongdong"}, {"name": "대치동", "path": "daechidong"}, {"name": "역삼동", "path": "yeoksamdong"}, {"name": "청담동", "path": "cheongdamdong"}]},
            {"gu": "songpagu", "gu_name": "송파구", "dongs": [{"name": "잠실동", "path": "jamsildong"}, {"name": "방이동", "path": "bangidong"}, {"name": "문정동", "path": "munjeongdong"}, {"name": "가락동", "path": "ganakdong"}]},
            {"gu": "gangdonggu", "gu_name": "강동구", "dongs": [{"name": "천호동", "path": "cheonhodong"}, {"name": "길동", "path": "gildong"}, {"name": "명일동", "path": "myeongildong"}]}
        ]
    },
    "gyeonggi": {
        "name": "경기",
        "full_name": "경기도",
        "districts": [
            {"gu": "suwon_jangan", "gu_name": "수원시 장안구", "dongs": [{"name": "정자동", "path": "jeongjadong"}, {"name": "조원동", "path": "jowondong"}, {"name": "파장동", "path": "pajangdong"}]},
            {"gu": "suwon_gwonseon", "gu_name": "수원시 권선구", "dongs": [{"name": "권선동", "path": "gwonseondong"}, {"name": "곡반정동", "path": "gokbanjeongdong"}, {"name": "세류동", "path": "seryudong"}]},
            {"gu": "suwon_paldal", "gu_name": "수원시 팔달구", "dongs": [{"name": "인계동", "path": "ingyedong"}, {"name": "우만동", "path": "umandong"}, {"name": "매산동", "path": "maesandong"}]},
            {"gu": "suwon_yeongtong", "gu_name": "수원시 영통구", "dongs": [{"name": "영통동", "path": "yeongtongdong"}, {"name": "매탄동", "path": "maetandong"}, {"name": "광교동", "path": "gwanggyodong"}]},
            {"gu": "seongnam_sujeong", "gu_name": "성남시 수정구", "dongs": [{"name": "태평동", "path": "taepyeongdong"}, {"name": "신흥동", "path": "sinheungdong"}, {"name": "수진동", "path": "sujindong"}]},
            {"gu": "seongnam_jungwon", "gu_name": "성남시 중원구", "dongs": [{"name": "성남동", "path": "seongnamdong"}, {"name": "금광동", "path": "geumgwangdong"}, {"name": "상대원동", "path": "sangdaewondong"}]},
            {"gu": "seongnam_bundang", "gu_name": "성남시 분당구", "dongs": [{"name": "정자동", "path": "jeongjadong"}, {"name": "서현동", "path": "seohyeondong"}, {"name": "수내동", "path": "sunaedong"}, {"name": "판교동", "path": "pangyodong"}]},
            {"gu": "goyang_deogyang", "gu_name": "고양시 덕양구", "dongs": [{"name": "화정동", "path": "hwajeongdong"}, {"name": "행신동", "path": "haengsindong"}, {"name": "삼송동", "path": "samsongdong"}]},
            {"gu": "goyang_ilsandong", "gu_name": "고양시 일산동구", "dongs": [{"name": "백석동", "path": "baekseokdong"}, {"name": "마두동", "path": "madudong"}, {"name": "정발산동", "path": "jeongbalsandong"}]},
            {"gu": "goyang_ilsanseo", "gu_name": "고양시 일산서구", "dongs": [{"name": "대화동", "path": "daehwadong"}, {"name": "주엽동", "path": "juyeopdong"}, {"name": "탄현동", "path": "tanhyeondong"}]},
            {"gu": "yongin_cheoin", "gu_name": "용인시 처인구", "dongs": [{"name": "역북동", "path": "yeokbukdong"}, {"name": "김량장동", "path": "kimryangjangdong"}]},
            {"gu": "yongin_giheung", "gu_name": "용인시 기흥구", "dongs": [{"name": "구갈동", "path": "gugaldong"}, {"name": "동백동", "path": "dongbaekdong"}, {"name": "신갈동", "path": "singaldong"}]},
            {"gu": "yongin_suji", "gu_name": "용인시 수지구", "dongs": [{"name": "풍덕천동", "path": "pungdeokcheondong"}, {"name": "죽전동", "path": "jukjeondong"}, {"name": "상현동", "path": "sanghyeondong"}]},
            {"gu": "bucheon_wonmi", "gu_name": "부천시 원미구", "dongs": [{"name": "중동", "path": "jungdong"}, {"name": "상동", "path": "sangdong"}, {"name": "심곡동", "path": "simgokdong"}]},
            {"gu": "bucheon_sosa", "gu_name": "부천시 소사구", "dongs": [{"name": "소사본동", "path": "sosabondong"}, {"name": "역곡동", "path": "yeokgokdong"}]},
            {"gu": "bucheon_ojeong", "gu_name": "부천시 오정구", "dongs": [{"name": "오정동", "path": "ojeongdong"}, {"name": "원종동", "path": "wonjongdong"}]},
            {"gu": "anyang_manan", "gu_name": "안양시 만안구", "dongs": [{"name": "안양동", "path": "anyangdong"}, {"name": "석수동", "path": "seoksudong"}]},
            {"gu": "anyang_dongan", "gu_name": "안양시 동안구", "dongs": [{"name": "비산동", "path": "bisandong"}, {"name": "평촌동", "path": "pyeongchondong"}, {"name": "호계동", "path": "hogyedong"}]},
            {"gu": "ansan_sangnok", "gu_name": "안산시 상록구", "dongs": [{"name": "본오동", "path": "bonodong"}, {"name": "사동", "path": "sadong"}, {"name": "이동", "path": "idong"}]},
            {"gu": "ansan_danwon", "gu_name": "안산시 단원구", "dongs": [{"name": "고잔동", "path": "gojandong"}, {"name": "초지동", "path": "chojidong"}, {"name": "선부동", "path": "seonbudong"}]},
            {"gu": "uijeongbusi", "gu_name": "의정부시", "dongs": [{"name": "의정부동", "path": "uijeongbudong"}, {"name": "신곡동", "path": "singokdong"}]},
            {"gu": "pyeongtaeksi", "gu_name": "평택시", "dongs": [{"name": "비전동", "path": "bijeondong"}, {"name": "동삭동", "path": "dongsakdong"}, {"name": "고덕동", "path": "godeokdong"}]},
            {"gu": "dongducheonsi", "gu_name": "동두천시", "dongs": [{"name": "생연동", "path": "saengyeondong"}, {"name": "지행동", "path": "jihaengdong"}]},
            {"gu": "gwangmyeongsi", "gu_name": "광명시", "dongs": [{"name": "철산동", "path": "cheolsandong"}, {"name": "하안동", "path": "haandong"}, {"name": "소하동", "path": "sohadong"}]},
            {"gu": "gwacheonsi", "gu_name": "과천시", "dongs": [{"name": "중앙동", "path": "jungangdong"}, {"name": "별양동", "path": "byeolyangdong"}]},
            {"gu": "gurisi", "gu_name": "구리시", "dongs": [{"name": "인창동", "path": "inchangdong"}, {"name": "수택동", "path": "sutaekdong"}]},
            {"gu": "namyangjusi", "gu_name": "남양주시", "dongs": [{"name": "다산동", "path": "dasandong"}, {"name": "별내동", "path": "byeolnaedong"}, {"name": "호평동", "path": "hopyeongdong"}]},
            {"gu": "osansi", "gu_name": "오산시", "dongs": [{"name": "궐동", "path": "gwoldong"}, {"name": "원동", "path": "wondong"}]},
            {"gu": "siheungsi", "gu_name": "시흥시", "dongs": [{"name": "배곧동", "path": "baegotdong"}, {"name": "정왕동", "path": "jeongwangdong"}]},
            {"gu": "gunposi", "gu_name": "군포시", "dongs": [{"name": "산본동", "path": "sanbondong"}, {"name": "금정동", "path": "geumjeongdong"}]},
            {"gu": "uiwangsi", "gu_name": "의왕시", "dongs": [{"name": "내손동", "path": "naesondong"}, {"name": "오전동", "path": "ojeondong"}]},
            {"gu": "hanamsi", "gu_name": "하남시", "dongs": [{"name": "미사동", "path": "misadong"}, {"name": "풍산동", "path": "pungsandong"}]},
            {"gu": "pajusi", "gu_name": "파주시", "dongs": [{"name": "운정동", "path": "unjeongdong"}, {"name": "금촌동", "path": "geumchondong"}]},
            {"gu": "icheonsi", "gu_name": "이천시", "dongs": [{"name": "증포동", "path": "jeungpodong"}, {"name": "창전동", "path": "changjeondong"}]},
            {"gu": "anseongsi", "gu_name": "안성시", "dongs": [{"name": "공도읍", "path": "gongdoeup"}, {"name": "안성동", "path": "anseongdong"}]},
            {"gu": "gimposi", "gu_name": "김포시", "dongs": [{"name": "구래동", "path": "guraedong"}, {"name": "장기동", "path": "janggidong"}, {"name": "운양동", "path": "unyangdong"}]},
            {"gu": "hwaseongsi", "gu_name": "화성시", "dongs": [{"name": "동탄동", "path": "dongtandong"}, {"name": "향남읍", "path": "hyangnameup"}, {"name": "병점동", "path": "byeongjeomdong"}]},
            {"gu": "gwangjusi", "gu_name": "광주시", "dongs": [{"name": "오포동", "path": "opodong"}, {"name": "경안동", "path": "gyeongandong"}]},
            {"gu": "yangjusi", "gu_name": "양주시", "dongs": [{"name": "회천동", "path": "hoecheondong"}, {"name": "양주동", "path": "yangjudong"}]},
            {"gu": "pocheonsi", "gu_name": "포천시", "dongs": [{"name": "소흘읍", "path": "soheuleup"}, {"name": "포천동", "path": "pocheondong"}]},
            {"gu": "yeojusi", "gu_name": "여주시", "dongs": [{"name": "오학동", "path": "ohakdong"}, {"name": "여흥동", "path": "yeoheungdong"}]},
            {"gu": "yeoncheongun", "gu_name": "연천군", "dongs": [{"name": "전곡읍", "path": "jeongokeup"}, {"name": "연천읍", "path": "yeoncheoneup"}]},
            {"gu": "gapyeonggun", "gu_name": "가평군", "dongs": [{"name": "가평읍", "path": "gapyeongeup"}, {"name": "청평면", "path": "cheongpyeongmyeon"}]},
            {"gu": "yangpyeonggun", "gu_name": "양평군", "dongs": [{"name": "양평읍", "path": "yangpyeongeup"}, {"name": "용문면", "path": "yongmunmyeon"}]}
        ]
    },
    "incheon": {
        "name": "인천",
        "full_name": "인천광역시",
        "districts": [
            {"gu": "jemulbogu", "gu_name": "제물포구", "dongs": [{"name": "신포동", "path": "sinpodong"}, {"name": "신흥동", "path": "sinheungdong"}, {"name": "송림동", "path": "songrimdong"}]},
            {"gu": "yeongjonggu", "gu_name": "영종구", "dongs": [{"name": "운서동", "path": "unseodong"}, {"name": "영종동", "path": "yeongjongdong"}, {"name": "용유동", "path": "yongyudong"}]},
            {"gu": "michuholgu", "gu_name": "미추홀구", "dongs": [{"name": "주안동", "path": "juandong"}, {"name": "용현동", "path": "yonghyeondong"}, {"name": "학익동", "path": "hakikdong"}]},
            {"gu": "yeonsugu", "gu_name": "연수구", "dongs": [{"name": "송도동", "path": "songdodong"}, {"name": "연수동", "path": "yeonsudong"}, {"name": "동춘동", "path": "dongchundong"}]},
            {"gu": "namdonggu", "gu_name": "남동구", "dongs": [{"name": "구월동", "path": "guwoldong"}, {"name": "간석동", "path": "ganseokdong"}, {"name": "논현동", "path": "nonhyeondong"}]},
            {"gu": "bupyeonggu", "gu_name": "부평구", "dongs": [{"name": "부평동", "path": "bupyeongdong"}, {"name": "산곡동", "path": "sangokdong"}, {"name": "삼산동", "path": "samsandong"}]},
            {"gu": "gyeyanggu", "gu_name": "계양구", "dongs": [{"name": "계산동", "path": "gyesandong"}, {"name": "효성동", "path": "hyoseongdong"}, {"name": "작전동", "path": "jakjeondong"}]},
            {"gu": "seohaegu", "gu_name": "서해구", "dongs": [{"name": "청라동", "path": "cheongradong"}, {"name": "연희동", "path": "yeonhuidong"}, {"name": "가정동", "path": "gajeongdong"}]},
            {"gu": "geomdangu", "gu_name": "검단구", "dongs": [{"name": "당하동", "path": "danghadong"}, {"name": "마전동", "path": "majeondong"}, {"name": "아라동", "path": "aradong"}]},
            {"gu": "ganghwagun", "gu_name": "강화군", "dongs": [{"name": "강화읍", "path": "ganghwaeup"}, {"name": "길상면", "path": "gilsangmyeon"}]},
            {"gu": "ongjingun", "gu_name": "옹진군", "dongs": [{"name": "영흥면", "path": "yeongheungmyeon"}, {"name": "북도면", "path": "bukdomyeon"}]}
        ]
    }
}

# 2. 동 단위 상세 페이지 HTML 템플릿
dong_html_template = """<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<title>{dong_name} 출장 마사지·홈타이 | {gu_name} 안마 추천 | 케어힐즈</title>
<meta name="description" content="{sido_name} {gu_name} {dong_name} 출장 마사지·홈타이·안마. 후불제 보장, 평균 25분 내 방문. 투명한 가격으로 안내합니다.">
<meta name="robots" content="index,follow">
<link rel="canonical" href="https://careheals.netlify.app/{sido_path}/{gu_path}/{dong_path}/">
<style>
:root{{--p:#1a3a5c;--a:#c9a84c;--bg:#f8f9fb;--bg2:#fff;--txt:#1a2332;--muted:#5a6a7e;--bdr:#dde3ec;--hd:#fff;--ft:#1a2332;--shadow:0 2px 12px rgba(26,58,92,.10);}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:var(--bg);color:var(--txt);font-family:'Pretendard',-apple-system,'Malgun Gothic',sans-serif;line-height:1.6;padding-bottom:80px}}
a{{color:inherit;text-decoration:none}}
.ch-hd{{background:var(--hd);border-bottom:2px solid var(--p);position:sticky;top:0;z-index:100;box-shadow:0 2px 8px rgba(0,0,0,.07)}}
.ch-hd-inner{{max-width:1100px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;height:62px;padding:0 20px}}
.ch-logo{{font-size:16px;font-weight:800;color:var(--p)}}
.ch-tel{{background:var(--a);color:#fff;padding:8px 18px;border-radius:6px;font-weight:700;font-size:14px}}
.ch-sec{{padding:44px 20px}}
.ch-sec-inner{{max-width:1100px;margin:0 auto}}
.ch-sec h2{{font-size:20px;font-weight:800;color:var(--p);margin-bottom:12px}}
.ch-info-box{{background:var(--p);color:#fff;border-radius:8px;padding:14px 18px;font-size:14px;margin-bottom:20px}}
.ch-info-box strong{{color:var(--a)}}
.ch-shop-list{{display:flex;flex-direction:column;gap:14px}}
.ch-shop{{background:#fff;border:1.5px solid var(--bdr);border-radius:12px;padding:20px;display:flex;justify-content:space-between;align-items:center;transition:all .15s}}
.ch-shop:hover{{border-color:var(--p);box-shadow:var(--shadow)}}
.ch-shop-name a{{font-size:17px;font-weight:800;color:var(--txt);text-decoration:none}}
.ch-shop-name a:hover{{color:var(--p);text-decoration:underline}}
.ch-shop-desc{{font-size:13px;color:var(--muted);margin-bottom:10px}}
.ch-shop-price{{font-size:15px;font-weight:800;color:var(--p)}}
.ch-btn-group{{display:flex;gap:8px;align-items:center}}
.ch-detail-btn{{background:#f0f3f8;color:var(--p);padding:10px 14px;border-radius:6px;font-weight:700;font-size:13px}}
.ch-call{{background:var(--a);color:#fff;padding:10px 20px;border-radius:6px;font-weight:700;font-size:13px;white-space:nowrap}}
.ch-ft{{background:var(--ft);padding:40px 20px;color:#8fa4be;font-size:12px;margin-top:40px;text-align:center}}
@media(max-width:768px){{.ch-shop{{flex-direction:column;align-items:flex-start;gap:12px}}.ch-btn-group{{width:100%;justify-content:space-between}}.ch-call{{flex:1;text-align:center}}}}
</style>
</head>
<body>
<header class="ch-hd">
  <div class="ch-hd-inner">
    <a href="https://careheals.netlify.app/" class="ch-logo">케어힐즈 (CAREHEALS)</a>
    <a href="tel:050-8202-7994" class="ch-tel">📞 050-8202-7994</a>
  </div>
</header>

<section class="ch-sec">
  <div class="ch-sec-inner">
    <h2>{sido_name} {gu_name} {dong_name} 출장 아로마 마사지 · 홈타이</h2>
    <div class="ch-info-box"><strong>💰 {dong_name} 최저가 안내:</strong> 선입금 없는 100% 후불제 케어 서비스 제공</div>
    
    <div style="margin-top:24px;margin-bottom:16px;">
      <h3 style="font-size:17px;font-weight:800;color:var(--p);">✨ {dong_name} 실시간 추천 제휴 업체</h3>
    </div>

    <div id="shop-list" class="ch-shop-list"></div>
  </div>
</section>

<footer class="ch-ft">
  <div style="max-width:1100px;margin:0 auto;">
    <p>대표번호: 050-8202-7994 · 운영시간: 매일 19:00 ~ 익일 05:00</p>
    <p style="margin-top:8px">© 2026 케어힐즈. All rights reserved.</p>
  </div>
</footer>

<script>
  const shops = [
    {{ name: "🔥 한국미인홈케어", id: "shop1", desc: "{sido_name}·{gu_name} 전지역 신속 방문! 정성 가득한 테라피 & 릴렉싱 프로그램", phone: "0507-1280-3303", price: "100,000원부터~" }},
    {{ name: "✨ 오늘밤테라피", id: "shop2", desc: "품격 있는 힐링을 선사하는 최고급 오일 프라이빗 방문 테라피 서비스", phone: "0507-1280-3223", price: "60,000원부터~" }},
    {{ name: "💎 주주테라피", id: "shop3", desc: "재방문율 1위! 칼도착 25분 보장, 철저한 위생 관리와 럭셔리 케er", phone: "0507-1280-3193", price: "60,000원부터~" }},
    {{ name: "🌟 퀸즈홈테라피", id: "shop4", desc: "전문 힐러들의 맞춤형 VIP 피로회복 특화 프로그램 진행 중", phone: "0507-1280-3334", price: "60,000원부터~" }},
    {{ name: "👑 골든테라피", id: "shop5", desc: "선입금 없는 100% 후불제! 수도권 전지역 평균 25분 내 실시간 도착", phone: "0507-1280-3360", price: "110,000원부터~" }}
  ];

  function shuffle(array) {{
    for (let i = array.length - 1; i > 0; i--) {{
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }}
    return array;
  }}

  function renderShops() {{
    const container = document.getElementById('shop-list');
    container.innerHTML = "";
    const shuffledShops = shuffle([...shops]);
    
    shuffledShops.forEach(shop => {{
      const item = document.createElement('div');
      item.className = 'ch-shop';
      item.innerHTML = `
        <div>
          <div class="ch-shop-name"><a href="./${{shop.id}}/">${{shop.name}}</a></div>
          <div class="ch-shop-desc">${{shop.desc}}</div>
          <div class="ch-shop-price">이용요금: ${{shop.price}}</div>
        </div>
        <div class="ch-btn-group">
          <a href="./${{shop.id}}/" class="ch-detail-btn">상세보기</a>
          <a href="tel:${{shop.phone}}" class="ch-call">📞 예약 전화</a>
        </div>
      `;
      container.appendChild(item);
    }});
  }}

  window.onload = renderShops;
</script>
</body>
</html>
"""

# 3. 시도별 허브 페이지 (예: 경기 지역 안내 페이지) HTML 템플릿
sido_html_template = """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{sido_full_name} 시·군·구 출장 마사지·홈타이 지역별 안내 | 케어힐즈</title>
  <meta name="description" content="{sido_full_name} 주요 시·군 및 세부 구 출장 마사지·홈타이·안마 업체 안내. 건식 6만원부터 투명한 가격.">
  <meta name="robots" content="index,follow">
  <link rel="canonical" href="https://careheals.netlify.app/{sido_path}/">
  <style>
    :root{{--p:#1a3a5c;--a:#c9a84c;--bg:#f8f9fb;--txt:#1a2332;--muted:#5a6a7e;--bdr:#dde3ec;--shadow:0 2px 12px rgba(26,58,92,.10);}}
    *{{box-sizing:border-box;margin:0;padding:0}}
    body{{background:var(--bg);color:var(--txt);font-family:'Pretendard',-apple-system,'Malgun Gothic',sans-serif;line-height:1.6;padding-bottom:80px}}
    a{{color:inherit;text-decoration:none}}
    .ch-hd{{background:#fff;border-bottom:2px solid var(--p);position:sticky;top:0;z-index:100;box-shadow:0 2px 8px rgba(0,0,0,.07)}}
    .ch-hd-inner{{max-width:1100px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;height:62px;padding:0 20px}}
    .ch-logo{{font-size:16px;font-weight:800;color:var(--p)}}
    .ch-tel{{background:var(--a);color:#fff;padding:8px 18px;border-radius:6px;font-weight:700;font-size:14px}}
    .ch-bc{{background:#fff;border-bottom:1px solid var(--bdr);padding:10px 20px}}
    .ch-bc-inner{{max-width:1100px;margin:0 auto;font-size:12px;color:var(--muted)}}
    .ch-bc-inner a{{color:var(--p)}}
    .ch-sec{{padding:44px 20px}}
    .ch-sec-inner{{max-width:1100px;margin:0 auto}}
    .ch-sec h2{{font-size:20px;font-weight:800;color:var(--p);margin-bottom:22px;position:relative}}
    .ch-sec h2::after{{content:'';display:block;width:32px;height:3px;background:var(--a);margin-top:6px;border-radius:2px}}
    .ch-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px}}
    .ch-card{{background:#fff;border:1.5px solid var(--bdr);border-radius:10px;padding:16px;transition:all .15s;display:block}}
    .ch-card:hover{{border-color:var(--p);box-shadow:var(--shadow);transform:translateY(-2px)}}
    .ch-card strong{{display:block;font-size:16px;font-weight:700;color:var(--txt);margin-bottom:4px}}
    .ch-card span{{font-size:12px;color:var(--muted)}}
    .ch-ft{{background:#1a2332;color:#8fa4be;padding:40px 20px;margin-top:40px;font-size:12px;line-height:1.8;text-align:center}}
  </style>
</head>
<body>
  <header class="ch-hd">
    <div class="ch-hd-inner">
      <a href="https://careheals.netlify.app/" class="ch-logo">케어힐즈 (CAREHEALS)</a>
      <a href="tel:050-8202-7994" class="ch-tel">📞 050-8202-7994</a>
    </div>
  </header>

  <nav class="ch-bc">
    <div class="ch-bc-inner"><a href="https://careheals.netlify.app/">케어힐즈</a> › {sido_name}</div>
  </nav>

  <section class="ch-sec">
    <div class="ch-sec-inner">
      <h2>{sido_full_name} 지역별 출장 마사지 안내</h2>
      <div class="ch-grid">
        {cards_html}
      </div>
    </div>
  </section>

  <footer class="ch-ft">
    <div style="max-width:1100px;margin:0 auto;"><p>© 2026 케어힐즈. All rights reserved.</p></div>
  </footer>
</body>
</html>
"""

def generate_static_pages():
    total_dong_count = 0
    
    for sido_path, sido_info in region_data.items():
        sido_name = sido_info["name"]
        sido_full_name = sido_info["full_name"]
        districts = sido_info["districts"]
        
        cards_html_list = []
        
        for dist in districts:
            gu_path = dist["gu"]
            gu_name = dist["gu_name"]
            
            # 시도 허브 페이지용 카드 생성 (구/시 단위 링크)
            cards_html_list.append(
                f'<a href="/{sido_path}/{gu_path}/" class="ch-card"><strong>{gu_name}</strong><span>전체 동 및 제휴업체 보기</span></a>'
            )
            
            for dong in dist["dongs"]:
                dong_name = dong["name"]
                dong_path = dong["path"]
                
                # 동 단위 폴더 및 index.html 생성
                dir_path = os.path.join("public", sido_path, gu_path, dong_path)
                os.makedirs(dir_path, exist_ok=True)
                
                page_content = dong_html_template.format(
                    sido_path=sido_path,
                    sido_name=sido_name,
                    gu_path=gu_path,
                    gu_name=gu_name,
                    dong_path=dong_path,
                    dong_name=dong_name
                )
                
                with open(os.path.join(dir_path, "index.html"), "w", encoding="utf-8") as f:
                    f.write(page_content)
                    
                total_dong_count += 1
        
        # 시도별 허브 페이지 생성 (예: public/gyeonggi/index.html)
        sido_dir = os.path.join("public", sido_path)
        os.makedirs(sido_dir, exist_ok=True)
        
        sido_page_content = sido_html_template.format(
            sido_path=sido_path,
            sido_name=sido_name,
            sido_full_name=sido_full_name,
            cards_html="\n        ".join(cards_html_list)
        )
        
        with open(os.path.join(sido_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(sido_page_content)

    print(f"🎉 성공적으로 시도별 허브 페이지 및 총 {total_dong_count}개의 동 페이지(index.html)가 생성되었습니다!")

if __name__ == "__main__":
    generate_static_pages()