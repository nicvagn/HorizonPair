#  id is a part of HorizonPair
#  HorizonPair is free software: you can redistribute it and/or modify it under the terms of the gnu general public license as published by the free software foundation, either version 3 of the license, or (at your option) any later version.
#
#  HorizonPair is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of merchantability or fitness for a particular purpose. see the gnu general public license for more details.
#
#  you should have received a copy of the gnu general public license along with HorizonPair. if not, see <https://www.gnu.org/licenses/>.


class CfcId:
    """A Canadian Chess Federation ID"""

    def __init__(self, cfc_id: str) -> None:
        # ensure CFC ID is valid
        assert cfc_id.isdigit() and len(cfc_id) == 6
        self.cfc_id = cfc_id

    def __str__(self) -> str:
        return self.cfc_id
