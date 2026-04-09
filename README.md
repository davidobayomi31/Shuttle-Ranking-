# Shuttle-Ranking-

##Chosen Problem (1-2 sentences)
I chose option 3, shuttle stop crowd ranking. this aplication sorts campus shuttle stops based on the current crowd count to help administration decide which location requires an extra shuttle to help manage the student crowd.
## Chosen Algorithm (name + why it fits)
The algorithm i chose for this project is quick sort. quick sort uses divide and conquer technique which i think would be efficient and can quickly rank the shuttle stops even if the list of location grows

## Demo (video/gif/screenshot of at least one run)
<img width="1352" height="878" alt="Screenshot 2026-04-08 at 9 13 01 PM" src="https://github.com/user-attachments/assets/af95a528-a6f7-4fbc-b380-08c660c9de8c" />

## Problem Breakdown & Computational Thinking (include a flowchart + the 4 pillars as brief bullets)
Decomposition: Breaking the sorting task into smaller steps. create a list where each element is a shuttle stop pair (["student Union", 85]. pick one stop as a pivot. group all stop with fewer people than the pivot to the left and those with more people ot the right.

Pattern recognition: i identified that the "split and swap" alwasys repeats. whether i am sorting a list of 50 stops or 2 stops, the process of comparing a stop's crowd count to a pivot and moving it to stay identical all through the recursion.

Abstraction: I focused on the essential data that is needed for the decision making process, kept numerical crowd count, becasue these are important in order to decide where the extra shuttle bus would go. Things that I would consider not as impottand would be the specific GPS coordinates or the buis drivers name. Thse dont impact the sortiong logic or the crowed ranking goal. 

Algorithmic thinking: design the application flow that acts as a live decision tool for campus transit.
Input: the user would interact with the GUI to input the list of campus shuttle stops and their passanger count.
Processig stage: the algorithm uses a quick sort. To help the user follow along, the app will highlight the Pivot in one color (e.g., Red) and the current Stops being compared in another (e.g., Yellow)
Output: The GUI outputs the final ranked list from "most crowed" to "least crowed".

-----------------------------------------------------------------------------------------
![IMG_1258](https://github.com/user-attachments/assets/96c83457-cee9-497a-b4ff-3fff5206423f)


## Steps to Run (local) + requirements.txt
## Hugging Face Link
## Testing (what you tried + edge cases)
## Author & Acknowledgment (sources + AI use, if any)


