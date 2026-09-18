import os
import random

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

# 서울, 경기 전 지역(44개), 인천 데이터 통합
all_regions = [
    # --- [서울시 25개 구] ---
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

    # --- [경기도 44개 전 지역] ---
    {"sido": "gyeonggi", "sido_name": "경기", "path": "suwon_jangan", "name": "수원시 장안구", "dongs": [{"name": "정자동", "path": "jeongjadong"}, {"name": "조원동", "path": "jowondong"}, {"name": "파장동", "path": "pajangdong"}, {"name": "율천동", "path": "yulcheondong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "suwon_gwonseon", "name": "수원시 권선구", "dongs": [{"name": "권선동", "path": "gwonseondong"}, {"name": "곡반정동", "path": "gokbanjeongdong"}, {"name": "세류동", "path": "seryudong"}, {"name": "탑동", "path": "tapdong"}, {"name": "호매실동", "path": "homaesildong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "suwon_paldal", "name": "수원시 팔달구", "dongs": [{"name": "인계동", "path": "ingyedong"}, {"name": "우만동", "path": "umandong"}, {"name": "지동", "path": "jidong"}, {"name": "매산동", "path": "maesandong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "suwon_yeongtong", "name": "수원시 영통구", "dongs": [{"name": "영통동", "path": "yeongtongdong"}, {"name": "매탄동", "path": "maetandong"}, {"name": "원천동", "path": "woncheondong"}, {"name": "광교동", "path": "gwanggyodong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "seongnam_sujeong", "name": "성남시 수정구", "dongs": [{"name": "태평동", "path": "taepyeongdong"}, {"name": "신흥동", "path": "sinheungdong"}, {"name": "수진동", "path": "sujindong"}, {"name": "산성동", "path": "sanseongdong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "seongnam_jungwon", "name": "성남시 중원구", "dongs": [{"name": "성남동", "path": "seongnamdong"}, {"name": "금광동", "path": "geumgwangdong"}, {"name": "상대원동", "path": "sangdaewondong"}, {"name": "하대원동", "path": "hadaewondong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "seongnam_bundang", "name": "성남시 분당구", "dongs": [{"name": "서현동", "path": "seohyeondong"}, {"name": "정자동", "path": "jeongjadong"}, {"name": "수내동", "path": "sunaedong"}, {"name": "야탑동", "path": "yatapdong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "goyang_deogyang", "name": "고양시 덕양구", "dongs": [{"name": "화정동", "path": "hwajeongdong"}, {"name": "행신동", "path": "haengsindong"}, {"name": "삼송동", "path": "samsongdong"}, {"name": "원흥동", "path": "wonheungdong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "goyang_ilsandong", "name": "고양시 일산동구", "dongs": [{"name": "백석동", "path": "baekseokdong"}, {"name": "마두동", "path": "madudong"}, {"name": "정발산동", "path": "jeongbalsandong"}, {"name": "식사동", "path": "siksadong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "goyang_ilsanseo", "name": "고양시 일산서구", "dongs": [{"name": "대화동", "path": "daehwadong"}, {"name": "주엽동", "path": "juyeopdong"}, {"name": "탄현동", "path": "tanhyeondong"}, {"name": "일산동", "path": "ilsandong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "yongin_cheoin", "name": "용인시 처인구", "dongs": [{"name": "역북동", "path": "yeokbukdong"}, {"name": "김량장동", "path": "kimryangjangdong"}, {"name": "유림동", "path": "yurimdong"}, {"name": "동부동", "path": "dongbudong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "yongin_giheung", "name": "용인시 기흥구", "dongs": [{"name": "구갈동", "path": "gugaldong"}, {"name": "동백동", "path": "dongbaekdong"}, {"name": "신갈동", "path": "singaldong"}, {"name": "보정동", "path": "bojeongdong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "yongin_suji", "name": "용인시 수지구", "dongs": [{"name": "풍덕천동", "path": "pungdeokcheondong"}, {"name": "죽전동", "path": "jukjeondong"}, {"name": "상현동", "path": "sanghyeondong"}, {"name": "성복동", "path": "seongbokdong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "bucheon_wonmi", "name": "부천시 원미구", "dongs": [{"name": "중동", "path": "jungdong"}, {"name": "상동", "path": "sangdong"}, {"name": "심곡동", "path": "simgokdong"}, {"name": "원미동", "path": "wonmidong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "bucheon_sosa", "name": "부천시 소사구", "dongs": [{"name": "소사본동", "path": "sosabondong"}, {"name": "범박동", "path": "beombakdong"}, {"name": "역곡동", "path": "yeokgokdong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "bucheon_ojeong", "name": "부천시 오정구", "dongs": [{"name": "오정동", "path": "ojeongdong"}, {"name": "원종동", "path": "wonjongdong"}, {"name": "고강동", "path": "gogangdong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "anyang_manan", "name": "안양시 만안구", "dongs": [{"name": "안양동", "path": "anyangdong"}, {"name": "석수동", "path": "seoksudong"}, {"name": "박달동", "path": "bakdaldong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "anyang_dongan", "name": "안양시 동안구", "dongs": [{"name": "비산동", "path": "bisandong"}, {"name": "평촌동", "path": "pyeongchondong"}, {"name": "호계동", "path": "hogyedong"}, {"name": "관양동", "path": "gwanyangdong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "ansan_sangnok", "name": "안산시 상록구", "dongs": [{"name": "본오동", "path": "bonodong"}, {"name": "사동", "path": "sadong"}, {"name": "이동", "path": "idong"}, {"name": "월피동", "path": "wolpidong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "ansan_danwon", "name": "안산시 단원구", "dongs": [{"name": "고잔동", "path": "gojandong"}, {"name": "초지동", "path": "chojidong"}, {"name": "선부동", "path": "seonbudong"}, {"name": "원곡동", "path": "wongokdong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "uijeongbusi", "name": "의정부시", "dongs": [{"name": "의정부동", "path": "uijeongbudong"}, {"name": "신곡동", "path": "singokdong"}, {"name": "가능동", "path": "ganeungdong"}, {"name": "호원동", "path": "howondong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "pyeongtaeksi", "name": "평택시", "dongs": [{"name": "비전동", "path": "bijeondong"}, {"name": "동삭동", "path": "dongsakdong"}, {"name": "고덕동", "path": "godeokdong"}, {"name": "서정동", "path": "seojeongdong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "dongducheonsi", "name": "동두천시", "dongs": [{"name": "생연동", "path": "saengyeondong"}, {"name": "지행동", "path": "jihaengdong"}, {"name": "보산동", "path": "bosandong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "gwangmyeongsi", "name": "광명시", "dongs": [{"name": "철산동", "path": "cheolsandong"}, {"name": "하안동", "path": "haandong"}, {"name": "소하동", "path": "sohadong"}, {"name": "광명동", "path": "gwangmyeongdong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "gwacheonsi", "name": "과천시", "dongs": [{"name": "중앙동", "path": "jungangdong"}, {"name": "별양동", "path": "byeolyangdong"}, {"name": "문원동", "path": "munwondong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "gurisi", "name": "구리시", "dongs": [{"name": "인창동", "path": "inchangdong"}, {"name": "수택동", "path": "sutaekdong"}, {"name": "교문동", "path": "gyomundong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "namyangjusi", "name": "남양주시", "dongs": [{"name": "다산동", "path": "dasandong"}, {"name": "별내동", "path": "byeolnaedong"}, {"name": "호평동", "path": "hopyeongdong"}, {"name": "평내동", "path": "pyeongnaedong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "osansi", "name": "오산시", "dongs": [{"name": "궐동", "path": "gwoldong"}, {"name": "원동", "path": "wondong"}, {"name": "오산동", "path": "osandong"}, {"name": "세교동", "path": "segyodong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "siheungsi", "name": "시흥시", "dongs": [{"name": "배곧동", "path": "baegotdong"}, {"name": "정왕동", "path": "jeongwangdong"}, {"name": "대야동", "path": "daeyadong"}, {"name": "목감동", "path": "mokgamdong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "gunposi", "name": "군포시", "dongs": [{"name": "산본동", "path": "sanbondong"}, {"name": "금정동", "path": "geumjeongdong"}, {"name": "대야미동", "path": "daeyamidong"}, {"name": "부곡동", "path": "bugokdong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "uiwangsi", "name": "의왕시", "dongs": [{"name": "내손동", "path": "naesondong"}, {"name": "오전동", "path": "ojeondong"}, {"name": "포일동", "path": "poildong"}, {"name": "부곡동", "path": "bugokdong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "hanamsi", "name": "하남시", "dongs": [{"name": "미사동", "path": "misadong"}, {"name": "풍산동", "path": "pungsandong"}, {"name": "신장동", "path": "sinjangdong"}, {"name": "창우동", "path": "changwudong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "pajusi", "name": "파주시", "dongs": [{"name": "운정동", "path": "unjeongdong"}, {"name": "금촌동", "path": "geumchondong"}, {"name": "교하동", "path": "gyohadong"}, {"name": "문산읍", "path": "munsaneup"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "icheonsi", "name": "이천시", "dongs": [{"name": "증포동", "path": "jeungpodong"}, {"name": "창전동", "path": "changjeondong"}, {"name": "중리동", "path": "junglidong"}, {"name": "부발읍", "path": "bubaleup"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "anseongsi", "name": "안성시", "dongs": [{"name": "공도읍", "path": "gongdoeup"}, {"name": "안성동", "path": "anseongdong"}, {"name": "대덕면", "path": "daedeokmyeon"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "gimposi", "name": "김포시", "dongs": [{"name": "구래동", "path": "guraedong"}, {"name": "장기동", "path": "janggidong"}, {"name": "운양동", "path": "unyangdong"}, {"name": "사우동", "path": "saudong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "hwaseongsi", "name": "화성시", "dongs": [{"name": "동탄동", "path": "dongtandong"}, {"name": "병점동", "path": "byeongjeomdong"}, {"name": "향남읍", "path": "hyangnameup"}, {"name": "남양읍", "path": "namyangeup"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "gwangjusi", "name": "광주시", "dongs": [{"name": "오포동", "path": "opodong"}, {"name": "경안동", "path": "gyeongandong"}, {"name": "초월읍", "path": "chowoleup"}, {"name": "곤지암읍", "path": "gonjigameup"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "yangjusi", "name": "양주시", "dongs": [{"name": "회천동", "path": "hoecheondong"}, {"name": "양주동", "path": "yangjudong"}, {"name": "옥정동", "path": "okjeongdong"}, {"name": "덕정동", "path": "deokjeongdong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "pocheonsi", "name": "포천시", "dongs": [{"name": "소흘읍", "path": "soheuleup"}, {"name": "포천동", "path": "pocheondong"}, {"name": "선단동", "path": "seandandong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "yeojusi", "name": "여주시", "dongs": [{"name": "오학동", "path": "ohakdong"}, {"name": "여흥동", "path": "yeoheungdong"}, {"name": "중앙동", "path": "jungangdong"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "yeoncheongun", "name": "연천군", "dongs": [{"name": "전곡읍", "path": "jeongokeup"}, {"name": "연천읍", "path": "yeoncheoneup"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "gapyeonggun", "name": "가평군", "dongs": [{"name": "가평읍", "path": "gapyeongeup"}, {"name": "청평면", "path": "cheongpyeongmyeon"}, {"name": "조종면", "path": "jojongmyeon"}]},
    {"sido": "gyeonggi", "sido_name": "경기", "path": "yangpyeonggun", "name": "양평군", "dongs": [{"name": "양평읍", "path": "yangpyeongeup"}, {"name": "용문면", "path": "yongmunmyeon"}, {"name": "강상면", "path": "gangsangmyeon"}]},

    # --- [인천시 개편 체제 (2군 9구)] ---
    {"sido": "incheon", "sido_name": "인천", "path": "jemulbogu", "name": "제물포구", "dongs": [{"name": "신포동", "path": "sinpodong"}, {"name": "신흥동", "path": "sinheungdong"}, {"name": "도원동", "path": "dowondong"}, {"name": "송림동", "path": "songrimdong"}]},
    {"sido": "incheon", "sido_name": "인천", "path": "yeongjonggu", "name": "영종구", "dongs": [{"name": "운서동", "path": "unseodong"}, {"name": "영종동", "path": "yeongjongdong"}, {"name": "용유동", "path": "yongyudong"}]},
    {"sido": "incheon", "sido_name": "인천", "path": "michuholgu", "name": "미추홀구", "dongs": [{"name": "주안동", "path": "juandong"}, {"name": "용현동", "path": "yonghyeondong"}, {"name": "학익동", "path": "hakikdong"}, {"name": "도화동", "path": "dohwadong"}]},
    {"sido": "incheon", "sido_name": "인천", "path": "yeonsugu", "name": "연수구", "dongs": [{"name": "송도동", "path": "songdodong"}, {"name": "연수동", "path": "yeonsudong"}, {"name": "동춘동", "path": "dongchundong"}, {"name": "옥련동", "path": "oknyeondong"}]},
    {"sido": "incheon", "sido_name": "인천", "path": "namdonggu", "name": "남동구", "dongs": [{"name": "구월동", "path": "guwoldong"}, {"name": "간석동", "path": "ganseokdong"}, {"name": "만수동", "path": "mansudong"}, {"name": "논현동", "path": "nonhyeondong"}]},
    {"sido": "incheon", "sido_name": "인천", "path": "bupyeonggu", "name": "부평구", "dongs": [{"name": "부평동", "path": "bupyeongdong"}, {"name": "산곡동", "path": "sangokdong"}, {"name": "청천동", "path": "cheongcheondong"}, {"name": "삼산동", "path": "samsandong"}]},
    {"sido": "incheon", "sido_name": "인천", "path": "gyeyanggu", "name": "계양구", "dongs": [{"name": "계산동", "path": "gyesandong"}, {"name": "효성동", "path": "hyoseongdong"}, {"name": "작전동", "path": "jakjeondong"}]},
    {"sido": "incheon", "sido_name": "인천", "path": "seohaegu", "name": "서해구", "dongs": [{"name": "청라동", "path": "cheongradong"}, {"name": "연희동", "path": "yeonhuidong"}, {"name": "가정동", "path": "gajeongdong"}, {"name": "석남동", "path": "seoknamdong"}]},
    {"sido": "incheon", "sido_name": "인천", "path": "geomdangu", "name": "검단구", "dongs": [{"name": "당하동", "path": "danghadong"}, {"name": "마전동", "path": "majeondong"}, {"name": "원당동", "path": "wondangdong"}, {"name": "아라동", "path": "aradong"}]}
]

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
.cm2-dong-wrap{{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:24px}}
.cm2-dong-badge{{background:#fff;border:1.5px solid var(--bdr);padding:6px 14px;border-radius:20px;font-size:13px;font-weight:600;color:var(--muted);transition:all .15s;display:inline-block}}
.cm2-dong-badge:hover, .cm2-dong-badge.active{{background:var(--p);color:#fff;border-color:var(--p)}}
.cm2-shop{{background:#fff;border:1.5px solid var(--bdr);border-radius:12px;overflow:hidden;box-shadow:var(--shadow);margin-bottom:14px}}
.cm2-shop-body{{padding:24px}}
.cm2-shop-hd{{display:flex;justify-content:space-between;align-items:flex-start;gap:8px;margin-bottom:12px}}
.cm2-shop-name{{font-size:22px;font-weight:800;color:var(--txt)}}
.cm2-shop-rating{{font-size:12px;background:#fff9ee;border:1px solid #e8c87a;color:#8a6000;padding:3px 10px;border-radius:4px;font-weight:700}}
.cm2-shop-intro{{font-size:15px;color:var(--muted);line-height:1.6;margin-bottom:16px}}
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
    {current_location}
  </div>
</nav>

<section class="cm2-sec">
  <div class="cm2-sec-inner" style="max-width:780px">
    <h2 style="font-size:22px;font-weight:800;color:var(--p);margin-bottom:12px;">{page_heading}</h2>
    {dong_badges_html}
    {content_body}
  </div>
</section>

<footer class="cm2-ft">
  <div class="cm2-ft-inner">
    <div class="cm2-ft-brand">케어힐즈<span>CAREHEALS</span></div>
    <p>수도권 출장 프리미엄 아로마 마사지 업체 지도. 내 위치 근처 방문마사지를 찾아보세요.</p>
    <p>대표번호: 050-8202-7994 · 운영시간: 매일 19:00 ~ 익일 05:00</p>
    <p style="margin-top:16px; color:#4a6a8a">© 2026 케어힐즈. All rights reserved.</p>
  </div>
</footer>

</body>
</html>
"""

sitemap_urls = []
global_index = 0

for reg in all_regions:
    sido_path = reg["sido"]
    sido_name = reg["sido_name"]
    gu_path = reg["path"]
    gu_name = reg["name"]
    
    gu_dir = os.path.join("public", sido_path, gu_path)
    os.makedirs(gu_dir, exist_ok=True)
    
    dong_badges_main = "".join([f'<a href="./{d["path"]}/" class="cm2-dong-badge">{d["name"]}</a>' for d in reg["dongs"]])
    dong_badges_section = f'<div style="margin-bottom:12px;font-weight:700;color:var(--p);">📍 방문 가능 행정동 전체 보기</div><div class="cm2-dong-wrap">{dong_badges_main}</div>'
    
    # 구 페이지용 샵 목록 랜덤 섞기
    shuffled_shops_gu = shops.copy()
    random.shuffle(shuffled_shops_gu)
    
    gu_shops_html = ""
    for shop in shuffled_shops_gu:
        gu_shops_html += f"""
        <div class="cm2-shop">
          <div class="cm2-shop-body">
            <div class="cm2-shop-hd"><div class="cm2-shop-name"><a href="./{shop['id']}/">{shop["tag"]}</a></div><div class="cm2-shop-rating">★ 4.8</div></div>
            <p class="cm2-shop-intro">{shop["desc"]}</p>
            <div class="cm2-shop-ft">
              <div><span class="cm2-price-label">이용 요금 </span><span class="cm2-price-val">{shop["price"]}</span></div>
              <a href="./{shop['id']}/" class="cm2-call">상세보기</a>
            </div>
          </div>
        </div>
        """
    
    gu_url = f"https://careheals.netlify.app/{sido_path}/{gu_path}/"
    with open(os.path.join(gu_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_template.format(
            shop_title=f"{gu_name} 출장 마사지·홈타이 추천 | 케어힐즈",
            shop_desc=f"{sido_name} {gu_name} 전 지역 출장 홈케어 및 마사지 제휴 업체 안내.",
            shop_url=gu_url,
            shop_phone="050-8202-7994",
            sido_path=sido_path, sido_name=sido_name, gu_path=gu_path, gu_name=gu_name,
            current_location=gu_name,
            page_heading=f"{gu_name} 제휴 업체 안내",
            dong_badges_html=dong_badges_section,
            content_body=gu_shops_html
        ))
    sitemap_urls.append(gu_url)

    for shop in shops:
        shop_dir = os.path.join(gu_dir, shop['id'])
        os.makedirs(shop_dir, exist_ok=True)
        
        t_pattern = title_patterns[global_index % len(title_patterns)]
        d_pattern = desc_patterns[global_index % len(desc_patterns)]
        global_index += 1
        
        shop_title_str = t_pattern.format(loc_title=gu_name, shop_name=shop["name"])
        shop_desc_str = d_pattern.format(loc_title=gu_name, shop_name=shop["name"])
        shop_url = f"https://careheals.netlify.app/{sido_path}/{gu_path}/{shop['id']}/"
        
        single_shop_html = f"""
        <div class="cm2-shop">
          <div class="cm2-shop-body">
            <div class="cm2-shop-hd"><div class="cm2-shop-name">{shop["tag"]}</div><div class="cm2-shop-rating">★ 4.8 (128건)</div></div>
            <p class="cm2-shop-intro">{shop["desc"]}</p>
            <div class="cm2-shop-ft">
              <div><span class="cm2-price-label">이용 요금 </span><span class="cm2-price-val">{shop["price"]}</span></div>
              <a href="tel:{shop["phone"]}" class="cm2-call">📞 {shop["phone"]} 예약 문의</a>
            </div>
          </div>
        </div>
        """
        
        with open(os.path.join(shop_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_template.format(
                shop_title=shop_title_str, shop_desc=shop_desc_str, shop_url=shop_url,
                shop_phone=shop["phone"], sido_path=sido_path, sido_name=sido_name,
                gu_path=gu_path, gu_name=gu_name, current_location=gu_name,
                page_heading=shop["name"], dong_badges_html="", content_body=single_shop_html
            ))
        sitemap_urls.append(shop_url)

    for dong in reg["dongs"]:
        dong_dir = os.path.join(gu_dir, dong['path'])
        os.makedirs(dong_dir, exist_ok=True)
        
        dong_badges_sub = "".join([f'<a href="../{d["path"]}/" class="cm2-dong-badge{" active" if d["path"] == dong["path"] else ""}">{d["name"]}</a>' for d in reg["dongs"]])
        dong_badges_section_sub = f'<div style="margin-bottom:12px;font-weight:700;color:var(--p);">📍 방문 가능 행정동 전체 보기</div><div class="cm2-dong-wrap">{dong_badges_sub}</div>'
        
        # 동 페이지용 샵 목록 랜덤 섞기
        shuffled_shops_dong = shops.copy()
        random.shuffle(shuffled_shops_dong)
        
        dong_shops_html = ""
        for shop in shuffled_shops_dong:
            dong_shops_html += f"""
            <div class="cm2-shop">
              <div class="cm2-shop-body">
                <div class="cm2-shop-hd"><div class="cm2-shop-name"><a href="./{shop['id']}/">{shop["tag"]}</a></div><div class="cm2-shop-rating">★ 4.8</div></div>
                <p class="cm2-shop-intro">{shop["desc"]}</p>
                <div class="cm2-shop-ft">
                  <div><span class="cm2-price-label">이용 요금 </span><span class="cm2-price-val">{shop["price"]}</span></div>
                  <a href="./{shop['id']}/" class="cm2-call">상세보기</a>
                </div>
              </div>
            </div>
            """
            
        dong_url = f"https://careheals.netlify.app/{sido_path}/{gu_path}/{dong['path']}/"
        with open(os.path.join(dong_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_template.format(
                shop_title=f"{gu_name} {dong['name']} 출장 마사지·홈타이 추천 | 케어힐즈",
                shop_desc=f"{sido_name} {gu_name} {dong['name']} 지역 맞춤형 방문 홈케어 및 제휴 안내.",
                shop_url=dong_url,
                shop_phone="050-8202-7994",
                sido_path=sido_path, sido_name=sido_name, gu_path=gu_path, gu_name=gu_name,
                current_location=dong['name'],
                page_heading=f"{gu_name} {dong['name']} 제휴 업체 안내",
                dong_badges_html=dong_badges_section_sub,
                content_body=dong_shops_html
            ))
        sitemap_urls.append(dong_url)

        for shop in shops:
            shop_dir = os.path.join(dong_dir, shop['id'])
            os.makedirs(shop_dir, exist_ok=True)
            
            t_pattern = title_patterns[global_index % len(title_patterns)]
            d_pattern = desc_patterns[global_index % len(desc_patterns)]
            global_index += 1
            
            loc_title = f"{gu_name} {dong['name']}"
            shop_title_str = t_pattern.format(loc_title=loc_title, shop_name=shop["name"])
            shop_desc_str = d_pattern.format(loc_title=loc_title, shop_name=shop["name"])
            shop_url = f"https://careheals.netlify.app/{sido_path}/{gu_path}/{dong['path']}/{shop['id']}/"
            
            single_shop_html = f"""
            <div class="cm2-shop">
              <div class="cm2-shop-body">
                <div class="cm2-shop-hd"><div class="cm2-shop-name">{shop["tag"]}</div><div class="cm2-shop-rating">★ 4.8 (128건)</div></div>
                <p class="cm2-shop-intro">{shop["desc"]}</p>
                <div class="cm2-shop-ft">
                  <div><span class="cm2-price-label">이용 요금 </span><span class="cm2-price-val">{shop["price"]}</span></div>
                  <a href="tel:{shop["phone"]}" class="cm2-call">📞 {shop["phone"]} 예약 문의</a>
                </div>
              </div>
            </div>
            """
            
            with open(os.path.join(shop_dir, "index.html"), "w", encoding="utf-8") as f:
                f.write(html_template.format(
                    shop_title=shop_title_str, shop_desc=shop_desc_str, shop_url=shop_url,
                    shop_phone=shop["phone"], sido_path=sido_path, sido_name=sido_name,
                    gu_path=gu_path, gu_name=gu_name, current_location=dong['name'],
                    page_heading=shop["name"], dong_badges_html="", content_body=single_shop_html
                ))
            sitemap_urls.append(shop_url)

sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for url in sitemap_urls:
    sitemap_content += f'  <url>\n    <loc>{url}</loc>\n  </url>\n'
sitemap_content += '</urlset>'

with open(os.path.join("public", "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap_content)

print(f"모든 지역(총 {len(sitemap_urls)}개 페이지)과 사이트맵이 public 폴더에 성공적으로 생성되었습니다.")