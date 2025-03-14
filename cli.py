from database import create_session
from models.event import Event
from models.attendee import Attendee
from models.service_provider import ServiceProvider

session = create_session()

def display_menu():
    print("\n--- Event Planner CLI ---")
    print("1. Create Event")
    print("2. Delete Event")
    print("3. View All Events")
    print("4. View Attendees of an Event")
    print("5. Create Service Provider")
    print("6. Delete Service Provider")
    print("7. View All Service Providers")
    print("8. Exit")

def create_event():
    name = input("Enter event name: ")
    date = input("Enter event date (YYYY-MM-DD): ")
    event = Event.create(session, name, date)
    print(f"Event created: {event}")

def delete_event():
    event_id = int(input("Enter event ID to delete: "))
    success = Event.delete(session, event_id)
    if success:
        print(f"Event with ID {event_id} deleted.")
    else:
        print("Event not found.")

def view_all_events():
    events = Event.get_all(session)
    if events:
        for event in events:
            print(event)
    else:
        print("No events found.")

def view_attendees():
    event_id = int(input("Enter event ID to view attendees: "))
    event = Event.find_by_id(session, event_id)
    if event:
        if event.attendees:
            for attendee in event.attendees:
                print(attendee)
        else:
            print("No attendees found for this event.")
    else:
        print("Event not found.")

def create_provider():
    name = input("Enter service provider name: ")
    service_type = input("Enter service provider type: ")
    provider = ServiceProvider.create(session, name, service_type)
    print(f"Service provider created: {provider}")

def delete_provider():
    provider_id = int(input("Enter provider ID to delete: "))
    success = ServiceProvider.delete(session, provider_id)
    if success:
        print(f"Provider with ID {provider_id} deleted.")
    else:
        print("Provider not found.")

def view_all_providers():
    providers = ServiceProvider.get_all(session)
    if providers:
        for provider in providers:
            print(provider)
    else:
        print("No providers found.")

def add_instance():
    
    event1 = Event.create(session, "Product promotion", "2025-04-15")
    event2 = Event.create(session, "Wedding Fair", "2025-05-20")
    event3 = Event.create(session, "Music Concert", "2025-06-10")

    
    provider1 = ServiceProvider.create(session, "Catering Service", "Food & Drink")
    provider2 = ServiceProvider.create(session, "Sound & Lighting", "Event Equipment")
    provider3 = ServiceProvider.create(session, "Security Service", "Event Security")

    
    Attendee.create(session, "Bin Amin", event1.id)
    Attendee.create(session, "Steve Mwangi", event1.id)
    Attendee.create(session, "Victor Kuria ", event2.id)
    Attendee.create(session, "Kasongo the 5th", event2.id)
    Attendee.create(session, "Citizen Wanjiku", event3.id)

    print("Database populated with 3 events, 3 service providers, and 5 attendees.")

def main():
    
    add_instance()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            create_event()
        elif choice == "2":
            delete_event()
        elif choice == "3":
            view_all_events()
        elif choice == "4":
            view_attendees()
        elif choice == "5":
            create_provider()
        elif choice == "6":
            delete_provider()
        elif choice == "7":
            view_all_providers()
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
