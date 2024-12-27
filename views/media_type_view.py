from models.repos.media_type_repo import MediaTypeRepo

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

def hello():
    print("Hello User")

if __name__=="__main__":
    view_media_type()