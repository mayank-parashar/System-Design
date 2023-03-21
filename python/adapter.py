class SortAlgo:
    def __init__(self, data_list: list[int]):
        self._data_list = data_list

    def sort_list(self) -> list[int]:
        return sorted(self._data_list)


class ListDataStore:
    def __init__(self, data: list[int]):
        self._data = data

    def get_data(self):
        return self._data


class MapDataStore:
    def __init__(self, data: dict[int, str]):
        self._data = data

    def get_data(self):
        return self._data


class IntDataStore(ListDataStore):
    pass


class Adapter(ListDataStore):

    def __init__(self, obj: MapDataStore):
        self._data_store = obj.get_data()
        super().__init__([i for i in self._data_store.keys()])


if __name__ == "__main__":
    int_data_store = IntDataStore([4, 5, 1, 2, 3])
    print(SortAlgo(int_data_store.get_data()).sort_list())

    map_data_store = MapDataStore({5: "5", 4: "4", 3: "3", 2: "2", 1: "1"})
    adapter = Adapter(map_data_store)
    print(SortAlgo(adapter.get_data()).sort_list())

    # here SortAlgo(map_data_store.get_data()).sort_list()) will not work because
    # SortAlgo class doesn't support dict datatype so we created a adapter class which will
    # inherit IntDataStore which is compatible with SortAlgo class and then wrap MapDataStore
    # object so that it will become compatible with SortAlgo class
