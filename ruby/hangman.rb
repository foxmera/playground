# By foxmera (MT Fischer), January 2018
#
# HANGMAN TERMINAL GAME IN RUBY 
#
#       _______
#      |/      |
#      |      (_)
#      |      \|/
#      |       |
#      |      / \
#      |
#     _|___
# 
# 
# Simple terminal game
# 
# Example:
#       _______
#      |/      |
#      |      
#      |      
#      |       
#      |      
#      |
#     _|___
# WORD LENGTH: 7
# REMAINING TRIES: 6
# PREVIOUS LETTERS: A,E,F,N,O,R,S
# ========================
# _E__N_S
# ========================
# Insert new character: f
# 
#    _______
#   |/      |
#   |      (_)
#   |      \|/
#   |       |
#   |      / \
#   |
#  _|___
#  === GAME OVER ===

$fail_status = [
" 
        
        
       
        

       
  
 
"," 
        

        
       
         
       
  
 _____
", " 

  |      
  |      
  |     
  |       
  |     
  |
 _|___
", " 
   _______
  |/      
  |      
  |     
  |       
  |     
  |
 _|___
", " 
   _______
  |/      |
  |      
  |      
  |       
  |     
  |
 _|___
", " 
   _______
  |/      |
  |      (_)
  |      
  |       
  |     
  |
 _|___
", " 
   _______
  |/      |
  |      (_)
  |       |
  |       |
  |     
  |
 _|___
", " 
   _______
  |/      |
  |      (_)
  |      \\|
  |       |
  |     
  |
 _|___
", " 
   _______
  |/      |
  |      (_)
  |      \\|/
  |       |
  |     
  |
 _|___
", " 
   _______
  |/      |
  |      (_)
  |      \\|/
  |       |
  |     _/ 
  |
 _|___
", " 
   _______
  |/      |
  |      (_)
  |      \\|/
  |       |
  |     _/ \\_
  |
 _|___
 === GAME OVER ===
"
]

