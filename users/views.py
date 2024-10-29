from rest_framework import generics, permissions
from .models import User
from .serializers import UserSerializer
import csv
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.contrib.auth import get_user_model

User = get_user_model()

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)
def export_users_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    # Write the header row
    writer.writerow(['ID', 'Email', 'First Name', 'Last Name'])

    # Write data rows
    for user in User.objects.all():
       writer.writerow([user.id, user.email, user.first_name, user.last_name])

    return response

# PDF Export
def export_users_pdf(request):
    template_path = 'users/user_pdf_template.html'  # HTML template for PDF
    users = User.objects.all()
    context = {'users': users}

    # Render the HTML template into a PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="users.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)

    # If PDF generation failed, return a response with the error
    if pisa_status.err:
        return HttpResponse('We had some errors with the PDF generation.', status=500)
    return response







def hello_world(request):
    return HttpResponse("hello sridhar")
