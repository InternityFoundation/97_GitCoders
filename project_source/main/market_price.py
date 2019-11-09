from geopy.distance import great_circle 
market_price_data = {
    'Kairana': [
 {
   "Crops": "लहसुन",
   "Min_Price": "Rs. 500",
   "Max_Price": "Rs. 1360"
 },
 {
   "Crops": "प्याज",
   "Min_Price": "Rs. 650",
   "Max_Price": "Rs. 850"
 },
 {
   "Crops": "आलू",
   "Min_Price": "Rs. 700",
   "Max_Price": "Rs. 850"
 },
 {
   "Crops": "बैगन",
   "Min_Price": "Rs. 300",
   "Max_Price": "Rs. 500"
 },
 {
   "Crops": "टमाटर",
   "Min_Price": "Rs. 850",
   "Max_Price": "Rs. 1000"
 }
],
    'Muradnagar':[
 {
   "Crops": "प्याज",
   "Min_Price": "Rs. 400",
   "Max_Price": "Rs. 1500"
 },
 {
   "Crops": "आलू",
   "Min_Price": "Rs. 300",
   "Max_Price": "Rs. 450"
 },
 {
   "Crops": "भिंडी",
   "Min_Price": "Rs. 1100",
   "Max_Price": "Rs. 1000"
 },
 {
   "Crops": "बैगन",
   "Min_Price": "Rs. 890",
   "Max_Price": "Rs. 1000"
 },
 {
   "Crops": "हरी मिर्च",
   "Min_Price": "Rs. 1500",
   "Max_Price": "Rs. 2000"
 },
 {
   "Crops": "टमाटर",
   "Min_Price": "Rs. 1100",
   "Max_Price": "Rs. 1500"
 }
],
    'Khatauli':[
 {
   "Crops": "आलू",
   "Min_Price": "Rs. 350",
   "Max_Price": "Rs. 500"
 },
 {
   "Crops": "बैगन",
   "Min_Price": "Rs. 350",
   "Max_Price": "Rs. 440"
 },
 {
   "Crops": "फूल गोभी",
   "Min_Price": "Rs. 400",
   "Max_Price": "Rs. 580"
 },
 {
   "Crops": "हरी मिर्च",
   "Min_Price": "Rs. 900",
   "Max_Price": "Rs. 1360"
 },
 {
   "Crops": "टमाटर",
   "Min_Price": "Rs. 700",
   "Max_Price": "Rs. 980"
 }
],
    'Ghaziabad':[
 {
   "Crops": "अरहर ( तुवर )",
   "Min_Price": "Rs. 4000",
   "Max_Price": "Rs. 5500"
 },
 {
   "Crops": "उड़द",
   "Min_Price": "Rs. 3500",
   "Max_Price": "Rs. 4500"
 },
 {
   "Crops": "चना",
   "Min_Price": "Rs. 3500",
   "Max_Price": "Rs. 4800"
 },
 {
   "Crops": "रायड़ा ( सरसों )",
   "Min_Price": "Rs. 3500",
   "Max_Price": "Rs. 4332"
 },
 {
   "Crops": "प्याज",
   "Min_Price": "Rs. 2200",
   "Max_Price": "Rs. 3000"
 },
 {
   "Crops": "चावल",
   "Min_Price": "Rs. 2650",
   "Max_Price": "Rs. 2800"
 },
 {
   "Crops": "सोयाबीन",
   "Min_Price": "Rs. 3400",
   "Max_Price": "Rs. 3885"
 },
 {
   "Crops": "गेहू एवरेज",
   "Min_Price": "Rs. 1700",
   "Max_Price": "Rs. 1980"
 },
 {
   "Crops": "बैगन",
   "Min_Price": "Rs. 800",
   "Max_Price": "Rs. 1300"
 },
 {
   "Crops": "फूल गोभी",
   "Min_Price": "Rs. 1800",
   "Max_Price": "Rs. 2210"
 },
 {
   "Crops": "हरी मिर्च",
   "Min_Price": "Rs. 2000",
   "Max_Price": "Rs. 2350"
 },
 {
   "Crops": "टमाटर",
   "Min_Price": "Rs. 1650",
   "Max_Price": "Rs. 2130"
 }
],
    'Thanabhawan':[
 {
   "Crops": "लहसुन",
   "Min_Price": "Rs. 2500",
   "Max_Price": "Rs. 4000"
 },
 {
   "Crops": "प्याज",
   "Min_Price": "Rs. 2000",
   "Max_Price": "Rs. 2500"
 },
 {
   "Crops": "आलू",
   "Min_Price": "Rs. 700",
   "Max_Price": "Rs. 1200"
 },
 {
   "Crops": "भिंडी",
   "Min_Price": "Rs. 500",
   "Max_Price": "Rs. 700"
 },
 {
   "Crops": "बैगन",
   "Min_Price": "Rs. 400",
   "Max_Price": "Rs. 500"
 },
 {
   "Crops": "हरी मिर्च",
   "Min_Price": "Rs. 900",
   "Max_Price": "Rs. 1100"
 },
 {
   "Crops": "टमाटर",
   "Min_Price": "Rs. 600",
   "Max_Price": "Rs. 800"
 }
],
    'Achnera':[
 {
   "Crops": "बाजरा",
   "Min_Price": "Rs. 1400",
   "Max_Price": "Rs. 1700"
 },
 {
   "Crops": "जौ",
   "Min_Price": "Rs. 1500",
   "Max_Price": "Rs. 1900"
 },
 {
   "Crops": "ग्वार",
   "Min_Price": "Rs. 2000",
   "Max_Price": "Rs. 3250"
 },
 {
   "Crops": "रायड़ा ( सरसों )",
   "Min_Price": "Rs. 2500",
   "Max_Price": "Rs. 4210"
 },
 {
   "Crops": "प्याज",
   "Min_Price": "Rs. 2800",
   "Max_Price": "Rs. 3700"
 },
 {
   "Crops": "आलू",
   "Min_Price": "Rs. 650",
   "Max_Price": "Rs. 900"
 },
 {
   "Crops": "चावल",
   "Min_Price": "Rs. 2200",
   "Max_Price": "Rs. 2560"
 },
 {
   "Crops": "गेहू एवरेज",
   "Min_Price": "Rs. 1700",
   "Max_Price": "Rs. 2000"
 },
 {
   "Crops": "हरी मिर्च",
   "Min_Price": "Rs. 2100",
   "Max_Price": "Rs. 2650"
 },
 {
   "Crops": "टमाटर",
   "Min_Price": "Rs. 2400",
   "Max_Price": "Rs. 2550"
 }
],
    'Agra':[
 {
   "Crops": "अरहर ( तुवर )",
   "Min_Price": "Rs. 3500",
   "Max_Price": "Rs. 5150"
 },
 {
   "Crops": "बाजरा",
   "Min_Price": "Rs. 1400",
   "Max_Price": "Rs. 1690"
 },
 {
   "Crops": "जौ",
   "Min_Price": "Rs. 1550",
   "Max_Price": "Rs. 1880"
 },
 {
   "Crops": "लहसुन",
   "Min_Price": "Rs. 4000",
   "Max_Price": "Rs. 7200"
 },
 {
   "Crops": "मुंग",
   "Min_Price": "Rs. 4000",
   "Max_Price": "Rs. 5650"
 },
 {
   "Crops": "मसूर",
   "Min_Price": "Rs. 4200",
   "Max_Price": "Rs. 4950"
 },
 {
   "Crops": "मक्का",
   "Min_Price": "Rs. 1650",
   "Max_Price": "Rs. 1990"
 },
 {
   "Crops": "रायड़ा ( सरसों )",
   "Min_Price": "Rs. 3400",
   "Max_Price": "Rs. 3740"
 },
 {
   "Crops": "प्याज",
   "Min_Price": "Rs. 2800",
   "Max_Price": "Rs. 3450"
 },
 {
   "Crops": "आलू",
   "Min_Price": "Rs. 850",
   "Max_Price": "Rs. 950"
 },
 {
   "Crops": "चावल",
   "Min_Price": "Rs. 2200",
   "Max_Price": "Rs. 2560"
 },
 {
   "Crops": "गेहू एवरेज",
   "Min_Price": "Rs. 1700",
   "Max_Price": "Rs. 1980"
 },
 {
   "Crops": "भिंडी",
   "Min_Price": "Rs. 1200",
   "Max_Price": "Rs. 1400"
 },
 {
   "Crops": "बैगन",
   "Min_Price": "Rs. 1200",
   "Max_Price": "Rs. 1500"
 },
 {
   "Crops": "हरी मिर्च",
   "Min_Price": "Rs. 1500",
   "Max_Price": "Rs. 3000"
 },
 {
   "Crops": "टमाटर",
   "Min_Price": "Rs. 2100",
   "Max_Price": "Rs. 2850"
 }
],
    'Fatehabad':[
 {
   "Crops": "बाजरा",
   "Min_Price": "Rs. 1400",
   "Max_Price": "Rs. 1630"
 },
 {
   "Crops": "जौ",
   "Min_Price": "Rs. 1000",
   "Max_Price": "Rs. 1220"
 },
 {
   "Crops": "लहसुन",
   "Min_Price": "Rs. 2200",
   "Max_Price": "Rs. 7000"
 },
 {
   "Crops": "रायड़ा ( सरसों )",
   "Min_Price": "Rs. 3300",
   "Max_Price": "Rs. 3750"
 },
 {
   "Crops": "प्याज",
   "Min_Price": "Rs. 2400",
   "Max_Price": "Rs. 3100"
 },
 {
   "Crops": "आलू",
   "Min_Price": "Rs. 500",
   "Max_Price": "Rs. 810"
 },
 {
   "Crops": "चावल",
   "Min_Price": "Rs. 2000",
   "Max_Price": "Rs. 2360"
 },
 {
   "Crops": "गेहू एवरेज",
   "Min_Price": "Rs. 1650",
   "Max_Price": "Rs. 1950"
 },
 {
   "Crops": "भिंडी",
   "Min_Price": "Rs. 1700",
   "Max_Price": "Rs. 2500"
 },
 {
   "Crops": "बैगन",
   "Min_Price": "Rs. 1000",
   "Max_Price": "Rs. 1200"
 },
 {
   "Crops": "फूल गोभी",
   "Min_Price": "Rs. 2500",
   "Max_Price": "Rs. 4000"
 },
 {
   "Crops": "टमाटर",
   "Min_Price": "Rs. 1400",
   "Max_Price": "Rs. 1850"
 }
],
    'Fatehpur':[
 {
   "Crops": "बाजरा",
   "Min_Price": "Rs. 1550",
   "Max_Price": "Rs. 1750"
 },
 {
   "Crops": "जौ",
   "Min_Price": "Rs. 1550",
   "Max_Price": "Rs. 1920"
 },
 {
   "Crops": "रायड़ा ( सरसों )",
   "Min_Price": "Rs. 3200",
   "Max_Price": "Rs. 3660"
 },
 {
   "Crops": "प्याज",
   "Min_Price": "Rs. 2800",
   "Max_Price": "Rs. 3170"
 },
 {
   "Crops": "आलू",
   "Min_Price": "Rs. 680",
   "Max_Price": "Rs. 900"
 },
 {
   "Crops": "चावल",
   "Min_Price": "Rs. 2250",
   "Max_Price": "Rs. 2600"
 },
 {
   "Crops": "गेहू एवरेज",
   "Min_Price": "Rs. 1750",
   "Max_Price": "Rs. 2000"
 },
 {
   "Crops": "बैगन",
   "Min_Price": "Rs. 700",
   "Max_Price": "Rs. 1040"
 },
 {
   "Crops": "फूल गोभी",
   "Min_Price": "Rs. 1250",
   "Max_Price": "Rs. 1650"
 },
 {
   "Crops": "हरी मिर्च",
   "Min_Price": "Rs. 1680",
   "Max_Price": "Rs. 2270"
 },
 {
   "Crops": "टमाटर",
   "Min_Price": "Rs. 1700",
   "Max_Price": "Rs. 2430"
 }
],
    'Hapur': [
 {
   "Crops": "मक्का",
   "Min_Price": "Rs. 1750",
   "Max_Price": "Rs. 2050"
 },
 {
   "Crops": "रायड़ा ( सरसों )",
   "Min_Price": "Rs. 3000",
   "Max_Price": "Rs. 4300"
 },
 {
   "Crops": "प्याज",
   "Min_Price": "Rs. 2400",
   "Max_Price": "Rs. 2800"
 },
 {
   "Crops": "आलू",
   "Min_Price": "Rs. 800",
   "Max_Price": "Rs. 930"
 },
 {
   "Crops": "चावल",
   "Min_Price": "Rs. 2500",
   "Max_Price": "Rs. 2900"
 },
 {
   "Crops": "गेहू एवरेज",
   "Min_Price": "Rs. 1700",
   "Max_Price": "Rs. 2040"
 },
 {
   "Crops": "बैगन",
   "Min_Price": "Rs. 700",
   "Max_Price": "Rs. 1050"
 },
 {
   "Crops": "हरी मिर्च",
   "Min_Price": "Rs. 1400",
   "Max_Price": "Rs. 1950"
 },
 {
   "Crops": "टमाटर",
   "Min_Price": "Rs. 1100",
   "Max_Price": "Rs. 1550"
 }
],
    'Kadhle':[
 {
   "Crops": "लहसुन",
   "Min_Price": "Rs. 2540",
   "Max_Price": "Rs. 4000"
 },
 {
   "Crops": "प्याज",
   "Min_Price": "Rs. 1700",
   "Max_Price": "Rs. 2400"
 },
 {
   "Crops": "आलू",
   "Min_Price": "Rs. 600",
   "Max_Price": "Rs. 1000"
 },
 {
   "Crops": "भिंडी",
   "Min_Price": "Rs. 500",
   "Max_Price": "Rs. 850"
 },
 {
   "Crops": "बैगन",
   "Min_Price": "Rs. 450",
   "Max_Price": "Rs. 610"
 },
 {
   "Crops": "हरी मिर्च",
   "Min_Price": "Rs. 1500",
   "Max_Price": "Rs. 2000"
 },
 {
   "Crops": "टमाटर",
   "Min_Price": "Rs. 1000",
   "Max_Price": "Rs. 1240"
 }
],
    'Muzaffarnagar':[
 {
   "Crops": "जौ",
   "Min_Price": "Rs. 1550",
   "Max_Price": "Rs. 1950"
 },
 {
   "Crops": "उड़द एवरेज",
   "Min_Price": "Rs. 4000",
   "Max_Price": "Rs. 5100"
 },
 {
   "Crops": "लहसुन",
   "Min_Price": "Rs. 4500",
   "Max_Price": "Rs. 7100"
 },
 {
   "Crops": "मसूर",
   "Min_Price": "Rs. 3650",
   "Max_Price": "Rs. 5450"
 },
 {
   "Crops": "मक्का",
   "Min_Price": "Rs. 1750",
   "Max_Price": "Rs. 2010"
 },
 {
   "Crops": "रायड़ा ( सरसों )",
   "Min_Price": "Rs. 3400",
   "Max_Price": "Rs. 3740"
 },
 {
   "Crops": "प्याज",
   "Min_Price": "Rs. 1850",
   "Max_Price": "Rs. 2300"
 },
 {
   "Crops": "आलू",
   "Min_Price": "Rs. 750",
   "Max_Price": "Rs. 950"
 },
 {
   "Crops": "चावल",
   "Min_Price": "Rs. 2400",
   "Max_Price": "Rs. 2750"
 },
 {
   "Crops": "गेहू एवरेज",
   "Min_Price": "Rs. 1600",
   "Max_Price": "Rs. 2020"
 },
 {
   "Crops": "भिंडी",
   "Min_Price": "Rs. 550",
   "Max_Price": "Rs. 1010"
 },
 {
   "Crops": "बैगन",
   "Min_Price": "Rs. 650",
   "Max_Price": "Rs. 1010"
 },
 {
   "Crops": "फूल गोभी",
   "Min_Price": "Rs. 1600",
   "Max_Price": "Rs. 1870"
 },
 {
   "Crops": "हरी मिर्च",
   "Min_Price": "Rs. 1650",
   "Max_Price": "Rs. 1910"
 },
 {
   "Crops": "टमाटर",
   "Min_Price": "Rs. 1750",
   "Max_Price": "Rs. 2200"
 }
],
    'Noida': [
 {
   "Crops": "प्याज",
   "Min_Price": "Rs. 2500",
   "Max_Price": "Rs. 3000"
 },
 {
   "Crops": "आलू",
   "Min_Price": "Rs. 700",
   "Max_Price": "Rs. 1100"
 },
 {
   "Crops": "बैगन",
   "Min_Price": "Rs. 750",
   "Max_Price": "Rs. 936"
 },
 {
   "Crops": "हरी मिर्च",
   "Min_Price": "Rs. 900",
   "Max_Price": "Rs. 1024"
 },
 {
   "Crops": "टमाटर",
   "Min_Price": "Rs. 1400",
   "Max_Price": "Rs. 2200"
 }
],
    'Shamli': [
 {
   "Crops": "लहसुन",
   "Min_Price": "Rs. 4500",
   "Max_Price": "Rs. 6400"
 },
 {
   "Crops": "मुंगफली",
   "Min_Price": "Rs. 4500",
   "Max_Price": "Rs. 5200"
 },
 {
   "Crops": "मसूर",
   "Min_Price": "Rs. 4500",
   "Max_Price": "Rs. 5385"
 },
 {
   "Crops": "मक्का",
   "Min_Price": "Rs. 1650",
   "Max_Price": "Rs. 2050"
 },
 {
   "Crops": "रायड़ा ( सरसों )",
   "Min_Price": "Rs. 2500",
   "Max_Price": "Rs. 4260"
 },
 {
   "Crops": "प्याज",
   "Min_Price": "Rs. 2400",
   "Max_Price": "Rs. 2900"
 },
 {
   "Crops": "आलू",
   "Min_Price": "Rs. 700",
   "Max_Price": "Rs. 1200"
 },
 {
   "Crops": "चावल",
   "Min_Price": "Rs. 2200",
   "Max_Price": "Rs. 2780"
 },
 {
   "Crops": "गेहू एवरेज",
   "Min_Price": "Rs. 1650",
   "Max_Price": "Rs. 2010"
 },
 {
   "Crops": "बैगन",
   "Min_Price": "Rs. 800",
   "Max_Price": "Rs. 1050"
 },
 {
   "Crops": "हरी मिर्च",
   "Min_Price": "Rs. 1800",
   "Max_Price": "Rs. 2500"
 },
 {
   "Crops": "टमाटर",
   "Min_Price": "Rs. 1500",
   "Max_Price": "Rs. 2200"
 }
]
}



