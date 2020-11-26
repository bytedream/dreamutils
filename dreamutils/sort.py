#!/usr/bin/python3

from typing import List as _List

"""
This file provides different sorting algorithms

Todo:
    Add `ignore_case` argument to `Sort.string(...)` or `string_ignore_case(...)` method
    
Thanks:
    https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm
    https://www.educative.io/edpresso/how-to-implement-quicksort-in-python
"""


def _copy_or_not(to_sort: list, copy=True) -> list:
    if copy:
        return to_sort.copy()
    else:
        return to_sort


class Sort:

    @classmethod
    def integer(cls, to_sort: _List[int], new_list=True) -> _List[int]:
        """
        Sorts a list of integers

        Args:
            to_sort: The list of integers to sort
            new_list: If True the given list is copied and returned. If False the given list will be updated

        Returns:
            The sorted list of integerss

        """
        return cls.object(to_sort, new_list)

    @staticmethod
    def object(to_sort: list, new_list=True) -> list:
        """
        Sorts a list, regardless of its type

        Args:
            to_sort: The list sort
            new_list: If True the given list is copied and returned. If False the given list will be updated

        Returns:
            The sorted list

        """
        pass

    @classmethod
    def string(cls, to_sort: _List[str], new_list=True) -> _List[str]:
        """
        Sorts a list of strings

        Args:
            to_sort: The list of strings to sort
            new_list: If True the given list is copied and returned. If False the given list will be updated

        Returns:
            The sorted list of strings

        """
        return cls.object(to_sort, new_list)


class BubbleSort(Sort):
    """Bubble sort is a comparison-based algorithm in which each pair of adjacent elements is compared and the elements are swapped if they are not in order"""

    @staticmethod
    def object(to_sort: list, new_list=True) -> list:
        sorted_list = _copy_or_not(to_sort, new_list)
        for num in range(len(sorted_list) - 1, 0, -1):
            for i in range(num):
                if sorted_list[i] > sorted_list[i + 1]:
                    temp = sorted_list[i]
                    sorted_list[i] = sorted_list[i + 1]
                    sorted_list[i + 1] = temp

        return sorted_list


class InsertionSort(Sort):
    """
    Insertion sort involves finding the right place for a given element in a sorted list.
    So in beginning we compare the first two elements and sort them by comparing them.
    Then we pick the third element and find its proper position among the previous two sorted elements.
    This way we gradually go on adding more elements to the already sorted list by putting them in their proper position
    """

    @staticmethod
    def object(to_sort: list, new_list=True) -> list:
        sorted_list = _copy_or_not(to_sort, new_list)
        for i in range(1, len(sorted_list)):
            j = i - 1
            key = sorted_list[i]

            while j >= 0 and key < sorted_list[j]:
                sorted_list[j + 1] = sorted_list[j]
                j -= 1
            sorted_list[j + 1] = key

        return sorted_list


class QuickSort(Sort):
    """QuickSort is an in-place sorting algorithm with worst-case time complexity of n^2"""

    @staticmethod
    def object(to_sort: list, new_list=True) -> list:
        sorted_list = _copy_or_not(to_sort, new_list)
        elements = len(sorted_list)

        if elements < 2:
            return sorted_list

        pos = 0

        for i in range(1, elements):
            if sorted_list[i] <= sorted_list[0]:
                pos += 1
                temp = sorted_list[i]
                sorted_list[i] = sorted_list[pos]
                sorted_list[pos] = temp

        temp = sorted_list[0]
        sorted_list[0] = sorted_list[pos]
        sorted_list[pos] = temp

        left = QuickSort.object(sorted_list[0:pos], False)
        right = QuickSort.object(sorted_list[pos + 1:elements], False)

        sorted_list = left + [sorted_list[pos]] + right

        return sorted_list


class SelectionSort(Sort):
    """
    In selection sort we start by finding the minimum value in a given list and move it to a sorted list.
    Then we repeat the process for each of the remaining elements in the unsorted list.
    The next element entering the sorted list is compared with the existing elements and placed at its correct position.
    So at the end all the elements from the unsorted list are sorted
    """

    @staticmethod
    def object(to_sort: list, new_list=True) -> list:
        sorted_list = _copy_or_not(to_sort, new_list)
        for index in range(len(sorted_list)):
            min_index = index
            for j in range(index + 1, len(sorted_list)):
                if sorted_list[min_index] > sorted_list[j]:
                    min_index = j

            sorted_list[index], sorted_list[min_index] = sorted_list[min_index], sorted_list[index]

        return sorted_list
