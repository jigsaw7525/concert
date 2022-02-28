from flask import Flask, render_template
from music import *

app = Flask(__name__)


@app.route('/')
def index():
    csite, site1, site2, site3, site4, site5, site6, site7, site8, site9, site10, ctitle, title1, title2, title3, title4, title5, title6, title7, title8, title9, title10, csourceWebName, sourceWebName1, sourceWebName2, sourceWebName3, sourceWebName4, sourceWebName5, sourceWebName6, sourceWebName7, sourceWebName8, sourceWebName9, sourceWebName10, cstartDate, startDate1, startDate2, startDate3, startDate4, startDate5, startDate6, startDate7, startDate8, startDate9, startDate10 = get_music()

    return render_template("./concert.html",
                           csite=csite,
                           site1=site1,
                           site2=site2,
                           site3=site3,
                           site4=site4,
                           site5=site5,
                           site6=site6,
                           site7=site7,
                           site8=site8,
                           site9=site9,
                           site10=site10,

                           ctitle=ctitle,
                           title1=title1,
                           title2=title2,
                           title3=title3,
                           title4=title4,
                           title5=title5,
                           title6=title6,
                           title7=title7,
                           title8=title8,
                           title9=title9,
                           title10=title10,

                           csourceWebName=csourceWebName,
                           sourceWebName1=sourceWebName1,
                           sourceWebName2=sourceWebName2,
                           sourceWebName3=sourceWebName3,
                           sourceWebName4=sourceWebName4,
                           sourceWebName5=sourceWebName5,
                           sourceWebName6=sourceWebName6,
                           sourceWebName7=sourceWebName7,
                           sourceWebName8=sourceWebName8,
                           sourceWebName9=sourceWebName9,
                           sourceWebName10=sourceWebName10,

                           cstartDate=cstartDate,
                           startDate1=startDate1,
                           startDate2=startDate2,
                           startDate3=startDate3,
                           startDate4=startDate4,
                           startDate5=startDate5,
                           startDate6=startDate6,
                           startDate7=startDate7,
                           startDate8=startDate8,
                           startDate9=startDate9,
                           startDate10=startDate10,
                           )


if __name__ == '__main__':
    app.run(debug=True)
