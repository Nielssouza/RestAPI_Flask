from flask_restful import Resource
from models.Site import SiteModel

class Sites (Resource):
    def get (self):
        return {'sites': [site.json() for site in SiteModel.query.all()]}

class Site(Resource):
    def get(self, url):
        site = SiteModel.find_site(url)
        if site:
            return site.json()
        return {'message': 'Site not found.'}, 404 #not found

    def post(self, url):
        if SiteModel.find_site(url):
            return {"message": "The site '{}' already exists"}, 400 #bad request
        Site = SiteModel(url)
        try:
            Site.save_site()
        except:
             return {'message': 'An internal error ocurred trying to create a new site.'}, 500
        return Site.json()    

    def delete(self, url):
        Site = SiteModel.find_site(url)
        if Site:
            Site.delete_site()
            return {'message': 'Site deleted.'}
        return {'message': 'Site not found.'}, 404  