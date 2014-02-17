from tastypie.resources import ModelResource,ALL,ALL_WITH_RELATIONS
from models import ShortenedURL,URLAccess
from tastypie.authorization import Authorization
from tastypie import fields


class ShorteningResource(ModelResource):
    
    class Meta:
        queryset = ShortenedURL.objects.all()
        resource_name = 'shorten'
        list_allowed_methods = ['post']
        detail_allowed_methods = ['get']
        authorization= Authorization()
        always_return_data = True
        filtering = {
                     "short_URL":ALL,
                     }
        
    def obj_create(self,bundle,**kwargs):
        bundle_fullURL = bundle.data["full_URL"]
        hasHttp = bundle_fullURL.find("http://")
        
        #append HTTP for instant redirection
        if(hasHttp < 0):
            bundle_fullURL = "http://"+bundle_fullURL
              
        sURL = None
        #if long url already exists in DB, return its shortened version
        try:
            sURL = ShortenedURL.objects.get(full_URL=bundle_fullURL)
            bundle.obj = sURL 
        #if it does not, create it
        except ShortenedURL.DoesNotExist:
            sURL = ShortenedURL()
            sURL.full_URL = bundle_fullURL
            sURL.save()
            #generate short_URL
            sURL.short_URL = ShortenedURL.objects.get_new_shortened_url(sURL.id)
            sURL.save()
            bundle.obj = sURL
        
        client_IP = bundle.request.META.get('REMOTE_ADDR')
        #register statistics in their own model
        self.register_stats(sURL,client_IP)
        
        return bundle
    
    def register_stats(self,sURL,clientIP,user_agent=None):
        url_acc_stat = URLAccess()
        url_acc_stat.shortened_url = sURL
        url_acc_stat.client_IP = clientIP
        url_acc_stat.save()
        

class StatsResource(ModelResource):
    url = fields.ForeignKey(ShorteningResource,'shortened_url',full=True)
    class Meta:
        queryset = URLAccess.objects.all()
        resource_name = 'stats'
        allowed_methods = ['get']
        authorization= Authorization()
        filtering = {
                     'client_IP':ALL,
                     'user_agent':ALL,
                     'timestamp':ALL,
                     'url':ALL_WITH_RELATIONS,
        }  
    
   