$word_list = ["Aerger","Aerztin","Abend","Abfahrt","Abflug","Absender","Adresse","Alkohol","Alter","Ampel","Anfang","Angebot","Angestellte","Angst","Ankunft","Anmeldung","Anrede","Anruf","Anrufbeantworter","Ansage","Anschluss","Antwort","Anzeige","Anzug","Apfel","Apotheke","Appartement","Appetit","April","Arbeit","Arbeitsplatz","Arm","Arzt","Aufenthalt","Aufgabe","Aufzug","Auge","August","Ausbildung","Ausflug","Ausgang","Auskunft","Auslaender","Auslaenderin","Ausland","Aussage","Ausstellung","Ausweis","Auto","Autobahn","Automat","Baeckerei","Buero","Baby","Bad","Bahn","Bahnhof","Bahnsteig","Balkon","Banane","Bank","Batterie","Baum","Beamte","Beamtin","Bein","Beispiel","Bekannte","Benzin","Beratung","Berg","Beruf","Berufsschule","Besuch","Betrag","Bett","Bewerbung","Bier","Bild","Bildschirm","Birne","Bitte","Blatt","Bleistift","Blick","Blume","Bluse","Blut","Bogen","Bohne","Broetchen","Bruecke","Brief","Briefkasten","Briefmarke","Brieftasche","Briefumschlag","Brille","Brot","Bruder","Buch","Buchstabe","Bus","Butter","Chef","Computer","Creme","Dach","Dame","Dank","Datum","Dauer","Deutsche","Dezember","Dienstag","Ding","Disco","Doktor","Dom","Donnerstag","Doppelzimmer","Dorf","Drucker","Durchsage","Durst","Dusche","EMail","Ecke","Ehefrau","Ehemann","Ei","Einfuehrung","Eingang","Einladung","Eintritt","Einwohner","Einzelzimmer","Eis","Eltern","Empfaenger","Empfang","Ende","Enkel","Entschuldigung","Erdgeschoss","Erfahrung","Ergebnis","Erlaubnis","Ermaessigung","Erwachsene","Essen","Export","Faehre","Fuehrerschein","Fuehrung","Fabrik","Fahrer","Fahrkarte","Fahrplan","Fahrrad","Familie","Familienname","Familienstand","Farbe","Fax","Februar","Fehler","Fenster","Ferien","Fernsehgeraet","Fest","Feuer","Feuerwehr","Feuerzeug","Fieber","Film","Firma","Fisch","Flasche","Fleisch","Flughafen","Flugzeug","Flur","Fluss","Formular","Foto","Fotoapparat","Fruehjahr","Fruehling","Fruehstueck","Frage","Frau","Freitag","Freizeit","Freund","Freundin","Friseur","Frist","Fuss","Fussball","Fundbuero","Gabel","Garage","Garten","Gas","Gast","Gebuehr","Geburtsjahr","Geburtsort","Geburtstag","Gegenteil","Geld","Geldboerse","Gemuese","Gepaeck","Gericht","Gesamtschule","Geschaeft","Geschenk","Geschirr","Geschwister","Gesicht","Gespraech","Gesundheit","Getraenk","Gewicht","Gewitter","Glueck","Glueckwunsch","Glas","Gleis","Groesse","Grenze","Grippe","Grosseltern","Grossmutter","Grossvater","Gruss","Grundschule","Gruppe","Guthaben","Gymnasium","Haehnchen","Haar","Halbpension","Halle","Hals","Haltestelle","Hand","Handtuch","Handy","Haus","Hausaufgabe","Hausfrau","Haushalt","Hausmann","Heimat","Heizung","Hemd","Herbst","Herd","Herr","Herz","Hilfe","Hobby","Holz","Hose","Hund","Hunger","Idee","Import","Industrie","Information","Inhalt","Internet","Jacke","Jahr","Januar","Job","Jugendherberge","Jugendliche","Juli","Junge","Juni","Kaese","Koerper","Kueche","Kuehlschrank","Kuendigung","Kaffee","Kalender","Kamera","Kanne","Karte","Kartoffel","Kasse","Kassette","Kassettenrecorder","Katze","Keller","Kellner","Kenntnisse","Kennzeichen","Kette","Kfz","Kind","Kindergarten","Kinderwagen","Kino","Kiosk","Kirche","Klasse","Kleid","Kleidung","Kneipe","Koffer","Kollege","Kollegin","Konsulat","Kontakt","Konto","Kontrolle","Konzert","Kopf","Kosmetik","Krankenkasse","Krankheit","Kredit","Kreditkarte","Kreis","Kreuzung","Kuchen","Kugelschreiber","Kunde","Kundin","Kurs","Loeffel","Loesung","Laden","Lager","Lampe","Land","Landschaft","Leben","Lebensmittel","Leid","Lehre","Lehrer","Lehrerin","Leute","Licht","Lied","Lkw","Loch","Lohn","Lokal","Luft","Lust","Maedchen","Maerz","Moebel","Muell","Muelltonne","Magen","Mai","Mal","Mann","Mantel","Markt","Maschine","Material","Mechaniker","Medikament","Meer","Mehrwertsteuer","Meinung","Menge","Mensch","Messer","Metall","Miete","Milch","Minute","Mittag","Mitte","Mitteilung","Mittel","Mittelschule","Mittwoch","Mode","Moment","Monat","Montag","Morgen","Motor","Mund","Museum","Musik","Mutter","Naehe","Nachbar","Nachbarin","Nachmittag","Nachrichten","Nacht","Name","Natur","Nebel","Norden","Notarzt","Note","Notfall","Notiz","November","Nudel","Nummer","Ober","Obst","Oktober","Oma","Opa","Operation","Orange","Ordnung","Ort","Osten","Oel","Paeckchen","Paket","Panne","Papier","Papiere","Parfuem","Park","Partei","Partner","Partnerin","Party","Pass","Pause","Pension","Pkw","Plan","Plastik","Platz","Polizei","Pommesfrites","Portion","Post","Postleitzahl","Pruefung","Praktikum","Praxis","Preis","Problem","Produkt","Programm","Prospekt","Pullover","Qualitaet","Quittung","Ruecken","Rabatt","Radio","Rathaus","Raucher","Raucherin","Raum","Realschule","Rechnung","Regen","Reifen","Reinigung","Reis","Reise","Reisebuero","Reisefuehrer","Reparatur","Restaurant","Rezept","Rezeption","Rind","Rock","Rose","Rundgang","Sueden","SBahn","Sache","Saft","Salat","Salz","Samstag","Sonnabend","Satz","Schueler","Schuelerin","Schalter","Scheckkarte","Schiff","Schild","Schinken","Schirm","Schluessel","Schloss","Schluss","Schmerzen","Schnee","Schnupfen","Schokolade","Schrank","Schuh","Schule","Schwein","Schwester","Schwimmbad","See","Sehenswuerdigkeit","Seife","Sekretaerin","Sekunde","Sendung","Senioren","September","Service","Sessel","Sofa","Sohn","Sommer","Sonderangebot","Sonne","Sonntag","Sorge","Spuelmaschine","Spass","Spaziergang","Speisekarte","Spielplatz","Sprache","Sprachschule","Sprechstunde","Stueck","Stadt","Standesamt","Stempel","Steuer","Stock","Stoff","Strasse","Strassenbahn","Strand","Streichholz","Strom","Student","Studentin","Studium","Stuhl","Stunde","Supermarkt","Suppe","Tuer","Tuete","Tag","Tankstelle","Tasche","Tasse","Taxi","Tee","Teil","Telefon","Telefonbuch","Teller","Teppich","Termin","Test","Text","Theater","Thema","Ticket","Tier","Tipp","Tisch","Tochter","Toilette","Tomate","Topf","Tourist","Treppe","Trinkgeld","Turm","UBahn","Uhr","Unfall","Universitaet","Unterhaltung","Unterkunft","Unterricht","Unterschied","Unterschrift","Untersuchung","Urlaub","Uebernachtung","Vater","Verbindung","Verein","Verkaeufer","Verkaeuferin","Verkehr","Vermieter","Versicherung","Verspaetung","Vertrag","Video","Vogel","Volksschule","Vormittag","Vorname","Vorsicht","Vorwahl","Waesche","Wagen","Wald","Wasser","Weg","Wein","Welt","Werkstatt","Werkzeug","Westen","Wetter","Wiederhoeren","Wiedersehen","Wind","Winter","Wirtschaft","Woche","Wochenende","Wochentag","Wohnung","Wolke","Wort","Wunsch","Wurst","Zahl","Zahn","Zeit","Zeitschrift","Zeitung","Zentrum","Zettel","Zeugnis","Zigarette","Zimmer","Zitrone","Zoll","Zucker","Zug"]
$number_of_fails = 0
$max_retries = $fail_status.length - 1
$guessed_characters = []

