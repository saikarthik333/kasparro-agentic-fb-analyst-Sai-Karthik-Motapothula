# test_setup.py
from src.agents.data_agent import DataAgent
agent = DataAgent("data/synthetic_fb_ads_undergarments.csv")
print(agent.get_summary_stats())