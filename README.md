# HIMSS Technical Assessment

Project guidelines here:
- [morkro/coding-challenge](https://github.com/morkro/coding-challenge)

## Installation
```
git clone git@github.com:ryannathanwilson/HIMSS_Interview.git
```

### Backend
Run the following bash commands to install the backend and run local django server.
```
cd HIMSS_Interview/backend
python3 -m venv .
source bin/activate // or 'source Scripts/activate'
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend
In a separate bash instance, run the following commands to install react/node dependencies and run local node server.
```
cd HIMSS_Interview/frontend
npm install
npm start
```

## Project Objectives
- Create running full stack application for spam protection
- Copy UI provided in project README
- Block content
- Resolve content with PUT request to /reports/:reportId

## Project Plan
- Use Django and React
    - I'm most familiar with these two platforms
    - Django has built in functionality for REST APIs
    - Django has many additional useful features in its ecosystem, if this project were further developed, such as authentication.
    - React is widely used, making it easy to find engineers to work on it.
    - React works well when API calls are being made, and state needs to be updated appropriately
- Backend / Django
    - Setup models to match data/reports.json
    - Create serializers
    - Create endpoint for reading all the data
    - Create endpoint for writing data
    - Create script for blocking
        - Write code that modifies patch function to run on PUT request
    - Create script for resolving
        - Same principle as blocking. Ensure resolved reports are removed from GET Report
- Frontend / React
    - Create function to get data
    - Create component to display data
    - Create function to block data
    - Create function to resolve Data
    - Create dummy component to write data/reports.json to backend

## Challenges
- How to format data model, specifically "sub objects".
	- Multiple tables with foreign key
	- Reference is primary object
		- Payload describes the Reference
		- Multiple reports may refer to the same reference, presumably multiple people have reported the same piece of spam.
- How to write to multiple tables with one layered object.
	- Nested serializers allow easy reading of all the layers
	- Standard serializers can then write to the separate tables.
- How to do a put request
    - PUT request works natively, but needs to be modified to include partial_update objects.
- Should resolving simply delete a report?
    - Report might be important for other functions, so add "ticketState" and update as per instruction.
- How to block?
    - Set state to "BLOCKED"
    - Configure "partial_update()"
	- Block the reference, so that all reports that correspond to that report will be updated as well.

## Next Step Features
- Authentication
- Toggle hide/show "BLOCKED" reports
- Testing
- Add loading state during async function operation
	- Move logic for complex write and delete to the backend.
- Animate card disappearing so it's visually obvious to user, that it has disappeard.