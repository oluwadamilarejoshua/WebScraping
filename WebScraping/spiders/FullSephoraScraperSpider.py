import scrapy
import requests
import json


def total_products_in_cat(url, page):
    ohh = os.getenv('326742128_80h100vCRCFOFTTITRKRCNJQSOJFJCPHJNVNMKH-0e0')
    headers = {
        'authority': 'www.sephora.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        'cookie': f"site_language=en; site_locale=ca; ConstructorioID_client_id=1dbfdbe6-0d80-4e5b-a701-b377f48bbc4b; s_ecid=MCMID%7C50180585077517533594566970019201084328; RES_TRACKINGID=830534701978109; ResonanceSegment=1; mdLogger=false; kampyle_userid=8475-9830-309e-931f-7e1c-505c-9ede-f657; cd_user_id=17f2a88e963cc-06d0017c0ff128-4e60796b-e1000-17f2a88e9641ee; BVBRANDID=69968a70-27b8-4f3a-ad4a-df56870902e8; _gcl_au=1.1.1605724288.1645686125; sti=34843f25-34a1-4f31-aadd-030e8c464e4c; _cs_c=1; __gads=ID=bc1b047c158f37cb:T=1645686132:S=ALNI_MbzOo4jrZUPyvBDv7zlhUUk0cbtZQ; ab.storage.deviceId.476615b3-3386-4e1c-a9fd-7e174eb9b8de=%7B%22g%22%3A%228974ed90-48af-ceac-3d9f-75f86dfae231%22%2C%22c%22%3A1645686370658%2C%22l%22%3A1645686370658%7D; _pin_unauth=dWlkPVlqWmlNbVZtWTJJdFlqZG1PUzAwTlRFMkxUaGtOV1V0TUdZd01ESXlPV1V3TVRSag; _scid=643e0691-308d-4ddd-9016-3d0a42e45051; ftr_ncd=6; rcps_stick=RWD; __olapicU=292Os9Ar6bq8vCQEvEhLLikrVPjTFyY5; forterToken=c598a725904943b59d2f1635ddd825e9_1648661638645__UDF43-mnf_9ck; pixlee_analytics_cookie=%7B%22CURRENT_PIXLEE_USER_ID%22%3A%2205c3b288-04ad-cf7a-8c32-8d256c60c751%22%7D; pixlee_analytics_cookie_legacy=%7B%22CURRENT_PIXLEE_USER_ID%22%3A%2205c3b288-04ad-cf7a-8c32-8d256c60c751%22%7D; _clck=1nwosu0|1|f0d|0; _fbp=fb.1.1649812752266.25167788; _gid=GA1.2.907038823.1650134709; __gpi=UID=000004c644a3f650:T=1649895844:RT=1650648919:S=ALNI_MZYeIrc3MmXIdIU0ujV07Xv0Y1XEA; device_type=desktop; current_country=PK; akacd_RWASP-default-phased-release=3828153710~rv=78~id=655683d1550626d5994b54aee01cb70d; PIM-SESSION-ID=BbeQQXMIDQYIywMX; rxVisitor=1650700914536501OBB1G1BF0RMO4CFUQQHA86T5MKN2P; at_check=true; AMCVS_F6281253512D2BB50A490D45%40AdobeOrg=1; s_cc=true; rvi_36840352868=2480689; adbanners=on; dtCookie=v_4_srv_5_sn_FD534AF38DB113E703E4F93A1308505B_perc_100000_ol_0_mul_1_app-3A010ad61344e68aed_1_app-3Aea7c4b59f27d43eb_1_rcs-3Acss_0; kampyleUserSession=1650923424202; kampyleUserSessionsCount=134; AMCV_F6281253512D2BB50A490D45%40AdobeOrg=-1712354808%7CMCIDTS%7C19108%7CMCMID%7C50180585077517533594566970019201084328%7CMCAAMLH-1651528233%7C3%7CMCAAMB-1651528233%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1650930633s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-19115%7CvVersion%7C4.3.0; _sctr=1|1650913200000; dtSa=-; mp_sephora_mixpanel=%7B%22distinct_id%22%3A%20%2217f2a8901bf64-0d4ca8476137ff-4e60796b-e1000-17f2a8901c05c1%22%2C%22bc_persist_updated%22%3A%201645686096442%2C%22hasLovesList%22%3A%20false%7D; inside-sephora=805890107-8c0b298ab686bb2da658418104c2249631996e56953a2338bcaa65bf25a0e690-0-0; kampyleSessionPageCounter=2; _ga=GA1.2.602851845.1645686125; _uetsid=55caa700b34211ecb358d13540d19568; _uetvid=3c36f990954011ecb3378b8fbc6cb868; bm_sz=731CC23B20820C9EEA92E9600DBBA430~YAAQNZ4QApJA71OAAQAA4RsGZQ8FBm1CJFhTn+oxjEpS/WdnplnAAZ6WbtGwFkkJxL8MTWCUnyqAP/ZdevamhFKR6Q/gIdTvgOwOsMKxVX/a420QQkJFeHvwYAVT9SSczUP5YpsT35XGkSP3xncOdEhRkd831+RFMrHG8G95SNYlSmnYS1bfV1RsvIjJA5IHG9793tnW49SQZhoQjrPRTwHpoPgzDilLLvuLROzDEigqZQHJmpwPFV6IujZgEV4XhGgm/fIeWl/6oI128YmAhkR9gCJgaKdby7AcN9WhnP6e3iNi~3551813~3752773; ak_bmsc=30FD31892DE054BB143C5CEB132BF223~000000000000000000000000000000~YAAQPZ4QAn+wyUiAAQAAqpohZQ86/76Mokun3B4iFboS7IdOSqM4cc/84RP03rNH1crYzmpSyeOdfkbNRyK3j6o0z1cxsu4vj+lA46l/chCebtIsuxrShyReo16l092bjyGdyB47PEI8N4OKvd60Pq2wydJCptmajsiYk5CNqypoISM8BYlCV+HnGgJFhJT4Ayc1pnGBWy9/V9yrFnYtPj1M6Gq0iQnr1MvZ+Xy5G9thZpyWy1EoDsTI44wVv9Rzzj5RgJ2xVe2QRU5UxDiuzbo6yZaDfnL5T3XdCZBF4EWkmX/LOoLXn+GkPJdojRmbSh9HTixJ/Tc2Nk1NrNEp3vDZIwO7Ut3EaKB0eUL4YAlAgG/ykbyhG07i05taBHHt+ZANEIQAs1ty; akamweb=H; akavpau_akaau=1650966541~id=08ec3c6b6f67f86f0e9af344bc1ecf87; s_dl=1; _cs_mk=0.5730812990907199_1650966229512; JSESSIONID=com1-54~SfFVEwFYfCEpjD4CYWOIyHBW.com1-54; _abck=356560CD7666894233C04126853178C5~0~YAAQNZ4QAouI71OAAQAAEo9BZQd7Mkwdu7pdeYTEi7N99dNBNbqEItp8egO10rX9tJ+Q9rka2FG3WyJcr7QeMxSl40Aycp9kn27bNnKeYTCwbF0C2yHjhuN8cechRQPwi/yi93+xpXdAf4CHx0Y+Z84xkmpbnX+iNWozvjE916G5Aic9+RXfOySdN7Q2CbQnhCpNXhmTGY88frrJq3JErlaCIHbPBRGGGqA+LSoErs7YQtCacR3YeCTvvNTFSnvnW/hvwjYopyeOQsKM0it1LdrmEpIQyRbeZ9667XoCk1ZpxklmA3oSahiJOrmCh/keiW2FyJ3oohslkYCfCzC+hgIDNW9z8+sXKV1AYK9h3hC5Mmqtq3wRaGkgu/kPffUNgODjVzqX4fgF9lkfpBt4qv4aqRJbPzt9y0Q=~-1~-1~1650969744; mboxEdgeCluster=38; _cs_cvars=%7B%221%22%3A%5B%22Page%20Name%22%2C%22gifts%22%5D%2C%222%22%3A%5B%22Primary%20Category%22%2C%22Gifts%22%5D%2C%223%22%3A%5B%22Page%20Type%22%2C%22category%22%5D%2C%224%22%3A%5B%22Sephora%20Page%20Info%22%2C%22category%3Agifts%3Agifts%3A*%22%5D%7D; _cs_id=2fbbeb30-514d-a26a-f91e-7c3668db1fce.1645686128.220.1650966255.1650966220.1.1679850128526; _cs_s=2.0.0.1650968055771; ssi=34843f25-34a1-4f31-aadd-030e8c464e4c.1650966256992; s_visit=1; s_ppvl=nthlevel%253A%252450%2520and%2520under%253Agifts%253A%2A%2C88%2C83%2C7199%2C1280%2C619%2C1280%2C720%2C1.5%2CL; _ga_HX1JZMWBCJ=GS1.1.1650966230.189.1.1650966271.19; RT=\"z=1&dm=www.sephora.com&si=1ea2fa42-4981-407b-81fc-a8810fd63a8c&ss=l2fyoukg&sl=1&tt=1&bcn=%2F%2F684d0d47.akstat.io%2F&ld=xy&nu=2vihp3bm&cl=nikxt\"; mbox=PC#7a56f8d2dc6640cba7b20780e9020f36.38_0#1714211076|session#17ee6d83738b40808341a7f9f1dc06e0#1650968136; anaNextPageData=%7B%22pageName%22%3A%22nthlevel%3Amakeup%3Agifts%3A*%22%2C%22pageType%22%3A%22nthlevel%22%7D; dtLatC=4; ab.storage.sessionId.476615b3-3386-4e1c-a9fd-7e174eb9b8de=%7B%22g%22%3A%22f0b162d3-146c-a69d-04c8-bc366e5ccafd%22%2C%22e%22%3A1650968079435%2C%22c%22%3A1650966243316%2C%22l%22%3A1650966279435%7D; _gat_gtag_UA_165841114_1=1; s_ppv=nthlevel%253A%2524100%2520and%2520under%2520%253Agifts%253A%2A%2C89%2C8%2C7353%2C1280%2C261%2C1280%2C720%2C1.5%2CL; bm_sv=150471E88FE53B07E9E7D50EC54978DB~dyyJGVKhREC58k4KqTLMzah9r7HZakwghqjSRIPlGz/HbHNdDj9LnT8YURXZWvBsmW/rNhfcRd1FcLEv2xzlK6Sc/BoV7t8LIj0EiZlOZUMU4AmxfBhvRqn9O8z4TgY2774qBdlPSQyg+zIi65jJw0flSUoRAkjTA5VLu6/sMQA=; s_sq=sephoracom%3D%2526c.%2526a.%2526activitymap.%2526page%253Dnthlevel%25253A%252524100%252520and%252520under%252520%25253Agifts%25253A%25252A%2526link%253DShow%252520More%252520Products%2526region%253DBODY%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dnthlevel%25253A%252524100%252520and%252520under%252520%25253Agifts%25253A%25252A%2526pidt%253D1%2526oid%253Dfunctionhn%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DBUTTON; rxvt=1650968089972|1650965936097; dtPC=5{ohh}",
        'exclude_personalized_content': 'true',
        'referer': f'{url}',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44',
        'x-dtpc': f"5{ohh}",
        'x-dtreferer': f'{url}',
        'x-requested-source': 'rwd',
        'x-timestamp': '1650966290818',
    }

    params = {
        'targetSearchEngine': 'NLP',
        'currentPage': '1',
        'pageSize': '60',
        'content': 'true',
        'includeRegionsMap': 'true',
    }

    session = requests.Session()

    response = session.get(f'{url}', params=params, headers=headers)
    return len(response.json()), response


