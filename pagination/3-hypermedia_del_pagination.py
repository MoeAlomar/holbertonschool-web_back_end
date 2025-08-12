#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination.
"""

import csv
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names."""
    
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize Server with empty dataset caches."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Return cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Return dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, 
                       page_size: int = 10) -> Dict:
        """
        Return deletion-resilient pagination.
        
        Args:
            index: Starting index for pagination
            page_size: Number of items per page
            
        Returns:
            Dict containing pagination information and data
            
        Raises:
            AssertionError: If index is None or out of range
        """
        indexed_data = self.indexed_dataset()
        assert (index is not None and 
                0 <= index < len(indexed_data)), "index out of range"

        data = []
        collected = 0
        current_index = index
        max_index = max(indexed_data.keys())

        while collected < page_size and current_index <= max_index:
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
                collected += 1
            current_index += 1

        # current_index now points to next index to query
        next_index = current_index
        # skip any deleted indexes for next_index
        while (next_index <= max_index and 
               next_index not in indexed_data):
            next_index += 1

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data
        }
