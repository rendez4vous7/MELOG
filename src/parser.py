import re


TOKEN_PATTERN = re.compile(
    r"(?P<clef>[GF]>)|"
    r"(?P<bracket>\[[^\]]+\])|"
    r"(?P<coord>(?P<string>\d+)(:(?P<id>\d+))?'(?P<fret>\d+)(?P<role>[\^_])?)|"
    r"(?P<end>\|\|)"
)


class MelogParser:

    def parse(self, text):

        tokens = []

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

                id_value = match.group("id")

                fret_value = int(match.group("fret"))

                role = match.group("role")

                tokens.append({
                    "type": "COORD",
                    "string": string_num,
                    "id": int(id_value) if id_value else None,
                    "fret": fret_value,
                    "role": role
                })

            elif match.group("end"):

                tokens.append({
                    "type": "END"
                })

        return tokens