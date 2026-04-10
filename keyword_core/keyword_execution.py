from keyword_core.keywords import KeywordData
from keyword_core.keyword_mapping import KeywordMapping
from typing import Any

class Execute:
    def __init__(self, keyword: KeywordData, data: Any | None) -> None:
        self.keyword_data = keyword
        self.data = data
        self._execute()
    
    def _execute(self):
        keyword_mapping = KeywordMapping()

        print(self.keyword_data.log_when_executed(self.data))
        
        execution_function = keyword_mapping._mapping_dict[self.keyword_data]
        execution_function(self.data)
