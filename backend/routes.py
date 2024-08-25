from flask import Flask, jsonify, make_response
app = Flask(__name__)

#############  IMPORTS  #################
from user import login, logout, signup
from logged_in_function import home, user_profile
from media_library import movies, tvshows, books, like_media


#############  TEST ROUTE  #################

@app.route("/test-route")
def test_route():
    return "OK"

#############  ROUTES  #################

def _auth_routes(app):
    @app.route('/api/signup/', methods=['POST'])
    def _signup():
        try:
            response_signup = signup._signup()
            return response_signup
        except Exception as ex:
            print(ex)
            return make_response("Error occured"), 500

    @app.route('/api/login/', methods=['POST'])
    def _login():
        try:
            response_login = login._login()
            return response_login
        except Exception as ex:
            print(ex)
            return make_response("Error occured"), 500

    @app.route('/api/logout', methods=['POST'])
    def _logout():
        try:
            response_logout = logout._logout()
            return response_logout
        except Exception as ex:
            print(ex)
            return make_response("Error occured"), 500

def _user_routes(app):
    @app.route('/api/home/', methods = ['GET'])
    def _home():
        try:
            response_home = home._home()
        
            if response_home is not None:
                response = make_response('Check sucessfull')
                response.status_code = 200  
                return response
            else:
                response = make_response('Error occured')
                response.status_code = 400
                return response
            
            
        except Exception as ex:
            print(ex)
            return make_response("Error occured"), 500
    
    @app.route('/api/user-profile/', methods = ['GET'])
    def _user_profile():
        try:
            response_user_profile = user_profile._user_profile()
            if response_user_profile is not None:
                response =  make_response(jsonify(response_user_profile))
                response.status_code = 200
                return response
            else:
                response = make_response('Error occured')
                response.status_code = 400
                return response
     
        except Exception as ex:
            print(ex)
            return make_response("Error occured"), 500



def _media_library(app):
    @app.route('/api/movies/', methods = ['GET'])
    def _movies():
        try:
            response_movies = movies._get_all_movies()
            response = make_response(jsonify(response_movies))
            response.status_code = 200
            return response
           
     
        except Exception as ex:
            print(ex)
            return make_response("Error occured"), 500
        
    @app.route('/api/tv-shows/', methods = ['GET'])
    def _tv_shows():
        try:
            response_tvshows = tvshows._get_all_tvshows()
            response = make_response(jsonify(response_tvshows))
            response.status_code = 200
            return response
           
     
        except Exception as ex:
            print(ex)
            return make_response("Error occured"), 500
        
    @app.route('/api/books/', methods = ['GET'])
    def _books():
        try:
            response_books = books._get_all_books()
            response = make_response(jsonify(response_books))
            response.status_code = 200
            return response
           
     
        except Exception as ex:
            print(ex)
            return make_response("Error occured"), 500
    
    @app.route('/api/like-tvshow/', methods = ['POST'])
    def _like_tvshow():
        try:
            response_like = like_media._like_tvshow()
            
            if response_like is not None:
                response = make_response('Check sucessfull')
                response.status_code = 200  
                return response
            else:
                response = make_response('Error occured')
                response.status_code = 400
                return response

           
     
        except Exception as ex:
            print(ex)
            return make_response("Error occured"), 500
    
    @app.route('/api/like-movie/', methods = ['POST'])
    def _like_movie():
        try:
            response_like = like_media._like_movie()
            
            if response_like is not None:
                response = make_response('Check sucessfull')
                response.status_code = 200  
                return response
            else:
                response = make_response('Error occured')
                response.status_code = 400
                return response
        except Exception as ex:
            print(ex)
            return make_response("Error occured"), 500
    
    @app.route('/api/like-book/', methods = ['POST'])
    def _like_book():
        try:
            response_like = like_media._like_book()
            
            if response_like is not None:
                response = make_response('Check sucessfull')
                response.status_code = 200  
                return response
            else:
                response = make_response('Error occured')
                response.status_code = 400
                return response
        except Exception as ex:
            print(ex)
            return make_response("Error occured"), 500