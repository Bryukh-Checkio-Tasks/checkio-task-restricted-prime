"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": 5,
            "answer": True
        },
        {
            "input": 18,
            "answer": False
        },
        {
            "input": 97,
            "answer": True
        },

    ],
    "Extra": [
        {
            "input": 1597,
            "answer": True
        },
        {
            "input": 5503,
            "answer": True
        },
        {
            "input": 8807,
            "answer": True
        },
        {
            "input": 2,
            "answer": True
        },
        {
            "input": 3,
            "answer": True
        },
        {
            "input": 9887,
            "answer": True
        },

        {
            "input": 1598,
            "answer": False
        },
        {
            "input": 9999,
            "answer": False
        },
        {
            "input": 8888,
            "answer": False
        },
        {
            "input": 1000,
            "answer": False
        },
        {
            "input": 7755,
            "answer": False
        },


    ]
}
