<div align="center">
  <h1>🐍 Hands-On Python Code2Xplore</h1>
  <p><strong>A structured collection of daily Python challenges to strengthen core programming skills.</strong></p>

  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/Progress-Day%209-success?style=for-the-badge" alt="Progress Badge"/>
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" alt="Status Badge"/>
</div>

---

## 📖 About This Repository
This repository documents my daily progress in solving Python challenges designed to strengthen core programming skills.

Each challenge focuses on applying Python concepts to practical problem statements. The aim is to build consistency, improve logical thinking, and gain confidence in writing clean and structured Python code.

---

## 📂 Completed Challenges

| Day | File Name | Description |
|:---:|:---|:---|
| **Day 1** | [`FirstDay.py`](https://github.com/SkTheAdvanceGamer/Hands_on_Python_Code2Xplore/blob/main/FirstDay.py) | Introduction to basic Python syntax |
| **Day 2** | [`day_2_smartid_credential_validator.py`](https://github.com/SkTheAdvanceGamer/Hands_on_Python_Code2Xplore/blob/main/day_2_smartid_credential_validator.py) | Input validation using conditional logic |
| **Day 3** | [`Day_3_Student_performance_Analyzer.py`](https://github.com/SkTheAdvanceGamer/Hands_on_Python_Code2Xplore/blob/main/Day_3_Student_performance_Analyzer.py) | Student marks analysis using loops and lists |
| **Day 4** | [`Day_4_Smart_List_Filter_&_Rebuilder.py`](https://github.com/SkTheAdvanceGamer/Hands_on_Python_Code2Xplore/blob/main/Day_4_Smart_List_Filter_%26_Rebuilder.py) | Filtering and rebuilding lists based on data types and conditions |
| **Day 5** | [`day_5.py`](https://github.com/SkTheAdvanceGamer/Hands_on_Python_Code2Xplore/blob/main/Smart_Transport_Load_Balancing_System_Day5.py) | Smart Transport Load Balancing System |
| **Day 6** | [`Day_6_Smart_Playlist_Intelligence_System.py`](https://github.com/SkTheAdvanceGamer/Hands_on_Python_Code2Xplore/blob/main/smart_playlist_intelligence_system_day6.py) | Playlist validation and analysis system |
| **Day 7** | [`Smart_Campus_Energy_Analyzer_day_7.py`](https://github.com/SkTheAdvanceGamer/Hands_on_Python_Code2Xplore/blob/main/Smart_Campus_Energy_Analyzer_day_7.py) | Campus energy consumption analysis with categorization and insights |
| **Day 8** | [`Day_8_Autonomous_Smart_City_Data_Intelligence_System.py`](https://github.com/SkTheAdvanceGamer/Hands_on_Python_Code2Xplore/blob/main/Day_8_Autonomous_Smart_City_Data_Intelligence_System.py) | Autonomous Smart City Data Intelligence System using Pandas & Numpy |
| **Day 9** | [`Day_9_Multi-Level_Data_Replication_&amp;_Integrity_Analyzer.py`](https://github.com/SkTheAdvanceGamer/Hands_on_Python_Code2Xplore/blob/main/Day_9_Multi-Level_Data_Replication_&amp;_Integrity_Analyzer.py) | 🌟 **NEW** Multi-Level Data Replication & Integrity Analyzer |

---

## 🌟 Daily Highlights

<details>
<summary><b>🛡️ Day 9: Multi-Level Data Replication & Integrity Analyzer</b> (Click to Expand)</summary>
<br>

The **Multi-Level Data Replication & Integrity Analyzer** demonstrates the critical differences between assignments, shallow copies, and deep copies in Python.

**Key Features:**
- 📝 **Data Generation:** Creates nested data structures representing user profiles and file usage.
- 🪞 **Replication Strategies:** Implements direct assignment, shallow copy (`list()`), and custom deep copy mechanisms.
- 🧬 **Mutation Tracking:** Modifies replicated data to observe effects on the original dataset based on the replication method used.
- 🔍 **Integrity Checking:** Uses set operations to meticulously compare original snapshots against shallow and deep copies.
- 🚨 **Leakage Detection:** Automatically detects data leakage and deep level mutations when inner references are shared.
- 📊 **Detailed Reporting:** Generates an integrity report tuple summarizing safe data, leakages, and overlaps.

</details>

<details>
<summary><b>🏙️ Day 8: Autonomous Smart City Data Intelligence System</b></summary>
<br>

The **Autonomous Smart City Data Intelligence System** evaluates multiple city zones by gathering data on Traffic, Air Quality (AQI), and Energy usage. 

**Key Features:**
- 📊 **Risk Score Engine:** Combines traffic, AQI, and energy to calculate precise risk scores with conditional bonus penalties.
- 🚦 **Intelligent Categorization:** Assigns zones as `Safe Zone`, `Moderate`, `High Risk`, or `Energy Critical`.
- 🔍 **Statistical Analysis:** Uses `numpy` for variance, min/max/average measurements, and trend analysis.
- 🚨 **High-Risk Clusters:** Automatically detects streaks of high-risk adjacent zones.
- 🗄️ **Data Tabulation:** Utilizes `pandas` DataFrames to elegantly present and format large sets of city data.
- 🏆 **Worst Zones Ranking:** Implements Bubble Sort to highlight the top 3 most critical zones.
- 🧠 **Final City Decision:** Outputs an actionable state (`City Stable`, `Moderate Risk`, `High Alert`, `Critical Emergency`).

</details>

<details>
<summary><b>⚡ Day 7: Smart Campus Energy Analyzer</b></summary>
<br>

- Collects energy readings for multiple buildings
- Categorizes usage into: Efficient (0–50), Moderate (51–150), High (>150), Invalid (<0)
- Calculates total energy consumption, highest/lowest readings
- Detects overconsumption, energy waste, and balanced usage
- Provides overall campus efficiency insights
</details>

<details>
<summary><b>🎵 Day 6: Smart Playlist Intelligence System</b></summary>
<br>

- Validation of song durations & detection of invalid inputs
- Total playlist duration calculation & duplicate duration checking
- Balance comparison between first half and second half
- Categorization of playlist (Too short, Too long, Repetitive, Balanced, Irregular)
- Generates recommendations based on playlist structure
</details>

<details>
<summary><b>📌 Day 5 Mandatory Details</b></summary>
<br>

- **L value:** 7  
- **PLI value:** 1  
- **Applied rule:** Rule B (Remove all Very Light items from the final plan)
</details>

---

## 🧠 Concepts Practiced
- **Data Science Basics:** `pandas` DataFrames and `numpy` arrays & statistical methods (New in Day 8!)
- **Control Flow:** Conditional statements (`if-else`) & Loops (`for`, `while`)
- **Algorithms:** Bubble Sort algorithm, Data filtering and logical validation
- **Data Structures:** Lists, Tuples, Sets, and Dictionaries
- **Math:** Built-in `math` library for formulas

---

## ▶️ How to Run the Programs
Ensure Python is installed on your system. Libraries like `pandas` and `numpy` might be required for recent scripts:

```bash
pip install pandas numpy
git clone https://github.com/SkTheAdvanceGamer/Hands_on_Python_Code2Xplore.git
cd Hands_on_Python_Code2Xplore
python "Day_9_Multi-Level_Data_Replication_&amp;_Integrity_Analyzer.py"
```
<p align="center">
  <i>Keep pushing the boundaries of code! 🚀</i>
</p>
