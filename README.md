# MELOG (Musical Engineering LOgic Graph)

**MELOG** is a music-based engineering data language that coordinates the world by converting the 6-line system of guitar TAB tablature into data categories, fret numbers into logical states, and the grid of *Jeongganbo* (traditional Korean notation) into an absolute time axis.

---

## 📑 Table of Contents
1. [Philosophy and Purpose](#1-philosophy-and-purpose)
2. [System and Symbol Definitions](#2-system-and-symbol-definitions)
3. [Morphology and Phonology](#3-morphology-and-phonology)
4. [Syntax](#4-syntax)
5. [Advanced Control Logic](#5-advanced-control-logic)
6. [Example: $DOMAIN ROBOTICS](#example-domain-robotics)
7. [Korean Documentation](#korean-documentation)

---

## 1. Philosophy and Purpose
*   **Language Type:** An engineering language aiming for both Logical Rigor and Experimental Information Compression.
*   **Core Objective:** Maximizing non-ambiguity and data compression during the transmission of research and academic data.

### Guiding Principles
*   **[Principle 1]** Every word has unique coordinates (TAB), and every relationship is calculated using musical symbols.
*   **[Principle 2]** The **Linear Mode** is for recording thoughts, while the **Graphical Mode** is for sharing insights.
*   **[Principle 3]** All numbers are automatically interpreted as 'Frets' or 'Numeric Values' based on the defined domain.

## 🌐 Potential Applications
MELOG serves as a powerful data interface in domains requiring high precision and information density:

*   **Robotics:** Recording multi-axis joint coordinates and precise control sequences.
*   **Autonomous Driving & Aerospace:** Compressing and monitoring high-speed sensor data streams in a graphical score format.
*   **Quant (Finance):** Analyzing correlations in multi-variable financial derivatives through rhythmic and harmonic structures.
*   **Defense & Security:** Encrypted transmission of unstructured data and schematic representation of real-time tactical situations.
*   **Biomedical Engineering:** Converting biosignals (EEG, ECG) into logical states for diagnostic assistance.

---

## 2. System and Symbol Definitions

### 2.1 Graphical Mode
The Graphical Mode serves as a system log sheet focusing on visual spatiality and simultaneity.

*   **X-axis (Jeongganbo Grid):** Absolute time clock. Every cell has physically identical horizontal length, representing a fixed unit of time. Coordinates within a single cell are processed in parallel.
*   **Y-axis (6-line TAB):** Data Domain. Strings 1 through 6 are responsible for fixed data categories.
*   **Data Node (Rhythmic Number):** Numbers within the grid represent states (frets), and stems control the data flow:
    *   **Up-stem:** Output (Transmission)
    *   **Down-stem:** Input (Reception)
    *   **Through-stem:** Relay and real-time processing
*   **Stem Texture:** 
    *   **Solid line:** Confirmed data
    *   **Dashed line:** Estimated data
    *   **Zigzag line:** Noise or unstable data
*   **Symbolic Operations:**
    *   **Tie:** The state value from the previous frame is maintained without change.
    *   **Slur:** Groups multiple coordinates/frames into a single logical group.
    *   **Dynamics (f, p):** Data reliability and weight ($f$: strong correlation, $p$: weak variable).
    *   **Vibrato (~~~):** Vibration within the Tolerance range.

### 2.2 Linear Mode
The Linear Mode converts score coordinates into strings, optimized for AI and data communication.

*   **Coordinate Notation:** `String'Fret` (e.g., `2'1`)
*   **Input/Output Markers:** `^` (Output/Active), `_` (Input/Passive), `|` (Relay/Real-time)
*   **Word Generation:** `Consonant (String) + Vowel (Fret)` (e.g., `NE`)
*   **Multi-digit Notation:** Fret numbers following the string number are written continuously without digit limits.
*   **Unit Declaration:** The base unit for the 3rd string is determined during domain declaration using brackets (e.g., `[kg]`). If a unit change is needed within a sentence, the standard English abbreviation in lowercase is attached directly to the value.

#### 2.2.1 Hierarchical Notation
*   **Single Tick ('):** Calls a logical state (fret number).
*   **Colon (:):** Designates a unique ID (Joint No., Sensor No.).
*   **Comma (,):** Collectively designates multiple IDs within the same domain.
*   **Complex Notation:** When designating both ID and state: `String:ID'State`.

---

## 3. Morphology and Phonology

### String (Consonant) - Data Category
| String | Category | Consonant | Phonetic (KR) |
| :--- | :--- | :--- | :--- |
| 1 | Time / Order / Frequency | **N** | ㄴ (Alveolar Nasal) |
| 2 | Subject / Object / Variable | **T** | ㄷ (Alveolar Plosive) |
| 3 | Value / Quantity / Range | **K** | ㄱ (Velar Plosive) |
| 4 | Status / Attribute / Property | **M** | ㅁ (Bilabial Nasal) |
| 5 | Relation / Logic / Operation | **L** | ㄹ (Liquid) |
| 6 | Environment / Background / Domain | **S** | ㅅ (Alveolar Fricative) |

### Fret (Vowel) - Logical State
| Fret | Meaning | Pronunciation |
| :--- | :--- | :--- |
| 0 | Neutral / Origin | **a** (아) |
| 1 | Positive / Internal / Forward | **e** (에) |
| 2 | Negative / External / Backward | **i** (이) |
| 3 | Repeat / Set / Multiple | **o** (오) |
| 4 | Deep / Lower / Fixed | **u** (우) |
| 5 | Expansion / Upper / Modified | **oi** (외) |
| 6 | Interior / Auxiliary / Waiting | **ʌ** (어) |
| 7 | Horizontal / Equilibrium / Pending | **ɯ** (으) |
| 8 | Focus / Emphasis / Special | **y** (위) |
| 9 | Complex / Complete / Total | **wa** (와) |

---

## 4. Syntax

### 4.0 Domain Declaration
The domain must be declared with the highest priority before any data packet or sentence group begins.

1.  **Global Declaration:**
    *   **Linear:** Write `$DOMAIN` at the top of the file/stream. Valid until session end (`||`).
    *   **Graphical:** Marked at the top-left of the first page.
2.  **Local Override:**
    *   **Linear:** Mark as `(DOMAIN)` immediately before the [Key Signature]. Valid until the end of the sentence (`||`).
    *   **Graphical:** Written in parentheses above a specific measure (grid).

### 4.1 Sentence Structure
*   **Linear:** `(Local Domain) [Key Sig][Clef][Time/Background][Subject^][Action][Object_][Conclusion] ||`

### 4.2 Key Declarators and Case Markers
*   **G> (High Clef):** State declaration (Static observation data).
*   **F> (Low Clef):** Action declaration (Dynamic energy flow).
*   **^ / _ :** Nominative (Agent) / Objective (Target).
*   **|| (Double Barline):** Sentence termination.

### 4.3 Logical and Relational Operators
*   `+` / `-` : Increase / Decrease
*   `!` / `*` : Negation (Halt) / Emphasis (Critical Point)
*   `?` : Question/Undetermined (`??`: Oscillating error, `~?`: Estimated value)
*   `~` / `:` : Connection (Belonging) / Value Assignment
*   `&` / `/` : Simultaneous Occurrence / Selective Parallel
*   `->` : Causal Relationship (Slur in score)
*   `>>` / `<<` : Crescendo (Acceleration) / Decrescendo (Deceleration)

### 4.4 Precision Control Notation
*   `\` : **Fine Calibration** (Used for micro-error correction)
*   `.` : **Single Pulse Execution** (Executes a discrete data pulse)

### 4.5 Numerical Expression & Digit Markers
Use these to compress long numbers:
*   **P** (Ending -p): $10^1$
*   **V** (Ending -v): $10^2$
*   **B** (Ending -b): $10^3$
*   **r** (re): Decimal point (`.`)
*   *Rule: Decomposition must always start from the highest digit marker (B > V > P).*

### 4.6 Numerical Decomposition Rules
1. If a **Thousands unit (`B`)** exists, the value must be decomposed based on `B` as the primary reference.
2. If the value is less than a thousand, the **Hundreds unit (`V`)** takes priority for decomposition.

### 4.7 Interpretation Priority
| String | Default Interpretation |
| :--- | :--- |
| 1, 4, 5 | Fret Priority |
| 2, 6 | ID Priority |
| 3 | Always interpreted as Physical Value |

### 4.8 Phonetic Expansion for ID Designation
Pronunciation rules when designating a specific target on String 2 (T) or String 6 (S):
*   **Rule:** `String Consonant + ID Fret Vowel + State Fret Vowel`

---

## 5. Advanced Control Logic

### 5.1 Key Signature
*   **Sharp (#):** System activation & Weight increase mode.
*   **Flat (b):** System standby & Conservative/Decrease mode.
*   **Natural (♮):** Reset all previous context variables.

### 5.2 Harmonic Collision
Conflicting data within a single grid (e.g., simultaneous + and -) is defined as **Dissonance**. The system detects this as an error or performs an offset calculation based on predefined priorities.

---

## Example: $DOMAIN ROBOTICS

### String Categories in Robotics
| String | Consonant | Original Category | Meaning in Robotics |
| :--- | :--- | :--- | :--- |
| 1 | **N** | Time / Order | Sequence and Velocity |
| 2 | **T** | Subject / Variable | Target Joint / Part |
| 3 | **K** | Value / Range | Target Value (Degree / Distance) |
| 4 | **M** | Status / Property | Motor Status |
| 5 | **L** | Relation / Logic | Inter-operational Logic |
| 6 | **S** | Environment | Sensor & Safety Feedback |

### Fret Definitions in Robotics
| Fret | Pronunciation | General Meaning | Meaning in Robotics |
| :--- | :--- | :--- | :--- |
| 0 | **a** | Neutral | Standby / Stop |
| 1 | **e** | Positive / Internal | Forward Rotation / ON |
| 2 | **i** | Negative / External | Backward Rotation / OFF |
| 3 | **o** | Repeat / Multiple | High-speed Motion Mode |
| 4 | **u** | Deep / Fixed | Torque Limit / Collision Warning |
| 5 | **oi** | Expansion / Modified | Trajectory Offset & Correction |
| 6 | **ʌ** | Interior / Auxiliary | Auxiliary Part Operation |
| 7 | **ɯ** | Horizontal / Pending | Balance Maintenance / Hold Position |
| 8 | **y** | Focus / Special | Fine Control (Precision Work) |
| 9 | **wa** | Complete / Total | Sequence Completion & Termination |

---

## Korean Documentation
원어(한국어)로 된 규칙서는 아래 링크에서 확인하실 수 있습니다.
*   [Korean Specification (README_KR.md)](./README_KR.md)

## 🛠 Tech Stack & Development Roadmap
We are planning to build a dedicated IDE for MELOG to streamline the data coordination process.

*   **Language:** Python 3.x
*   **Framework:** `PyQt6` (Currently in the learning & prototyping phase)
*   **Key Goals:**
    *   Implementation of a 6-line TAB-based data entry interface.
    *   Real-time rendering between Linear Mode (text) and Graphical Mode (score).
    *   Auto-completion features for domain-specific dictionaries.

> **Developer's Note:** I am proficient in general Python programming, but I am currently learning `PyQt` specifically for this project. Suggestions regarding GUI architecture or best practices for PyQt are highly encouraged and appreciated!
