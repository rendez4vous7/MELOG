import re
from models import MelogNode, MelogCell


TOKEN_PATTERN = re.compile(
    r"(?P<clef>[GF]>)|"
    r"(?P<bracket>\[[^\]]+\])|"
    r"(?P<coord>(?P<string>\d+)(:(?P<id>\d+))?'(?P<fret>\d+)(?P<role>[\^_])?)|"
    r"(?P<end>\|\|)|"
    r"(?P<cell>;)"
)


class MelogParser:

    def parse(self, text):

        tokens = []
        current_cell = MelogCell(time=0)
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
                id_value = match.group("id")

                if id_value is not None:
                    id_value = int(id_value)

                role = match.group("role") or ""

                if role == "^":

                    stem = "up"


                elif role == "_":

                    stem = "down"


                else:

                    stem = "through"

                node = MelogNode(
                        string=string_num,
                        id=id_value,
                        fret=fret_value,
                        time=time_index,
                        role=role,
                        stem=stem
                    )

                current_cell.nodes.append(node)



            elif match.group("cell"):

                tokens.append(current_cell)

                time_index += 1

                current_cell = MelogCell(

                    time=time_index

                )


            elif match.group("end"):

                tokens.append(current_cell)

                tokens.append({

                    "type": "END"

                })

                time_index = 0

                current_cell = MelogCell(

                    time=time_index

                )

        return tokens