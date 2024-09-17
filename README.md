# MediScheduler
Automated scheduling for medical student clerkship rotations. 
# Installation 
TODO
# What is this? 
At Canadian medical schools, all medical students are required, during 3rd-year, to complete a number of clerkship rotations in different specialties-- for example, "Family Medicine", "Geriatrics", "Psychiatry", etc. 

On these rotations, students are scheduled to work with real patients under the superivison of practicing doctors in community training sites. These sites can be
geographically dispersed. 

Scheduling is usually done manually by administrative staff at the medical school.

This application automates the scheduling process. 

It also provides, for each student, route and directions to their training site. 

# Example Use 
TODO 

# Important 
Assumes that a clerkship schedule for an academic-year is divided into 12 "sessions" or tracks.  

Assumes each Excel file is structured into the following columns:<br>
Student Data: ID | FirstName | LastName | Address |TravelMethods | Session# <br>
Teacher Data: ID | FirstName | LastName | EmailAddress | Address | Availability

Users upload two Excel files, one containing student data and another containing teacher data. 

The application then returns an optimized schedule, where "optimized" is defined as minimizing the 
required travel-time for students who bike/walk/use transit. 

# Notes 
This  is basically a proof of concept. Results for certain regions may be inaccurate.
 