$secret_word = {}
$secret_word["solution"] = $word_list.sample.upcase
$secret_word["guess"] = $secret_word["solution"].gsub(/./, "_")
$secret_word["length"] = $secret_word["solution"].length

def insert_character()
  print "Insert new character: "
  char = gets.chomp

  unless char.length == 1 
    puts "Only single letters please"
    return insert_character()
  end

  unless /[a-zA-Z]/.match(char)
    puts "Only a-z letters please"
    return insert_character()
  end

  char.upcase!

  return char
end

def get_all_occurrences(word, char)
  return (0 ... word.length).find_all { |i| word[i,1] == char }
end

def add_letter(char)
  occurrences = get_all_occurrences($secret_word["solution"], char)
  occurrences.each do |i|
    $secret_word["guess"][i] = char
  end
end

def add_fail()
  $number_of_fails += 1
end

def guess_char(char)
  if $guessed_characters.include? char
    return
  end

  $guessed_characters.push(char)

  if $secret_word["solution"].include? char
    add_letter(char)
  else  
    add_fail()
  end 
end

def puts_info()
  puts `clear`
  
  puts $fail_status[$number_of_fails]
  puts "WORD LENGTH: #{$secret_word["length"]}" 
  puts "REMAINING TRIES: #{$max_retries - $number_of_fails}"
  puts "PREVIOUS LETTERS: #{$guessed_characters.uniq.sort.join(',')}" 

  puts "========================"
  puts $secret_word["guess"]
  puts "========================"
end

def run_hangman()
  # GAMEPLAY
  until $secret_word["solution"] == $secret_word["guess"] || $number_of_fails == $max_retries
    puts_info()
    
    try_char = insert_character()
    guess_char(try_char)
    
    puts $fail_status[$number_of_fails]
  end

  # SUCCESS OR GAME OVER
  if $secret_word["solution"] == $secret_word["guess"]
    puts `clear`
    puts $secret_word["solution"]
    puts '=== GZ! YOU SOLVED IT! ==='
  else
    puts `clear`
    puts $fail_status[$fail_status.length - 1]
  end
end

run_hangman()