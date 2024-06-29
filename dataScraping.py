import requests
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine, Table, Column, Integer, String, DateTime, MetaData
from urllib.parse import quote_plus
import time

def scrape_and_store_data():
    cookie = "wfmStoreId=16; kndctr_68B620B35350F1650A490D45_AdobeOrg_identity=CiY0NjQwNTk2Mjk4NDAzNjE1MjMzMTQ4NDM0ODYwOTkwNzQyODQ2NVIRCIuLouKFMhgBKgRJTkQxMAPwAYuLouKFMg==; _fbp=fb.1.1719535175397.539812915277718071; _pin_unauth=dWlkPVptRmlPREE1TVRZdE1qWmxZaTAwTm1ObUxUazBOemN0WldGak5qRmhaV0ZpWVdNdw; _gcl_au=1.1.1623023489.1719535177; ajs_anonymous_id=9644bb49-b009-45b5-a5a7-5bbd1f7ce4d7; inRedirectTestAudience=1; inRedirectGlutenFreeAudience=1; inChampagneRedirectCookie=1; inRedirectGoldPanAudience=1; sa-user-id=s%253A0-2db6acae-9bb0-5ac7-7b93-b66dff7951a1.O%252FZavnuMdpczTp4RjH%252FNIwZiiQTYgmzIZ%252Bs%252BT1Q2a8g; sa-user-id-v2=s%253ALbasrpuwWsd7k7Zt_3lRoWezxE4.8u%252Fk%252BrSICKn6B%252BtkzroqrqSK5JzT%252FQuSvZm8BPoNGXo; sa-user-id-v3=s%253AAQAKIE7EpYeu6LeIS0JfHXR7fCCuV7_mRfIqJ5soZ04DBlEAEAEYAyDb6fCzBjABOgSsj1yIQgQ1HfKO.X8rg52Ti%252Fq6u0%252ByX19HcMylWT9gRqSVEToiR9MJ4wdQ; _pin_unauth=dWlkPVptRmlPREE1TVRZdE1qWmxZaTAwTm1ObUxUazBOemN0WldGak5qRmhaV0ZpWVdNdw; __stripe_mid=39de8629-e9b3-40ad-baf4-9d427eb36b388f6164; ajs_anonymous_id=9644bb49-b009-45b5-a5a7-5bbd1f7ce4d7; __cf_bm=49ltmfGLrlut8jPZA.fT9JgguAG8SOfSpdt1ntL8lCE-1719595907-1.0.1.1-dW5MUofuDfKInKn1MIB4_W.K0zH07OIY6BGcKFPAw2ZtB6xmEs514PIBeO7x_fjK.bXxtm4IKtoSCenRuDBaMQ; kndctr_68B620B35350F1650A490D45_AdobeOrg_cluster=ind1; wfm.tracking.sessionStart=1719595910813; at_check=true; AMCVS_68B620B35350F1650A490D45%40AdobeOrg=1; AMCV_68B620B35350F1650A490D45%40AdobeOrg=179643557%7CMCIDTS%7C19903%7CMCMID%7C46405962984036152331484348609907428465%7CMCAAMLH-1720200711%7C12%7CMCAAMB-1720200711%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1719603111s%7CNONE%7CMCSYNCSOP%7C411-19910%7CMCCIDH%7C0%7CvVersion%7C5.5.0; wfm.tracking.s10=1; dotcomSearchId=4433be17-0780-4a0f-a1df-78c1f5a38de0; lux_uid=171959593302937250; wfm.tracking.x2p=1; at_check=true; __stripe_sid=6c1173a9-17e4-4a84-836b-ecf57b086134a11f38; s_gpv=Search%20Results:%20pink%20lady%20apple%20|%20Wegmans; _uetsid=e627f46034e611ef83aa315f5a3a4891; _uetvid=e628582034e611efbff20daf66d39e01; session-prd-weg=.eJwdjk2PgjAYhP9Lz2qEhVW4-bExJUAXBYtcCMKrtEIhFFTY7H_fZg9zeWYyMz8ovXUgS2TfskrCDKUtdHUmQPTI7rtBEQlSskakffMAgWwEo1NeDzkjzMHRhDWfOdZCQS3Xz6PSlOvV81pZbbLDn5h7Bjk4tX-4TG64GT0a9P7-_iYnjSX7LXep8viWExqZJLyrMiyxOE9J7NwyGjDCA8OfVH6PX_7pxS702GfU_N-K9eqBeTsU9C3dnTpVWwNQ7VnEHiPiOBY0kriuykL98ML8TcJo8sOvDy9eLniDgW8tQUZzzKHtqvk9MiBuHpvvUvpwDFxrPq-zEFYYzdAgoUtZgWxjvVpra31p_v4BnkJqoA.GWCFgA.-bOQdIq3gcvIUnQSEoX53vG3TO4; _dd_s=rum=0&expire=1719596933781; mbox=session#269c6ff530a54e78923a8be18fc6b2e3#1719597895|PC#269c6ff530a54e78923a8be18fc6b2e3.41_0#1782840779"

    HEADERS = {
        'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
        'Cookie': cookie
    }

    URL = "https://shop.wegmans.com/api/v2/store_products?fulfillment_type=instore&ads_enabled=true&ads_pagination_improvements=true&limit=60&offset=0&page=1&prophetScorer=frecency&sort=rank&allow_autocorrect=true&search_is_autocomplete=false&search_provider=ic&search_term=pink%20lady%20apple&secondary_results=true&unified_search_shadow_test_enabled=false"
    
    try:
        response = requests.get(URL, headers=HEADERS)
        if response.status_code == 200:
            wegmansData = response.json()
            fruitsData = wegmansData['items']

            data_to_store = []
            for item in fruitsData:
                name = item.get('name', '')
                base_price = item.get('base_price', 0.0)
                availability_status = item.get('availability_status', False)

                if not availability_status:
                    base_price = 0.0

                current_datetime = datetime.now().replace(microsecond=0)

                data_to_store.append({
                    'name': name,
                    'base_price': base_price,
                    'scrape_datetime': current_datetime
                })

            filteredData = pd.DataFrame(data_to_store)

            password = "Sooraj@rotech2023"
            encoded_password = quote_plus(password)

            engine = create_engine(f"mysql+pymysql://sooraj_usr:{encoded_password}@localhost/wegmanData")
            metadata = MetaData()
            table_name = 'Wegmans_data'
            table = Table(table_name, metadata,
                          Column('id', Integer, primary_key=True, autoincrement=True),
                          Column('name', String(255)),
                          Column('base_price', String(10)),
                          Column('scrape_datetime', DateTime)
                          )

            metadata.create_all(engine, checkfirst=True)

            filteredData.to_sql(name=table_name, con=engine, if_exists='append', index=False)
            print(f"Data successfully inserted into MySQL table at {datetime.now().replace(microsecond=0)}.")
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
    
    except requests.RequestException as e:
        print(f"Request failed: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")
        

# Run the scraping and storing process every 5 minutes(300s)
while True:
    scrape_and_store_data()
    time.sleep(300)
