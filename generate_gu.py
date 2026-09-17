import os

# 서울 25개 구, 경기 주요 시·군·구, 인천 2군 9구 통합 행정구역 데이터
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

    # --- 경기도 주요 시·군 및 구 ---
    {"sido": "gyeonggi", "sido_name": "경기", "path": "suwon_paldal", "name": "수원시 팔달구", "dongs": [{"name": "인계동", "path": "ingyedong"}, {"name": "우만동", "path": "umandong"}, {"name": "지동", "path": "jidong"}, {"name": "매산동", "path": "maesandong"}, {"name": "고등동", "path": "godeungdong"}, {"name": "화서동", "path": "hwaseodong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "seongnam_bundang", "name": "성남시 분당구", "dongs": [{"name": "서현동", "path": "seohyeondong"}, {"name": "정자동", "path": "jeongjadong"}, {"name": "수내동", "path": "sunaedong"}, {"name": "야탑동", "path": "yatapdong"}, {"name": "이매동", "path": "imaedong"}, {"name": "판교동", "path": "pangyodong"}, {"name": "백현동", "path": "baekhyeondong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "goyang_ilsandong", "name": "고양시 일산동구", "dongs": [{"name": "백석동", "path": "baekseokdong"}, {"name": "마두동", "path": "madudong"}, {"name": "정발산동", "path": "jeongbalsandong"}, {"name": "식사동", "path": "siksadong"}, {"name": "중산동", "path": "jungsandong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "yongin_suji", "name": "용인시 수지구", "dongs": [{"name": "풍덕천동", "path": "pungdeokcheondong"}, {"name": "죽전동", "path": "jukjeondong"}, {"name": "상현동", "path": "sanghyeondong"}, {"name": "성복동", "path": "seongbokdong"}, {"name": "동천동", "path": "dongcheondong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "bucheon_wonmi", "name": "부천시 원미구", "dongs": [{"name": "중동", "path": "jungdong"}, {"name": "상동", "path": "sangdong"}, {"name": "심곡동", "path": "simgokdong"}, {"name": "원미동", "path": "wonmidong"}, {"name": "역곡동", "path": "yeokgokdong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "anyang_dongan", "name": "안양시 동안구", "dongs": [{"name": "비산동", "path": "bisandong"}, {"name": "평촌동", "path": "pyeongchondong"}, {"name": "호계동", "path": "hogyedong"}, {"name": "관양동", "path": "gwanyangdong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "ansan_danwon", "name": "안산시 단원구", "dongs": [{"name": "고잔동", "path": "gojandong"}, {"name": "초지동", "path": "chojidong"}, {"name": "선부동", "path": "seonbudong"}, {"name": "원곡동", "path": "wongokdong"}, {"name": "와동", "path": "wadong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "hwaseongsi", "name": "화성시", "dongs": [{"name": "동탄동", "path": "dongtandong"}, {"name": "병점동", "path": "byeongjeomdong"}, {"name": "향남읍", "path": "hyangnameup"}, {"name": "남양읍", "path": "namyangeup"}, {"name": "봉담읍", "path": "bongdameup"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "pyeongtaeksi", "name": "평택시", "dongs": [{"name": "비전동", "path": "bijeondong"}, {"name": "동삭동", "path": "dongsakdong"}, {"name": "고덕동", "path": "godeokdong"}, {"name": "서정동", "path": "seojeongdong"}, {"name": "송탄동", "path": "songtandong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "gimposi", "name": "김포시", "dongs": [{"name": "구래동", "path": "guraedong"}, {"name": "장기동", "path": "janggidong"}, {"name": "운양동", "path": "unyangdong"}, {"name": "사우동", "path": "saudong"}, {"name": "풍무동", "path": "pungmudong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "namyangjusi", "name": "남양주시", "dongs": [{"name": "다산동", "path": "dasandong"}, {"name": "별내동", "path": "byeolnaedong"}, {"name": "호평동", "path": "hopyeongdong"}, {"name": "평내동", "path": "pyeongnaedong"}, {"name": "진접읍", "path": "jinjeopeup"}]},

    # --- 인천 개편 체제 (2군 9구) ---
    {"sido": "incheon", "sido_name": "인천", "path": "jemulbogu", "name": "제물포구", "dongs": [{"name": "신포동", "path": "sinpodong"}, {"name": "신흥동", "path": "sinheungdong"}, {"name": "도원동", "path": "dowondong"}, {"name": "송림동", "path": "songrimdong"}, {"name": "만석동", "path": "manseokdong"}]},
    {"sido": "incheon", "sido_name": "인천", "path": "yeongjonggu", "name": "영종구", "dongs": [{"name": "운서동", "path": "unseodong"}, {"name": "영종동", "path": "yeongjongdong"}, {"name": "용유동", "path": "yongyudong"}]},
    {"sido": "incheon", "sido_name": "인천", "path": "michuholgu", "name": "미추홀구", "dongs": [{"name": "주안동", "path": "juandong"}, {"name": "용현동", "path": "yonghyeondong"}, {"name": "학익동", "path": "hakikdong"}, {"name": "도화동", "path": "dohwadong"}]},
    {"sido": "incheon", "sido_name": "인천", "path": "yeonsugu", "name": "연수구", "dongs": [{"name": "송도동", "path": "songdodong"}, {"name": "연수동", "path": "yeonsudong"}, {"name": "동춘동", "path": "dongchundong"}, {"name": "옥련동", "path": "oknyeondong"}]},
    {"sido": "incheon", "sido_name": "인천", "path": "namdonggu", "name": "남동구", "dongs": [{"name": "구월동", "path": "guwoldong"}, {"name": "간석동", "path": "ganseokdong"}, {"name": "만수동", "path": "mansudong"}, {"name": "논현동", "path": "nonhyeondong"}, {"name": "서창동", "path": "seochangdong"}]},
    {"sido": "incheon", "sido_name": "인천", "path": "bupyeonggu", "name": "부평구", "dongs": [{"name": "부평동", "path": "bupyeongdong"}, {"name": "산곡동", "path": "sangokdong"}, {"name": "청천동", "path": "cheongcheondong"}, {"name": "삼산동", "path": "samsandong"}, {"name": "부개동", "path": "bugaedong"}]},
    {"sido": "incheon", "sido_name": "인천", "path": "gyeyanggu", "name": "계양구", "dongs": [{"name": "계산동", "path": "gyesandong"}, {"name": "효성동", "path": "hyoseongdong"}, {"name": "작전동", "path": "jakjeondong"}]},
    {"sido": "incheon", "sido_name": "인천", "path": "seohaegu", "name": "서해구", "dongs": [{"name": "청라동", "path": "cheongradong"}, {"name": "연희동", "path": "yeonhuidong"}, {"name": "가정동", "path": "gajeongdong"}, {"name": "석남동", "path": "seoknamdong"}]},
    {"sido": "incheon", "sido_name": "인천", "path": "geomdangu", "name": "검단구", "dongs": [{"name": "당하동", "path": "danghadong"}, {"name": "마전동", "path": "majeondong"}, {"name": "원당동", "path": "wondangdong"}, {"name": "아라동", "path": "aradong"}]}
]

# 제휴 업체 5개 데이터
shops = [
    { "name": "🔥 한국미인홈케어", "desc": "신속 방문! 정성 가득한 테라피 & 릴렉싱 프로그램", "phone": "0507-1280-3303", "price": "100,000원부터~" },
    { "name": "✨ 오늘밤테라피", "desc": "품격 있는 힐링을 선사하는 최고급 오일 프라이빗 방문 테라피", "phone": "0507-1280-3223", "price": "60,000원부터~" },
    { "name": "💎 주주테라피", "desc": "재방문율 1위! 칼도착 25분 보장, 철저한 위생 관리와 럭셔리 케어", "phone": "0507-1280-3193", "price": "60,000원부터~" },
    { "name": "🌟 퀸즈홈테라피", "desc": "전문 힐러들의 맞춤형 VIP 피로회복 특화 프로그램 진행 중", "phone": "0507-1280-3334", "price": "60,000원부터~" },
    { "name": "👑 골든테라피", "desc": "선입금 없는 100% 후불제! 수도권 전지역 평균 25분 내 실시간 도착", "phone": "0507-1280-3360", "price": "110,000원부터~" }
]

gu_template = """<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{gu_name} 출장 마사지·홈타이 | 실시간 제휴 업체 안내 | 케어힐즈</title>
<style>
:root{{--p:#1a3a5c;--a:#c9a84c;--bg:#f8f9fb;--bg2:#fff;--txt:#1a2332;--muted:#5a6a7e;--bdr:#dde3ec;--shadow:0 2px 12px rgba(26,58,92,.10);}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:var(--bg);color:var(--txt);font-family:'Pretendard',sans-serif;line-height:1.6;padding-bottom:80px}}
a{{color:inherit;text-decoration:none}}
.ch-hd{{background:#fff;border-bottom:2px solid var(--p);position:sticky;top:0;z-index:100;box-shadow:0 2px 8px rgba(0,0,0,.07)}}
.ch-hd-inner{{max-width:1100px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;height:62px;padding:0 20px}}
.ch-logo{{font-size:16px;font-weight:800;color:var(--p)}}
.ch-tel{{background:var(--a);color:#fff;padding:8px 18px;border-radius:6px;font-weight:700;font-size:14px}}
.ch-sec{{padding:44px 20px}}
.ch-sec-inner{{max-width:1100px;margin:0 auto}}
.ch-sec h2{{font-size:20px;font-weight:800;color:var(--p);margin-bottom:12px}}
.ch-info-box{{background:var(--p);color:#fff;border-radius:8px;padding:14px 18px;font-size:14px;margin-bottom:20px}}
.ch-info-box strong{{color:var(--a)}}
.ch-dong-wrap{{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:30px}}
.ch-dong-badge{{background:#fff;border:1.5px solid var(--bdr);padding:6px 14px;border-radius:20px;font-size:13px;font-weight:600;color:var(--muted);transition:all .15s;display:inline-block}}
.ch-dong-badge:hover{{background:var(--p);color:#fff;border-color:var(--p)}}
.ch-shop-list{{display:flex;flex-direction:column;gap:14px}}
.ch-shop{{background:#fff;border:1.5px solid var(--bdr);border-radius:12px;padding:20px;display:flex;justify-content:space-between;align-items:center;transition:all .15s}}
.ch-shop:hover{{border-color:var(--p);box-shadow:var(--shadow)}}
.ch-shop-name{{font-size:17px;font-weight:800;color:var(--txt);margin-bottom:6px}}
.ch-shop-desc{{font-size:13px;color:var(--muted);margin-bottom:10px}}
.ch-shop-price{{font-size:15px;font-weight:800;color:var(--p)}}
.ch-call{{background:var(--a);color:#fff;padding:10px 20px;border-radius:6px;font-weight:700;font-size:13px;white-space:nowrap}}
.ch-ft{{background:#1a2332;color:#8fa4be;padding:40px 20px;margin-top:40px;text-align:center;font-size:12px}}
@media(max-width:768px){{.ch-shop{{flex-direction:column;align-items:flex-start;gap:12px}}.ch-call{{width:100%;text-align:center}}}}
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
    <h2>{sido_name} {gu_name} 마사지 · 힐링 출장 홈케어 안내</h2>
    <div class="ch-info-box"><strong>💰 {gu_name} 전 지역 단일 요금:</strong> 선입금 없는 100% 후불제 케어 서비스 제공</div>
    
    <div style="margin-bottom:12px;font-weight:700;color:var(--p);">📍 방문 가능 행정동 전체 보기</div>
    <div class="ch-dong-wrap">
      {dong_badges}
    </div>

    <div style="margin-top:30px;margin-bottom:16px;">
      <h3 style="font-size:18px;font-weight:800;color:var(--p);">✨ {gu_name} 실시간 추천 제휴 업체</h3>
    </div>
    <div class="ch-shop-list">
      {shop_items}
    </div>
  </div>
</section>
<footer class="ch-ft"><p>© 2026 케어힐즈. All rights reserved.</p></footer>
</body>
</html>
"""

# 사이트맵(sitemap.xml) URL 리스트 수집 시작
sitemap_urls = [
    "https://careheals.netlify.app/",
    "https://careheals.netlify.app/seoul/",
    "https://careheals.netlify.app/gyeonggi/",
    "https://careheals.netlify.app/incheon/"
]

count = 0
for reg in all_regions:
    sido_path = reg["sido"]
    sido_name = reg["sido_name"]
    gu_path = reg["path"]
    gu_name = reg["name"]
    
    # 동 배지 생성 (클릭 시 해당 동 경로로 이동하도록 링크 부여)
    dong_badges = "".join([f'<a href="./{dong["path"]}/" class="ch-dong-badge">{dong["name"]}</a>' for dong in reg["dongs"]])
    
    # 제휴 업체 목록 HTML 생성
    shop_items = ""
    for shop in shops:
        shop_items += f"""
        <div class="ch-shop">
          <div>
            <div class="ch-shop-name">{shop["name"]}</div>
            <div class="ch-shop-desc">{shop["desc"]}</div>
            <div class="ch-shop-price">이용요금: {shop["price"]}</div>
          </div>
          <div>
            <a href="tel:{shop["phone"]}" class="ch-call">📞 예약 전화 ({shop["phone"]})</a>
          </div>
        </div>
        """
    
    # 구 폴더 경로 생성
    dir_path = f"{sido_path}/{gu_path}"
    os.makedirs(dir_path, exist_ok=True)
    
    # 구 허브 페이지 URL 추가
    sitemap_urls.append(f"https://careheals.netlify.app/{sido_path}/{gu_path}/")
    
    # 하위 동별 폴더 및 index.html 생성
    for dong in reg["dongs"]:
        dong_dir = f"{dir_path}/{dong['path']}"
        os.makedirs(dong_dir, exist_ok=True)
        
        dong_file = f"{dong_dir}/index.html"
        with open(dong_file, "w", encoding="utf-8") as f:
            f.write(gu_template.format(
                sido_name=sido_name,
                gu_name=f"{gu_name} {dong['name']}",
                dong_badges=dong_badges,
                shop_items=shop_items
            ))
        
        # 동별 URL 추가
        sitemap_urls.append(f"https://careheals.netlify.app/{sido_path}/{gu_path}/{dong['path']}/")

    # 메인 구 허브 index.html 파일 생성
    file_path = f"{dir_path}/index.html"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(gu_template.format(
            sido_name=sido_name,
            gu_name=gu_name,
            dong_badges=dong_badges,
            shop_items=shop_items
        ))
    count += 1

# sitemap.xml 파일 생성
sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for url in sitemap_urls:
    sitemap_content += f'  <url>\n    <loc>{url}</loc>\n  </url>\n'
sitemap_content += '</urlset>'

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_content)

print(f"✨ 총 {count}개의 구·시·군 허브 및 하위 동 페이지가 생성되었으며, sitemap.xml도 성공적으로 생성되었습니다!")