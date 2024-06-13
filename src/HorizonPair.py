"""
    This file is a part of Horizon Pair

    Horizon Pair is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 
"""

import sys
from pathlib import Path
from typing import List

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

# Horizon Pair imports
from bracket import Bracket
from colour import Colour
from match import Match
from player import Player


def generate_pairings(scoreGroups: List[Player]) -> Bracket:
    """generate pairings for a chess tournament
    @param: scoreGroups - all the score groups in the tournament
    """

    # TODO:
    for group in scoreGroups:
        if False:
            pass


QML_file = Path(__file__).parent / "gui.qml"

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load(QML_file.resolve())
    if not engine.rootObjects():
        sys.exit(-1)
    exit_code = app.exec()
    del engine
    sys.exit(exit_code)
