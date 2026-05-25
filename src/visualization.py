"""Visualization utilities for player data analysis."""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from pathlib import Path


class PlayerVisualizer:
    """Generate visualizations for player analysis."""
    
    def __init__(self, df, output_dir='outputs'):
        """Initialize visualizer with player data."""
        self.df = df.copy()
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Set style
        sns.set_style('whitegrid')
        plt.rcParams['figure.figsize'] = (12, 6)
    
    def save_figure(self, filename, tight_layout=True):
        """Save figure to output directory."""
        if tight_layout:
            plt.tight_layout()
        filepath = self.output_dir / filename
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        print(f"Saved: {filepath}")
        plt.close()
    
    def plot_kda_distribution(self):
        """Plot KDA ratio distribution."""
        if 'kda_ratio' not in self.df.columns:
            print("KDA ratio not found in data")
            return
        
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.histplot(data=self.df, x='kda_ratio', bins=20, kde=True, ax=ax)
        ax.set_title('KDA Ratio Distribution', fontsize=14, fontweight='bold')
        ax.set_xlabel('KDA Ratio', fontsize=12)
        ax.set_ylabel('Number of Players', fontsize=12)
        
        self.save_figure('01_kda_distribution.png')
    
    def plot_level_distribution(self):
        """Plot player level distribution."""
        if 'level' not in self.df.columns:
            print("Level not found in data")
            return
        
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.histplot(data=self.df, x='level', bins=15, kde=True, ax=ax, color='skyblue')
        ax.set_title('Player Level Distribution', fontsize=14, fontweight='bold')
        ax.set_xlabel('Level', fontsize=12)
        ax.set_ylabel('Number of Players', fontsize=12)
        
        self.save_figure('02_level_distribution.png')
    
    def plot_playtime_vs_kills(self):
        """Plot playtime vs kills correlation."""
        if 'playtime_hours' not in self.df.columns or 'kills' not in self.df.columns:
            print("Playtime or kills not found in data")
            return
        
        fig, ax = plt.subplots(figsize=(12, 6))
        scatter = ax.scatter(self.df['playtime_hours'], self.df['kills'], 
                            alpha=0.6, s=100, c=self.df['level'], cmap='viridis')
        
        # Add trend line
        z = np.polyfit(self.df['playtime_hours'], self.df['kills'], 1)
        p = np.poly1d(z)
        ax.plot(self.df['playtime_hours'], p(self.df['playtime_hours']), 
               "r--", alpha=0.8, linewidth=2, label='Trend')
        
        ax.set_title('Playtime vs Kills (colored by Level)', fontsize=14, fontweight='bold')
        ax.set_xlabel('Playtime (hours)', fontsize=12)
        ax.set_ylabel('Kills', fontsize=12)
        ax.legend()
        
        cbar = plt.colorbar(scatter, ax=ax)
        cbar.set_label('Player Level', fontsize=10)
        
        self.save_figure('03_playtime_vs_kills.png')
    
    def plot_top_players(self, metric='kda_ratio', top_n=10):
        """Plot top players by metric."""
        if metric not in self.df.columns:
            print(f"{metric} not found in data")
            return
        
        top_players = self.df.nlargest(top_n, metric)
        
        fig, ax = plt.subplots(figsize=(12, 6))
        bars = ax.barh(range(len(top_players)), top_players[metric], color='coral')
        ax.set_yticks(range(len(top_players)))
        ax.set_yticklabels(top_players['player_name'])
        ax.invert_yaxis()
        ax.set_title(f'Top {top_n} Players by {metric.replace("_", " ").title()}', 
                    fontsize=14, fontweight='bold')
        ax.set_xlabel(metric.replace('_', ' ').title(), fontsize=12)
        
        # Add value labels
        for i, bar in enumerate(bars):
            width = bar.get_width()
            ax.text(width, bar.get_y() + bar.get_height()/2, 
                   f'{width:.2f}', ha='left', va='center', fontsize=10)
        
        self.save_figure(f'04_top_{top_n}_by_{metric}.png')
    
    def plot_kills_deaths_comparison(self):
        """Plot kills vs deaths scatter plot."""
        if 'kills' not in self.df.columns or 'deaths' not in self.df.columns:
            print("Kills or deaths not found in data")
            return
        
        fig, ax = plt.subplots(figsize=(12, 6))
        scatter = ax.scatter(self.df['deaths'], self.df['kills'], 
                            alpha=0.6, s=100, c=self.df['level'], cmap='plasma')
        
        ax.set_title('Kills vs Deaths (colored by Level)', fontsize=14, fontweight='bold')
        ax.set_xlabel('Deaths', fontsize=12)
        ax.set_ylabel('Kills', fontsize=12)
        
        cbar = plt.colorbar(scatter, ax=ax)
        cbar.set_label('Player Level', fontsize=10)
        
        self.save_figure('05_kills_vs_deaths.png')
    
    def plot_engagement_by_level(self):
        """Plot engagement metrics by level group."""
        if 'level' not in self.df.columns or 'playtime_hours' not in self.df.columns:
            print("Level or playtime not found in data")
            return
        
        # Create level groups
        df_grouped = self.df.copy()
        df_grouped['level_group'] = pd.cut(df_grouped['level'], 
                                           bins=[0, 10, 20, 30, 40, 50, 100],
                                           labels=['1-10', '11-20', '21-30', '31-40', '41-50', '50+'])
        
        engagement = df_grouped.groupby('level_group', observed=True).agg({
            'playtime_hours': 'mean',
            'kills': 'mean',
            'player_id': 'count'
        }).rename(columns={'player_id': 'player_count'})
        
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))
        
        # Average playtime
        engagement['playtime_hours'].plot(kind='bar', ax=axes[0], color='steelblue')
        axes[0].set_title('Average Playtime by Level Group', fontsize=12, fontweight='bold')
        axes[0].set_xlabel('Level Group', fontsize=11)
        axes[0].set_ylabel('Hours', fontsize=11)
        axes[0].tick_params(axis='x', rotation=45)
        
        # Average kills
        engagement['kills'].plot(kind='bar', ax=axes[1], color='coral')
        axes[1].set_title('Average Kills by Level Group', fontsize=12, fontweight='bold')
        axes[1].set_xlabel('Level Group', fontsize=11)
        axes[1].set_ylabel('Kills', fontsize=11)
        axes[1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        self.save_figure('06_engagement_by_level.png', tight_layout=False)
    
    def plot_win_rate_distribution(self):
        """Plot win rate distribution if available."""
        if 'wins' not in self.df.columns or 'matches' not in self.df.columns:
            print("Wins or matches not found in data")
            return
        
        self.df['win_rate'] = (self.df['wins'] / self.df['matches'] * 100).round(2)
        
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.histplot(data=self.df, x='win_rate', bins=15, kde=True, ax=ax, color='lightgreen')
        ax.set_title('Win Rate Distribution (%)', fontsize=14, fontweight='bold')
        ax.set_xlabel('Win Rate (%)', fontsize=12)
        ax.set_ylabel('Number of Players', fontsize=12)
        
        self.save_figure('07_win_rate_distribution.png')
    
    def plot_player_stats_heatmap(self):
        """Plot correlation heatmap of numeric stats."""
        numeric_df = self.df.select_dtypes(include=[np.number])
        
        fig, ax = plt.subplots(figsize=(10, 8))
        corr_matrix = numeric_df.corr()
        sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', 
                   center=0, ax=ax, square=True, cbar_kws={'label': 'Correlation'})
        ax.set_title('Player Statistics Correlation Heatmap', fontsize=14, fontweight='bold')
        
        self.save_figure('08_correlation_heatmap.png')
    
    def plot_activity_timeline(self):
        """Plot player join dates over time."""
        if 'join_date' not in self.df.columns:
            print("Join date not found in data")
            return
        
        df_sorted = self.df.copy()
        df_sorted['join_date'] = pd.to_datetime(df_sorted['join_date'])
        df_sorted = df_sorted.sort_values('join_date')
        df_sorted['cumulative_players'] = range(1, len(df_sorted) + 1)
        
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(df_sorted['join_date'], df_sorted['cumulative_players'], 
               marker='o', linewidth=2, markersize=6, color='steelblue')
        ax.fill_between(df_sorted['join_date'], df_sorted['cumulative_players'], 
                       alpha=0.3, color='steelblue')
        
        ax.set_title('Cumulative Player Registrations Over Time', fontsize=14, fontweight='bold')
        ax.set_xlabel('Date', fontsize=12)
        ax.set_ylabel('Cumulative Players', fontsize=12)
        ax.grid(True, alpha=0.3)
        
        plt.xticks(rotation=45)
        self.save_figure('09_activity_timeline.png')
    
    def plot_summary_dashboard(self):
        """Create a summary dashboard with multiple metrics."""
        fig = plt.figure(figsize=(16, 10))
        gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)
        
        # 1. Level distribution
        if 'level' in self.df.columns:
            ax1 = fig.add_subplot(gs[0, 0])
            self.df['level'].hist(bins=15, ax=ax1, color='skyblue', edgecolor='black')
            ax1.set_title('Level Distribution', fontweight='bold')
            ax1.set_xlabel('Level')
            ax1.set_ylabel('Count')
        
        # 2. KDA ratio
        if 'kda_ratio' in self.df.columns:
            ax2 = fig.add_subplot(gs[0, 1])
            self.df['kda_ratio'].hist(bins=15, ax=ax2, color='coral', edgecolor='black')
            ax2.set_title('KDA Ratio Distribution', fontweight='bold')
            ax2.set_xlabel('KDA Ratio')
            ax2.set_ylabel('Count')
        
        # 3. Playtime distribution
        if 'playtime_hours' in self.df.columns:
            ax3 = fig.add_subplot(gs[0, 2])
            self.df['playtime_hours'].hist(bins=15, ax=ax3, color='lightgreen', edgecolor='black')
            ax3.set_title('Playtime Distribution', fontweight='bold')
            ax3.set_xlabel('Hours')
            ax3.set_ylabel('Count')
        
        # 4. Top players by KDA
        if 'kda_ratio' in self.df.columns:
            ax4 = fig.add_subplot(gs[1, :2])
            top_5 = self.df.nlargest(5, 'kda_ratio')
            ax4.barh(top_5['player_name'], top_5['kda_ratio'], color='steelblue')
            ax4.set_title('Top 5 Players by KDA', fontweight='bold')
            ax4.set_xlabel('KDA Ratio')
        
        # 5. Kills vs Deaths
        if 'kills' in self.df.columns and 'deaths' in self.df.columns:
            ax5 = fig.add_subplot(gs[1, 2])
            ax5.scatter(self.df['deaths'], self.df['kills'], alpha=0.6, color='purple')
            ax5.set_title('Kills vs Deaths', fontweight='bold')
            ax5.set_xlabel('Deaths')
            ax5.set_ylabel('Kills')
        
        # 6. Playtime vs Kills
        if 'playtime_hours' in self.df.columns and 'kills' in self.df.columns:
            ax6 = fig.add_subplot(gs[2, :2])
            ax6.scatter(self.df['playtime_hours'], self.df['kills'], alpha=0.6, color='coral')
            ax6.set_title('Playtime vs Kills', fontweight='bold')
            ax6.set_xlabel('Playtime (hours)')
            ax6.set_ylabel('Kills')
        
        # 7. Summary stats
        ax7 = fig.add_subplot(gs[2, 2])
        ax7.axis('off')
        stats_text = f"""
        Total Players: {len(self.df)}
        Avg Level: {self.df['level'].mean():.1f}
        Avg KDA: {self.df['kda_ratio'].mean():.2f}
        Avg Playtime: {self.df['playtime_hours'].mean():.1f}h
        """
        ax7.text(0.1, 0.5, stats_text, fontsize=11, verticalalignment='center',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        plt.suptitle('Player Analysis Dashboard', fontsize=16, fontweight='bold', y=0.995)
        self.save_figure('10_dashboard_summary.png', tight_layout=False)
    
    def generate_all_visualizations(self):
        """Generate all available visualizations."""
        print("\nGenerating visualizations...\n")
        
        self.plot_kda_distribution()
        self.plot_level_distribution()
        self.plot_playtime_vs_kills()
        self.plot_top_players('kda_ratio', 10)
        self.plot_kills_deaths_comparison()
        self.plot_engagement_by_level()
        self.plot_player_stats_heatmap()
        
        if 'joins_date' in self.df.columns:
            self.plot_activity_timeline()
        
        if 'wins' in self.df.columns and 'matches' in self.df.columns:
            self.plot_win_rate_distribution()
        
        self.plot_summary_dashboard()
        
        print("\n✓ All visualizations generated!")
