from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from libmgmt.models import Author, Publisher

class AuthorResource(ModelResource):
	class Meta:
		resource_name = 'author'
		queryset = Author.objects.all()
		authorization = Authorization()