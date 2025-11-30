import pandas as pd
import logging
from typing import Dict, List, Any

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataAgent:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None
        self.load_data()

    def load_data(self):
        """Loads the dataset and performs initial cleaning."""
        try:
            self.df = pd.read_csv(self.file_path)
            # Convert date column to datetime objects
            self.df['date'] = pd.to_datetime(self.df['date'])
            logger.info(f"Data loaded successfully. Rows: {len(self.df)}")
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            raise e

    def get_summary_stats(self) -> Dict[str, Any]:
        """Returns high-level stats for the Planner."""
        return {
            "total_spend": float(self.df['spend'].sum()),
            "total_revenue": float(self.df['revenue'].sum()),
            "overall_roas": float(self.df['revenue'].sum() / self.df['spend'].sum()),
            "date_range": (self.df['date'].min().strftime('%Y-%m-%d'), 
                           self.df['date'].max().strftime('%Y-%m-%d')),
            "unique_campaigns": self.df['campaign_name'].nunique()
        }

    def filter_data(self, start_date: str = None, end_date: str = None, 
                   campaign_name: str = None) -> pd.DataFrame:
        """Filters data based on query parameters."""
        temp_df = self.df.copy()
        
        if start_date:
            temp_df = temp_df[temp_df['date'] >= start_date]
        if end_date:
            temp_df = temp_df[temp_df['date'] <= end_date]
        if campaign_name:
            temp_df = temp_df[temp_df['campaign_name'].str.contains(campaign_name, case=False)]
            
        return temp_df

    def get_underperforming_creatives(self, ctr_threshold: float = 0.01) -> List[Dict]:
        """Identifies creatives with low CTR for the Creative Generator."""
        low_ctr = self.df[self.df['ctr'] < ctr_threshold].copy()
        return low_ctr[['creative_message', 'ctr', 'campaign_name', 'roas']].to_dict('records')