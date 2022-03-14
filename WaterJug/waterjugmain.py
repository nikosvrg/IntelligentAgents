"""# **Water Jug Problem**

Στο πρόβλημα της κανάτας νερού στην Τεχνητή Νοημοσύνη, μας παρέχονται δύο κανάτες οι οποίες περιέχουν έναν γνωστό ακέραιο όγκο υγρού, όχι απαραίτητα ίσο με την χωρητικότητα της. Στόχος είναι να βρεθούν πόσα βήματα ρίψης νερού απο την μία κανάτα στην άλλη ( μέχρι να αδειάσει είτει η μια κανάτα είτε η άλλη να γεμίσει) για να επιτευχθεί η κατάσταση στόχου, που καθορίζεται απο τον χρήστη.

**Αναπαράσταση κατάστασης:**

Θα αντιπροσωπεύσουμε μια κατάσταση του προβλήματος ως πλειάδα (x,y) όπου το x αντιπροσωπεύει την ποσότητα νερού στην κανάτα Α  και το y αντιπροσωπεύει την ποσότητα στην κανάτα Β.
Σημειώνεται ότι 0 <= x <= χωρητικότητα_y και 0 <= y <= χωρητικότητα_y.

**Κανόνες Παραγωγής:**

*   (x, y) -> (a, y) if x < a
*   (x, y) -> (x, b) if y < b
*   (x, y) -> (0, y) if x > 0
*   (x, y) -> (x, 0) if y > 0
*   (x, y) -> (min(x+y, a), max(0, x+y - a)) if y > 0
*  (x, y) -> (max(0, x+y - b), min(x+y, b)) if x > 0

Αυτοί οι κανόνες παραγωγής χρησιμοποιούνται για την εύρεση των γειτονικών καταστάσεων από τις τρέχουσες καταστάσεις.
Ο αλγόριθμος έχει ως εξής:





1.   Δημιουργία κενού μονοπατιού
2.   Προσθήκη αρχικής κατάστασης στην ουρά
3.   Αν επισκευτεί την μαρκάρουμε σαν visited
4.   Αν η front είνια κενή, ακολουθούμε τα βήματα 5-7
5.   Αφαιρούμε την κατάσταση απο την front και την ονομάζουμε current. Προσθέτουμε την current στην path list.
6.   Αναπτύσουμε τους γείτονες σύμφωνα με τους κανόνες παραγωγής.
7.   Αν οι γείτονες δεν είναι visited, τους προσθέτουμε στην λίστα visited και τους προσθέτουμε στην ουρά front
8.   Επιστρέφουμε το μονοπάτι

Ο χρήστης θα ορίσει ενα σύνολο τελεστών που θα μας μεταφέρουν απο την μία κατάσταση στην άλλη.

Κανάτα Α: x γαλόνια νερού

Κανάτα Β: y γαλόνια νερού

Στόχος: z γαλόνια σε μια κανάτα
"""

a_capacity = int(input("Xwritikotita kanatas A: "))
b_capacity = int(input("Xwritikotita kanatas B: "))
goal = int(input("Stoxos: "))

def gcd(a, b):
 if a == 0:
		 return b
 else:
	    return gcd(b%a, a)

def bfs(start, goal, a_capacity, b_capacity):
	path = []
	front = []
	front.append(start)
	visited = []
	#visited.append(start)
	while(not (not front)):
		current = front.pop()
		x = current[0]
		y = current[1]
		path.append(current)
		if x == goal or y == goal:
			print ("Vrethike Lysh")
			return path
		# kanonas 1
		if current[0] < a_capacity and ([a_capacity, current[1]] not in visited):
			front.append([a_capacity, current[1]])
			visited.append([a_capacity, current[1]])

		# kanonas 2
		if current[1] < b_capacity and ([current[0], b_capacity] not in visited):
			front.append([current[0], b_capacity])
			visited.append([current[0], b_capacity])

		# kanonas 3
		if current[0] > a_capacity and ([0, current[1]] not in visited):
			front.append([0, current[1]])
			visited.append([0, current[1]])

		# kanonas 4
		if current[1] > b_capacity and ([a_capacity, 0] not in visited):
			front.append([a_capacity, 0])
			visited.append([a_capacity, 0])

		# kanonas 5
		#(x, y) -> (min(x + y, a_capacity), max(0, x + y - a_capacity)) if y > 0
		if current[1] > 0 and ([min(x + y, a_capacity), max(0, x + y - a_capacity)] not in visited):
			front.append([min(x + y, a_capacity), max(0, x + y - a_capacity)])
			visited.append([min(x + y, a_capacity), max(0, x + y - a_capacity)])

		# kanonas 6
		# (x, y) -> (max(0, x + y - b_capacity), min(x + y, b_capacity)) if x > 0
		if current[0] > 0  and ([max(0, x + y - b_capacity), min(x + y, b_capacity)] not in visited):
			front.append([max(0, x + y - b_capacity), min(x + y, b_capacity)])
			visited.append([max(0, x + y - b_capacity), min(x + y, b_capacity)])

	return "Den vrethike"


# start state: a = 0 , b = 0
start = [0, 0]


if goal % gcd(a_capacity,b_capacity) == 0:
	 print("Monopati:",bfs(start, goal, a_capacity, b_capacity))
else:
 	 print("Den vrethike lysh")

"""**ΠΕΡΙΓΡΑΦΗ ΛΥΣΗΣ**

*Αρχική Κατάσταση*: Κανάτα Α = 0 Κανάτα Β = 0 **[0,0]**

*Επόμενη Κατάσταση*: Γεμίζουμε την κανάτα Β **[0,3]**

*Επόμενη Κατάσταση*: Αδειάζουμε την κανάτα Α στην κανάτα Β **[3,0]**

*Επόμενη Κατάσταση*: Γεμίζουμε την κανάτα Β **[3,3]**

*Επόμενη Κατάσταση*: Γεμίζουμε την κανάτα Α ρίχνοντας 2 λίτρα απο την κανάτα Β **[5,1]**

*Επόμενη Κατάσταση*: Γεμίζουμε την κανάτα Β **[5,3]**

*Επόμενη Κατάσταση*: Αδειάζουμε την κανάτα Β καθώς έχουμε τα απαραίτητα λίτρα **[5,0]**

*Επόμενη Κατάσταση*:Γεμίζουμε την κανάτα Β μέχρι να έχουμε 2 λίτρα σε μία κανάτα **[2,3]** όπου είναι και ο τελικός μας στόχος.
"""