# MediScheduler
Automated scheduling for medical student clerkship rotations. 
# Installation 
# What is this? 
At Canadian medical schools, all medical students are required, during 3rd-year, to complete a number of clerkship rotations in different specialties-- for example, "Family Medicine", "Geriatrics", "Psychiatry", etc. 

On these rotations, students are scheduled to work with real patients under the superivison of practicing doctors in community training sites. These sites can be numerous and geographically dispersed. 

Scheduling is usually done manually by administrative staff at the medical school.

This application automates the scheduling process. 

It also provides a user-interface to display, for each student, route and directions to their training site. Admin can export this to PDF and give it to the student. 

# Important 
Assumes that a clerkship schedule for an academic-year is divided into 6 "sessions" or tracks.  

Assumes each Excel file is structured into the following columns: 
Student Data: ID | FirstName | LastName | Address |TravelMethods | Session#
Teacher Data: ID | FirstName | LastName | EmailAddress | Address | Availability

Users upload two Excel files, one containing student data and another containing teacher data. 

The application then returns an optimized schedule, where "optimized" is defined as minimizing the 
required travel-time for students who bike/walk/use transit. 

This  is basically a proof of concept. Many results for certain cities are inaccurate-- if those cities haven't been well mapped to OSM, then Nominatim can't geocode them accurately. 

It could easily be made accurate by using a paid geocoding service like Google's Geocoding API. 

# Notes 
Configured a Docker container to run an instance of osrm-backend to handle routing queries 
Developed a frontend to display route and directions using leaflet and implemented an export-to-pdf option 
Designed and implemented a greedy algorithm to minimize travel time for students 
