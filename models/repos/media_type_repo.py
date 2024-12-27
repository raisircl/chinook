from models.media_type import MediaType
from models.repos.a_media_type import AMediaType
import sqlite3

class MediaTypeRepo(AMediaType):
    def create_media_type(self, model: MediaType) -> None:
        pass

    def update_media_type(self, mt_id: int, model: MediaType) -> None:
        pass

    def delete_media_type(self, mt_id: int) -> None:
        pass

    def get_media_type(self, mt_id: int) -> MediaType:
        pass

    def get_all_media_types(self) -> list[MediaType]:
        data_list = []
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.execute("SELECT * FROM media_types")
                for row in cursor:
                    mt = MediaType(media_type_id=row[0], media_type_name=row[1])
                    data_list.append(mt)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return data_list
