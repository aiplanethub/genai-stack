# A Base class to connect to use different kinds of data aggregators which can read and transform data


class BaseAggregator:
    def run(self):
        pass

    def get_vectors(self):
        ...
