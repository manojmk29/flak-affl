from urllib.parse import urlparse, urlunparse, parse_qs,urlencode


def amazonify(url):
    new_url = urlparse(url)
    if not new_url.netloc:
        return None
    query_dict = parse_qs(new_url[4])
    query_dict['tag'] = "krishnaventur-21"
    new_url = new_url[:4] + (urlencode(query_dict, True), ) + new_url[5:]
    return urlunparse(new_url)

print(amazonify("https://www.amazon.in/dp/B09TVQQGK7?ie=UTF8&ref_=s9_acss_bw_cg_survey_1a1_w&tag=krishnaventur-21&th=1"))