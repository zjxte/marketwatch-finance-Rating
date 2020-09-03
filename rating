import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.marketwatch.com/tools/upgrades-downgrades'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    'Cookie': 'refresh=off; letsGetMikey=enabled; ab_uuid=f457914e-a5ab-469c-98fa-c023eb4bdf91; letsGetMikey=enabled; D_IID=F8E8DC35-1CD2-3D75-A6DF-9F9D6EACBF06; D_UID=3CB4F08B-1332-3A7A-B3FC-D06680BCC14C; D_ZID=9BA4A93A-50B8-337A-9527-E34CAAD9226E; D_ZUID=310D569E-518D-3A17-BCF2-270975B97F47; D_HID=724A6829-6C57-3B68-AA0D-C1A223BF1F94; D_SID=82.12.73.19:karWOGdy3uvfhjsHLh8nifo+pAcwYqrEuY+32WH6Uuk; wsjregion=na%2Cus; usr_bkt=HY0f8Of9M1; vidoraUserId=3ifl6mfnatah7s4keafg6vlqafebfu; kayla=g=f9bd7b898b1745358746a89a91edf39d; djcs_route=4f815e1b-39c5-471b-9a80-26fb3f6e9677; TR=V2-f15b445c9abe7b58f6347fa866b00fa36f3526d51f91c11aaea54687c518c627; ssgl=false; recentqsmkii=Stock-US-TSLA|Index-DX-DAX|Stock-US-CRM|Stock-US-AMGN|Stock-US-AAPL; cbsc=false; djcs_auto=M1598907824%2Fqm6UadckfBSBcnKatYDwW%2B95UL5YvF4cbdiXrnGoLQRWXsAW2l0CIW4VFlVO3d7zYPc%2BgvQCyBLTiw%2BSwFIdIZ0oYPZqIIQA%2Bsrhq4Ly2r2hj%2Bb5nOAULIkHIVWCFiS1rv4tpxExIVR5EVH5TwnFRiZvlZo2oh01tkPptLUIYhfN7F%2F9RLqq1qYJOe9RguKof6L%2BC2JroqeCG63%2BWW6J04zG%2Bpcil3O067vllwY3Aa6hTyRIJhcfDKL36ap2UOIlnCvLj2ng861t4xOYLGArITCY%2BtKch3jIQVnPD6xjr6allJ8Phw0kfdJBKtcWuVVhihdVayidlAHLZuHX%2BDzRs5gefmDiQQjbbDsL5ZhRAZUE4HIIzlXt3taU980BX11cG; djcs_session=M1598985828%2F02d4MXd0r0y8EN33bSV9U7vxGObXzMrZY0tf0F2G%2FiP5R%2BNL2%2FBaf1FxWAm48%2FehDfyVPjwhfVJPSAlHmt7cU62dCr5oc9izeiMwQ5wgsCCJlwUj7zQkUDrwxLvisECNSa90O8b%2FHVQw0DlSIGubq6VcS0Uft1q5W3xSNCxIWCRI7GPbSFGTlk2NMvEhdzR7cGX2ooYPCeA%2F5Yo5WY9Dyi%2BTOhx%2FDfxpMPJRTjUNAqMv7stSpNJXRQfP%2Fu%2B64pWYCaNJ6R1zcU4KkYbPfDNGLgcva7pIhP1adOXZIfBc7rSQDJw8yfcWtv0Lq1BuIT3HZKcKQFbGswSgij4Cd3l4g2nwoeaztpCBZEPGn9PwPyMXOAd%2FEezsS%2Fs43VQ8WZ2gdeqRBjwIAa8FDumFB0L2Dh2YSwXDBVPjmKuB%2BIpbug5tOaxQ8cWIiioN9rBNDUZgG; DJSESSION=country%3Dgb%7C%7Ccontinent%3Deu%7C%7Cregion%3Den%7C%7Ccity%3Dhuddersfield%7C%7Clatitude%3D53.65%7C%7Clongitude%3D-1.78%7C%7Ctimezone%3Dgmt; gdprApplies=true; ccpaApplies=false; usr_prof_v2=eyJpYyI6M30%3D; AMCVS_CB68E4BA55144CAA0A4C98A5%40AdobeOrg=1; spotim_visitId={%22visitId%22:%22ceb71a3e-c25b-4638-99a8-c10035a29723%22%2C%22creationDate%22:%222020-09-01T19:57:09.238Z%22%2C%22duration%22:6}; mw_loc=%7B%22country%22%3A%22GB%22%2C%22region%22%3A%22EN%22%2C%22city%22%3A%22HUDDERSFIELD%22%2C%22county%22%3A%5B%22%22%5D%2C%22continent%22%3A%22EU%22%7D; fullcss-tools=tools-4f2bdd6f7c.min.css; icons-loaded=true; utag_main=v_id:0173a02131c3001fd81d0385fcbf03072003506a00978$_sn:12$_ss:0$_st:1598993119193$vapi_domain:marketwatch.com$ses_id:1598990229357%3Bexp-session$_pn:2%3Bexp-session$_prevpage:MW_Upgrades%20%26%20Downgrades%3Bexp-1598994919213; AMCV_CB68E4BA55144CAA0A4C98A5%40AdobeOrg=1585540135%7CMCIDTS%7C18506%7CMCMID%7C91712052039724371398153356146553616161%7CMCAID%7CNONE%7CMCOPTOUT-1598998519s%7CNONE%7CvVersion%7C4.4.0',
    'Host': 'www.marketwatch.com',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1'
}

response = requests.get(url, headers = headers)
html_content = response.text

soup = BeautifulSoup(html_content,'html.parser')

for tr in soup.find_all('tr'):
  tds = tr.find_all('td')
  print(tds)
