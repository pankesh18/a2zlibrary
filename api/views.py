from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    person={'name':'Denis', 'age':28}
    return Response(person)
    
# @api_view(['POST'])
# def IssueBook(request):
#     print()
