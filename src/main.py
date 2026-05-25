"""Main entry point for player data analysis."""

import sys
import os
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from data_loader import load_all_data, clean_data
from analysis import PlayerAnalyzer
import pandas as pd


def main():
    """Run player analysis pipeline."""
    print("=" * 60)
    print("ApexQuest Games - Player Data Analysis")
    print("=" * 60)
    
    # Load data
    print("\n[1/5] Loading player data...")
    df = load_all_data('data')
    
    if df is None or len(df) == 0:
        print("No player data found. Please add CSV files to the 'data/' directory.")
        print("Expected columns: player_id, player_name, level, kills, deaths, wins, playtime_hours")
        return
    
    # Clean data
    print("\n[2/5] Cleaning data...")
    df = clean_data(df)
    
    # Initialize analyzer
    print("\n[3/5] Analyzing player statistics...")
    analyzer = PlayerAnalyzer(df)
    
    # Generate reports
    print("\n[4/5] Generating reports...")
    os.makedirs('outputs', exist_ok=True)
    
    # Engagement stats
    engagement = analyzer.get_engagement_stats()
    print("\nPlayer Engagement Summary:")
    for key, value in engagement.items():
        print(f"  {key}: {value}")
    
    # Top players
    if 'kda_ratio' in analyzer.df.columns or 'kills' in analyzer.df.columns and 'deaths' in analyzer.df.columns:
        kda = analyzer.calculate_kda_ratio()
        if kda is not None:
            print("\nTop 10 Players by KDA Ratio:")
            print(kda.head(10).to_string(index=False))
    
    # Player segmentation
    if 'level' in analyzer.df.columns:
        segments = analyzer.segment_players_by_level()
        if segments is not None:
            print("\nPlayer Segmentation by Level:")
            print(segments.to_string())
    
    # Save summary
    print("\n[5/5] Saving outputs...")
    summary_file = 'outputs/player_summary.txt'
    with open(summary_file, 'w') as f:
        f.write("ApexQuest Games - Player Analysis Report\n")
        f.write("=" * 60 + "\n\n")
        f.write("Engagement Summary:\n")
        for key, value in engagement.items():
            f.write(f"  {key}: {value}\n")
        
        f.write("\n\nStatistical Summary:\n")
        f.write(analyzer.get_player_stats_summary().to_string())
    
    print(f"Report saved to: {summary_file}")
    print("\n✓ Analysis complete!")


if __name__ == '__main__':
    main()
