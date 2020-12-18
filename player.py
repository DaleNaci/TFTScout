import bs4 as bs
import urllib.request


class Player:
    def __init__(self, sn):
        self.summoner_name = sn
        self.champ_uses = {}
        self.__obtain_info()


    def __obtain_info(self):
        url = f"https://lolchess.gg/profile/na/{self.summoner_name}"
        source = urllib.request.urlopen(url).read()
        soup = bs.BeautifulSoup(source, "lxml")

        table = soup.find("div", class_="profile__recent__trends__units"
                          ).find("table")

        name_td_tags = table.find_all("td", "name")
        plays_td_tags = table.find_all("td", "plays")

        for name_td, plays_td in zip(name_td_tags, plays_td_tags):
            self.champ_uses[name_td.text.strip()] = int(plays_td.text.strip())


    def __str__(self):
        text = f"{self.summoner_name}\n"

        for champ, uses in self.champ_uses.items():
            print(f"{champ} - {uses}")
            text += f"{champ} - {uses}\n"

        return text
