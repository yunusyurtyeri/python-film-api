# -*- coding: utf-8 -*-

import requests

class theMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "themoviedb api key"
        
    def getPopulars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()
    def getSearchResults(self,keyword):
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()
    
movieApi = theMovieDb()

while True:
    choice = input("1- Popoler Movies\n2- Search Movies\n3- Exit\nSeçim: ")
    
    if choice == "3":
        break
    else:
        if choice == "1":
            movies = movieApi.getPopulars()
            for movie in movies['results']:
                print(movie['title'])
        
        if choice == "2":
            keyword = input("Keyword: ")
            movies = movieApi.getSearchResults(keyword)
            for movie in movies['results']:
                print(movie['name'])