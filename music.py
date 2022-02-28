import pandas as pd
url = "https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=1"

df = pd.read_json(url).dropna()


def get_music():
    csite = ['相關網站']
    sites = df['webSales'].values.tolist()
    site1 = sites[0:5]
    site2 = sites[5:10]
    site3 = sites[10:15]
    site4 = sites[15:20]
    site5 = sites[20:25]
    site6 = sites[25:30]
    site7 = sites[30:35]
    site8 = sites[35:40]
    site9 = sites[40:45]
    site10 = sites[45:50]

    ctitle = ['節目名稱']
    titles = df['title'].values.tolist()
    title1 = titles[0:5]
    title2 = titles[5:10]
    title3 = titles[10:15]
    title4 = titles[15:20]
    title5 = titles[20:25]
    title6 = titles[25:30]
    title7 = titles[30:35]
    title8 = titles[35:40]
    title9 = titles[40:45]
    title10 = titles[45:50]

    csourceWebName = ['售票處']
    sourceWebNames = df['sourceWebName'].values.tolist()
    sourceWebName1 = sourceWebNames[0:5]
    sourceWebName2 = sourceWebNames[5:10]
    sourceWebName3 = sourceWebNames[10:15]
    sourceWebName4 = sourceWebNames[15:20]
    sourceWebName5 = sourceWebNames[20:25]
    sourceWebName6 = sourceWebNames[25:30]
    sourceWebName7 = sourceWebNames[30:35]
    sourceWebName8 = sourceWebNames[35:40]
    sourceWebName9 = sourceWebNames[40:45]
    sourceWebName10 = sourceWebNames[45:50]

    cstartDate = ['首演日期']
    startDates = df['startDate'].values.tolist()
    startDate1 = startDates[0:5]
    startDate2 = startDates[5:10]
    startDate3 = startDates[10:15]
    startDate4 = startDates[15:20]
    startDate5 = startDates[20:25]
    startDate6 = startDates[25:30]
    startDate7 = startDates[30:35]
    startDate8 = startDates[35:40]
    startDate9 = startDates[40:45]
    startDate10 = startDates[45:50]

    return csite, site1, site2, site3, site4, site5, site6, site7, site8, site9, site10,\
        ctitle, title1, title2, title3, title4, title5, title6, title7, title8, title9, title10,\
        csourceWebName, sourceWebName1, sourceWebName2, sourceWebName3, sourceWebName4, sourceWebName5, sourceWebName6, sourceWebName7, sourceWebName8, sourceWebName9, sourceWebName10,\
        cstartDate, startDate1, startDate2, startDate3, startDate4, startDate5, startDate6, startDate7, startDate8, startDate9, startDate10
