# HIMSS Technical Assessment

Project guidelines here:
- [morkro/coding-challenge](https://github.com/morkro/coding-challenge)


## Project Objectives
- Create running full stack application for spam protection
- Copy UI provided in project README
- Block content
- Resolve content with PUT request to /reports/:reportId

## Project Plan
- Use Django and React
    - I'm most familiar with these two platforms
    - Django has built in functionality for REST APIs
    - Django has many additional useful features in its ecosystem including authentication
    - React is widely used, making it easy to find engineers to work on it.
    - React works well when API calls are being made, and state needs to be updated appropriately
- Backend / Django
    - Setup models to match data/reports.json
    - Create serializers
    - Create endpoint for reading all the data
    - Create endpoint for writing data
    - Create endpoint for blocking
        - Write code that runs at blockig endpoint
    - Create endpoint for resolving
        - Write code that runs at resolving endpoint
- Frontend / React
    - Create hook to get data
    - Create component to display data
    - Create hook to block data
    - Create hook to resolve Data
    - Create dummy component to write data/reports.json to backend

## Challenges
- How to format data model, specifically "sub objects"?
	- Multiple tables with foreign key
- How to write to multiple tables with one layered object
- How to do a put request
- Should resolving simply delete a report?
    - I would prefer to mark "resolved" column to true
    - Archive periodically
- How to block?
    - Set state to "BLOCKED"

## Next Step Features
- Authentication
- Toggle hide/show "BLOCKED" reports
- Testing

## Installation
### Backend
- git clone git@github.com:ryannathanwilson/HIMSS_Interview.git
- cd backend
- python3 -m venv .
- source bin/activate (or 'source Scripts/activate')
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver

### Frontend
- cd frontend
- npm install
- npm start