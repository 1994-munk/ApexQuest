# 🎮 ApexQuest Games - Player Data Analysis

<div align="center">

![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-Internal-orange?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-green?style=flat-square)
![Last Updated](https://img.shields.io/badge/Last%20Updated-May%202026-lightblue?style=flat-square)

**🚀 A powerful data analysis platform for gaming player statistics, performance metrics, and engagement insights**

[Features](#-features) • [Quick Start](#-quick-start) • [Visualizations](#-visualizations) • [Contributing](#-contributing)

</div>

---

## ⚡ Overview

ApexQuest Games Player Data Analysis is a comprehensive Python project that transforms raw player data into actionable insights. Analyze performance trends, segment players by skill levels, and discover engagement patterns with beautiful, interactive visualizations.

### 🎯 What This Project Does

- 📊 **Analyzes** player performance metrics (KDA, win rates, playtime)
- 🎯 **Segments** players by skill level and engagement
- 📈 **Visualizes** trends with 10+ chart types
- 📉 **Generates** professional reports and insights
- 🔄 **Processes** multiple data sources automatically
- 💾 **Exports** results to CSV, PNG, and TXT formats

---

## 🚀 Quick Start

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/1994-munk/ApexQuest.git
cd ApexQuestgames

# 2. Install Python 3.10+

# 3. Install dependencies
pip install -r requirements.txt
```

### 🎬 Run Analysis

```bash
# Run full automated analysis pipeline
python src/main.py

# Launch interactive Jupyter notebook
jupyter notebook notebooks/player_analysis.ipynb
```

✨ **That's it!** Results automatically save to the `outputs/` folder.

---

## 📁 Project Structure

```
ApexQuestgames/
├── 📊 data/                        # Player data (CSV files)
│   └── sample_players.csv         # Example dataset
├── 🐍 src/
│   ├── main.py                    # Entry point 🎯
│   ├── data_loader.py             # Data loading & cleaning 🧹
│   ├── analysis.py                # Analysis functions 📈
│   └── visualization.py           # Chart generation 🎨
├── 📓 notebooks/
│   └── player_analysis.ipynb      # Interactive exploration 🔬
├── 📤 outputs/                    # Generated reports & charts
├── requirements.txt               # Dependencies
└── README.md                      # This file
```

---

## 🎨 Features

### 📊 10+ Visualization Types

| Chart Type | Purpose | Output |
|-----------|---------|--------|
| 📈 **KDA Distribution** | View skill level spread | Histogram with KDE |
| 📊 **Level Distribution** | Player level breakdown | Frequency chart |
| 🎯 **Top Players** | Identify star performers | Ranked bar chart |
| 📉 **Playtime vs Kills** | Engagement correlation | Scatter plot + trend line |
| 🔥 **Performance Heatmap** | Stat relationships | Correlation matrix |
| 📅 **Activity Timeline** | Player growth over time | Cumulative line chart |
| 🏆 **Engagement Metrics** | Level-based insights | Multi-chart analysis |
| ⚔️ **Kills vs Deaths** | Combat performance | Colored scatter plot |
| 🎲 **Summary Dashboard** | All-in-one overview | 7-panel visual |
| 🎪 **Win Rate Analysis** | Victory distribution | Histogram |

### 📈 Analysis Capabilities

✅ **Performance Metrics**
- Kill/Death/Assist (KDA) ratio calculations
- Win rate analysis
- Average playtime tracking
- Combat efficiency scores

✅ **Player Segmentation**
- Group by skill level
- Activity-based clustering
- Engagement classification
- Progression tracking

✅ **Engagement Insights**
- Player retention analysis
- Playtime correlations
- Activity trends
- Level progression patterns

✅ **Data Processing**
- Batch CSV loading
- Automatic deduplication
- Missing data handling
- Date parsing & validation

---

## 📋 Data Format

### Expected CSV Columns

Place your player data in `data/` directory with these columns:

```csv
player_id,player_name,level,kills,deaths,wins,playtime_hours,join_date,last_active
1,ShadowNinja,45,2850,520,340,1250,2023-01-15,2024-05-20
2,PhoenixFire,38,2100,680,280,980,2023-02-20,2024-05-19
...
```

| Column | Type | Description |
|--------|------|-------------|
| `player_id` | Integer | Unique identifier |
| `player_name` | String | Display name |
| `level` | Integer | Current level (1-50+) |
| `kills` | Integer | Total kills |
| `deaths` | Integer | Total deaths |
| `wins` | Integer | Match victories |
| `playtime_hours` | Float | Total hours played |
| `join_date` | Date | Account creation date |
| `last_active` | Date | Last login date |

---

## 📊 Usage Examples

### Automated Analysis
```bash
python src/main.py
```
Generates: Statistics summary, player rankings, visualizations, CSV exports

### Interactive Exploration
```bash
jupyter notebook notebooks/player_analysis.ipynb
```
Run cells individually to explore data step-by-step

### Programmatic Access
```python
from src.data_loader import load_all_data, clean_data
from src.analysis import PlayerAnalyzer
from src.visualization import PlayerVisualizer

# Load and analyze
df = load_all_data('data')
df = clean_data(df)

analyzer = PlayerAnalyzer(df)
visualizer = PlayerVisualizer(df)

# Get insights
top_players = analyzer.get_top_players('kda_ratio', top_n=10)
visualizer.plot_summary_dashboard()
```

---

## 📤 Output Files

After running analysis, check `outputs/` for:

| File | Format | Content |
|------|--------|---------|
| `player_summary.txt` | Text | Statistical summary |
| `top_10_players.csv` | CSV | Top performers |
| `engagement_stats.csv` | CSV | Engagement metrics |
| `01_kda_distribution.png` | Image | KDA ratio chart |
| `03_playtime_vs_kills.png` | Image | Correlation chart |
| `10_dashboard_summary.png` | Image | All-in-one view |

---

## 🛠️ Tech Stack

```
├── 🐍 Python 3.10+          Core language
├── 📊 Pandas 2.0+           Data manipulation
├── 🔢 NumPy 1.24+           Numerical computing
├── 📉 Matplotlib 3.7+       Plotting library
├── 🎨 Seaborn 0.12+         Statistical visualization
├── 🧪 Jupyter 1.0+          Interactive notebooks
└── 📈 SciPy 1.11+           Statistical functions
```

---

## 📋 Requirements

- **Python**: 3.10 or higher
- **OS**: Windows, macOS, or Linux
- **Disk Space**: ~100MB (including sample data)
- **Memory**: 2GB minimum

See `requirements.txt` for complete dependency list with versions.

---

## 🎯 Common Tasks

### ➕ Add More Player Data
```bash
# 1. Create CSV file with same columns
# 2. Save to data/ folder
# 3. Run analysis
python src/main.py
```

### 🔧 Customize Analysis
Edit `src/analysis.py` and add new methods to `PlayerAnalyzer` class:
```python
def custom_metric(self):
    """Your custom analysis"""
    return self.df[...].calculate(...)
```

### 📊 Generate Specific Charts
```python
from src.visualization import PlayerVisualizer
viz = PlayerVisualizer(df, output_dir='outputs')
viz.plot_kda_distribution()
viz.plot_top_players('kills', top_n=15)
```

---

## 🤝 Contributing

We welcome contributions! To add features:

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/amazing-feature`)
3. ✏️ Commit changes (`git commit -m 'Add amazing feature'`)
4. 📤 Push to branch (`git push origin feature/amazing-feature`)
5. 🔀 Open a Pull Request

**Guidelines:**
- Follow PEP 8 style guide
- Add docstrings to functions
- Test your changes
- Update README if needed

---

## 📝 License

This project is proprietary software for **ApexQuest Games** (Internal Use Only).

---

## 🙋 Support & Questions

📧 For issues or questions, please reach out to the development team.

---

<div align="center">

### 🌟 Made with ❤️ for ApexQuest Games

**⭐ If you find this useful, please star the repository!**

![GitHub Stars](https://img.shields.io/github/stars/1994-munk/ApexQuest?style=social)
![GitHub Forks](https://img.shields.io/github/forks/1994-munk/ApexQuest?style=social)

</div>
