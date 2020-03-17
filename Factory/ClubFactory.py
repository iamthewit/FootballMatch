from random import choice

from FootballMatch.Club import Club


class ClubFactory:
    def create(self):
        club_name = self.get_random_name() + " FC"
        club_name.capitalize()

        return Club(club_name)

    def get_random_name(self):
        word_file_path = "/usr/share/dict/words"
        word_file = open(word_file_path)
        name = choice(word_file.read().splitlines())
        word_file.close()

        return name

