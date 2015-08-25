import Data.Utils

class Map:
    """Map """

    def __init__(self):
        """Initialize"""
        self.carte = [
            [
                [Data.Utils.load_image("cube.png", -1), Data.Utils.load_image("cube.png", -1), Data.Utils.load_image("cube.png", -1), Data.Utils.load_image("cube.png", -1)],
                [Data.Utils.load_image("cube.png", -1), Data.Utils.load_image("cube.png", -1), Data.Utils.load_image("cube.png", -1), Data.Utils.load_image("cube.png", -1)],
                [Data.Utils.load_image("cube.png", -1), Data.Utils.load_image("cube.png", -1), Data.Utils.load_image("cube.png", -1), Data.Utils.load_image("cube.png", -1)],
                [Data.Utils.load_image("cube.png", -1), Data.Utils.load_image("cube.png", -1), Data.Utils.load_image("cube.png", -1), Data.Utils.load_image("cube.png", -1)]
            ],
            [
                [Data.Utils.load_image("cube.png", -1), 0, 0, Data.Utils.load_image("cube.png", -1)],
                [],
                [],
                [Data.Utils.load_image("cube.png", -1)]
            ],
            [
                [Data.Utils.load_image("cube.png", -1), 0, 0, Data.Utils.load_image("cube.png", -1)],
                [],
                [],
                [Data.Utils.load_image("cube.png", -1)]
            ],
            [
                [Data.Utils.load_image("cube.png", -1), Data.Utils.load_image("cube.png", -1), Data.Utils.load_image("cube.png", -1), Data.Utils.load_image("cube.png", -1)],
                [Data.Utils.load_image("cube.png", -1)],
                [Data.Utils.load_image("cube.png", -1)],
                [Data.Utils.load_image("cube.png", -1)]
            ]
        ]

    def __len__(self):
        return len(self.carte)
