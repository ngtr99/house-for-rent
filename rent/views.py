from django.shortcuts import render, get_object_or_404
from .models import Account, House

# Create your views here.
def HomePage(request):
    houses = House.objects.all()
    return render(request, 'HomePage.html', {'houses': houses})


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = Account.objects.get(username=username, password=password)
            message = 'Login successful'
            if user.status == 'Owner':
                return render(request, 'Login.html', {'message': message})
            else:
                return render(request, 'Login.html', {'message': message})
        except Account.DoesNotExist:
            message = 'Invalid username or password'
            return render(request, 'Login.html', {'message': message})
    return render(request, 'Login.html')


def Register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        status = request.POST.get('status')

        if not username or not password or not status:
            message = 'All fields are required'
            return render(request, 'Register.html', {'message': message})

        if Account.objects.filter(username=username).exists():
            message = 'Username already exists'
            return render(request, 'Register.html', {'message': message})

        user = Account(username=username, password=password, status=status)
        user.save()
        message = 'Account created successfully'
        return render(request, 'Register.html', {'message': message})

    return render(request, 'Register.html')

def Logout(request):
    message = 'Logged out successfully'
    return render(request, 'Login.html', {'message': message})

def AdjustHouse(request, id):
    house = get_object_or_404(House, id=id)

    if request.method == 'POST':
        house.name = request.POST.get('name', house.name)
        house.price = request.POST.get('price', house.price)
        house.location = request.POST.get('location', house.location)
        house.description = request.POST.get('description', house.description)
        house.image = request.FILES.get('image', house.image)  
        house.save()
        message = 'House details updated successfully'
        return render(request, 'AdjustHouse.html', {'house': house, 'message': message})
    else:
        message = 'You can not adjust this house'
        return render(request, 'AdjustHouse.html', {'house': house, 'message': message})


def AddHouse(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        location = request.POST.get('location')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        # Validate fields
        if not all([name, price, location, description, image]):
            message = 'All fields are required'
            return render(request, 'AddHouse.html', {'message': message})

        # Create a new house linked to the logged-in owner
        house = House(
            name=name,
            price=price,
            location=location,
            description=description,
            image=image
        )
        house.save()
        message = 'House added successfully'
        return render(request, 'AddHouse.html', {'message': message})

    return render(request, 'AddHouse.html')


def DeleteHouse(request, id):
    house = get_object_or_404(House, id=id)
    
    if request.method == 'POST':
        house.delete()
        message = 'House deleted successfully'
        return render(request, 'HomePage.html', {'house': house, 'message': message})
    else:
        message = 'You can not delete this house'
        return render(request, 'DeleteHouse.html', {'house': house, 'message': message})