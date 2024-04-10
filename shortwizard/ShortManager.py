from enum import Enum
import json

class ShortManager:

    def __init__(self, path, Class):
        

        self.group_name = str(path).split("/")[-1].replace(".json", "")

        with open(path, encoding="utf-8") as text_bank:
            json_short_list = json.load(text_bank)

            if isinstance(json_short_list, list):
                self.shorts = [Class(short, index)
                               for index, short in enumerate(json_short_list)]
            else:
                self.shorts = [Class(json_short_list, 0)]

    def get_group_name(self):
        return self.group_name

    def get_next_short(self):
        short = self.shorts.pop(0)
        self.current_short = short
        return short

    def has_next_short(self):
        return len(self.shorts) > 0