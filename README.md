# room-generator

This app generates a set of Inform 7 rooms.

- Room names are assigned from a list of room names.
- Rooms are connected breadth first from the list of generated rooms.
- Each room contains one unique item from a list of object names.
- A TEST command is generated for one path from the starting room to a "leaf" node room, which has no exits, except to return to the previous room.

## License

Copyright (c) 2025 [Jim Tyhurst](https://jimtyhurst.com)

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.
