# ΕΠΑΝΗΛΗΨΗ ΒΑΣΙΚΩΝ ΕΝΝΟΙΩΝ ΣΤΗΝ PYTHON

> ΑΡΧΕΣ ΓΛΩΣΣΩΝ ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΥ
 
> ΤΜΗΜΑ ΠΛΗΡΟΦΟΡΙΚΗΣ ΚΑΙ ΤΗΛΕΠΙΚΟΙΝΩΝΙΩΝ-ΕΞΑΜΗΝΟ 4ο

> ΑΡΤΑ,2021

---

## ΑΛΦΑΡΙΘΜΗΤΙΚΑ

### ΠΑΡΑΔΕΙΓΜΑΤΑ ΜΕ ΑΛΦΑΡΙΘΜΗΤΙΚΑ
  
  * [string1.py](STRINGS/string1.py)
  * [string2.py](STRINGS/string2.py)
  * [string3.py](STRINGS/string3.py)
  * [string4.py](STRINGS/string4.py)
  * [string5.py](STRINGS/string5.py)
  * [string6.py](STRINGS/string6.py)

## ΛΙΣΤΕΣ

**Αποθήκευση πολλαπλών δεδομένων σε μία δομή.Οι λέστες είναι mutable.Αυτο σημαίνει ότι μπορεί να τροποποιηθεί το μέγεθος τους και να αλλάξουν οι τιμές των δεδομένων τους**

### ΠΑΡΑΔΕΙΓΜΑΤΑ ΜΕ ΛΙΣΤΕΣ

* [list1.py](LISTS/list1.py)
* [list2.py](LISTS/list2.py)
* [list3.py](LISTS/list3.py)
* [list4.py](LISTS/list4.py)
* [list5.py](LISTS/list5.py)
* [list6.py](LISTS/list6.py)
* [list7.py](LISTS/list7.py)
* [list8.py](LISTS/list8.py)
* [list9.py](LISTS/list9.py)
* [list10.py](LISTS/list10.py)

## ΠΛΕΙΑΔΕΣ(TUPLES)

**Συλλογή από αντικείμενα που είναι προκαθορισμένο και immutable.Τα δεδομένα και το πλήθος των δεδομένων μίας πλειάδας δεν μπορεί να αλλάξει.**

### ΠΑΡΑΔΕΙΓΜΑΤΑ ΜΕ ΠΛΕΙΑΔΕΣ
* [tuple1.py](TUPLES/tuple1.py)
* [tuple2.py](TUPLES/tuple2.py)
* [tuple3.py](TUPLES/tuple3.py)
* [tuple4.py](TUPLES/tuple4.py)
* [tuple5.py](TUPLES/tuple5.py)

## ΛΕΞΙΚΑ(DICTIONARIES)

**Δομές οι οποίες αποθηκεύουν δεδομένα σε μορφή key:value.Τα λεξικά είναι δομές προκαθορισμένες(Μπορείς να ανεφερθεί σε ένα αντικείμενο του λεξικού με ένα συγκεκριμένο index) ,με μεταβλητό μήκος οι οποίες δεν επιτρέπουν διπλότυπα,ωστόσο η τιμή ενός κλειδιού μπορεί να τροποποιηθεί.**

### ΠΑΡΑΔΕΙΓΜΑΤΑ ΜΕ ΛΕΞΙΚΑ

* [dictionary1.py](DICTIONARIES/dictionary1.py)
* [dictionary2.py](DICTIONARIES/dictionary2.py)
* [dictionary3.py](DICTIONARIES/dictionary3.py)
* [dictionary4.py](DICTIONARIES/dictionary4.py)
* [dictionary5.py](DICTIONARIES/dictionary5.py)

## PYTHON SCOPE(ΕΜΒΕΛΕΙΑ)

**Η εμβέλεια καθορίζει μέχρι ποιό σημείο του προγράμματος μας μία μεταβλητή είναι ορατή.Η εμβέλεια εξαρτάται από το σημείο τοποθέτησης στο κώδικα μας.Κοινες κατηγορίες εμβέλεια είναι η τοπική και η καθολική εμβέλεια.**
 
* **Καθολική εμβέλεια:Διαθεσιμότητα σε όλο τον κώδικα.**
* **Τοπική εμβέλεια:Διαθεσιμότητα σε ένα συγκεκριμένο τμήμα του κώδικα.**

### ΠΑΡΑΔΕΙΓΜΑΤΑ ΕΜΒΕΛΕΙΑΣ

* [scope1.py](SCOPE/scope1.py)
* [scope2.py](SCOPE/scope2.py)
* [scope3.py](SCOPE/scope3.py)
* [scope4.py](SCOPE/scope4.py)
* [scope5.py](SCOPE/scope5.py)
* [scope6.py](SCOPE/scope6.py)

## COMPREHENSIONS

**Η python φημίζεται για το ότι επιτρέπει στον χρήστη να γράψει εκλεπτυσμένο κώδικα,δηλαδή κώδικα εύκολο στην συγγραφή του και εύκολο στην ανάγνωση του(σαν καθημερινή γλώσσα).Τα Comprehensions είναι ένα  από τα μοναδικότερα χαρακτηριστικά της python.Με τα Comprehensions επιτυνχάνεται δυναμική λειτουργικότητα σε μόνο μία γραμμή κώδικα.**

  > * List Comprehension για δημιουργία μίας λίστας με 10 τυχαίους αριθμούς
  ```
    import random as r
    from time import time
    r.seed(time()*1000)
    alist=[r.randint(1,1000) for _ in range(10)]
    print(alist)
  ```
  
  > * List Comprehension για filtering λίστας

  ```
    import random as r
    from time import time
    r.seed(time()*1000)
    alist=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    odd_numbers=[x for x in alist if x%2!=0]
    print(odd_numbers)
  ```


  <br>


  >**Σύνταξη:expression for member in iterable (if condition)]**


### ΠΑΡΑΔΕΙΓΜΑΤΑ ΜΕ COMPREHENSIONS

* [comprehension1.py](COMPREHENSIONS/comprehension1.py)
* [comprehension2.py](COMPREHENSIONS/comprehension2.py)
* [comprehension3.py](COMPREHENSIONS/comprehension3.py)
* [comprehension4.py](COMPREHENSIONS/comprehension4.py)
* [comprehension5.py](COMPREHENSIONS/comprehension5.py)

## OOP--PYTHON
**Είναι μια μέθοδος δομής ενός προγράμματος με τη δέσμευση σχετικών ιδιοτήτων και συμπεριφορών σε μεμονωμένα αντικείμενα.**

### ΠΑΡΑΔΕΙΓΜΑΤΑ ΜΕ OOP
* [oop1.py](OOP/oop1.py)
* [oop2.py](OOP/oop2.py)
* [oop3.py](OOP/oop3.py)
* [oop4.py](OOP/oop4.py)
* [oop5.py](OOP/oop5.py)

## FILES

### ΠΑΡΑΔΕΙΓΜΑΤΑ ME FILES
* [file1.py](FILES/file1.py)
* [file2.py](FILES/file2.py)
* [file3.py](FILES/file3.py)



