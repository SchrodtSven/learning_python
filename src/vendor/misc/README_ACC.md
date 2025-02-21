Du sollst verschiedene Arten von Bankkonten verwalten. Eine Basisklasse namens BankAccount bildet die Grundlage für verschiedene Kontotypen wie PrimeAccount, PlatinumAccount und SavingsAccount, die jeweils spezielle Funktionen und Verhaltensweisen besitzen.

BankAccount (Basisklasse):

Attribute:
* owner (Name des Kontoinhabers)
* balance (Kontostand, Standardwert: 0)

Methoden:
* deposit(amount) – Fügt dem Konto einen Betrag hinzu.
* withdraw(amount) – Hebt Geld ab, sofern genügend Guthaben vorhanden ist.
* get_balance() – Zeigt den aktuellen Kontostand an.

<hr>

PrimeAccount (Erbt von BankAccount):

Fügt eine Zinsrate für das Konto hinzu.<br>
Neue Methode:<br>
apply_interest() – Wendet Zinsen (Standardwert: 2 %) auf den Kontostand an.

<hr>

SavingsAccount (Erbt von BankAccount):

Hat einen blockierten Zustand, der Abhebungen verhindert.<br>
Höhere Zinsrate (Standardwert: 5 %) für das Sparen.<br>
Überschreibt withdraw() – Abhebungen sind nur erlaubt, wenn das Konto entsperrt ist.<br>
Neue Methoden:<br>
apply_interest() – Wendet höhere Zinsen auf den Kontostand an.<br>
unblock_account() – Ermöglicht es dem Kontoinhaber, das Konto zu entsperren, um Abhebungen zu ermöglichen.<br>

<hr>

Aufgabenbeschreibung:
Erkunde die Vererbungsstruktur:

Identifiziere, wie die Kindklassen (PrimeAccount und SavingsAccount) von der Basisklasse BankAccount erben.
Achte darauf, wie bestimmte Methoden überschrieben werden (z.B. withdraw()), um spezifische Funktionalitäten für jeden Kontotyp zu bieten.
Implementiere und teste die Konten:

Erstelle mindestens ein Objekt für jeden Kontotyp (BankAccount, PrimeAccount, PlatinumAccount, SavingsAccount).
Führe folgende Aktionen für jeden Kontotyp aus:
Einzahlen von Geld.
Abheben von Geld (sorge dafür, dass verschiedene Verhaltensweisen ausgelöst werden).
Zinsen anwenden (für Konten, die diese Funktion unterstützen).
Entsperre und hebe Geld von einem Sparkonto ab.
Erweiterung (Optional):

Modifiziere die Klassen, um zusätzliche Funktionen hinzuzufügen, wie z.B.:
Eine Strafgebühr für Sparkonten, die frühzeitig entsperrt werden.
Transaktionslimits für Prime-Konten.
Anpassung der Zinsrate für jeden Kontoinhaber.