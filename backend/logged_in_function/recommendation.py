from flask import request, jsonify
from database.database_queries import get_all_books, get_all_movies, get_all_tvshows
import random 

def _get_recommendation():
    try:
        request_user_data = request.json
        
        media_type = request_user_data["type"]
        media_genre = request_user_data["genre"]
        
        
        matching_media = []
        
        
        if media_type == "movie":
            all_movies = get_all_movies._get_all_movies()
            for movie in all_movies:
                movie_name = movie[1]
                movie_year = movie[2]
                movie_genre = movie[3]
                
                if media_genre.lower() in movie_genre.lower():
                    recommendation_info = {
                        "Name":movie_name,
                        "Year": movie_year,
                        "Genre":movie_genre
                    }
                    matching_media.append(recommendation_info)

                
                
        elif media_type == "tv_show":
            all_tv_shows = get_all_tvshows._get_all_tvshows()
            for show in all_tv_shows:
                show_name = show[1]
                show_year = show[2]
                show_genre = show[3]
                
                if media_genre.lower() in show_genre.lower():
                    
                    recommendation_info = {
                        "Name":show_name,
                        "Year": show_year,
                        "Genre":show_genre
                    }
                    matching_media.append(recommendation_info)
                    
                    
                    
        elif media_type == "book":
            all_books = get_all_books._get_all_books()
            for book in all_books:
                book_name = book[1]
                book_year = book[2]
                book_genre = book[3]
                
                if media_genre.lower() in book_genre.lower():
                    recommendation_info = {
                        "Name":book_name,
                        "Year": book_year,
                        "Genre":book_genre
                    }
                    matching_media.append(recommendation_info)
        else:
            return None
        
        
        

        if matching_media:
            recommendation_match = random.choice(matching_media)
            print(recommendation_match)
            return recommendation_match
            
        
        
    except Exception as ex:
        print(ex)
        
        
