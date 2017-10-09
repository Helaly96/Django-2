from rest_framework import serializers
from .models import Applicants


class ApplicantSerializer(serializers.ModelSerializer):



    class Meta:
        model = Applicants
        # fields= ('name','email','mobile',"national_id","faculty","major","minor","expected_year","university","profilepic")
        fields="__all__"


    # def validate_mobile(self,value):
    #
    #     data=self.get_initial()
    #     mobile=data.get("mobile")
    #
    #     if mobile.isdigit():
    #         pass
    #     else:
    #         raise serializers.ValidationError("You entered a Character,dude!")
    #


    # def validate_mobile(self, value):
    #
    #     if self.mobile.isdigit():
    #         pass
    #     else:
    #         raise serializers.ValidationError("You entered a character,dude")
    #
    #
    #     if not ( (self.mobile[0]=="0") and (self.mobile[1]=="1") and (self.mobile[2]=="1" or "2" or "5") ):
    #
    #         raise serializers.ValidationError("It must start with a 011,012,010,015")
    #
    #     # if(True):
    #     #     raise serializers.ValidationError("Working at least.")
    #
    #     return value






