import pandas as pd

class MelogConverter:
    def __init__(self, domain):
        self.domain = domain
        # Mapping strings to consonants
        self.strings = {
            1: {'name': 'Time/Order', 'consonant': 'N'},
            2: {'name': 'Subject/ID', 'consonant': 'T'},
            3: {'name': 'Value/Range', 'consonant': 'K'},
            4: {'name': 'Status/Property', 'consonant': 'M'},
            5: {'name': 'Logic/Operation', 'consonant': 'L'},
            6: {'name': 'Environment', 'consonant': 'S'}
        }
        # Mapping frets to vowels
        self.vowels = {
            0: 'a', 1: 'e', 2: 'i', 3: 'o', 4: 'u',
            5: 'oi', 6: 'ʌ', 7: 'ɯ', 8: 'y', 9: 'wa'
        }
        # Digit markers
        self.markers = {
            1000: 'b',
            100: 'v',
            10: 'p'
        }

    def _decompose_numeric(self, value):
        """
        Applies numerical decomposition rules
        Decomposes values using B > V > P markers.
        """
        val = int(value)

        if val < 10:
            return self.vowels[val]

        result = ""
        # Process thousands (B), hundreds (V), and tens (P)
        for unit in [1000, 100, 10]:
            count = val // unit

            if count > 0:
                # String consonant + count vowel + marker
                result += f"{self.vowels[count]}{self.markers[unit]}"
                val %= unit

        # Add remaining single digit if exists
        if val > 0 or result == "":
            result += self.vowels[val]

        return result

    def _get_phonetic(self, string_num, value):
        """
        Generate phonetic output based on string consonant + fret vowel
        Handles multi-digit expansion for string 3
        """
        consonant = self.strings[string_num]['consonant']

        # String 3 is always physical value, apply decomposition
        if string_num == 3:
            vowel_part = self._decompose_numeric(value)
        else:
            # For other strings, treat as direct Fret-to-Vowel mapping
            try:
                val_str = str(int(value))
                vowel_part = "".join([self.vowels[int(d)] for d in val_str])
            except (ValueError, KeyError):
                vowel_part = f"'{value}"

        return f"{consonant}{vowel_part}"

    def convert_row(self, row, mapping, roles=None):
        """
        Converts a CSV row into linear mode and phonetic strings.
        Includes dynamic clef (G>/F>) and case markers (^/_).
        """
        # Determine clef: F> if motor_status > 0 (action), else G> (status)
        clef = "F>" if row.get('motor_status', 0) > 0 else "G>"

        melog_elements = []
        phonetic_elements = []

        # Default roles to empty dict if not provided
        if roles is None: roles = {}

        for s_num in range(1, 7):
            if s_num in mapping:
                col_name = mapping[s_num]
                val = row[col_name]

                if pd.notna(val):
                    # Apply case markers: ^ (Agent), _ (Target)
                    marker = roles.get(s_num, "")

                    # String'Fret + Marker
                    melog_elements.append(f"{s_num}'{val}{marker}")
                    # Phonology
                    phonetic_elements.append(self._get_phonetic(s_num, val))

        # Sentence construction with dynamic clef
        linear_sentence = f"{clef} " + " ".join(melog_elements) + " ||"
        phonetic_sentence = "-".join(phonetic_elements)

        return linear_sentence, phonetic_sentence


# --- Execution Logic ---

# Test values for decomposition
data = {
    'timestamp': [1, 2, 3],
    'joint_id': [2, 2, 2],
    'angle': [45, 90, 0],
    'motor_status': [0, 8, 0],
    'sensor_feedback': [7, 7, 4]
}
df = pd.DataFrame(data)

column_mapping = {1: 'timestamp', 2: 'joint_id', 3: 'angle', 4: 'motor_status', 6: 'sensor_feedback'}

# Define which strings act as agent (^) or target (_)
role_mapping = {2: '^', 6: '_'}

converter = MelogConverter(domain="ROBOTICS")

print(f"$DOMAIN {converter.domain}\n")

for index, row in df.iterrows():
    # Pass role_mapping to apply ^ and _ markers
    linear, phonetic = converter.convert_row(row, column_mapping, roles=role_mapping)
    print(f"Log {index + 1}:")
    print(f"  Linear:   {linear}")
    print(f"  Phonetic: /{phonetic}/")
    print("-" * 40)