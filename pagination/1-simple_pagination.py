#!/usr/bin/env python3
import csv
from typing import List

"""
In this module, I implement a method that helps in pagination,
specifically in calculating the starting and ending index to reach
the starting point of a chosen page.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start index and end index to reach a specific page
    with a limited page size.

    Args:
        page (int): The page number to reach (starting from 1).
        page_size (int): The size of each page.

    Returns:
        tuple: A tuple of (start_index, end_index).

    Formula:
        n: (page number)
        p: (page size)
        start_index = (n - 1) * p
        end_index = n * p
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the server with no dataset loaded."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Load and cache the dataset from the CSV file.

        Returns:
            List[List]: The dataset without the header row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # skip header

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of the dataset.

        Args:
            page (int): The page number (default is 1).
            page_size (int): The number of items per page (default is 10).

        Returns:
            List[List]: The rows corresponding to the requested page.
                        Returns an empty list if page is out of range.

        Raises:
            AssertionError: If page or page_size are not positive integers.
        """
        assert type(page) is int and page > 0, "page must be a positive integer"
        assert type(page_size) is int and page_size > 0, "page_size must be a positive integer"

        dataset = self.dataset()
        start, end = index_range(page, page_size)

        if start >= len(dataset):
            return []

        return dataset[start:end]
