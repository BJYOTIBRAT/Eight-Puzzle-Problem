"""
Enhanced data processing module for Eight-Puzzle-Problem
"""

import json
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional

class DataProcessor:
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.processed_count = 0
        self.logger = logging.getLogger(__name__)
    
    def validate_data(self, data: Any) -> bool:
        if not data:
            return False
        
        if isinstance(data, dict):
            return len(data) > 0
        elif isinstance(data, list):
            return len(data) > 0
        
        return False
    
    def process_data(self, data: Any) -> Dict[str, Any]:
        try:
            if not self.validate_data(data):
                raise ValueError("Invalid input data")
            
            result = {
                'original': data,
                'processed_at': datetime.now().isoformat(),
                'status': 'success'
            }
            
            self.processed_count += 1
            return result
            
        except Exception as e:
            self.logger.error(f"Processing failed: {str(e)}")
            return {
                'status': 'error',
                'error_message': str(e),
                'timestamp': datetime.now().isoformat()
            }
