"""Player analysis functions."""

import pandas as pd
import numpy as np


class PlayerAnalyzer:
    """Analyze player statistics and performance metrics."""
    
    def __init__(self, df):
        """Initialize analyzer with player data."""
        self.df = df.copy()
    
    def calculate_kda_ratio(self):
        """Calculate Kill/Death/Assist ratio for each player."""
        if 'kills' in self.df.columns and 'deaths' in self.df.columns:
            self.df['kda_ratio'] = self.df.apply(
                lambda row: row['kills'] / max(row['deaths'], 1),
                axis=1
            )
            return self.df[['player_id', 'player_name', 'kda_ratio']].sort_values('kda_ratio', ascending=False)
        return None
    
    def calculate_win_rate(self):
        """Calculate win rate for each player."""
        if 'wins' in self.df.columns and 'matches' in self.df.columns:
            self.df['win_rate'] = (self.df['wins'] / self.df['matches'] * 100).round(2)
            return self.df[['player_id', 'player_name', 'wins', 'matches', 'win_rate']].sort_values('win_rate', ascending=False)
        return None
    
    def get_top_players(self, metric='kda_ratio', top_n=10):
        """Get top N players by specified metric."""
        if metric not in self.df.columns:
            return None
        
        return self.df.nlargest(top_n, metric)[['player_id', 'player_name', metric]]
    
    def get_player_stats_summary(self):
        """Get summary statistics for all players."""
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        summary = self.df[numeric_cols].describe().round(2)
        return summary
    
    def segment_players_by_level(self, level_ranges=None):
        """Segment players into level groups."""
        if level_ranges is None:
            level_ranges = [1, 10, 20, 30, 40, 50, 100]
        
        if 'level' not in self.df.columns:
            return None
        
        self.df['level_group'] = pd.cut(self.df['level'], bins=level_ranges, labels=[
            f"{level_ranges[i]}-{level_ranges[i+1]}" for i in range(len(level_ranges)-1)
        ])
        
        return self.df.groupby('level_group', observed=True).agg({
            'player_id': 'count',
            'kills': 'mean',
            'deaths': 'mean'
        }).rename(columns={'player_id': 'player_count'})
    
    def get_engagement_stats(self):
        """Analyze player engagement metrics."""
        stats = {
            'total_players': len(self.df),
            'active_players': len(self.df[self.df.get('playtime_hours', 0) > 0]),
        }
        
        if 'playtime_hours' in self.df.columns:
            stats['avg_playtime'] = self.df['playtime_hours'].mean().round(2)
            stats['total_playtime'] = self.df['playtime_hours'].sum().round(2)
        
        if 'kills' in self.df.columns:
            stats['avg_kills'] = self.df['kills'].mean().round(2)
            stats['total_kills'] = self.df['kills'].sum()
        
        return stats
