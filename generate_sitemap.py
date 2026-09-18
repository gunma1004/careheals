import datetime
import os

# 1. 서울, 경기, 인천 전체 행정구역 데이터 (앞서 사용한 데이터와 동일)
region_data = {
    "seoul": {
        "districts": [
            {"gu": "jongrogu", "dongs": ["sajikdong", "samcheongdong", "jongrodong"]},
            {"gu": "junggu", "dongs": ["sogongdong", "myeongdong", "euljirodong"]},
            {"gu": "yongsangu", "dongs": ["huamdong", "itaewondong", "hannamdong"]},
            {"gu": "seongdonggu", "dongs": ["wangsipridong", "seongsudong", "oksudong"]},
            {"gu": "gwangjingu", "dongs": ["hwayangdong", "guuidong", "jayangdong"]},
            {"gu": "dongdaemungu", "dongs": ["hoegidong", "cheongryangridong", "jangandong"]},
            {"gu": "jungnanggu", "dongs": ["myeonmokdong", "sangbongdong", "junghwadong"]},
            {"gu": "seongbukgu", "dongs": ["donamdong", "anamdong", "gileumdong"]},
            {"gu": "gangbukgu", "dongs": ["miadong", "suyudong", "beondong"]},
            {"gu": "dobonggu", "dongs": ["ssangmundong", "changdong", "banghakdong"]},
            {"gu": "nowongu", "dongs": ["sanggyedong", "junggyedong", "hagyedong"]},
            {"gu": "eunpyeonggu", "dongs": ["bulgwangdong", "eungamdong", "yeonsinnaedong"]},
            {"gu": "seodaemungu", "dongs": ["sinchondong", "hongjedong", "yeonhuidong"]},
            {"gu": "mapogu", "dongs": ["seogyodong", "hapjeongdong", "yeonnamdong", "gongdeokdong"]},
            {"gu": "yangcheongu", "dongs": ["mokdong", "sinjeongdong", "sinwoldong"]},
            {"gu": "gangseogu", "dongs": ["hwagokdong", "deungchondong", "balsandong"]},
            {"gu": "gurogu", "dongs": ["gurodong", "sindorimdong", "gaebongdong"]},
            {"gu": "geumcheongu", "dongs": ["gasandong", "doksandong", "siheungdong"]},
            {"gu": "yeongdeungpogu", "dongs": ["yeouidong", "yeongdeungpodong", "dangsandong"]},
            {"gu": "dongjakgu", "dongs": ["noryangjindong", "sadangdong", "sangdodong"]},
            {"gu": "gwanakgu", "dongs": ["sinlimdong", "bongcheondong", "namhyeondong"]},
            {"gu": "seochogu", "dongs": ["seochodong", "banpodong", "bangbaedong", "yangjaedong"]},
            {"gu": "gangnamgu", "dongs": ["sinsadong", "nonhyeondong", "samseongdong", "daechidong", "yeoksamdong", "cheongdamdong"]},
            {"gu": "songpagu", "dongs": ["jamsildong", "bangidong", "munjeongdong", "ganakdong"]},
            {"gu": "gangdonggu", "dongs": ["cheonhodong", "gildong", "myeongildong"]}
        ]
    },
    "gyeonggi": {
        "districts": [
            {"gu": "suwon_jangan", "dongs": ["jeongjadong", "jowondong", "pajangdong"]},
            {"gu": "suwon_gwonseon", "dongs": ["gwonseondong", "gokbanjeongdong", "seryudong"]},
            {"gu": "suwon_paldal", "dongs": ["ingyedong", "umandong", "maesandong"]},
            {"gu": "suwon_yeongtong", "dongs": ["yeongtongdong", "maetandong", "gwanggyodong"]},
            {"gu": "seongnam_sujeong", "dongs": ["taepyeongdong", "sinheungdong", "sujindong"]},
            {"gu": "seongnam_jungwon", "dongs": ["seongnamdong", "geumgwangdong", "sangdaewondong"]},
            {"gu": "seongnam_bundang", "dongs": ["jeongjadong", "seohyeondong", "sunaedong", "pangyodong"]},
            {"gu": "goyang_deogyang", "dongs": ["hwajeongdong", "haengsindong", "samsongdong"]},
            {"gu": "goyang_ilsandong", "dongs": ["baekseokdong", "madudong", "jeongbalsandong"]},
            {"gu": "goyang_ilsanseo", "dongs": ["daehwadong", "juyeopdong", "tanhyeondong"]},
            {"gu": "yongin_cheoin", "dongs": ["yeokbukdong", "kimryangjangdong"]},
            {"gu": "yongin_giheung", "dongs": ["gugaldong", "dongbaekdong", "singaldong"]},
            {"gu": "yongin_suji", "dongs": ["pungdeokcheondong", "jukjeondong", "sanghyeondong"]},
            {"gu": "bucheon_wonmi", "dongs": ["jungdong", "sangdong", "simgokdong"]},
            {"gu": "bucheon_sosa", "dongs": ["sosabondong", "yeokgokdong"]},
            {"gu": "bucheon_ojeong", "dongs": ["ojeongdong", "wonjongdong"]},
            {"gu": "anyang_manan", "dongs": ["anyangdong", "seoksudong"]},
            {"gu": "anyang_dongan", "dongs": ["bisandong", "pyeongchondong", "hogyedong"]},
            {"gu": "ansan_sangnok", "dongs": ["bonodong", "sadong", "idong"]},
            {"gu": "ansan_danwon", "dongs": ["gojandong", "chojidong", "seonbudong"]},
            {"gu": "uijeongbusi", "dongs": ["uijeongbudong", "singokdong"]},
            {"gu": "pyeongtaeksi", "dongs": ["bijeondong", "dongsakdong", "godeokdong"]},
            {"gu": "dongducheonsi", "dongs": ["saengyeondong", "jihaengdong"]},
            {"gu": "gwangmyeongsi", "dongs": ["cheolsandong", "haandong", "sohadong"]},
            {"gu": "gwacheonsi", "dongs": ["jungangdong", "byeolyangdong"]},
            {"gu": "gurisi", "dongs": ["inchangdong", "sutaekdong"]},
            {"gu": "namyangjusi", "dongs": ["dasandong", "byeolnaedong", "hopyeongdong"]},
            {"gu": "osansi", "dongs": ["gwoldong", "wondong"]},
            {"gu": "siheungsi", "dongs": ["baegotdong", "jeongwangdong"]},
            {"gu": "gunposi", "dongs": ["sanbondong", "geumjeongdong"]},
            {"gu": "uiwangsi", "dongs": ["naesondong", "ojeondong"]},
            {"gu": "hanamsi", "dongs": ["misadong", "pungsandong"]},
            {"gu": "pajusi", "dongs": ["unjeongdong", "geumchondong"]},
            {"gu": "icheonsi", "dongs": ["jeungpodong", "changjeondong"]},
            {"gu": "anseongsi", "dongs": ["gongdoeup", "anseongdong"]},
            {"gu": "gimposi", "dongs": ["guraedong", "janggidong", "unyangdong"]},
            {"gu": "hwaseongsi", "dongs": ["dongtandong", "hyangnameup", "byeongjeomdong"]},
            {"gu": "gwangjusi", "dongs": ["opodong", "gyeongandong"]},
            {"gu": "yangjusi", "dongs": ["hoecheondong", "yangjudong"]},
            {"gu": "pocheonsi", "dongs": ["soheuleup", "pocheondong"]},
            {"gu": "yeojusi", "dongs": ["ohakdong", "yeoheungdong"]},
            {"gu": "yeoncheongun", "dongs": ["jeongokeup", "yeoncheoneup"]},
            {"gu": "gapyeonggun", "dongs": ["gapyeongeup", "cheongpyeongmyeon"]},
            {"gu": "yangpyeonggun", "dongs": ["yangpyeongeup", "yongmunmyeon"]}
        ]
    },
    "incheon": {
        "districts": [
            {"gu": "jemulbogu", "dongs": ["sinpodong", "sinheungdong", "songrimdong"]},
            {"gu": "yeongjonggu", "dongs": ["unseodong", "yeongjongdong", "yongyudong"]},
            {"gu": "michuholgu", "dongs": ["juandong", "yonghyeondong", "hakikdong"]},
            {"gu": "yeonsugu", "dongs": ["songdodong", "yeonsudong", "dongchundong"]},
            {"gu": "namdonggu", "dongs": ["guwoldong", "ganseokdong", "nonhyeondong"]},
            {"gu": "bupyeonggu", "dongs": ["bupyeongdong", "sangokdong", "samsandong"]},
            {"gu": "gyeyanggu", "dongs": ["gyesandong", "hyoseongdong", "jakjeondong"]},
            {"gu": "seohaegu", "dongs": ["cheongradong", "yeonhuidong", "gajeongdong"]},
            {"gu": "geomdangu", "dongs": ["danghadong", "majeondong", "aradong"]},
            {"gu": "ganghwagun", "dongs": ["ganghwaeup", "gilsangmyeon"]},
            {"gu": "ongjingun", "dongs": ["yeongheungmyeon", "bukdomyeon"]}
        ]
    }
}

