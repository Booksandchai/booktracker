
import os
import requests
from models import UserBook

GOOGLE_API_KEY = os.getenv("GOOGLE_BOOKS_API_KEY", "")
BASE_URL = "https://www.googleapis.com/books/v1/volumes"

def get_recommendations(user_id, genre_filters=["fantasy", "romance"], max_results=10):
    user_books = UserBook.list_for_user(user_id)
    excluded_ids = {ub.google_book_id for ub in user_books if ub.status == "read"}

    recs = []
    for genre in genre_filters:
        params = {
            "q": f"subject:{genre}",
            "key": GOOGLE_API_KEY,
            "maxResults": 5,
        }
        try:
            r = requests.get(BASE_URL, params=params, timeout=5)
            data = r.json()
        except Exception:
            continue
        if "items" in data:
            for item in data["items"]:
                if item.get("id") in excluded_ids:
                    continue
                volume = item.get("volumeInfo", {})
                recs.append({
                    "id": item.get("id"),
                    "title": volume.get("title"),
                    "authors": volume.get("authors", []),
                    "thumbnail": volume.get("imageLinks", {}).get("thumbnail"),
                })
                if len(recs) >= max_results:
                    break
        if len(recs) >= max_results:
            break
    return recs
