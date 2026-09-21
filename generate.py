import os
import random

# 서울, 경기, 인천 전체 동이 빠짐없이 포함된 전체 행정구역 데이터
all_regions = [
    # --- 서울특별시 25개 구 전체 ---
    {
        "sido": "seoul", "sido_name": "서울", "path": "jongrogu", "name": "종로구",
        "dongs": [
            {"name": "청운동", "path": "cheongundong"}, {"name": "효자동", "path": "hyojadong"}, {"name": "사직동", "path": "sajikdong"},
            {"name": "삼청동", "path": "samcheongdong"}, {"name": "부암동", "path": "buamdong"}, {"name": "평창동", "path": "pyeongchangdong"},
            {"name": "무악동", "path": "muakdong"}, {"name": "교남동", "path": "gyonamdong"}, {"name": "가회동", "path": "gahoedong"},
            {"name": "종로1.2.3.4가동", "path": "jongro1234gadong"}, {"name": "종로5.6가동", "path": "jongro56gadong"}, {"name": "이화동", "path": "ihwadong"},
            {"name": "혜화동", "path": "hyehwadong"}, {"name": "창신동", "path": "changsindong"}, {"name": "숭인동", "path": "sungindong"}
        ]
    },
    {
        "sido": "seoul", "sido_name": "서울", "path": "junggu", "name": "중구",
        "dongs": [
            {"name": "소공동", "path": "sogongdong"}, {"name": "회현동", "path": "hoehyeondong"}, {"name": "명동", "path": "myeongdong"},
            {"name": "필동", "path": "pildong"}, {"name": "장충동", "path": "jangchungdong"}, {"name": "광희동", "path": "gwanghuidong"},
            {"name": "을지로동", "path": "euljirodong"}, {"name": "신당동", "path": "sindangdong"}, {"name": "다산동", "path": "dasandong"},
            {"name": "약수동", "path": "yaksudong"}, {"name": "청구동", "path": "cheongudong"}, {"name": "동화동", "path": "donghwadong"},
            {"name": "황학동", "path": "hwanghakdong"}, {"name": "중림동", "path": "jungrimdong"}
        ]
    },
    {
        "sido": "seoul", "sido_name": "서울", "path": "yongsangu", "name": "용산구",
        "dongs": [
            {"name": "후암동", "path": "huamdong"}, {"name": "용산2가동", "path": "yongsan2gadong"}, {"name": "남영동", "path": "namyeongdong"},
            {"name": "청파동", "path": "cheongpadong"}, {"name": "원효로1동", "path": "wonhyoro1dong"}, {"name": "원효로2동", "path": "wonhyoro2dong"},
            {"name": "효창동", "path": "hyochangdong"}, {"name": "용문동", "path": "yongmundong"}, {"name": "이촌1동", "path": "ichon1dong"},
            {"name": "이촌2동", "path": "ichon2dong"}, {"name": "이태원1동", "path": "itaewon1dong"}, {"name": "이태원2동", "path": "itaewon2dong"},
            {"name": "한남동", "path": "hannamdong"}, {"name": "서빙고동", "path": "seobinggodong"}, {"name": "보광동", "path": "bogwangdong"}
        ]
    },
    {
        "sido": "seoul", "sido_name": "서울", "path": "seongdonggu", "name": "성동구",
        "dongs": [
            {"name": "왕십리2동", "path": "wangsibri2dong"}, {"name": "왕십리도선동", "path": "wangsibridoseondong"}, {"name": "마장동", "path": "majangdong"},
            {"name": "사근동", "path": "sageundong"}, {"name": "행당1동", "path": "haengdang1dong"}, {"name": "행당2동", "path": "haengdang2dong"},
            {"name": "응봉동", "path": "eungbongdong"}, {"name": "금호1가동", "path": "geumho1gadong"}, {"name": "금호2.3가동", "path": "geumho23gadong"},
            {"name": "금호4가동", "path": "geumho4gadong"}, {"name": "옥수동", "path": "oksudong"}, {"name": "성수1가1동", "path": "seongsu1ga1dong"},
            {"name": "성수1가2동", "path": "seongsu1ga2dong"}, {"name": "성수2가1동", "path": "seongsu2ga1dong"}, {"name": "성수2가3동", "path": "seongsu2ga3동"},
            {"name": "송정동", "path": "songjeongdong"}, {"name": "용답동", "path": "yongdapdong"}
        ]
    },
    {
        "sido": "seoul", "sido_name": "서울", "path": "gwangjingu", "name": "광진구",
        "dongs": [
            {"name": "중곡1동", "path": "junggok1dong"}, {"name": "중곡2동", "path": "junggok2dong"}, {"name": "중곡3동", "path": "junggok3dong"},
            {"name": "중곡4동", "path": "junggok4dong"}, {"name": "능동", "path": "neungdong"}, {"name": "구의1동", "path": "guui1dong"},
            {"name": "구의2동", "path": "guui2dong"}, {"name": "구의3동", "path": "guui3dong"}, {"name": "광장동", "path": "gwangjangdong"},
            {"name": "자양1동", "path": "jayang1dong"}, {"name": "자양2동", "path": "jayang2dong"}, {"name": "자양3동", "path": "jayang3dong"},
            {"name": "자양4동", "path": "jayang4dong"}, {"name": "화양동", "path": "hwayangdong"}, {"name": "군자동", "path": "gunjadong"}
        ]
    },
    {
        "sido": "seoul", "sido_name": "서울", "path": "dongdaemungu", "name": "동대문구",
        "dongs": [
            {"name": "신설동", "path": "sinsuldong"}, {"name": "용두동", "path": "yongdudong"}, {"name": "제기동", "path": "jegidong"},
            {"name": "전농1동", "path": "jeonnong1dong"}, {"name": "전농2동", "path": "jeonnong2dong"}, {"name": "답십리1동", "path": "dapsipri1dong"},
            {"name": "답십리2동", "path": "dapsipri2dong"}, {"name": "장안1동", "path": "jangan1dong"}, {"name": "장안2동", "path": "jangan2dong"},
            {"name": "청량리동", "path": "cheongryangridong"}, {"name": "회기동", "path": "hoegidong"}, {"name": "휘경1동", "path": "hwigyeong1dong"},
            {"name": "휘경2동", "path": "hwigyeong2dong"}, {"name": "이문1동", "path": "imun1dong"}, {"name": "이문2동", "path": "imun2dong"}
        ]
    },
    {
        "sido": "seoul", "sido_name": "서울", "path": "jungnanggu", "name": "중랑구",
        "dongs": [
            {"name": "면목본동", "path": "myeonmokbondong"}, {"name": "면목2동", "path": "myeonmok2dong"}, {"name": "면목3.4동", "path": "myeonmok34dong"},
            {"name": "면목5동", "path": "myeonmok5dong"}, {"name": "면목7동", "path": "myeonmok7dong"}, {"name": "상봉1동", "path": "sangbong1dong"},
            {"name": "상봉2동", "path": "sangbong2dong"}, {"name": "중화1동", "path": "junghwa1dong"}, {"name": "중화2동", "path": "junghwa2dong"},
            {"name": "묵1동", "path": "muk1dong"}, {"name": "묵2동", "path": "muk2dong"}, {"name": "망우본동", "path": "mangwobondong"},
            {"name": "망우3동", "path": "mangwu3dong"}, {"name": "신내1동", "path": "sinnae1dong"}, {"name": "신내2동", "path": "sinnae2dong"}
        ]
    },
    {
        "sido": "seoul", "sido_name": "서울", "path": "seongbukgu", "name": "성북구",
        "dongs": [
            {"name": "성북동", "path": "seongbukdong"}, {"name": "삼선동", "path": "samseondong"}, {"name": "동선동", "path": "dongseondong"},
            {"name": "돈암1동", "path": "donam1dong"}, {"name": "돈암2동", "path": "donam2dong"}, {"name": "안암동", "path": "anamdong"},
            {"name": "보문동", "path": "bomundong"}, {"name": "정릉1동", "path": "jeongreung1dong"}, {"name": "정릉2동", "path": "jeongreung2dong"},
            {"name": "정릉3동", "path": "jeongreung3동"}, {"name": "정릉4동", "path": "jeongreung4dong"}, {"name": "길음1동", "path": "gileum1dong"},
            {"name": "길음2동", "path": "gileum2dong"}, {"name": "종암동", "path": "jongamdong"}, {"name": "월곡1동", "path": "wolgok1dong"},
            {"name": "월곡2동", "path": "wolgok2dong"}, {"name": "장위1동", "path": "jangwi1dong"}, {"name": "장위2동", "path": "jangwi2dong"},
            {"name": "장위3동", "path": "jangwi3dong"}, {"name": "석관동", "path": "seokgwandong"}
        ]
    },
    {
        "sido": "seoul", "sido_name": "서울", "path": "gangbukgu", "name": "강북구",
        "dongs": [
            {"name": "삼양동", "path": "samyangdong"}, {"name": "미아동", "path": "miadong"}, {"name": "송중동", "path": "songjungdong"},
            {"name": "송천동", "path": "songcheondong"}, {"name": "삼각산동", "path": "samgaksandong"}, {"name": "번1동", "path": "beon1dong"},
            {"name": "번2동", "path": "beon2dong"}, {"name": "번3동", "path": "beon3dong"}, {"name": "수유1동", "path": "suyu1dong"},
            {"name": "수유2동", "path": "suyu2dong"}, {"name": "수유3동", "path": "suyu3dong"}, {"name": "우이동", "path": "uidong"},
            {"name": "인수동", "path": "insudong"}
        ]
    },
    {
        "sido": "seoul", "sido_name": "서울", "path": "dobonggu", "name": "도봉구",
        "dongs": [
            {"name": "창1동", "path": "chang1dong"}, {"name": "창2동", "path": "chang2dong"}, {"name": "창3동", "path": "chang3dong"},
            {"name": "창4동", "path": "chang4dong"}, {"name": "창5동", "path": "chang5dong"}, {"name": "도봉1동", "path": "dobong1dong"},
            {"name": "도봉2동", "path": "dobong2dong"}, {"name": "쌍문1동", "path": "ssangmun1dong"}, {"name": "쌍문2동", "path": "ssangmun2dong"},
            {"name": "쌍문3동", "path": "ssangmun3dong"}, {"name": "쌍문4동", "path": "ssangmun4dong"}, {"name": "방학1동", "path": "banghak1dong"},
            {"name": "방학2동", "path": "banghak2dong"}, {"name": "방학3동", "path": "banghak3dong"}
        ]
    },
    {
        "sido": "seoul", "sido_name": "서울", "path": "nowongu", "name": "노원구",
        "dongs": [
            {"name": "상계1동", "path": "sanggye1dong"}, {"name": "상계2동", "path": "sanggye2dong"}, {"name": "상계3.4동", "path": "sanggye34dong"},
            {"name": "상계5동", "path": "sanggye5dong"}, {"name": "상계6.7동", "path": "sanggye67dong"}, {"name": "상계8동", "path": "sanggye8dong"},
            {"name": "상계9동", "path": "sanggye9dong"}, {"name": "상계10동", "path": "sanggye10dong"}, {"name": "중계본동", "path": "junggyebondong"},
            {"name": "중계1동", "path": "junggye1dong"}, {"name": "중계2.3동", "path": "junggye23dong"}, {"name": "중계4동", "path": "junggye4dong"},
            {"name": "하계1동", "path": "hagye1dong"}, {"name": "하계2동", "path": "hagye2dong"}, {"name": "공릉1동", "path": "gongreung1dong"},
            {"name": "공릉2동", "path": "gongreung2dong"}
        ]
    },
    {
        "sido": "seoul", "sido_name": "서울", "path": "eunpyeonggu", "name": "은평구",
        "dongs": [
            {"name": "불광1동", "path": "bulgwang1dong"}, {"name": "불광2동", "path": "bulgwang2dong"}, {"name": "갈현1동", "path": "galhyeon1dong"},
            {"name": "갈현2동", "path": "galhyeon2dong"}, {"name": "구산동", "path": "gusandong"}, {"name": "대조동", "path": "daejodong"},
            {"name": "응암1동", "path": "eungam1dong"}, {"name": "응암2동", "path": "eungam2dong"}, {"name": "응암3동", "path": "eungam3dong"},
            {"name": "역촌동", "path": "yeokchondong"}, {"name": "신사1동", "path": "sinsa1dong"}, {"name": "신사2동", "path": "sinsa2dong"},
            {"name": "증산동", "path": "jeungsandong"}, {"name": "수색동", "path": "susaekdong"}, {"name": "진관동", "path": "jingwandong"}
        ]
    },
    {
        "sido": "seoul", "sido_name": "서울", "path": "seodaemungu", "name": "서대문구",
        "dongs": [
            {"name": "천연동", "path": "cheonyeondong"}, {"name": "북아현동", "path": "bukahyeondong"}, {"name": "충현동", "path": "chunghyeondong"},
            {"name": "신촌동", "path": "sinchondong"}, {"name": "연희동", "path": "yeonhuidong"}, {"name": "홍제1동", "path": "hongje1dong"},
            {"name": "홍제2동", "path": "hongje2dong"}, {"name": "홍제3동", "path": "hongje3dong"}, {"name": "홍은1동", "path": "hongeun1dong"},
            {"name": "홍은2동", "path": "hongeun2dong"}, {"name": "남가좌1동", "path": "namgajwa1dong"}, {"name": "남가좌2동", "path": "namgajwa2dong"},
            {"name": "북가좌1동", "path": "bukgajwa1dong"}, {"name": "북가좌2동", "path": "bukgajwa2dong"}
        ]
    },
    {
        "sido": "seoul", "sido_name": "서울", "path": "mapogu", "name": "마포구",
        "dongs": [
            {"name": "공덕동", "path": "gongdeokdong"}, {"name": "아현동", "path": "ahyeondong"}, {"name": "도화동", "path": "dohwadong"},
            {"name": "용강동", "path": "yonggangdong"}, {"name": "대흥동", "path": "daeheungdong"}, {"name": "염리동", "path": "yeomridong"},
            {"name": "신수동", "path": "sinsudong"}, {"name": "서교동", "path": "seogyodong"}, {"name": "합정동", "path": "hapjeongdong"},
            {"name": "망원1동", "path": "mangwon1dong"}, {"name": "망원2동", "path": "mangwon2dong"}, {"name": "연남동", "path": "yeonnamdong"},
            {"name": "성산1동", "path": "seongsan1dong"}, {"name": "성산2동", "path": "seongsan2dong"}, {"name": "상암동", "path": "sangamdong"}
        ]
    },
    {
        "sido": "seoul", "sido_name": "서울", "path": "yangcheongu", "name": "양천구",
        "dongs": [
            {"name": "목1동", "path": "mok1dong"}, {"name": "목2동", "path": "mok2dong"}, {"name": "목3동", "path": "mok3dong"},
            {"name": "목4동", "path": "mok4dong"}, {"name": "목5동", "path": "mok5dong"}, {"name": "신월1동", "path": "sinwol1dong"},
            {"name": "신월2동", "path": "sinwol2dong"}, {"name": "신월3동", "path": "sinwol3dong"}, {"name": "신월4동", "path": "sinwol4dong"},
            {"name": "신월5동", "path": "sinwol5dong"}, {"name": "신월6동", "path": "sinwol6dong"}, {"name": "신월7동", "path": "sinwol7dong"},
            {"name": "신정1동", "path": "sinjeong1dong"}, {"name": "신정2동", "path": "sinjeong2dong"}, {"name": "신정3동", "path": "sinjeong3dong"},
            {"name": "신정4동", "path": "sinjeong4dong"}, {"name": "신정6동", "path": "sinjeong6dong"}, {"name": "신정7동", "path": "sinjeong7dong"}
        ]
    },
    {
        "sido": "seoul", "sido_name": "서울", "path": "gangseogu", "name": "강서구",
        "dongs": [
            {"name": "등촌1동", "path": "deungchon1dong"}, {"name": "등촌2동", "path": "deungchon2dong"}, {"name": "등촌3동", "path": "deungchon3dong"},
            {"name": "화곡본동", "path": "hwagokbondong"}, {"name": "화곡1동", "path": "hwagok1dong"}, {"name": "화곡2동", "path": "hwagok2dong"},
            {"name": "화곡3동", "path": "hwagok3dong"}, {"name": "화곡4동", "path": "hwagok4dong"}, {"name": "화곡6동", "path": "hwagok6dong"},
            {"name": "화곡8동", "path": "hwagok8dong"}, {"name": "우장산동", "path": "ujangsandong"}, {"name": "가양1동", "path": "gayang1dong"},
            {"name": "가양2동", "path": "gayang2dong"}, {"name": "가양3동", "path": "gayang3dong"}, {"name": "발산1동", "path": "balsan1dong"},
            {"name": "공항동", "path": "gonghangdong"}, {"name": "방화1동", "path": "banghwa1dong"}, {"name": "방화2동", "path": "banghwa2dong"},
            {"name": "방화3동", "path": "banghwa3dong"}
        ]
    },
    {
        "sido": "seoul", "sido_name": "서울", "path": "gurogu", "name": "구로구",
        "dongs": [
            {"name": "신도림동", "path": "sindorimdong"}, {"name": "구로1동", "path": "guro1dong"}, {"name": "구로2동", "path": "guro2dong"},
            {"name": "구로3동", "path": "guro3dong"}, {"name": "구로4동", "path": "guro4dong"}, {"name": "구로5동", "path": "guro5dong"},
            {"name": "가리봉동", "path": "garibongdong"}, {"name": "고척1동", "path": "gocheok1dong"}, {"name": "고척2동", "path": "gocheok2dong"},
            {"name": "개봉1동", "path": "gaebong1dong"}, {"name": "개봉2동", "path": "gaebong2dong"}, {"name": "개봉3동", "path": "gaebong3dong"},
            {"name": "오류1동", "path": "oryu1dong"}, {"name": "오류2동", "path": "oryu2dong"}, {"name": "수궁동", "path": "sugungdong"}
        ]
    },
    {
        "sido": "seoul", "sido_name": "서울", "path": "geumcheongu", "name": "금천구",
        "dongs": [
            {"name": "가산동", "path": "gasandong"}, {"name": "독산1동", "path": "doksan1dong"}, {"name": "독산2동", "path": "doksan2dong"},
            {"name": "독산3동", "path": "doksan3dong"}, {"name": "독산4동", "path": "doksan4dong"}, {"name": "시흥1동", "path": "siheung1dong"},
            {"name": "시흥2동", "path": "siheung2dong"}, {"name": "시흥3동", "path": "siheung3dong"}, {"name": "시흥4동", "path": "siheung4dong"},
            {"name": "시흥5동", "path": "siheung5dong"}
        ]
    },
    {
        "sido": "seoul", "sido_name": "서울", "path": "yeongdeungpogu", "name": "영등포구",
        "dongs": [
            {"name": "영등포본동", "path": "yeongdeungpobondong"}, {"name": "영등포동", "path": "yeongdeungpodong"}, {"name": "여의동", "path": "yeouidong"},
            {"name": "당산1동", "path": "dangsan1dong"}, {"name": "당산2동", "path": "dangsan2dong"}, {"name": "도림동", "path": "dorimdong"},
            {"name": "문래동", "path": "munraedong"}, {"name": "양평1동", "path": "yangpyeong1dong"}, {"name": "양평2동", "path": "yangpyeong2dong"},
            {"name": "신길1동", "path": "singil1dong"}, {"name": "신길3동", "path": "singil3dong"}, {"name": "신길4동", "path": "singil4dong"},
            {"name": "신길5동", "path": "singil5dong"}, {"name": "신길6동", "path": "singil6dong"}, {"name": "신길7동", "path": "singil7dong"},
            {"name": "대림1동", "path": "daerim1dong"}, {"name": "대림2동", "path": "daerim2dong"}, {"name": "대림3동", "path": "daerim3dong"}
        ]
    },
    {
        "sido": "seoul", "sido_name": "서울", "path": "dongjakgu", "name": "동작구",
        "dongs": [
            {"name": "노량진1동", "path": "noryangjin1dong"}, {"name": "노량진2동", "path": "noryangjin2dong"}, {"name": "상도1동", "path": "sangdo1dong"},
            {"name": "상도2동", "path": "sangdo2dong"}, {"name": "상도3동", "path": "sangdo3동"}, {"name": "상도4동", "path": "sangdo4동"},
            {"name": "흑석동", "path": "heukseokdong"}, {"name": "사당1동", "path": "sadang1dong"}, {"name": "사당2동", "path": "sadang2dong"},
            {"name": "사당3동", "path": "sadang3dong"}, {"name": "사당4동", "path": "sadang4dong"}, {"name": "사당5동", "path": "sadang5dong"},
            {"name": "대방동", "path": "daebangdong"}, {"name": "신대방1동", "path": "sindaebang1dong"}, {"name": "신대방2동", "path": "sindaebang2dong"}
        ]
    },
    {
        "sido": "seoul", "sido_name": "서울", "path": "gwanakgu", "name": "관악구",
        "dongs": [
            {"name": "보라매동", "path": "boramaedong"}, {"name": "청림동", "path": "cheongrimdong"}, {"name": "성현동", "path": "seonghyeondong"},
            {"name": "행운동", "path": "haengundong"}, {"name": "낙성대동", "path": "nakseongdaedong"}, {"name": "청룡동", "path": "cheongyongdong"},
            {"name": "은천동", "path": "euncheondong"}, {"name": "상현동", "path": "sanghyeondong"}, {"name": "서원동", "path": "seowondong"},
            {"name": "신원동", "path": "sinwondong"}, {"name": "서림동", "path": "seorimdong"}, {"name": "신사동", "path": "sinsadong"},
            {"name": "난향동", "path": "nanhyangdong"}, {"name": "조원동", "path": "jowondong"}, {"name": "대학동", "path": "daehakdong"},
            {"name": "난곡동", "path": "nangokdong"}, {"name": "삼성동", "path": "samsungdong"}, {"name": "미성동", "path": "misongdong"}
        ]
    },
    {
        "sido": "seoul", "sido_name": "서울", "path": "seochogu", "name": "서초구",
        "dongs": [
            {"name": "서초1동", "path": "seocho1dong"}, {"name": "서초2동", "path": "seocho2dong"}, {"name": "서초3동", "path": "seocho3dong"},
            {"name": "서초4동", "path": "seocho4dong"}, {"name": "잠원동", "path": "jamwondong"}, {"name": "반포본동", "path": "banpobondong"},
            {"name": "반포1동", "path": "banpo1dong"}, {"name": "반포2동", "path": "banpo2dong"}, {"name": "반포3동", "path": "banpo3dong"},
            {"name": "반포4동", "path": "banpo4dong"}, {"name": "방배본동", "path": "bangbaebondong"}, {"name": "방배1동", "path": "bangbae1dong"},
            {"name": "방배2동", "path": "bangbae2dong"}, {"name": "방배3동", "path": "bangbae3dong"}, {"name": "방배4동", "path": "bangbae4dong"},
            {"name": "양재1동", "path": "yangjae1dong"}, {"name": "양재2동", "path": "yangjae2dong"}, {"name": "내곡동", "path": "naegokdong"}
        ]
    },
    {
        "sido": "seoul", "sido_name": "서울", "path": "gangnamgu", "name": "강남구",
        "dongs": [
            {"name": "역삼1동", "path": "yeoksam1dong"}, {"name": "역삼2동", "path": "yeoksam2dong"}, {"name": "개포1동", "path": "gaepo1dong"},
            {"name": "개포2동", "path": "gaepo2dong"}, {"name": "개포4동", "path": "gaepo4dong"}, {"name": "청담동", "path": "cheongdamdong"},
            {"name": "삼성1동", "path": "samsung1dong"}, {"name": "삼성2동", "path": "samsung2dong"}, {"name": "대치1동", "path": "daechi1dong"},
            {"name": "대치2동", "path": "daechi2dong"}, {"name": "대치4동", "path": "daechi4dong"}, {"name": "신사동", "path": "sinsadong"},
            {"name": "논현1동", "path": "nonhyeon1dong"}, {"name": "논현2동", "path": "nonhyeon2dong"}, {"name": "압구정동", "path": "apgujeongdong"},
            {"name": "세곡동", "path": "segokdong"}, {"name": "자곡동", "path": "jagokdong"}, {"name": "일원동", "path": "ilwondong"},
            {"name": "수서동", "path": "suseodong"}, {"name": "도곡1동", "path": "dogok1dong"}, {"name": "도곡2동", "path": "dogok2dong"}
        ]
    },
    {
        "sido": "seoul", "sido_name": "서울", "path": "songpagu", "name": "송파구",
        "dongs": [
            {"name": "잠실본동", "path": "jamsilbondong"}, {"name": "잠실2동", "path": "jamsil2dong"}, {"name": "잠실3동", "path": "jamsil3동"},
            {"name": "잠실4동", "path": "jamsil4dong"}, {"name": "잠실6동", "path": "jamsil6dong"}, {"name": "잠실7동", "path": "jamsil7dong"},
            {"name": "풍납1동", "path": "pungnap1dong"}, {"name": "풍납2동", "path": "pungnap2dong"}, {"name": "거여1동", "path": "geoyeo1dong"},
            {"name": "거여2동", "path": "geoyeo2dong"}, {"name": "마천1동", "path": "macheon1dong"}, {"name": "마천2동", "path": "macheon2dong"},
            {"name": "방이1동", "path": "bangi1dong"}, {"name": "방이2동", "path": "bangi2dong"}, {"name": "오륜동", "path": "oryundong"},
            {"name": "오금동", "path": "ogeumdong"}, {"name": "송파1동", "path": "songpa1dong"}, {"name": "송파2동", "path": "songpa2dong"},
            {"name": "석촌동", "path": "seokchondong"}, {"name": "삼전동", "path": "samjeondong"}, {"name": "가락본동", "path": "garakbondong"},
            {"name": "가락1동", "path": "garak1dong"}, {"name": "가락2동", "path": "garak2dong"}, {"name": "문정1동", "path": "munjeong1dong"},
            {"name": "문정2동", "path": "munjeong2dong"}, {"name": "장지동", "path": "jangjidong"}, {"name": "위례동", "path": "wiryedong"},
            {"name": "잠실동", "path": "jamsildong"}
        ]
    },
    {
        "sido": "seoul", "sido_name": "서울", "path": "gangdonggu", "name": "강동구",
        "dongs": [
            {"name": "강일동", "path": "gangildong"}, {"name": "상일1동", "path": "sangil1dong"}, {"name": "상일2동", "path": "sangil2dong"},
            {"name": "명일1동", "path": "myeongil1dong"}, {"name": "명일2동", "path": "myeongil2dong"}, {"name": "고덕1동", "path": "godeok1dong"},
            {"name": "고덕2동", "path": "godeok2dong"}, {"name": "암사1동", "path": "amsa1dong"}, {"name": "암사2동", "path": "amsa2동"},
            {"name": "암사3동", "path": "amsa3dong"}, {"name": "천호1동", "path": "cheonho1dong"}, {"name": "천호2동", "path": "cheonho2dong"},
            {"name": "천호3동", "path": "cheonho3dong"}, {"name": "성내1동", "path": "seongnae1dong"}, {"name": "성내2동", "path": "seongnae2dong"},
            {"name": "성내3동", "path": "seongnae3동"}, {"name": "둔촌1동", "path": "dunchon1dong"}, {"name": "둔촌2동", "path": "dunchon2dong"}
        ]
    },

    # --- 경기도 전체 시·군·구 ---
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "suwon_jangan", "name": "수원시 장안구",
        "dongs": [
            {"name": "파장동", "path": "pajangdong"}, {"name": "정자1동", "path": "jeongja1dong"}, {"name": "정자2동", "path": "jeongja2dong"},
            {"name": "정자3동", "path": "jeongja3dong"}, {"name": "영화동", "path": "yeonghwadong"}, {"name": "송죽동", "path": "songjukdong"},
            {"name": "조원1동", "path": "jowon1dong"}, {"name": "조원2동", "path": "jowon2dong"}, {"name": "율천동", "path": "yulcheondong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "suwon_gwonseon", "name": "수원시 권선구",
        "dongs": [
            {"name": "세류1동", "path": "seryu1dong"}, {"name": "세류2동", "path": "seryu2dong"}, {"name": "세류3동", "path": "seryu3dong"},
            {"name": "권선1동", "path": "gwonseon1dong"}, {"name": "권선2동", "path": "gwonseon2dong"}, {"name": "곡선동", "path": "gokseondong"},
            {"name": "평동", "path": "pyeongdong"}, {"name": "호매실동", "path": "homaesildong"}, {"name": "서둔동", "path": "seodundong"},
            {"name": "금곡동", "path": "geumgokdong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "suwon_paldal", "name": "수원시 팔달구",
        "dongs": [
            {"name": "매교동", "path": "maegyodong"}, {"name": "매산동", "path": "maesandong"}, {"name": "고등동", "path": "godeungdong"},
            {"name": "화서1동", "path": "hwaseo1dong"}, {"name": "화서2동", "path": "hwaseo2dong"}, {"name": "지동", "path": "jidong"},
            {"name": "우만1동", "path": "uman1dong"}, {"name": "우만2동", "path": "uman2dong"}, {"name": "인계동", "path": "ingyedong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "suwon_yeongtong", "name": "수원시 영통구",
        "dongs": [
            {"name": "매탄1동", "path": "maetan1dong"}, {"name": "매탄2동", "path": "maetan2dong"}, {"name": "매탄3동", "path": "maetan3동"},
            {"name": "매탄4동", "path": "maetan4dong"}, {"name": "원천동", "path": "woncheondong"}, {"name": "영통1동", "path": "yeongtong1dong"},
            {"name": "영통2동", "path": "yeongtong2dong"}, {"name": "영통3동", "path": "yeongtong3동"}, {"name": "망포1동", "path": "mangpo1dong"},
            {"name": "망포2동", "path": "mangpo2dong"}, {"name": "광교1동", "path": "gwanggyo1dong"}, {"name": "광교2동", "path": "gwanggyo2dong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "seongnam_sujeong", "name": "성남시 수정구",
        "dongs": [
            {"name": "신흥1동", "path": "sinheung1dong"}, {"name": "신흥2동", "path": "sinheung2dong"}, {"name": "신흥3동", "path": "sinheung3dong"},
            {"name": "태평1동", "path": "taepyeong1dong"}, {"name": "태평2동", "path": "taepyeong2dong"}, {"name": "태평3동", "path": "taepyeong3동"},
            {"name": "태평4동", "path": "taepyeong4동"}, {"name": "수진1동", "path": "sujin1dong"}, {"name": "수진2동", "path": "sujin2dong"},
            {"name": "단대동", "path": "dandaedong"}, {"name": "산성동", "path": "sanseongdong"}, {"name": "양지동", "path": "yangjidong"},
            {"name": "복정동", "path": "bokjeongdong"}, {"name": "위례동", "path": "wiryedong"}, {"name": "신촌동", "path": "sinchondong"},
            {"name": "고등동", "path": "godeungdong"}, {"name": "창곡동", "path": "changgokdong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "seongnam_jungwon", "name": "성남시 중원구",
        "dongs": [
            {"name": "성남동", "path": "seongnamdong"}, {"name": "중앙동", "path": "jungangdong"}, {"name": "금광1동", "path": "geumgwang1dong"},
            {"name": "금광2동", "path": "geumgwang2dong"}, {"name": "은행1동", "path": "eunhaeng1dong"}, {"name": "은행2동", "path": "eunhaeng2dong"},
            {"name": "상대원1동", "path": "sangdaewon1dong"}, {"name": "상대원2동", "path": "sangdaewon2dong"}, {"name": "상대원3동", "path": "sangdaewon3동"},
            {"name": "하대원동", "path": "hadaewondong"}, {"name": "도촌동", "path": "dochondong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "seongnam_bundang", "name": "성남시 분당구",
        "dongs": [
            {"name": "분당동", "path": "bundangdong"}, {"name": "수내1동", "path": "sunae1dong"}, {"name": "수내2동", "path": "sunae2dong"},
            {"name": "수내3동", "path": "sunae3동"}, {"name": "정자동", "path": "jeongjadong"}, {"name": "정자1동", "path": "jeongja1dong"},
            {"name": "정자2동", "path": "jeongja2dong"}, {"name": "정자3동", "path": "jeongja3dong"}, {"name": "서현1동", "path": "seohyeon1dong"},
            {"name": "서현2동", "path": "seohyeon2dong"}, {"name": "이매1동", "path": "imae1dong"}, {"name": "이매2동", "path": "imae2dong"},
            {"name": "야탑1동", "path": "yatap1dong"}, {"name": "야탑2동", "path": "yatap2dong"}, {"name": "야탑3동", "path": "yatap3dong"},
            {"name": "금곡동", "path": "geumgokdong"}, {"name": "미금동", "path": "migumdong"}, {"name": "구미동", "path": "gumidong"},
            {"name": "판교동", "path": "pangyodong"}, {"name": "삼평동", "path": "sampyeongdong"}, {"name": "백현동", "path": "baekhyeondong"},
            {"name": "운중동", "path": "unjungdong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "goyang_deogyang", "name": "고양시 덕양구",
        "dongs": [
            {"name": "원신동", "path": "wonsindong"}, {"name": "흥도동", "path": "heungdodong"}, {"name": "효자동", "path": "hyojadong"},
            {"name": "창릉동", "path": "changneungdong"}, {"name": "능곡동", "path": "neunggokdong"}, {"name": "행신1동", "path": "haengsin1dong"},
            {"name": "행신2동", "path": "haengsin2dong"}, {"name": "행신3동", "path": "haengsin3dong"}, {"name": "화정1동", "path": "hwajeong1dong"},
            {"name": "화정2동", "path": "hwajeong2dong"}, {"name": "대덕동", "path": "daedeokdong"}, {"name": "고양동", "path": "goyangdong"},
            {"name": "관산동", "path": "gwansandong"}, {"name": "성사동", "path": "seongsadong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "goyang_ilsandong", "name": "고양시 일산동구",
        "dongs": [
            {"name": "식사동", "path": "siksadong"}, {"name": "중산1동", "path": "jungsan1dong"}, {"name": "중산2동", "path": "jungsan2dong"},
            {"name": "정발산동", "path": "jeongbalsandong"}, {"name": "풍산동", "path": "pungsandong"}, {"name": "백석1동", "path": "baekseok1dong"},
            {"name": "백석2동", "path": "baekseok2dong"}, {"name": "마두1동", "path": "madu1dong"}, {"name": "마두2동", "path": "madu2dong"},
            {"name": "장항1동", "path": "janghang1dong"}, {"name": "장항2동", "path": "janghang2dong"}, {"name": "고봉동", "path": "gobongdong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "goyang_ilsanseo", "name": "고양시 일산서구",
        "dongs": [
            {"name": "일산1동", "path": "ilsan1dong"}, {"name": "일산2동", "path": "ilsan2dong"}, {"name": "일산3동", "path": "ilsan3동"},
            {"name": "탄현1동", "path": "tanhyeon1dong"}, {"name": "탄현2동", "path": "tanhyeon2동"}, {"name": "주엽1동", "path": "juyeop1dong"},
            {"name": "주엽2동", "path": "juyeop2dong"}, {"name": "대화동", "path": "daehwadong"}, {"name": "송포동", "path": "songpodong"},
            {"name": "덕이동", "path": "deogidong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "yongin_cheoin", "name": "용인시 처인구",
        "dongs": [
            {"name": "포곡읍", "path": "pogokeup"}, {"name": "모현읍", "path": "mohyeoneup"}, {"name": "남사읍", "path": "namsaeup"},
            {"name": "원삼면", "path": "wonsanmyeon"}, {"name": "백암면", "path": "baegammyeon"}, {"name": "동부동", "path": "dongbudong"},
            {"name": "중앙동", "path": "jungangdong"}, {"name": "역삼동", "path": "yeoksamdong"}, {"name": "유림동", "path": "yurimdong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "yongin_giheung", "name": "용인시 기흥구",
        "dongs": [
            {"name": "신갈동", "path": "singaldong"}, {"name": "마북동", "path": "mabukdong"}, {"name": "구성동", "path": "guuseongdong"},
            {"name": "동백동", "path": "dongbaekdong"}, {"name": "보정동", "path": "bojeongdong"}, {"name": "상갈동", "path": "sanggaldong"},
            {"name": "기흥동", "path": "giheungdong"}, {"name": "서농동", "path": "seonongdong"}, {"name": "중동", "path": "jungdong"},
            {"name": "상하동", "path": "sanghadong"}, {"name": "보라동", "path": "boradong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "yongin_suji", "name": "용인시 수지구",
        "dongs": [
            {"name": "풍덕천1동", "path": "pungdeokcheon1dong"}, {"name": "풍덕천2동", "path": "pungdeokcheon2dong"}, {"name": "신봉동", "path": "sinbongdong"},
            {"name": "죽전1동", "path": "jukjeon1dong"}, {"name": "죽전2동", "path": "jukjeon2dong"}, {"name": "동천동", "path": "dongcheondong"},
            {"name": "상현1동", "path": "sanghyeon1dong"}, {"name": "상현2동", "path": "sanghyeon2dong"}, {"name": "성복동", "path": "seongbokdong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "bucheon_wonmi", "name": "부천시 원미구",
        "dongs": [
            {"name": "심곡동", "path": "simgokdong"}, {"name": "원미동", "path": "wonmidong"}, {"name": "소사동", "path": "sosadong"},
            {"name": "역곡동", "path": "yeokgokdong"}, {"name": "중동", "path": "jungdong"}, {"name": "상동", "path": "sangdong"},
            {"name": "약대동", "path": "yakdaedong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "bucheon_sosa", "name": "부천시 소사구",
        "dongs": [
            {"name": "소사본동", "path": "sosabondong"}, {"name": "범박동", "path": "beombakdong"}, {"name": "옥길동", "path": "okgildong"},
            {"name": "괴안동", "path": "goeandong"}, {"name": "송내동", "path": "songnaedong"}, {"name": "춘의동", "path": "chunuidong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "bucheon_ojeong", "name": "부천시 오정구",
        "dongs": [
            {"name": "오정동", "path": "ojeongdong"}, {"name": "고강동", "path": "gogangdong"}, {"name": "원종동", "path": "wonjongdong"},
            {"name": "성곡동", "path": "seonggokdong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "ansan_sangnok", "name": "안산시 상록구",
        "dongs": [
            {"name": "반월동", "path": "banwoldong"}, {"name": "사동", "path": "sadong"}, {"name": "일동", "path": "ildong"},
            {"name": "이동", "path": "idong"}, {"name": "본오동", "path": "bonodong"}, {"name": "수암동", "path": "suamdong"},
            {"name": "장상동", "path": "jangsangdong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "ansan_danwon", "name": "안산시 단원구",
        "dongs": [
            {"name": "와동", "path": "wadong"}, {"name": "고잔동", "path": "gozandong"}, {"name": "초지동", "path": "chojidong"},
            {"name": "원곡동", "path": "wongokdong"}, {"name": "백운동", "path": "baekundong"}, {"name": "신길동", "path": "singildong"},
            {"name": "성곡동", "path": "seonggokdong"}, {"name": "대부동", "path": "daebudong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "anyang_manan", "name": "안양시 만안구",
        "dongs": [
            {"name": "안양1동", "path": "anyang1dong"}, {"name": "안양2동", "path": "anyang2dong"}, {"name": "안양3동", "path": "anyang3dong"},
            {"name": "안양4동", "path": "anyang4dong"}, {"name": "안양5동", "path": "anyang5dong"}, {"name": "안양6동", "path": "anyang6dong"},
            {"name": "안양7동", "path": "anyang7dong"}, {"name": "안양8동", "path": "anyang8dong"}, {"name": "안양9동", "path": "anyang9dong"},
            {"name": "석수동", "path": "seoksudong"}, {"name": "박달동", "path": "bakdaldong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "anyang_dongan", "name": "안양시 동안구",
        "dongs": [
            {"name": "비산동", "path": "bisandong"}, {"name": "부흥동", "path": "buheungdong"}, {"name": "달안동", "path": "dalandong"},
            {"name": "관양동", "path": "gwanyangdong"}, {"name": "평촌동", "path": "pyeongchondong"}, {"name": "평안동", "path": "pyeongandong"},
            {"name": "귀인동", "path": "gwiindong"}, {"name": "범계동", "path": "beomgyedong"}, {"name": "호계동", "path": "hogyedong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "uijeongbusi", "name": "의정부시",
        "dongs": [
            {"name": "의정부동", "path": "uijeongbudong"}, {"name": "호원동", "path": "howondong"}, {"name": "장암동", "path": "jangamdong"},
            {"name": "신곡동", "path": "singokdong"}, {"name": "송산동", "path": "songsandong"}, {"name": "가능동", "path": "ganeungdong"},
            {"name": "흥선동", "path": "heungseondong"}, {"name": "자금동", "path": "jageumdong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "gwangmyeongsi", "name": "광명시",
        "dongs": [
            {"name": "광명동", "path": "gwangmyeongdong"}, {"name": "철산동", "path": "cheolsandong"}, {"name": "하안동", "path": "haandong"},
            {"name": "소하동", "path": "sohadong"}, {"name": "학온동", "path": "hakondong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "pyeongtaeksi", "name": "평택시",
        "dongs": [
            {"name": "진위면", "path": "jinwimyeon"}, {"name": "서탄면", "path": "seotanmyeon"}, {"name": "고덕면", "path": "godeokmyeon"},
            {"name": "청북읍", "path": "cheongbukeup"}, {"name": "포승읍", "path": "poseongeup"}, {"name": "현덕면", "path": "hyeondeokmyeon"},
            {"name": "팽성읍", "path": "paengseongeup"}, {"name": "신장동", "path": "sinjangdong"}, {"name": "서정동", "path": "seojeongdong"},
            {"name": "송탄동", "path": "songtandong"}, {"name": "지산동", "path": "jisandong"}, {"name": "원평동", "path": "wonpyeongdong"},
            {"name": "비전동", "path": "bijeondong"}, {"name": "소사동", "path": "sosadong"}, {"name": "세교동", "path": "segyodong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "dongducheonsi", "name": "동두천시",
        "dongs": [
            {"name": "생연동", "path": "saengyeondong"}, {"name": "보산동", "path": "bosandong"}, {"name": "동두천동", "path": "dongducheondong"},
            {"name": "상패동", "path": "sangpaedong"}, {"name": "중앙동", "path": "jungangdong"}, {"name": "송내동", "path": "songnaedong"},
            {"name": "불현동", "path": "bulhyeondong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "gurisi", "name": "구리시",
        "dongs": [
            {"name": "갈매동", "path": "galmaedong"}, {"name": "동구동", "path": "donggudong"}, {"name": "인창동", "path": "inchangdong"},
            {"name": "교문1동", "path": "gyomun1dong"}, {"name": "교문2동", "path": "gyomun2dong"}, {"name": "토평동", "path": "topyeongdong"},
            {"name": "수택1동", "path": "sutaek1dong"}, {"name": "수택2동", "path": "sutaek2dong"}, {"name": "수택3동", "path": "sutaek3dong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "namyangjusi", "name": "남양주시",
        "dongs": [
            {"name": "와부읍", "path": "wabueup"}, {"name": "진접읍", "path": "jinjeopeup"}, {"name": "화도읍", "path": "hwadoeup"},
            {"name": "수동면", "path": "sudongmyeon"}, {"name": "조안면", "path": "joanmyeon"}, {"name": "퇴계원읍", "path": "toegyewoneup"},
            {"name": "별내면", "path": "byeollaemyeon"}, {"name": "별내동", "path": "byeolnaedong"}, {"name": "금곡동", "path": "geumgokdong"},
            {"name": "양정동", "path": "yangjeongdong"}, {"name": "다산동", "path": "dasandong"}, {"name": "평내동", "path": "pyeongnaedong"},
            {"name": "호평동", "path": "hopyeongdong"}, {"name": "오남읍", "path": "onameup"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "osansi", "name": "오산시",
        "dongs": [
            {"name": "중앙동", "path": "jungangdong"}, {"name": "신장동", "path": "sinjangdong"}, {"name": "세마동", "path": "semadong"},
            {"name": "초평동", "path": "chopyeongdong"}, {"name": "대원동", "path": "daewondong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "siheungsi", "name": "시흥시",
        "dongs": [
            {"name": "대야동", "path": "daeyadong"}, {"name": "신천동", "path": "sincheondong"}, {"name": "신현동", "path": "sinhyeondong"},
            {"name": "은행동", "path": "eunhaengdong"}, {"name": "매화동", "path": "maehwadong"}, {"name": "목감동", "path": "mokgamdong"},
            {"name": "군자동", "path": "gunjadong"}, {"name": "월곶동", "path": "wolgotdong"}, {"name": "정왕동", "path": "jeongwangdong"},
            {"name": "배곧동", "path": "baegotdong"}, {"name": "과림동", "path": "gwarimdong"}, {"name": "연성동", "path": "yeonseongdong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "gunposi", "name": "군포시",
        "dongs": [
            {"name": "군포동", "path": "gunpodong"}, {"name": "산본동", "path": "sanbondong"}, {"name": "금정동", "path": "geumjeongdong"},
            {"name": "재궁동", "path": "jaegungdong"}, {"name": "오금동", "path": "ogeumdong"}, {"name": "수리동", "path": "suridong"},
            {"name": "대야미동", "path": "daeyamidong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "uiwangsi", "name": "의왕시",
        "dongs": [
            {"name": "고천동", "path": "gocheondong"}, {"name": "부곡동", "path": "bugokdong"}, {"name": "내손1동", "path": "naeson1dong"},
            {"name": "내손2동", "path": "naeson2dong"}, {"name": "청계동", "path": "cheonggyedong"}, {"name": "오전동", "path": "ojeondong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "hanamsi", "name": "하남시",
        "dongs": [
            {"name": "천현동", "path": "cheonhyeondong"}, {"name": "신장동", "path": "sinjangdong"}, {"name": "덕풍동", "path": "deokpungdong"},
            {"name": "감북동", "path": "gambukdong"}, {"name": "위례동", "path": "wiryedong"}, {"name": "미사동", "path": "misadong"},
            {"name": "춘궁동", "path": "chungungdong"}, {"name": "초이동", "path": "choidong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "pajusi", "name": "파주시",
        "dongs": [
            {"name": "문산읍", "path": "munsaneup"}, {"name": "조리읍", "path": "jorieup"}, {"name": "법원읍", "path": "beopwoneup"},
            {"name": "파주읍", "path": "pajueup"}, {"name": "탄현면", "path": "tanhyeonmyeon"}, {"name": "광탄면", "path": "gwangtanmyeon"},
            {"name": "월롱면", "path": "wollongmyeon"}, {"name": "적성면", "path": "jeokseongmyeon"}, {"name": "파평면", "path": "papyeongmyeon"},
            {"name": "교하동", "path": "gyohadong"}, {"name": "운정동", "path": "unjeongdong"}, {"name": "금촌동", "path": "geumchondong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "icheonsi", "name": "이천시",
        "dongs": [
            {"name": "창전동", "path": "changjeondong"}, {"name": "중리동", "path": "junglidong"}, {"name": "증포동", "path": "jeungpodong"},
            {"name": "부발읍", "path": "bubaleup"}, {"name": "장호원읍", "path": "janghowoneup"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "anseongsi", "name": "안성시",
        "dongs": [
            {"name": "공도읍", "path": "gongdoeup"}, {"name": "죽산면", "path": "juksanmyeon"}, {"name": "삼죽면", "path": "samjukmyeon"},
            {"name": "보개면", "path": "bogaemyeon"}, {"name": "금광면", "path": "geumgwangmyeon"}, {"name": "서운면", "path": "seounmyeon"},
            {"name": "미양면", "path": "miyangmyeon"}, {"name": "대덕면", "path": "daedeokmyeon"}, {"name": "원곡면", "path": "wongokmyeon"},
            {"name": "양성면", "path": "yangseongmyeon"}, {"name": "안성동", "path": "anseongdong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "gimposi", "name": "김포시",
        "dongs": [
            {"name": "고촌읍", "path": "gochoneup"}, {"name": "통진읍", "path": "tongjineup"}, {"name": "대곶면", "path": "daegotmyeon"},
            {"name": "월곶면", "path": "wolgotmyeon"}, {"name": "하성면", "path": "haseongmyeon"}, {"name": "사우동", "path": "saudong"},
            {"name": "풍무동", "path": "pungmudong"}, {"name": "장기동", "path": "janggidong"}, {"name": "구래동", "path": "guraedong"},
            {"name": "운양동", "path": "unyangdong"}, {"name": "마산동", "path": "masandong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "hwaseongsi", "name": "화성시",
        "dongs": [
            {"name": "봉담읍", "path": "bongdameup"}, {"name": "우정읍", "path": "ujeongeup"}, {"name": "향남읍", "path": "hyangnameup"},
            {"name": "남양읍", "path": "namyangeup"}, {"name": "매송면", "path": "maesongmyeon"}, {"name": "비봉면", "path": "bibongmyeon"},
            {"name": "팔탄면", "path": "paltanmyeon"}, {"name": "장안면", "path": "janganmyeon"}, {"name": "양감면", "path": "yanggammyeon"},
            {"name": "정남면", "path": "jeongnammyeon"}, {"name": "새솔동", "path": "saesoldong"}, {"name": "진안동", "path": "jinandong"},
            {"name": "병점동", "path": "byeongjeomdong"}, {"name": "반월동", "path": "banwoldong"}, {"name": "기배동", "path": "gibaedong"},
            {"name": "화산동", "path": "hwasandong"}, {"name": "동탄동", "path": "dongtandong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "gwangjusi", "name": "광주시",
        "dongs": [
            {"name": "오포읍", "path": "opoeup"}, {"name": "초월읍", "path": "chowoleup"}, {"name": "퇴촌면", "path": "toechonmyeon"},
            {"name": "남종면", "path": "namjongmyeon"}, {"name": "남한산성면", "path": "namhansanseongmyeon"}, {"name": "송정동", "path": "songjeongdong"},
            {"name": "광남동", "path": "gwangnamdong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "yangjusi", "name": "양주시",
        "dongs": [
            {"name": "회천동", "path": "hoecheondong"}, {"name": "양주동", "path": "yangjudong"}, {"name": "백석읍", "path": "baekseokeup"},
            {"name": "은현면", "path": "eunhyeonmyeon"}, {"name": "남면", "path": "nammyeon"}, {"name": "장흥면", "path": "jangheungmyeon"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "pocheonsi", "name": "포천시",
        "dongs": [
            {"name": "소흘읍", "path": "soheuleup"}, {"name": "군내면", "path": "gunnaemyeon"}, {"name": "내촌면", "path": "naechonmyeon"},
            {"name": "가산면", "path": "gasanmyeon"}, {"name": "일동면", "path": "ildongmyeon"}, {"name": "이동면", "path": "idongmyeon"},
            {"name": "영중면", "path": "yeongjungmyeon"}, {"name": "창수면", "path": "changsumyeon"}, {"name": "관인면", "path": "gwaninmyeon"},
            {"name": "화현면", "path": "hwahyeonmyeon"}, {"name": "포천동", "path": "pocheondong"}, {"name": "선단동", "path": "seandandong"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "yeojusi", "name": "여주시",
        "dongs": [
            {"name": "여흥동", "path": "yeoheungdong"}, {"name": "중앙동", "path": "jungangdong"}, {"name": "오학동", "path": "ohakdong"},
            {"name": "가남읍", "path": "ganameup"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "yeoncheongun", "name": "연천군",
        "dongs": [
            {"name": "연천읍", "path": "yeoncheoneup"}, {"name": "전곡읍", "path": "jeongokeup"}, {"name": "군남면", "path": "gunnammyeon"},
            {"name": "청산면", "path": "cheongsanmyeon"}, {"name": "백학면", "path": "baekhakmyeon"}, {"name": "미산면", "path": "misanmyeon"},
            {"name": "왕징면", "path": "wangjingmyeon"}, {"name": "신서면", "path": "sinseomyeon"}, {"name": "중면", "path": "jungmyeon"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "gapyeonggun", "name": "가평군",
        "dongs": [
            {"name": "가평읍", "path": "gapyeongeup"}, {"name": "설악면", "path": "seorakmyeon"}, {"name": "청평면", "path": "cheongpyeongmyeon"},
            {"name": "상면", "path": "sangmyeon"}, {"name": "조종면", "path": "jojongmyeon"}, {"name": "북면", "path": "bukmyeon"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "yangpyeonggun", "name": "양평군",
        "dongs": [
            {"name": "양평읍", "path": "yangpyeongeup"}, {"name": "강상면", "path": "gangsangmyeon"}, {"name": "강하면", "path": "ganghamyeon"},
            {"name": "양서면", "path": "yangseomyeon"}, {"name": "옥천면", "path": "okcheonmyeon"}, {"name": "지평면", "path": "jipyeongmyeon"},
            {"name": "용문면", "path": "yongmunmyeon"}, {"name": "개군면", "path": "gaegunmyeon"}
        ]
    },
    {
        "sido": "gyeonggi", "sido_name": "경기", "path": "gwacheonsi", "name": "과천시",
        "dongs": [
            {"name": "중앙동", "path": "jungangdong"}, {"name": "갈현동", "path": "galhyeondong"}, {"name": "별양동", "path": "byeolyangdong"},
            {"name": "부림동", "path": "burimdong"}, {"name": "원문동", "path": "wonmundong"}, {"name": "과천동", "path": "gwacheondong"},
            {"name": "문원동", "path": "munwondong"}
        ]
    },

    # --- 인천광역시 전체 구·군 ---
    {
        "sido": "incheon", "sido_name": "인천", "path": "junggu", "name": "중구",
        "dongs": [
            {"name": "신포동", "path": "sinpodong"}, {"name": "연안동", "path": "yeonandong"}, {"name": "신흥동", "path": "sinheungdong"},
            {"name": "도원동", "path": "dowondong"}, {"name": "율목동", "path": "yulmokdong"}, {"name": "동인천동", "path": "dongincheondong"},
            {"name": "개항동", "path": "gaehangdong"}, {"name": "영종동", "path": "yeongjongdong"}, {"name": "영종1동", "path": "yeongjong1dong"},
            {"name": "영종2동", "path": "yeongjong2dong"}, {"name": "운서동", "path": "unseodong"}, {"name": "용유동", "path": "yongyudong"}
        ]
    },
    {
        "sido": "incheon", "sido_name": "인천", "path": "donggu", "name": "동구",
        "dongs": [
            {"name": "만석동", "path": "manseokdong"}, {"name": "화수1.화평동", "path": "hwaru1hwapyeongdong"}, {"name": "화수2동", "path": "hwasu2dong"},
            {"name": "송현1.2동", "path": "songhyeon12dong"}, {"name": "송현3동", "path": "songhyeon3dong"}, {"name": "송림1동", "path": "songnim1dong"},
            {"name": "송림2동", "path": "songnim2dong"}, {"name": "송림3.5동", "path": "songnim35dong"}, {"name": "송림4동", "path": "songnim4dong"},
            {"name": "송림6동", "path": "songnim6dong"}, {"name": "금창동", "path": "geumchangdong"}
        ]
    },
    {
        "sido": "incheon", "sido_name": "인천", "path": "michuhol", "name": "미추홀구",
        "dongs": [
            {"name": "숭의1.4동", "path": "sungui14dong"}, {"name": "숭의2동", "path": "sungui2dong"}, {"name": "숭의3동", "path": "sungui3dong"},
            {"name": "용현1.4동", "path": "yonghyeon14dong"}, {"name": "용현2동", "path": "yonghyeon2dong"}, {"name": "용현3동", "path": "yonghyeon3dong"},
            {"name": "용현5동", "path": "yonghyeon5dong"}, {"name": "학익1동", "path": "hakik1dong"}, {"name": "학익2동", "path": "hakik2dong"},
            {"name": "도화1동", "path": "dohwa1dong"}, {"name": "도화2.3동", "path": "dohwa23dong"}, {"name": "주안1동", "path": "juan1dong"},
            {"name": "주안2동", "path": "juan2dong"}, {"name": "주안3동", "path": "juan3dong"}, {"name": "주안4동", "path": "juan4dong"},
            {"name": "주안5동", "path": "juan5dong"}, {"name": "주안6동", "path": "juan6dong"}, {"name": "주안7동", "path": "juan7dong"},
            {"name": "주안8동", "path": "juan8dong"}, {"name": "관교동", "path": "gwangyodong"}, {"name": "문학동", "path": "munhakdong"}
        ]
    },
    {
        "sido": "incheon", "sido_name": "인천", "path": "yeonsu", "name": "연수구",
        "dongs": [
            {"name": "옥련1동", "path": "oknyeon1dong"}, {"name": "옥련2동", "path": "oknyeon2dong"}, {"name": "선학동", "path": "seonhakdong"},
            {"name": "연수1동", "path": "yeonsu1dong"}, {"name": "연수2동", "path": "yeonsu2dong"}, {"name": "연수3동", "path": "yeonsu3dong"},
            {"name": "청학동", "path": "cheonghakdong"}, {"name": "동춘1동", "path": "dongchun1dong"}, {"name": "동춘2동", "path": "dongchun2dong"},
            {"name": "동춘3동", "path": "dongchun3동"}, {"name": "송도1동", "path": "songdo1dong"}, {"name": "송도2동", "path": "songdo2dong"},
            {"name": "송도3동", "path": "songdo3동"}, {"name": "송도4동", "path": "songdo4동"}, {"name": "송도5동", "path": "songdo5동"}
        ]
    },
    {
        "sido": "incheon", "sido_name": "인천", "path": "namdong", "name": "남동구",
        "dongs": [
            {"name": "구월1동", "path": "guwol1dong"}, {"name": "구월2동", "path": "guwol2dong"}, {"name": "구월3동", "path": "guwol3dong"},
            {"name": "구월4동", "path": "guwol4dong"}, {"name": "간석1동", "path": "ganseok1dong"}, {"name": "간석2동", "path": "ganseok2dong"},
            {"name": "간석3동", "path": "ganseok3dong"}, {"name": "간석4동", "path": "ganseok4dong"}, {"name": "만수1동", "path": "mansu1dong"},
            {"name": "만수2동", "path": "mansu2dong"}, {"name": "만수3동", "path": "mansu3동"}, {"name": "만수4동", "path": "mansu4dong"},
            {"name": "만수5동", "path": "mansu5dong"}, {"name": "만수6동", "path": "mansu6동"}, {"name": "장수서창동", "path": "jangsuseochangdong"},
            {"name": "서창2동", "path": "seochang2dong"}, {"name": "남촌도림동", "path": "namchondorimdong"}, {"name": "논현1동", "path": "nonhyeon1dong"},
            {"name": "논현2동", "path": "nonhyeon2dong"}, {"name": "논현고잔동", "path": "nonhyeongojandong"}
        ]
    },
    {
        "sido": "incheon", "sido_name": "인천", "path": "bupyeong", "name": "부평구",
        "dongs": [
            {"name": "부평1동", "path": "bupyeong1dong"}, {"name": "부평2동", "path": "bupyeong2dong"}, {"name": "부평3동", "path": "bupyeong3dong"},
            {"name": "부평4동", "path": "bupyeong4dong"}, {"name": "부평5동", "path": "bupyeong5dong"}, {"name": "부평6동", "path": "bupyeong6dong"},
            {"name": "산곡1동", "path": "sangok1dong"}, {"name": "산곡2동", "path": "sangok2dong"}, {"name": "산곡3동", "path": "sangok3dong"},
            {"name": "산곡4동", "path": "sangok4dong"}, {"name": "청천1동", "path": "cheongcheon1dong"}, {"name": "청천2동", "path": "cheongcheon2dong"},
            {"name": "갈산1동", "path": "galsan1dong"}, {"name": "갈산2동", "path": "galsan2dong"}, {"name": "삼산1동", "path": "samsan1dong"},
            {"name": "삼산2동", "path": "samsan2dong"}, {"name": "부개1동", "path": "bugae1dong"}, {"name": "부개2동", "path": "bugae2dong"},
            {"name": "부개3동", "path": "bugae3dong"}, {"name": "일신동", "path": "ilsindong"}, {"name": "십정1동", "path": "sipjeong1dong"},
            {"name": "십정2동", "path": "sipjeong2dong"}
        ]
    },
    {
        "sido": "incheon", "sido_name": "인천", "path": "gyeyang", "name": "계양구",
        "dongs": [
            {"name": "효성1동", "path": "hyoseong1dong"}, {"name": "효성2동", "path": "hyoseong2dong"}, {"name": "계산1동", "path": "gyesan1dong"},
            {"name": "계산2동", "path": "gyesan2dong"}, {"name": "계산3동", "path": "gyesan3dong"}, {"name": "계산4동", "path": "gyesan4dong"},
            {"name": "작전1동", "path": "jakjeon1dong"}, {"name": "작전2동", "path": "jakjeon2dong"}, {"name": "작전서운동", "path": "jakjeonseowundong"},
            {"name": "계양1동", "path": "gyeyang1dong"}, {"name": "계양2동", "path": "gyeyang2dong"}, {"name": "계양3동", "path": "gyeyang3dong"}
        ]
    },
    {
        "sido": "incheon", "sido_name": "인천", "path": "seogu", "name": "서구",
        "dongs": [
            {"name": "검암경서동", "path": "geomamgyeongseodong"}, {"name": "연희동", "path": "yeonhuidong"}, {"name": "청라1동", "path": "cheongra1dong"},
            {"name": "청라2동", "path": "cheongra2dong"}, {"name": "청라3동", "path": "cheongra3dong"}, {"name": "가정1동", "path": "gajeong1dong"},
            {"name": "가정2동", "path": "gajeong2dong"}, {"name": "가정3동", "path": "gajeong3dong"}, {"name": "신현원창동", "path": "sinhyeonwonchangdong"},
            {"name": "석남1동", "path": "seoknam1dong"}, {"name": "석남2동", "path": "seoknam2dong"}, {"name": "석남3동", "path": "seoknam3dong"},
            {"name": "가좌1동", "path": "gajwa1dong"}, {"name": "가좌2동", "path": "gajwa2dong"}, {"name": "가좌3동", "path": "gajwa3dong"},
            {"name": "가좌4동", "path": "gajwa4dong"}, {"name": "검단동", "path": "geomdandong"}, {"name": "불로대곡동", "path": "bullodaegokdong"},
            {"name": "원당동", "path": "wondangdong"}, {"name": "당하동", "path": "danghadong"}, {"name": "오류왕길동", "path": "oryuwanggildong"},
            {"name": "마전동", "path": "majeondong"}, {"name": "아라동", "path": "aradong"}
        ]
    },
    {
        "sido": "incheon", "sido_name": "인천", "path": "ganghwa", "name": "강화군",
        "dongs": [
            {"name": "강화읍", "path": "ganghwaeup"}, {"name": "선원면", "path": "seonwonmyeon"}, {"name": "불은면", "path": "bureunmyeon"},
            {"name": "길상면", "path": "gilsangmyeon"}, {"name": "화도면", "path": "hwadomyeon"}, {"name": "양도면", "path": "yangdomyeon"},
            {"name": "내가면", "path": "naegamyeon"}, {"name": "하점면", "path": "hajeommyeon"}, {"name": "양사면", "path": "yangsamyeon"},
            {"name": "송해면", "path": "songhaemyeon"}, {"name": "교동면", "path": "gyodongmyeon"}, {"name": "삼산면", "path": "samsanmyeon"},
            {"name": "서도면", "path": "seodomyeon"}
        ]
    },
    {
        "sido": "incheon", "sido_name": "인천", "path": "ongjin", "name": "옹진군",
        "dongs": [
            {"name": "북도면", "path": "bukdomyeon"}, {"name": "연평면", "path": "yeonpyeongmyeon"}, {"name": "백령면", "path": "baengnyeongmyeon"},
            {"name": "대청면", "path": "daecheongmyeon"}, {"name": "덕적면", "path": "deokjeokmyeon"}, {"name": "자월면", "path": "jawolmyeon"},
            {"name": "영흥면", "path": "yeongheungmyeon"}
        ]
    }
]

shops = [
    { 
        "id": "shop1", "name": "🔥 한국미인테라피", "phone": "0507-1280-3303", 
        "courses": [
            ("아로디시 90분", "100,000원"), ("아로디시 120분", "130,000원"),
            ("VIP스웨디시 60분", "110,000원"), ("VIP스웨디시 90분", "130,000원"), ("VIP스웨디시 120분", "150,000원"),
            ("한국인스웨디시 60분", "140,000원"), ("한국인스웨디시 90분", "180,000원")
        ]
    },
    { 
        "id": "shop2", "name": "✨ 오늘밤테라피", "phone": "0507-1280-3223", 
        "courses": [
            ("타이코스 60분", "60,000원"), ("타이코스 90분", "80,000원"), ("타이코스 120분", "100,000원"),
            ("전신아로마 60분", "70,000원"), ("전신아로마 90분", "90,000원"), ("전신아로마 120분", "110,000원"),
            ("VIP 감성힐링코스 ★추천 60분", "90,000원"), ("VIP 감성힐링코스 ★추천 90분", "110,000원"), ("VIP 감성힐링코스 ★추천 120분", "130,000원"),
            ("VIP 스페셜코스 ★추천 60분", "100,000원"), ("VIP 스페셜코스 ★추천 90분", "120,000원"), ("VIP 스페셜코스 ★추천 120분", "140,000원"),
            ("VIP 프리미엄 코스 (타이&아로마&풋) 150분", "160,000원"),
            ("한국인스웨디시 60분", "140,000원"), ("한국인스웨디시 90분", "180,000원")
        ]
    },
    { 
        "id": "shop3", "name": "💎 주주테라피", "phone": "0507-1280-3193", 
        "courses": [
            ("타이코스 60분", "60,000원"), ("타이코스 90분", "80,000원"), ("타이코스 120분", "100,000원"),
            ("전신아로마 60분", "70,000원"), ("전신아로마 90분", "90,000원"), ("전신아로마 120분", "110,000원"),
            ("VIP 감성힐링코스 ★추천 60분", "90,000원"), ("VIP 감성힐링코스 ★추천 90분", "110,000원"), ("VIP 감성힐링코스 ★추천 120분", "130,000원"),
            ("VIP 스페셜코스 ★추천 60분", "100,000원"), ("VIP 스페셜코스 ★추천 90분", "120,000원"), ("VIP 스페셜코스 ★추천 120분", "140,000원"),
            ("VIP 프리미엄 코스 (타이&아로마&풋) 150분", "160,000원"),
            ("한국인스웨디시 60분", "140,000원"), ("한국인스웨디시 90분", "180,000원")
        ]
    },
    { 
        "id": "shop4", "name": "🌟 퀸즈홈테라피", "phone": "0507-1280-3334", 
        "courses": [
            ("건식 힐링 코스 60분", "60,000원"), ("건식 힐링 코스 90분", "80,000원"), ("건식 힐링 코스 120분", "100,000원"),
            ("아로마 힐링 코스 60분", "70,000원"), ("아로마 힐링 코스 90분", "80,000원"), ("아로마 힐링 코스 120분", "100,000원"),
            ("힐링스웨디시 코스 60분", "80,000원"), ("힐링스웨디시 코스 90분", "100,000원"), ("힐링스웨디시 코스 120분", "120,000원"),
            ("VIP스페셜코스 60분", "100,000원"), ("VIP스페셜코스 90분", "120,000원"), ("VIP스페셜코스 120분", "150,000원"),
            ("한국 관리사 코스 60분", "150,000원"), ("한국 관리사 코스 90분", "180,000원")
        ]
    },
    { 
        "id": "shop5", "name": "👑 한국골든테라피", "phone": "0507-1280-3360", 
        "courses": [
            ("스웨디시 코스 60분", "140,000원"), ("스웨디시 코스 90분", "190,000원"),
            ("프리미엄 코스 60분", "110,000원"), ("프리미엄 코스 90분", "130,000원"), ("프리미엄 코스 120분", "150,000원")
        ]
    }
]

page_template = """<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{page_title} | 케어힐즈</title>
<meta name="description" content="{page_desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{page_url}">
<meta property="og:title" content="{page_title} | 케어힐즈">
<meta property="og:description" content="{page_desc}">
<meta property="og:locale" content="ko_KR">
<style>
:root{{--p:#9c3854;--a:#e07a93;--bg:#fff8f9;--bg2:#fff;--txt:#2d2024;--muted:#7a656b;--bdr:#ecd2d7;--shadow:0 2px 12px rgba(156,56,84,.08);}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:var(--bg);color:var(--txt);font-family:'Pretendard',sans-serif;line-height:1.6;padding-bottom:80px}}
a{{color:inherit;text-decoration:none}}
.ch-hd{{background:#fff;border-bottom:2px solid var(--p);position:sticky;top:0;z-index:100;box-shadow:0 2px 8px rgba(0,0,0,.05)}}
.ch-hd-inner{{max-width:1100px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;height:62px;padding:0 20px}}
.ch-logo{{font-size:16px;font-weight:800;color:var(--p)}}
.ch-bc{{background:#fff;border-bottom:1px solid var(--bdr);padding:10px 20px;font-size:12px;color:var(--muted)}}
.ch-bc a{{color:var(--p)}}
.ch-sec{{padding:44px 20px}}
.ch-sec-inner{{max-width:1100px;margin:0 auto}}
.ch-sec h2{{font-size:20px;font-weight:800;color:var(--p);margin-bottom:12px}}
.ch-info-box{{background:var(--p);color:#fff;border-radius:8px;padding:14px 18px;font-size:14px;margin-bottom:20px}}
.ch-info-box strong{{color:#ffd1dc}}
.ch-dong-wrap{{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:30px}}
.ch-dong-badge{{background:#fff;border:1.5px solid var(--bdr);padding:6px 14px;border-radius:20px;font-size:13px;font-weight:600;color:var(--muted);transition:all .15s;display:inline-block}}
.ch-dong-badge:hover, .ch-dong-badge.active{{background:var(--p);color:#fff;border-color:var(--p)}}
.ch-shop-list{{display:flex;flex-direction:column;gap:14px}}
.ch-shop{{background:#fff;border:1.5px solid var(--bdr);border-radius:12px;padding:20px;display:flex;justify-content:space-between;align-items:center;transition:all .15s}}
.ch-shop:hover{{border-color:var(--p);box-shadow:var(--shadow)}}
.ch-shop-name a{{font-size:17px;font-weight:800;color:var(--txt);text-decoration:none}}
.ch-shop-name a:hover{{color:var(--p);text-decoration:underline}}
.ch-shop-desc{{font-size:13px;color:var(--muted);margin-bottom:10px}}
.ch-btn-group{{display:flex;gap:8px;align-items:center}}
.ch-detail-btn{{background:#f3e2e6;color:var(--p);padding:10px 14px;border-radius:6px;font-weight:700;font-size:13px}}
.ch-call{{background:var(--p);color:#fff;padding:10px 20px;border-radius:6px;font-weight:700;font-size:13px;white-space:nowrap}}
.ch-ft{{background:#3d232b;color:#d4b5bc;padding:40px 20px;margin-top:40px;text-align:center;font-size:12px}}
@media(max-width:768px){{.ch-shop{{flex-direction:column;align-items:flex-start;gap:12px}}.ch-btn-group{{width:100%;justify-content:space-between}}.ch-call{{flex:1;text-align:center}}}}
</style>
</head>
<body>
<header class="ch-hd">
  <div class="ch-hd-inner">
    <a href="https://careheals.netlify.app/" class="ch-logo">케어힐즈 (CAREHEALS)</a>
  </div>
</header>
<nav class="ch-bc">
  <div style="max-width:1100px;margin:0 auto;">
    <a href="https://careheals.netlify.app/">홈</a> › <a href="https://careheals.netlify.app/{sido_path}/">{sido_name}</a> › {gu_name} {current_dong}
  </div>
</nav>
<section class="ch-sec">
  <div class="ch-sec-inner">
    <h2>{page_title}</h2>
    <div class="ch-info-box"><strong>💰 전 지역 단일 요금:</strong> 선입금 없는 100% 후불제 케어 서비스 제공</div>
    
    <div style="margin-bottom:12px;font-weight:700;color:var(--p);">📍 방문 가능 행정동 전체 보기</div>
    <div class="ch-dong-wrap">
      {dong_badges}
    </div>

    <div style="margin-top:30px;margin-bottom:16px;">
      <h3 style="font-size:18px;font-weight:800;color:var(--p);">✨ 실시간 추천 제휴 업체</h3>
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

shop_template = """<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{shop_title}</title>
<meta name="description" content="{shop_desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{shop_url}">
<meta property="og:title" content="{shop_title}">
<meta property="og:description" content="{shop_desc}">
<meta property="og:locale" content="ko_KR">
<style>
:root{{--p:#9c3854;--a:#e07a93;--bg:#fff8f9;--txt:#2d2024;--muted:#7a656b;--bdr:#ecd2d7;}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:var(--bg);color:var(--txt);font-family:'Pretendard',sans-serif;line-height:1.6;padding-bottom:80px}}
a{{color:inherit;text-decoration:none}}
.ch-hd{{background:#fff;border-bottom:2px solid var(--p);position:sticky;top:0;z-index:100;height:62px;display:flex;align-items:center;justify-content:space-between;padding:0 20px}}
.ch-logo{{font-size:16px;font-weight:800;color:var(--p)}}
.ch-tel{{background:var(--p);color:#fff;padding:8px 18px;border-radius:6px;font-weight:700;font-size:14px}}
.ch-sec{{padding:44px 20px}}
.ch-sec-inner{{max-width:700px;margin:0 auto;background:#fff;border:1.5px solid var(--bdr);border-radius:12px;padding:24px}}
.ch-title{{font-size:22px;font-weight:800;color:var(--p);margin-bottom:6px}}
.ch-sub{{font-size:13px;color:var(--muted);margin-bottom:20px}}
.ch-table{{width:100%;border-collapse:collapse;margin-bottom:24px}}
.ch-table th, .ch-table td{{padding:12px;border-bottom:1px solid var(--bdr);text-align:left;font-size:14px}}
.ch-table th{{color:var(--p);font-weight:700;background:#fff5f7}}
.ch-table td:last-child{{text-align:right;font-weight:800;color:var(--p)}}
.ch-call-btn{{display:block;background:var(--p);color:#fff;text-align:center;padding:14px;border-radius:8px;font-weight:800;font-size:16px}}
</style>
</head>
<body>
<header class="ch-hd">
  <a href="https://careheals.netlify.app/" class="ch-logo">케어힐즈 (CAREHEALS)</a>
  <a href="tel:{shop_phone}" class="ch-tel">📞 {shop_phone}</a>
</header>
<section class="ch-sec">
  <div class="ch-sec-inner">
    <h1 class="ch-title">{shop_name}</h1>
    <p class="ch-sub">📍 서비스 지역: {loc_title} 전 지역 (100% 후불제)</p>
    
    <table class="ch-table">
      <thead>
        <tr>
          <th>관리 코스 및 프로그램</th>
          <th>이용 요금</th>
        </tr>
      </thead>
      <tbody>
        {course_rows}
      </tbody>
    </table>

    <a href="tel:{shop_phone}" class="ch-call-btn">📞 전화로 빠른 예약하기 ({shop_phone})</a>
  </div>
</section>
</body>
</html>
"""

title_patterns = [
    "{loc_title} 스웨디시 마사지 추천 {shop_name} | 케어힐즈",
    "{loc_title} 타이 마사지 전문 {shop_name} | 케어힐즈",
    "{loc_title} 아로마 케어 샵 {shop_name} | 케어힐즈",
    "{loc_title} 감성 홈케어 마사지 {shop_name} | 케어힐즈",
    "{loc_title} 힐링 테라피 코스 {shop_name} | 케어힐즈"
]

desc_patterns = [
    "{loc_title} 지역에서 이용 가능한 출장 전문 매장 {shop_name} 제휴 안내. 선입금 없는 후불제 홈케어 마사지 코스 및 가격표 정보.",
    "{loc_title} 맞춤형 방문 프로그램 운영 중인 {shop_name} 안내. 안전한 후불제 시스템으로 이용하는 전문 마사지 정보.",
    "{loc_title} 전 지역 출장 케어 서비스 {shop_name} 제휴 페이지. 신뢰할 수 있는 후불제 아로마 및 타이 마사지 안내.",
    "{loc_title} 감성 충전 홈케어 전문 {shop_name} 방문 안내. 부담 없는 후불제로 즐기는 프리미엄 마사지 코스 모음."
]

sitemap_urls = [
    "https://careheals.netlify.app/",
    "https://careheals.netlify.app/seoul/",
    "https://careheals.netlify.app/gyeonggi/",
    "https://careheals.netlify.app/incheon/"
]

global_shop_index = 0

for reg in all_regions:
    sido_path = reg["sido"]
    sido_name = reg["sido_name"]
    gu_path = reg["path"]
    gu_name = reg["name"]
    
    dir_path = os.path.join("public", sido_path, gu_path)
    os.makedirs(dir_path, exist_ok=True)
    
    shuffled_shops_gu = shops.copy()
    random.shuffle(shuffled_shops_gu)
    
    shop_items_main = ""
    for shop in shuffled_shops_gu:
        shop_items_main += f"""
        <div class="ch-shop">
          <div>
            <div class="ch-shop-name"><a href="./{shop['id']}/">{shop["name"]}</a></div>
            <div class="ch-shop-desc">선입금 없는 100% 후불제 맞춤 방문 힐링 케어</div>
          </div>
          <div class="ch-btn-group">
            <a href="./{shop['id']}/" class="ch-detail-btn">상세보기 및 가격</a>
            <a href="tel:{shop["phone"]}" class="ch-call">📞 예약 전화</a>
          </div>
        </div>
        """

    dong_badges_main = "".join([f'<a href="./{d["path"]}/" class="ch-dong-badge">{d["name"]}</a>' for d in reg["dongs"]])
    
    # 구 페이지 생성
    main_file = os.path.join(dir_path, "index.html")
    gu_url = f"https://careheals.netlify.app/{sido_path}/{gu_path}/"
    gu_title = f"{gu_name} 스웨디시 마사지 추천｜전국 감성 아로마 케어 총정리"
    gu_desc = f"{sido_name} {gu_name} 전 지역에서 이용 가능한 전문 홈케어 및 제휴 업체 안내 플랫폼입니다. 신뢰도 높은 후불제 마사지 서비스를 만나보세요."
    
    with open(main_file, "w", encoding="utf-8") as f:
        f.write(page_template.format(
            page_title=gu_title, page_desc=gu_desc, page_url=gu_url,
            sido_path=sido_path, sido_name=sido_name, gu_name=gu_name, current_dong="",
            dong_badges=dong_badges_main, shop_items=shop_items_main
        ))
    sitemap_urls.append(gu_url)

    # 구 하위 샵 상세 페이지 생성
    for shop in shops:
        shop_dir = os.path.join(dir_path, shop['id'])
        os.makedirs(shop_dir, exist_ok=True)
        
        t_pattern = title_patterns[global_shop_index % len(title_patterns)]
        d_pattern = desc_patterns[global_shop_index % len(desc_patterns)]
        global_shop_index += 1
        
        shop_title_str = t_pattern.format(loc_title=gu_name, shop_name=shop["name"])
        shop_desc_str = d_pattern.format(loc_title=gu_name, shop_name=shop["name"])
        
        course_rows = "".join([f"<tr><td>{c}</td><td>{p}</td></tr>\n" for c, p in shop["courses"]])
        shop_url = f"https://careheals.netlify.app/{sido_path}/{gu_path}/{shop['id']}/"
            
        with open(os.path.join(shop_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(shop_template.format(
                shop_title=shop_title_str, shop_desc=shop_desc_str,
                loc_title=gu_name, shop_name=shop["name"], shop_phone=shop["phone"],
                course_rows=course_rows, shop_url=shop_url
            ))
        sitemap_urls.append(shop_url)

    # 동별 페이지 및 동 하위 샵 상세 페이지 생성
    for dong in reg["dongs"]:
        dong_dir = os.path.join(dir_path, dong['path'])
        os.makedirs(dong_dir, exist_ok=True)
        
        dong_badges_sub = "".join([f'<a href="../{d["path"]}/" class="ch-dong-badge{" active" if d["path"] == dong["path"] else ""}">{d["name"]}</a>' for d in reg["dongs"]])
        
        shuffled_shops_dong = shops.copy()
        random.shuffle(shuffled_shops_dong)
        
        shop_items_sub = ""
        for shop in shuffled_shops_dong:
            shop_items_sub += f"""
            <div class="ch-shop">
              <div>
                <div class="ch-shop-name"><a href="./{shop['id']}/">{shop["name"]}</a></div>
                <div class="ch-shop-desc">선입금 없는 100% 후불제 맞춤 방문 힐링 케어</div>
              </div>
              <div class="ch-btn-group">
                <a href="./{shop['id']}/" class="ch-detail-btn">상세보기 및 가격</a>
                <a href="tel:{shop["phone"]}" class="ch-call">📞 예약 전화</a>
              </div>
            </div>
            """
            
        dong_url = f"https://careheals.netlify.app/{sido_path}/{gu_path}/{dong['path']}/"
        dong_title = f"{gu_name} {dong['name']} 스웨디시 마사지 추천｜전국 감성 아로마 케어 총정리"
        dong_desc = f"{sido_name} {gu_name} {dong['name']} 지역 맞춤형 방문 홈케어 및 제휴 안내 페이지입니다. 안전한 후불제 마사지 서비스를 제공합니다."
        
        with open(os.path.join(dong_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(page_template.format(
                page_title=dong_title, page_desc=dong_desc, page_url=dong_url,
                sido_path=sido_path, sido_name=sido_name, gu_name=gu_name, current_dong=f"› {dong['name']}",
                dong_badges=dong_badges_sub, shop_items=shop_items_sub
            ))
        sitemap_urls.append(dong_url)

        loc_dong_title = f"{gu_name} {dong['name']}"
        for shop in shops:
            dong_shop_dir = os.path.join(dong_dir, shop['id'])
            os.makedirs(dong_shop_dir, exist_ok=True)
            
            t_pattern = title_patterns[global_shop_index % len(title_patterns)]
            d_pattern = desc_patterns[global_shop_index % len(desc_patterns)]
            global_shop_index += 1
            
            shop_title_str = t_pattern.format(loc_title=loc_dong_title, shop_name=shop["name"])
            shop_desc_str = d_pattern.format(loc_title=loc_dong_title, shop_name=shop["name"])
            
            course_rows = "".join([f"<tr><td>{c}</td><td>{p}</td></tr>\n" for c, p in shop["courses"]])
            dong_shop_url = f"https://careheals.netlify.app/{sido_path}/{gu_path}/{dong['path']}/{shop['id']}/"
                
            with open(os.path.join(dong_shop_dir, "index.html"), "w", encoding="utf-8") as f:
                f.write(shop_template.format(
                    shop_title=shop_title_str, shop_desc=shop_desc_str,
                    loc_title=loc_dong_title, shop_name=shop["name"], shop_phone=shop["phone"],
                    course_rows=course_rows, shop_url=dong_shop_url
                ))
            sitemap_urls.append(dong_shop_url)

# sitemap.xml 파일 생성 (public 폴더 아래 저장)
sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for url in sitemap_urls:
    sitemap_content += f'  <url>\n    <loc>{url}</loc>\n  </url>\n'
sitemap_content += '</urlset>'

os.makedirs("public", exist_ok=True)
with open(os.path.join("public", "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap_content)

print(f"✨ 서울, 경기, 인천 전체 동 및 샵 상세 페이지 포함 총 {len(sitemap_urls)}개의 URL이 public/sitemap.xml로 완벽하게 생성되었습니다!")