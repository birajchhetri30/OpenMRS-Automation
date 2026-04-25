from keyword_core.keywords import KeywordData
from keyword_core.keyword_mapping import KeywordMapping
from typing import Any
import logging

class Execute:
    def __init__(self, keyword: KeywordData, data: Any | None = None) -> None:
        if keyword.data_type is not None and data is None:
            raise TypeError(f"Execute.__init__() missing required argument: 'data'. Expected data of type {keyword.data_type.__name__}.")
        if keyword.data_type is not None and not isinstance(data, keyword.data_type):
            raise TypeError(f"Execute.__init__() argument 'data' must be of type {keyword.data_type.__name__}, got {type(data).__name__} instead.")
        self.keyword_data = keyword
        self.data = data
        self._execute()
    
    def _execute(self):
        keyword_mapping = KeywordMapping()

        logging.info(self.keyword_data.log_when_executed(self.data))
        
        execution_function = keyword_mapping._mapping_dict[self.keyword_data]
        execution_function(self.data)
