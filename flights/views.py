from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Flight, Airport, Passenger
from .forms import BookingForm, FlightForm

def index(request):
    return render(request, "flights\index.html",{
        "flights":Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    passengers = flight.passengers.all()
    non_passengers = Passenger.objects.exclude(flights=flight).all()
    
    form = BookingForm(non_passengers=non_passengers)

    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": passengers,
        # "non_passengers": non_passengers
        "form": form
    })

def book(request, flight_id):
    # For a post request, add a new flight
    if request.method == "POST":
        # Accessing the flight
        flight = Flight.objects.get(pk=flight_id)
        non_passengers = Passenger.objects.exclude(flights=flight).all()


        # # Finding the passenger id from the submitted form data
        # passenger_id = int(request.POST["passenger"])

        # # Finding the passenger based on the id
        # passenger = Passenger.objects.get(pk=passenger_id)

        # # Add passenger to the flight
        # passenger.flights.add(flight)
        form = BookingForm(request.POST, non_passengers=non_passengers)

        if form.is_valid():
            passenger = form.cleaned_data["passenger"]
            passenger.flights.add(flight)
            
        # Redirect user to flight page
        # return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
        return redirect("flight", flight.id)


def forms_page(request):
   
    # create object of form
    form = FlightForm(request.POST)
      # check if form data is valid
    if form.is_valid():

        # save the form data to model
        form.save()
        form = FlightForm()
    return render(request, "flights/forms.html", {
        	   'form':form,
            })
 
