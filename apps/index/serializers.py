#from django.contrib.auth.models import User
#from rest_framework import serializers
#
#
#
#class UserSerializer(serializers.HyperlinkedModelSerializer):
#    #url = serializers.HyperlinkedIdentityField(view_name="index:user-detail")
#
#    class Meta:
#        model = User
#        fields = ['username', 'email']
#
#    def validate_username(self, data):
#        users = User.objects.filter(username = data)
#        if len(users) != 0 :
#            raise serializers.ValidationError('Este nombre de usuario ya existe, ingrese uno nuevo')
#        else:
#            return data 
