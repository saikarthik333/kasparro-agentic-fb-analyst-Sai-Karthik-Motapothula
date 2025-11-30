import pytest
import os
from src.agents.data_agent import DataAgent

def test_data_file_exists():
    """Verify that the dataset is present."""
    assert os.path.exists("data/synthetic_fb_ads_undergarments.csv")

def test_data_loading():
    """Verify DataAgent can load rows."""
    agent = DataAgent("data/synthetic_fb_ads_undergarments.csv")
    stats = agent.get_summary_stats()
    assert stats['total_spend'] > 0