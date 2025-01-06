from models.media_type import MediaType
from models.repos.a_media_type import AMediaType
import sqlite3

class MediaTypeRepo(AMediaType):
    def create_media_type(self, model: MediaType) -> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(f"insert into media_types values({model.media_type_id},'{model.media_type_name}')")
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def update_media_type(self, mt_id: int, model: MediaType) -> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(f"update media_types set Name = '{model.media_type_name}' where MediaTypeId={mt_id}")
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def delete_media_type(self, mt_id: int) -> None:
        try:
            with sqlite3.connect("chinook.db") as conn:
                conn.execute(f"delete from media_types where MediaTypeId={mt_id}")
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def get_media_type(self, mt_id: int) -> MediaType:
        mt= MediaType(0,"Media Type Not Found")
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.execute(f"SELECT * FROM media_types where MediaTypeId={mt_id}")
                row=cursor.fetchone()
                mt.media_type_id = row[0]
                mt.media_type_name= row[1]
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return mt

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
