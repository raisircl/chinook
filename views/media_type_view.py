from models.repos.media_type_repo import MediaTypeRepo
from models.media_type import MediaType
def view_media_type():
    """Fetches and displays all media types."""
    try:
        mtr = MediaTypeRepo()
        gamt = mtr.get_all_media_types()
        if not gamt:
            print("No media types found.")
        else:
            for li in gamt:
                print(f"Id: {li.media_type_id}, Name: {li.media_type_name}")
    except Exception as e:
        print(f"An error occurred: {e}")
def view_media_type_by_id(mt_id):
    """Fetches and display media type by providing its id."""
    try:
        mtr = MediaTypeRepo()
        gamt = mtr.get_media_type(mt_id)
        if not gamt:
            print("No media types found.")
        else:
            print(f"Id: {gamt.media_type_id}, Name: {gamt.media_type_name}")
    except Exception as e:
        print(f"An error occurred: {e}")

def create_media():
    mtid = input("enter media type id")
    mtname = input("enter media type name")
    new_media_type=MediaType(mtid,mtname)
    mtr = MediaTypeRepo()
    mtr.create_media_type(new_media_type)
    view_media_type()

def update_media():
    mtid = input("enter media type id")
    mtname = input("enter media type name")
    umt=MediaType(mtid,mtname)
    mtr = MediaTypeRepo()
    mtr.update_media_type(mtid,umt)
    view_media_type()
    
def delete_media():
    mtid = input("enter media type id")
    mtr = MediaTypeRepo()
    mtr.delete_media_type(mtid)
    view_media_type()

if __name__=="__main__":
    delete_media()