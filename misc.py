class BiDict(object):
    """Bidirectional dict-like structure.

        Example
        =======

        >>> d = BiDict({'a': 1, 'b': 2})
        >>> d.get('a')
        1
        >>> d.get(2)
        'b'

    """
    def __init__(self, bi_map):
        self.bi_map = bi_map

    def get(self, key):
        try:
            return self.bi_map[key]
        except KeyError:
            return self.get_reversed(key)

    def get_reversed(self, key):
        for k, item in self.bi_map.items():
            if item == key:
                return k
        raise KeyError
