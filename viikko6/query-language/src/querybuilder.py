from matchers import And, PlaysIn, HasAtLeast, HasFewerThan, All

class QueryBuilder:
    def __init__(self):
        self._matchers = []

    def plays_in(self, team):
        return QueryBuilder(self._matchers + [PlaysIn(team)])

    def has_at_least(self, value, attr):
        return QueryBuilder(self._matchers + [HasAtLeast(value, attr)])

    def has_fewer_than(self, value, attr):
        return QueryBuilder(self._matchers + [HasFewerThan(value, attr)])

    def build(self):
        if not self._matchers:
            return All()
        return And(*self._matchers)