def generate_sitemap():
    base_url = "https://careheals.netlify.app"
    today = datetime.date.today().isoformat()
    url_entries = []

    # 1. 메인 홈 페이지 추가
    url_entries.append({"loc": base_url, "priority": "1.0", "changefreq": "daily"})

    # 2. 시도별 허브 페이지 추가 (예: /gyeonggi/)
    for sido_path in region_data.keys():
        url_entries.append({"loc": f"{base_url}/{sido_path}/", "priority": "0.9", "changefreq": "daily"})

    # 3. 모든 구/시·군 및 동별 페이지 추가
    for sido_path, sido_info in region_data.items():
        for dist in sido_info["districts"]:
            gu_path = dist["gu"]
            # 구 단위 허브 페이지
            url_entries.append({"loc": f"{base_url}/{sido_path}/{gu_path}/", "priority": "0.85", "changefreq": "daily"})
            
            for dong in dist["dongs"]:
                dong_path = dong
                # 동 단위 상세 페이지
                url_entries.append({"loc": f"{base_url}/{sido_path}/{gu_path}/{dong_path}/", "priority": "0.8", "changefreq": "weekly"})

    # XML 문서 생성
    xml_content = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml_content.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    for entry in url_entries:
        xml_content.append("  <url>")
        xml_content.append(f"    <loc>{entry['loc']}</loc>")
        xml_content.append(f"    <lastmod>{today}</lastmod>")
        xml_content.append(f"    <changefreq>{entry['changefreq']}</changefreq>")
        xml_content.append(f"    <priority>{entry['priority']}</priority>")
        xml_content.append("  </url>")

    xml_content.append("</urlset>")

    # public 폴더 아래 저장
    os.makedirs("public", exist_ok=True)
    file_name = "public/sitemap.xml"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("\n".join(xml_content))

    print(f"🎉 총 {len(url_entries)}개의 URL이 포함된 사이트맵이 public/sitemap.xml로 생성되었습니다!")

if __name__ == "__main__":
    generate_sitemap()