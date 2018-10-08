class Feature():

    def __init__(self):
        pass

    @classmethod
    def data(cls):
        # Return some dummy data
        return {
            "table_data": [
                {
                    "col": ["I", "AM", "ROW", "ONE"],
                    "expand": "This is from the python server"
                },
                {
                    "col": ["I", "AM", "ROW", "TWO"],
                    "expand": "I am also from the python server"
                },
                {
                    "col": ["FOO", "BAR", "FOOBAR", "FOOBAR"],
                    "expand": "Nothing to see here!"
                }
            ]
        }

    @classmethod
    def action(cls):
        return "Nothing"