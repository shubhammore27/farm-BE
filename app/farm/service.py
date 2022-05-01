from farm.models import *
from farm.forms import *
from farm.serializer import GetTeamPredictionSerializer
from rest_framework import status
from django.core.mail import BadHeaderError, send_mail

# post request EXAMPLE

# def savePrediction(req):
#     try:
#         send_mail(
#             'Subject here',
#             'Here is the message.',
#             'shubham.more26@gmail.com',
#             ['luck2731@gmail.com'],
#         )
#         fd = TeamPredictionMapping(req)
#         if fd.is_valid():
#             is_valid = CreateTeam.objects.filter(teamId=req['teamId']).exists()
#             print(is_valid)
#             if is_valid:
#                 fd.save()
#                 return { 'message' :'Team Prediction Saved Successfully', 'status': status.HTTP_200_OK}
#             else:
#                 return { 'message' :'Team Not Found, Prediction Saved Failed', 'status': status.HTTP_404_NOT_FOUND}
#         else:
#             print(fd.errors())
#     except Exception as e:
#         print(e)
#         return { 'message' :'Team Prediction Not Saved', 'status': status.HTTP_400_BAD_REQUEST}
