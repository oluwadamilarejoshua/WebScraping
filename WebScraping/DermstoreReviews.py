import scrapy
from time import sleep
from random import randint
from bs4 import BeautifulSoup as bs
import requests
import json

session = requests.Session()
reviewURLs = ["https://www.dermstore.com/dhc-deep-cleansing-oil-various-sizes/11207442.reviews",
              "https://www.dermstore.com/skinmedica-ultra-sheer-moisturizer/11289690.reviews"]
product_reviews = [1428, 150]
product_url = ["https://www.dermstore.com/dhc-deep-cleansing-oil-various-sizes/11207442.reviews",
               "https://www.dermstore.com/skinmedica-ultra-sheer-moisturizer/11289690.html"]


def reveiwsFunction(session, reviews_url, product_reviews, product_url):
    review_list = []
    if int(product_reviews) > 200:
        rheaders = {
            'authority': 'www.dermstore.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-US,en;q=0.9',
            # Requests sorts cookies= alphabetically
            'cookie': f"locale_V6=en_US; LPVID=RkZTk2Mjk5MzAwOTg5Y2Zl; OptanonAlertBoxClosed=2022-05-01T11:27:32.091Z; actualOptanonConsent=%2CC0003%2CC0002%2CC0001%2CC0004%2CC0005%2C; chumewe_user=1923a016-f705-4f6a-aa99-8c8646c1df4a; _cs_c=1; _scid=18926b0e-86b3-4eec-9de7-19e23c8ad840; cjConsent=MHxOfDB8Tnww; _qubitTracker=eyk6zx06icw-0l2n7l75r-j5yy13o; qb_generic=:YB/YJp7:.dermstore.com; _pin_unauth=dWlkPU5qWmlNR0U1TldZdE1UUmhOQzAwTlRsaUxUbGpPREF0WldGaVpUVTVZbVl4WVRRNQ; dtCookie=v_4_srv_51_sn_E954BE697862BA6A2ED6185AC6EDE46A_perc_100000_ol_0_mul_1_app-3A922849586501456e_1_rcs-3Acss_0; csrf_token=91863163611717852874; rxVisitor=16525140146255PDCADCQEPL42B89I8LHDDARHBQ2P7HS; OTnoShow=popup; us_chosenSubsite_V6=us; JSESSIONID=57FD7188440288433FEA032ED80EEB6B; chumewe_sess=8ba5a154-1f05-4490-a3a7-7ed6ea580deb; NSC_mc_wtsw_efgbvmu_xfctsw_8010_J=ffffffff09031f2c45525d5f4f58455e445a4a42297a; _cs_mk_ga=0.8073409363095643_1653236034319; _gid=GA1.2.77791871.1653236035; _tq_id.TV-18454590-1.daf8=9cb831b4f21aeaeb.1653236041.0.1653236041..; LPSID-64479670=NCQDEeGvQSqe7a-ZrtSKog; _sctr=1|1653159600000; _ga_X159F68BV3=GS1.1.1653236034.3.1.1653236623.60; _ga=GA1.2.806291063.1651404465; _cs_id=c0ccc184-90d5-a5cc-8754-44d178ed27e6.1651404466.3.1653236625.1653236034.1.1685568466132; _cs_s=5.0.0.1653238425058; OptanonConsent=isGpcEnabled=0&datestamp=Sun+May+22+2022+21%3A23%3A48+GMT%2B0500+(Pakistan+Standard+Time)&version=6.32.0&isIABGlobal=false&hosts=&consentId=7f9306df-f6fb-4ede-865a-3f19d9aa1d4f&interactionCount=1&landingPath=NotLandingPage&groups=C0003%3A1%2CC0002%3A1%2CC0001%3A1%2CC0004%3A1%2CC0005%3A1&geolocation=PK%3BKP&AwaitingReconsent=false; rxvt=1653238429206|1653236031615; _uetsid=31163750d9ea11ecbb816707967200d1; _uetvid=c0dc9090c94111ec9594f15d842db693; qb_permanent=eyk6zx06icw-0l2n7l75r-j5yy13o:10:5:4:3:0::0:1:0:Bibm7B:BiimOZ:A::::182.185.22.188:kotka%20malik%20ayaz:526865:pakistan:PK:33.03:70.54:unknown:unknown:khyber%20pakhtunkhwa:25877::::YDslQ7p:YDsjAro:0:0:0::0:0:.dermstore.com:0; qb_session=5:1:13::0:YDsjAro:0:0:0:0:.dermstore.com; dtLatC=438; dtSa=true%7CC%7C-1%7CathenaProductReviews_paginationNextIcon%7C-%7C1653236939959%7C236254904_731%7Chttps%3A%2F%2Fwww.dermstore.com%2Feltamd-uv-sport-broad-spectrum-spf50-tube%2F11370299.reviews%7C%7C%7C%7C",
            'referer': f'{reviews_url}',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Microsoft Edge";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32',
        }
        rc = 0
        print('**** SCRAPING REVIEWS ...')
        for rcp in range(1, int(int(product_reviews) / 10) + 1):
            rparams = {
                'pageNumber': f'{rcp}',
            }
            sleep_time = randint(1, 3)
            print('---> Sleeping for', sleep_time)
            sleep(sleep_time)

            response3 = session.get(reviews_url, params=rparams, headers=rheaders)
            rhtml = bs(response3.text, 'lxml')
            reviews = rhtml.find_all('div', class_='athenaProductReviews_review')

            single_review = []
            for review in reviews:
                rc += 1
                review_title, review_rating, review_desc, review_owner, review_date, review_footer = '', '', '', '', '', ''
                try:
                    review_title = review.find('h3').text
                except:
                    pass
                try:
                    review_rating = review.find('span', class_='athenaProductReviews_schemaRatingValue').text.strip()
                except:
                    pass
                try:
                    review_desc = review.find('p', class_='athenaProductReviews_reviewContent').text.strip()
                except:
                    pass
                try:
                    review_footer = review.find('div', class_='athenaProductReviews_footerDateAndName').text.strip()
                except:
                    pass
                try:
                    review_date = review_footer.split('by')[0].strip()
                except:
                    pass
                try:
                    review_owner = review_footer.split('by')[1].strip()
                except:
                    pass

                prod_reviews = {
                    'No': rc,
                    # 'Product_ID': product_id,
                    # 'Product_Name': product_title,
                    'Author_Name': review_owner,
                    'Rating': review_rating,
                    'Title': review_title,
                    'ReviewText': review_desc,
                    'Date': review_date,
                }
                single_review.append(prod_reviews)

            print('**** GOT TOTAL REVIEWs..', rc)
    else:
        rc = 0
        rheaders2 = {
            'authority': 'www.dermstore.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            # Requests sorts cookies= alphabetically
            'cookie': f"locale_V6=en_US; LPVID=RkZTk2Mjk5MzAwOTg5Y2Zl; OptanonAlertBoxClosed=2022-05-01T11:27:32.091Z; actualOptanonConsent=%2CC0003%2CC0002%2CC0001%2CC0004%2CC0005%2C; chumewe_user=1923a016-f705-4f6a-aa99-8c8646c1df4a; _cs_c=1; _scid=18926b0e-86b3-4eec-9de7-19e23c8ad840; cjConsent=MHxOfDB8Tnww; _qubitTracker=eyk6zx06icw-0l2n7l75r-j5yy13o; qb_generic=:YB/YJp7:.dermstore.com; _pin_unauth=dWlkPU5qWmlNR0U1TldZdE1UUmhOQzAwTlRsaUxUbGpPREF0WldGaVpUVTVZbVl4WVRRNQ; dtCookie=v_4_srv_51_sn_E954BE697862BA6A2ED6185AC6EDE46A_perc_100000_ol_0_mul_1_app-3A922849586501456e_1_rcs-3Acss_0; csrf_token=91863163611717852874; rxVisitor=16525140146255PDCADCQEPL42B89I8LHDDARHBQ2P7HS; OTnoShow=popup; us_chosenSubsite_V6=us; _gid=GA1.2.77791871.1653236035; _tq_id.TV-18454590-1.daf8=9cb831b4f21aeaeb.1653236041.0.1653236041..; _sctr=1|1653159600000; JSESSIONID=7ACC991A48DCDC7A55268E4D36015171; chumewe_sess=fd87b853-4385-43bb-a61b-dbb42472edc8; NSC_mc_wtsw_efgbvmu_xfctsw_8010_J=ffffffff09031f5b45525d5f4f58455e445a4a42297a; _cs_mk_ga=0.2737729026300064_1653288937635; LPSID-64479670=UY-WJivpQxecnJWjmS1Upw; _ga_X159F68BV3=GS1.1.1653288937.6.1.1653289241.60; _ga=GA1.2.806291063.1651404465; _cs_id=c0ccc184-90d5-a5cc-8754-44d178ed27e6.1651404466.7.1653289242.1653288938.1.1685568466132; _cs_s=4.0.0.1653291042117; OptanonConsent=isGpcEnabled=0&datestamp=Mon+May+23+2022+12%3A00%3A44+GMT%2B0500+(Pakistan+Standard+Time)&version=6.32.0&isIABGlobal=false&hosts=&consentId=7f9306df-f6fb-4ede-865a-3f19d9aa1d4f&interactionCount=1&landingPath=NotLandingPage&groups=C0003%3A1%2CC0002%3A1%2CC0001%3A1%2CC0004%3A1%2CC0005%3A1&geolocation=PK%3BKP&AwaitingReconsent=false; qb_permanent=eyk6zx06icw-0l2n7l75r-j5yy13o:23:4:7:4:0::0:1:0:Bibm7B:BiizEf:A::::182.185.47.172:acheeni%20payan:519004:pakistan:PK:34.04:71.49:unknown:unknown:khyber%20pakhtunkhwa:25877::::YDvt+Fz:YDvs0LC:0:0:0::0:0:.dermstore.com:0; qb_session=4:1:13::0:YDvs0LC:0:0:0:0:.dermstore.com; _uetsid=31163750d9ea11ecbb816707967200d1; _uetvid=c0dc9090c94111ec9594f15d842db693; rxvt=1653291048003|1653288311667; dtLatC=2; dtSa=-",
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Microsoft Edge";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32',
        }

        presponse = session.get(f'{product_url}', headers=rheaders2)
        phtml = bs(presponse.text, 'lxml')

        reviews = phtml.find_all('div', class_='athenaProductReviews_topReviewSingle')
        single_review = []
        for review in reviews:
            rc += 1
            review_title, review_rating, review_desc, review_owner, review_date, review_footer = '', '', '', '', '', ''
            try:
                review_title = review.find('h3').text
            except:
                pass
            try:
                review_rating = review.find('div', class_='athenaProductReviews_topReviewsRatingStarsContainer').get(
                    'aria-label').split(' ')[0].strip()
            except:
                pass
            try:
                review_desc = review.find('p', class_='athenaProductReviews_topReviewsExcerpt').text.strip()
            except:
                pass
            try:
                review_footer = review.find('div', class_='athenaProductReviews_footerDateAndName').text.strip()
            except:
                pass
            try:
                review_date = review_footer.split('by')[0].strip()
            except:
                pass
            try:
                review_owner = review_footer.split('by')[1].strip()
            except:
                pass

            prod_reviews = {
                'No': rc,
                # 'Product_ID': product_id,
                # 'Product_Name': product_title,
                'Author_Name': review_owner,
                'Rating': review_rating,
                'Title': review_title,
                'ReviewText': review_desc,
                'Date': review_date,
            }
            single_review.append(prod_reviews)
    review_list.append(single_review)
    return review_list, rc


the_reviews, total = reveiwsFunction(session, reviewURLs[0], product_reviews[0], product_url[0])

with open('sampleReviews.json', 'w') as file:
    json.dump(the_reviews, file)