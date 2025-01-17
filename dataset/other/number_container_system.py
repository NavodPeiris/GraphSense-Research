

class NumberContainer:
    def __init__(self) -> None:
        
        
        self.numbermap: dict[int, list[int]] = {}
        
        self.indexmap: dict[int, int] = {}

    def binary_search_delete(self, array: list | str | range, item: int) -> list[int]:
        if isinstance(array, (range, str)):
            array = list(array)
        elif not isinstance(array, list):
            raise TypeError(
                "binary_search_delete() only accepts either a list, range or str"
            )

        low = 0
        high = len(array) - 1

        while low <= high:
            mid = (low + high) // 2
            if array[mid] == item:
                array.pop(mid)
                return array
            elif array[mid] < item:
                low = mid + 1
            else:
                high = mid - 1
        raise ValueError(
            "Either the item is not in the array or the array was unsorted"
        )

    def binary_search_insert(self, array: list | str | range, index: int) -> list[int]:
        if isinstance(array, (range, str)):
            array = list(array)
        elif not isinstance(array, list):
            raise TypeError(
                "binary_search_insert() only accepts either a list, range or str"
            )

        low = 0
        high = len(array) - 1

        while low <= high:
            mid = (low + high) // 2
            if array[mid] == index:
                
                
                array.insert(mid + 1, index)
                return array
            elif array[mid] < index:
                low = mid + 1
            else:
                high = mid - 1

        
        array.insert(low, index)
        return array

    def change(self, index: int, number: int) -> None:
        
        if index in self.indexmap:
            n = self.indexmap[index]
            if len(self.numbermap[n]) == 1:
                del self.numbermap[n]
            else:
                self.numbermap[n] = self.binary_search_delete(self.numbermap[n], index)

        
        self.indexmap[index] = number

        
        if number not in self.numbermap:
            self.numbermap[number] = [index]

        
        
        else:
            self.numbermap[number] = self.binary_search_insert(
                self.numbermap[number], index
            )

    def find(self, number: int) -> int:
        
        return self.numbermap.get(number, [-1])[0]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
