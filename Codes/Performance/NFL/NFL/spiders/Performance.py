import scrapy


class PerformaceSpider(scrapy.Spider):
    name = 'Performance'
    REDIRECT_MAX = 50

    def team_parse(self, ini):
        if ini == "ATL":
            return "Atlanta Falcons"
        elif ini == "ARI":
            return "Arizona Cardinals"
        elif ini == "BAL":
            return "Baltimore Ravens"
        elif ini == "BUF":
            return "Buffalo Bills"
        elif ini == "MIA":
            return "Miami Dolphins"
        elif ini == "NE":
            return "New England Patriots"
        elif ini == "NYJ":
            return "New York Jets"
        elif ini == "DAL":
            return "Dallas Cowboys"
        elif ini == "NYG":
            return "New York Giants"
        elif ini == "PHI":
            return "Philadelphia Eagles"
        elif ini == "WSH":
            return "Washington Redskins"
        elif ini == "CIN":
            return "Cincinnati Bengals"
        elif ini == "CLE":
            return "Cleveland Browns"
        elif ini == "PIT":
            return "Pittsburgh Steelers"
        elif ini == "CHI":
            return "Chicago Bears"
        elif ini == "DET":
            return "Detroit Lions"
        elif ini == "GB":
            return "Green Bay Packers"
        elif ini == "MIN":
            return "Minnesota Vikings"
        elif ini == "HOU":
            return "Houston Texans"
        elif ini == "IND":
            return "Indianapolis Colts"
        elif ini == "JAX":
            return "Jacksonville Jaguars"
        elif ini == "TEN":
            return "Tennesse Titans"
        elif ini == "CAR":
            return "Carolina Panthers"
        elif ini == "NO":
            return "New Orleans Saints"
        elif ini == "TB":
            return "Tampa Bay Buccaneers"
        elif ini == "DEN":
            return "Denver Broncos"
        elif ini == "KC":
            return "Kansas City Chiefs"
        elif ini == "LAC":
            return "Los Angeles Chargers"
        elif ini == "OAK":
            return "Oakland Raiders"
        elif ini == "LAR":
            return "Los Angeles Rams"
        elif ini == "SF":
            return "San Francisco 49ers"
        elif ini == "SEA":
            return "Seattle Seahawks"

    def start_requests(self):
        url = ['http://www.espn.com/nfl/statistics/player/_/stat/defense/sort/totalTackles/year/2017']

        yield scrapy.Request(url = url[0], callback = self.parse)

    def parse(self, response):
        i = 0
        for row in response.xpath('//*[@class="tablehead"]//tr'):
            if i == 12:
                i = 0
            if i > 1:
                team = self.team_parse(row.xpath('td//text()')[3].extract())
                yield{
                    'name' :  row.xpath('td//text()')[1].extract(),
                    'team' :  team,
                    'ast' :   row.xpath('td//text()')[4].extract(),
                    'total' : row.xpath('td//text()')[5].extract(),
                    'comb' :  row.xpath('td//text()')[6].extract(),
                    'sack' :  row.xpath('td//text()')[7].extract(),
                    'ydsl' :  row.xpath('td//text()')[8].extract(),
                    'pd' :    row.xpath('td//text()')[9].extract(),
                    'int' :   row.xpath('td//text()')[10].extract(),
                    'yds' :   row.xpath('td//text()')[11].extract(),
                    'long' :  row.xpath('td//text()')[12].extract(),
                    'itd' :   row.xpath('td//text()')[13].extract(),
                    'ff' :    row.xpath('td//text()')[14].extract(),
                    'rec' :   row.xpath('td//text()')[15].extract(),
                    'ftd' :   row.xpath('td//text()')[16].extract()
                }

            i += 1