def scrape_products_from_response(response, url, dir_name):
    headers = {
        'authority': 'bluemercury.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        # Requests sorts cookies= alphabetically
        'cookie': '_vuid=50575891-8427-4111-bcb8-2c67bb455211; secure_customer_sig=; localization=US; _orig_referrer=https%3A%2F%2Fwww.upwork.com%2F; _landing_page=%2F; _y=bd6c7c7e-f7e7-4a2c-b939-ad75562d64dc; _shopify_y=bd6c7c7e-f7e7-4a2c-b939-ad75562d64dc; _tracking_consent=%7B%22reg%22%3A%22%22%2C%22v%22%3A%222.0%22%2C%22con%22%3A%7B%22GDPR%22%3A%22%22%7D%2C%22lim%22%3A%5B%22CCPA_BLOCK_ALL%22%2C%22GDPR%22%5D%7D; _shopify_tw=; _shopify_m=persistent; ku1-vid=ee0019fe-5b86-0d32-32ab-640620861548; _mibhv=anon-1651613394151-2417647208_6425; BVBRANDID=5d89aee1-b19d-45c4-aeb5-ac4637d7766e; swym-pid="FX2uiw+c1GfrGxB8/Pw1W3f9WFPfCiQgOVX6kwSA0wY="; _gcl_au=1.1.2093848782.1651613397; swym-swymRegid="QvSbwC2Sa7G4HqMJOveQadIafR5jH96IHBKefrqXvmuk9v0zlNKgAawUuDx5REjEvsr_0eMUKqNEsK92vD2c3kuzDqT_0CX-rAF-GZRgnCu7C0E2CGuC3hHKGo8xG2JmGPLUmCqer-MfpQZQeLhI9PBXZMmGdm_XMifUxzHyRx4"; swym-email=null; _bamls_usid=3bbb840e-af1b-4c4c-ba2a-2b21870c6c4e; swym-cu_ct=undefined; GSIDITPmVMzaL4E1=ed92ad6b-1af3-4247-9098-db2bbe578064; STSIDITPmVMzaL4E1=8e3336e2-2966-4a30-9483-829c1b20ef9d; _pin_unauth=dWlkPU5tSTBObU0zTTJNdE5tVXhaUzAwWVRSa0xXRTNOelV0TTJOaFptVmhaVFF4TkRZeQ; ltkpopup-suppression-82ba628a-4ed4-44da-981c-e9c9100839e3=1; _hjSessionUser_2095881=eyJpZCI6ImRhMDU3NzZjLTRkZTYtNTRlMS04YzJmLWU0Nzk1MmI5MmUxNiIsImNyZWF0ZWQiOjE2NTE2MTM0MDA5NjcsImV4aXN0aW5nIjp0cnVlfQ==; truyoConsent={}; rskxRunCookie=0; rCookie=5wlbni0we8nlr69uksjmal2qnzzfi; _shg_user_id=530b86ad-11ab-452b-ab76-01c5a0e04f5f; rmStore=dmid:false|amid:43420|smid:9a709236-a0b9-4a4e-a626-7728b4493dea; swym-instrumentMap={}; ku1-sid=1v9_XxetcnUE_CV44-Km9; ltkSubscriber-Header=eyJsdGtDaGFubmVsIjoiZW1haWwiLCJsdGtUcmlnZ2VyIjoibG9hZCJ9; ltkSubscriber-Footer=eyJsdGtDaGFubmVsIjoiZW1haWwiLCJsdGtUcmlnZ2VyIjoibG9hZCJ9; _gid=GA1.2.1938613967.1652042782; XsellHiPerHistory=3#; ltkpopup-session-depth=1-4; ltkSubscriber-Footer - New=eyJsdGtDaGFubmVsIjoiZW1haWwiLCJsdGtUcmlnZ2VyIjoibG9hZCIsImx0a0VtYWlsIjoiIn0%3D; nxtck-identity-mgmt=1; _s=aa4cb6d5-4094-40C5-7625-04C4BE162C81; _shopify_s=aa4cb6d5-4094-40C5-7625-04C4BE162C81; _shopify_sa_p=; swym-session-id="x5z4hrc462hxzzkentq7rva7rrwm7d3ovpwppz4tdrdjtw4nn59i6dk4of26ocee"; swym-o_s=true; _shopify_tm=; XsellHiPerRef=https%3A%2F%2Fbluemercury.com%2Fcollections%2Fmakeup%20; XsellHiPerUserAlias=%23; XsellHiPerVisit=2#1652042784; rr_rcs=eF5j4cotK8lMETC0MDPVNdQ1ZClN9kg1NUs1M7M007U0NTDTNTFITtI1NzWz1DWxNDMwMkozTktKNgUAhbMNww; BVBRANDSID=332ae72b-b670-420f-b172-ccbde1853851; _hjIncludedInSessionSample=0; _hjSession_2095881=eyJpZCI6IjAyZDE0MDhjLTZkODktNDBlNC1hOWI2LWZhMDIwNjEyZjYwMyIsImNyZWF0ZWQiOjE2NTIxMjQ2MDcwODEsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _clck=xam7tk|1|f1b|0; _shg_session_id=1c2c6801-6063-4db8-975c-7f073bda08d3; lastRskxRun=1652124615028; cto_bundle=wjoEmV9CMFNCWGYzR3ZsM0F5OUNrdEVtSHpZYXR5eHR1Y2x0N3BoQ0xHdUhtTEp1RzZPR3YzbklZdCUyQjd3NnNJYkpWJTJCS0ZwVDQ1UjR6dVZ5cGhSJTJGdXR2RDEybXY2SDdTNGZHN2JYOCUyQiUyRkhrcllEeUE4a1h2d3hkOHJOc0dtJTJGWVd5WnNoTGRnbFFtRkdFUm9jUjZuRzVXMHglMkJmQSUzRCUzRA; XsellHiPerAgentAvatar=; XsellHiPerChatWindow=%7C0%7C; XsellHiPerNoProactiveChat=no; _clsk=1b068d5|1652124684976|2|1|l.clarity.ms/collect; _shopify_sa_t=2022-05-09T19%3A33%3A06.764Z; _ga_4KL76R32P5=GS1.1.1652124598.6.1.1652124788.0; _ga=GA1.2.1099441137.1651613392; _gat=1; _gat_UA-2217560-1=1; _uetsid=ed7e7480cf0f11ec859a6d7910815d65; _uetvid=2dcee970cb2811ecafda5db1d4272fb2',
        'referer': f'{url}',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Microsoft Edge";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32',
    }
    if response:
        prod_list = {}
        for prod_ in range(len(response.json())):
            product_info = response.json()[prod_]
            product = {}
            product['ProductID'] = product_id = product_info['id']
            product['ProductName'] = product_name = product_info['title']
            product['Product_URL'] = product_url = f'https://bluemercury.com{product_info["url"]}'
            product['Price'] = product_info['price']
            product['Min_Price'] = product_info['priceMin']
            product['Max_Price'] = product_info['priceMax']
            product['Vendor'] = product_info['vendor']
            product['Is_Available'] = product_info['available']
            product_img = ''
            try:
                product_img = product_info['images'][0]['src']
                if 'http' not in product_img:
                    product_img = f'https:{product_img}'
            except:
                pass
            product['Image_URL'] = product_img

            offset = 0
            params_raw = {
                'Filter': f'ProductId:{product_id}',
                'Sort': 'SubmissionTime:desc',
                'Limit': '100',
                'Offset': f'{offset}',
                'Include': 'Products,Comments',
                'Stats': 'Reviews',
                'passkey': 'cahurH4YTLYFW0G5tMOsmjT7mau3DH0bwAqogWpgsB0SU',
                'apiversion': '5.4',
            }

            reviews_raw = requests.get('https://api.bazaarvoice.com/data/reviews.json', params=params_raw)
            total_reviews = reviews_raw.json()
            num_of_rev = total_reviews['TotalResults']
            review_dict = {'TotalReviews': num_of_rev,
                           'ReviewLanguage': total_reviews['Locale']}
            if num_of_rev is not 0:
                individual_reviews = total_reviews['Results']
                ind_rev_dict = []
                for ind in individual_reviews:
                    rate = ind['Rating']
                    range_ = ind['RatingRange']
                    review_of_each = {'UserID': ind['Id'],
                                      'SubmissionTime': ind['LastModificationTime'],
                                      'UserLocation': ind['UserLocation'],
                                      'Rating': f'{rate}/{range_}',
                                      'ReviewText': ind['ReviewText'],
                                      }
                    ind_rev_dict.append(review_of_each)
                review_dict['ProductReviews'] = ind_rev_dict

            product[f'{product_name}_reviews'] = review_dict

            prod_list[f'{dir_name}//{product_name}'] = product

        return prod_list


class BlueMercurySpider(scrapy.Spider):
    name = 'Sephora_bot'
    start_urls = [''
                  ]

    def parse(self, response):
        url = response.request.url.strip()
        print('**** SCRAPING CATEGORY: ', url)

        dir_name = url.split('/')[-1]

        scrapped_ = []

        for page in range(1, 100):
            total_products, _response_ = total_products_in_cat(url, page)
            scrapped_.append(scrape_products_from_response(_response_, url, dir_name))

        with open('Blue_Mercury_bot.json', 'w') as outfile:
            json.dump(scrapped_, outfile)
