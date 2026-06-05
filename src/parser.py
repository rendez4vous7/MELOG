import re
from models import MelogNode


TOKEN_PATTERN = re.compile(
    r"(?P<clef>[GF]>)|"
    r"(?P<bracket>\[[^\]]+\])|"
    r"(?P<coord>(?P<string>\d+)(:(?P<id>\d+))?'(?P<fret>\d+)(?P<role>[\^_])?)|"
    r"(?P<end>\|\|)"
)


class MelogParser:

    def parse(self, text):

        tokens = []
        time_index = 0

        for match in TOKEN_PATTERN.finditer(text):

            if match.group("clef"):

                tokens.append({
                    "type": "CLEF",
                    "value": match.group("clef")
                })

            elif match.group("bracket"):

                content = match.group("bracket")[1:-1]

                tokens.append({
                    "type": "BRACKET",
                    "value": content
                })



            elif match.group("coord"):

                string_num = int(match.group("string"))

                fret_value = int(match.group("fret"))

                role = match.group("role") or ""

                if role == "^":

                    stem = "up"


                elif role == "_":

                    stem = "down"


                else:

                    stem = "through"

                tokens.append(

                    MelogNode(

                        string=string_num,
                        fret=fret_value,
                        time=time_index,
                        role=role,
                        stem=stem

                    )

                )

                time_index += 1

            elif match.group("end"):

                tokens.append({
                    "type": "END"
                })

        return tokens