def find_nearest_city_market(city_name):
    latlon = {
        "Achnera":(27.1774, 77.7538),
        "Agra":(27.1767, 78.0081),
        "Fatehabad":(29.5132, 75.4510),
        "Fatehpur":(25.9210, 80.7996),
        "Ghaziabad":(28.6692, 77.4538),
        "Hapur":(28.7306, 77.7759),
        "Kadhle":(29.3239, 77.2721),
        "Kairana":(29.3940, 77.2003),
        "Khatauli":(29.2773, 77.7338),
        "Muradnagar":(28.7718, 77.5075),
        "Muzaffarnagar":(29.4727, 77.7085),
        "Noida":(28.5355, 77.3910),
        "Shamli":(29.4502, 77.3172),
        "Thanabhawan":(29.5875, 77.4168)
    }
    
    dist = []
    for city in latlon:
        dist.append((great_circle(latlon[city_name], latlon[city]).km, city))
    preferred = sorted(dist)[0:4]
    result = []
    for i in preferred:
        result.append({i[1]: market_price_data[i[1]]})
    return result
    # for c in preferred:
    #     print(c[1])
    #     print("Crops"+"             Min Price"+"          Max Price")
    #     for row in x[c[1]]:
    #         print(row["Crops"]+"            "+row["Min_Price"]+"             "+row["Max_Price"])