# Enhanced data processing module
import json
from datetime import datetime
from typing import Dict, List, Any

class DataProcessor:
    """Enhanced data processor with improved error handling"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.processed_count = 0
    
    def validate_data(self, data: Any) -> bool:
        """Validate input data structure"""
        if not isinstance(data, (dict, list)):
            return False
        return len(data) > 0 if data else False
    
    def process_item(self, item: Dict[str, Any]) -> Dict[str, Any]:
        """Process a single data item with enhanced logic"""
        try:
            processed_item = {
                **item,
                'processed_at': datetime.now().isoformat(),
                'processor_version': '2.0',
                'status': 'processed'
            }
            self.processed_count += 1
            return processed_item
        except Exception as e:
            return {
                'error': str(e),
                'original_item': item,
                'status': 'error'
            }
    
    def get_stats(self) -> Dict[str, Any]:
        """Get processing statistics"""
        return {
            'processed_count': self.processed_count,
            'last_updated': datetime.now().isoformat()
        }