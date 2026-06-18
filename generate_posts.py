import itertools
import html
import random
from datetime import datetime, timedelta

# List of 48 teams in FIFA World Cup 2026
TEAMS = [
    {
        "name": "Mexico",
        "formation": "4-3-3",
        "lineup": ["Santiago Gimenez", "Hirving Lozano", "Edson Alvarez", "Luis Chavez", "Erick Sanchez", "Uriel Antuna", "Cesar Montes", "Johan Vasquez", "Jorge Sanchez", "Jesus Gallardo", "Guillermo Ochoa"],
        "star": "Santiago Gimenez",
        "tactical_style": "utilizes high-intensity pressing and swift wing transitions through Hirving Lozano to stretch the opposition defense",
        "defensive_style": "maintains a high defensive line organized by Cesar Montes, aiming to trap opponent attackers offside"
    },
    {
        "name": "South Africa",
        "formation": "4-2-3-1",
        "lineup": ["Percy Tau", "Themba Zwane", "Teboho Mokoena", "Sphephelo Sithole", "Evidence Makgopa", "Thapelo Morena", "Mothobi Mvala", "Grant Kekana", "Khuliso Mudau", "Aubrey Modiba", "Ronwen Williams"],
        "star": "Percy Tau",
        "tactical_style": "focuses on possession-based buildup in the midfield and quick short passes coordinated by Themba Zwane",
        "defensive_style": "deploys a deep defensive block led by Mothobi Mvala, relying heavily on the shot-stopping ability of Ronwen Williams"
    },
    {
        "name": "South Korea",
        "formation": "4-2-3-1",
        "lineup": ["Son Heung-min", "Hwang Hee-chan", "Lee Kang-in", "Hwang In-beom", "Lee Jae-sung", "Park Yong-woo", "Kim Min-jae", "Kim Young-gwon", "Seol Young-woo", "Kim Jin-su", "Jo Hyeon-woo"],
        "star": "Son Heung-min",
        "tactical_style": "relies on lethal counter-attacks spearheaded by Son Heung-min and technical playmaking from Lee Kang-in",
        "defensive_style": "anchors their backline with the world-class physicality and recovery pace of defender Kim Min-jae"
    },
    {
        "name": "Czechia",
        "formation": "3-4-2-1",
        "lineup": ["Patrik Schick", "Tomas Soucek", "Ladislav Krejci", "Vladimir Coufal", "Robin Hranac", "Tomas Holes", "David Jurasek", "Lukas Provod", "Vaclav Cerny", "Jan Kuchta", "Jindrich Stanek"],
        "star": "Patrik Schick",
        "tactical_style": "utilizes physical dominance in midfield through Tomas Soucek and direct long balls aiming for Patrik Schick",
        "defensive_style": "sets up a rigid three-back system under Ladislav Krejci, emphasizing physical aerial clearances"
    },
    {
        "name": "Canada",
        "formation": "4-4-2",
        "lineup": ["Jonathan David", "Alphonso Davies", "Cyle Larin", "Stephen Eustaquio", "Ismael Kone", "Tajon Buchanan", "Alistair Johnston", "Moise Bombito", "Derek Cornelius", "Richie Laryea", "Maxime Crepeau"],
        "star": "Alphonso Davies",
        "tactical_style": "exploits the explosive speed of Alphonso Davies on the overlap and direct combinations between Larin and David",
        "defensive_style": "defends with an energetic, high-pressing block that drops into a narrow mid-block marshaled by Moise Bombito"
    },
    {
        "name": "Bosnia & Herzegovina",
        "formation": "4-3-3",
        "lineup": ["Edin Dzeko", "Ermedin Demirovic", "Rade Krunic", "Benjamin Tahirovic", "Haris Hajradinovic", "Amar Dedic", "Dennis Hadzikadunic", "Anel Ahmedhodzic", "Jusuf Gazibegovic", "Sead Kolasinac", "Nikola Vasilj"],
        "star": "Edin Dzeko",
        "tactical_style": "looks to control the tempo through Rade Krunic and feeds the legendary hold-up play of Edin Dzeko in the box",
        "defensive_style": "relies on a physical low-block led by Anel Ahmedhodzic, prioritizing protection of the penalty area"
    },
    {
        "name": "Qatar",
        "formation": "3-5-2",
        "lineup": ["Akram Afif", "Almoez Ali", "Hassan Al-Haydos", "Ahmed Fatehi", "Jassem Gaber", "Mohammed Waad", "Lucas Mendes", "Boualem Khoukhi", "Ro-Ro", "Homam Ahmed", "Meshaal Barsham"],
        "star": "Akram Afif",
        "tactical_style": "deploys a fast wingback system, creating goalscoring opportunities via the creative brilliance of Akram Afif",
        "defensive_style": "congests the central areas with a five-man midfield and three central defenders anchored by Lucas Mendes"
    },
    {
        "name": "Switzerland",
        "formation": "3-4-2-1",
        "lineup": ["Breel Embolo", "Xerdan Shaqiri", "Granit Xhaka", "Remo Freuler", "Michel Aebischer", "Ruben Vargas", "Manuel Akanji", "Fabian Schar", "Ricardo Rodriguez", "Silvan Widmer", "Yann Sommer"],
        "star": "Granit Xhaka",
        "tactical_style": "implements a highly structured possession game controlled masterfully by veteran midfielder Granit Xhaka",
        "defensive_style": "features an organized, compact backline marshaled by Manuel Akanji, restricting space between lines"
    },
    {
        "name": "Brazil",
        "formation": "4-2-3-1",
        "lineup": ["Vinicius Jr", "Rodrygo", "Endrick", "Bruno Guimaraes", "Lucas Paqueta", "Douglas Luiz", "Marquinhos", "Eder Militao", "Danilo", "Gabriel Magalhaes", "Alisson Becker"],
        "star": "Vinicius Jr",
        "tactical_style": "combines samba flair, explosive wing play from Vinicius Jr, and rapid central combinations through Rodrygo",
        "defensive_style": "maintains a solid, aggressive defense anchored by Eder Militao and Marquinhos with a high-press system"
    },
    {
        "name": "Morocco",
        "formation": "4-3-3",
        "lineup": ["Youssef En-Nesyri", "Hakim Ziyech", "Brahim Diaz", "Sofyan Amrabat", "Azzedine Ounahi", "Achraf Hakimi", "Nayef Aguerd", "Romain Saiss", "Yahia Attiyat Allah", "Selim Amallah", "Yassine Bounou"],
        "star": "Achraf Hakimi",
        "tactical_style": "controls the flanks through the overlapping runs of Achraf Hakimi and creative output of Brahim Diaz",
        "defensive_style": "stands strong with a world-renowned compact defensive mid-block anchored by Sofyan Amrabat and Romain Saiss"
    },
    {
        "name": "Haiti",
        "formation": "4-2-3-1",
        "lineup": ["Frantzdy Pierrot", "Duckens Nazon", "Derrick Etienne Jr", "Carlens Arcus", "Danley Jean Jacques", "Bryan Alceus", "Wilde-Donald Guerrier", "Garven Metusala", "Ricardo Ade", "Alex Christian", "Johny Placide"],
        "star": "Frantzdy Pierrot",
        "tactical_style": "relies on physical attacking threats from Frantzdy Pierrot and quick transitions on the counter",
        "defensive_style": "deploys a deep-lying defensive line led by Ricardo Ade, focusing on narrow spacing to prevent central runs"
    },
    {
        "name": "Scotland",
        "formation": "3-4-2-1",
        "lineup": ["Che Adams", "John McGinn", "Scott McTominay", "Callum McGregor", "Billy Gilmour", "Andrew Robertson", "Kieran Tierney", "Jack Hendry", "Ryan Porteous", "Anthony Ralston", "Angus Gunn"],
        "star": "Scott McTominay",
        "tactical_style": "attacks with energetic late runs into the box by Scott McTominay and wingback crosses from Andrew Robertson",
        "defensive_style": "maintains a resolute five-man defensive block out of possession, led by Kieran Tierney"
    },
    {
        "name": "United States",
        "formation": "4-3-3",
        "lineup": ["Christian Pulisic", "Folarin Balogun", "Timothy Weah", "Weston McKennie", "Tyler Adams", "Yunus Musah", "Antonee Robinson", "Chris Richards", "Tim Ream", "Joe Scally", "Matt Turner"],
        "star": "Christian Pulisic",
        "tactical_style": "leverages the creativity and driving dribbles of Christian Pulisic and dynamic overlaps by Antonee Robinson",
        "defensive_style": "implements a high-press system triggers by Tyler Adams, closing down opponents rapidly in the middle third"
    },
    {
        "name": "Paraguay",
        "formation": "4-2-3-1",
        "lineup": ["Julio Enciso", "Miguel Almiron", "Alex Arce", "Mathias Villasanti", "Andres Cubas", "Damian Bobadilla", "Gustavo Gomez", "Fabian Balbuena", "Omar Alderete", "Matias Espinoza", "Carlos Coronel"],
        "star": "Miguel Almiron",
        "tactical_style": "relies on the direct running speed of Miguel Almiron and playmaker vision from Julio Enciso",
        "defensive_style": "utilizes a hard-tackling, aggressive defensive structure led by veteran Gustavo Gomez"
    },
    {
        "name": "Australia",
        "formation": "4-2-3-1",
        "lineup": ["Mitchell Duke", "Craig Goodwin", "Jackson Irvine", "Connor Metcalfe", "Keanu Baccus", "Martin Boyle", "Harry Souttar", "Kye Rowles", "Aziz Behich", "Gethin Jones", "Mathew Ryan"],
        "star": "Jackson Irvine",
        "tactical_style": "focuses on physical aerial duels, crossing from Craig Goodwin, and second-ball dominance by Jackson Irvine",
        "defensive_style": "anchors the box with the imposing physical height of Harry Souttar, excelling in clearing set-pieces"
    },
    {
        "name": "Türkiye",
        "formation": "4-2-3-1",
        "lineup": ["Baris Alper Yilmaz", "Arda Guler", "Hakan Calhanoglu", "Kenan Yildiz", "Kaan Ayhan", "Salih Ozcan", "Ferdi Kadioglu", "Abdulkerim Bardakci", "Samet Akaydin", "Mert Muldur", "Mert Gunok"],
        "star": "Hakan Calhanoglu",
        "tactical_style": "commands the midfield through the passing range of Hakan Calhanoglu and flair of youngster Arda Guler",
        "defensive_style": "employs a tactical mid-block with high fullback involvements, marshaled by Abdulkerim Bardakci"
    },
    {
        "name": "Germany",
        "formation": "4-2-3-1",
        "lineup": ["Niclas Fullkrug", "Jamal Musiala", "Florian Wirtz", "Kai Havertz", "Ilkay Gundogan", "Robert Andrich", "Joshua Kimmich", "Antonio Rudiger", "Jonathan Tah", "David Raum", "Manuel Neuer"],
        "star": "Jamal Musiala",
        "tactical_style": "creates intricate attacking patterns via Jamal Musiala and Florian Wirtz, dominating possession",
        "defensive_style": "presses high with aggressive ball-winning from Antonio Rudiger and structural protection from Robert Andrich"
    },
    {
        "name": "Curaçao",
        "formation": "4-3-3",
        "lineup": ["Juninho Bacuna", "Brandley Kuwas", "Kenji Gorre", "Leandro Bacuna", "Vurnon Anita", "Roly Bonevacia", "Cuco Martina", "Jurien Gaari", "Sherel Floranus", "Nathangelo Markelo", "Eloy Room"],
        "star": "Juninho Bacuna",
        "tactical_style": "attacks directly through Juninho Bacuna in a fluid system utilizing quick switches of play",
        "defensive_style": "focuses on a narrow defensive line marshaled by Cuco Martina to protect the central channels"
    },
    {
        "name": "Ivory Coast",
        "formation": "4-3-3",
        "lineup": ["Sebastian Haller", "Simon Adingra", "Franck Kessie", "Seko Fofana", "Ibrahim Sangare", "Max Gradel", "Evan Ndicka", "Ousmane Diomande", "Wilfried Singo", "Ghislain Konan", "Yahia Fofana"],
        "star": "Franck Kessie",
        "tactical_style": "dominates the middle of the pitch through Franck Kessie and Seko Fofana, feeding Sebastian Haller",
        "defensive_style": "uses a highly athletic backline led by Evan Ndicka, excels in physical recovery duels"
    },
    {
        "name": "Ecuador",
        "formation": "4-2-3-1",
        "lineup": ["Enner Valencia", "Kendry Paez", "Moises Caicedo", "Alan Franco", "Carlos Gruezo", "Jeremy Sarmiento", "Piero Hincapie", "Willian Pacho", "Felix Torres", "Angelo Preciado", "Alexander Dominguez"],
        "star": "Moises Caicedo",
        "tactical_style": "rebuilds through the tireless energy of Moises Caicedo and direct creative bursts of prodigy Kendry Paez",
        "defensive_style": "establishes a strong defensive wall led by Piero Hincapie and Willian Pacho, hard to break down"
    },
    {
        "name": "Netherlands",
        "formation": "4-3-3",
        "lineup": ["Memphis Depay", "Cody Gakpo", "Xavi Simons", "Jerdy Schouten", "Tijjani Reijnders", "Joey Veerman", "Denzel Dumfries", "Virgil van Dijk", "Stefan de Vrij", "Nathan Ake", "Bart Verbruggen"],
        "star": "Virgil van Dijk",
        "tactical_style": "initiates play from the back using Virgil van Dijk's long balls and width from fullback Denzel Dumfries",
        "defensive_style": "maintains a solid zonal defense under Virgil van Dijk's leadership, restricting entry into the box"
    },
    {
        "name": "Japan",
        "formation": "4-2-3-1",
        "lineup": ["Ayase Ueda", "Takumi Minamino", "Takefusa Kubo", "Wataru Endo", "Hidemasa Morita", "Ritsu Doan", "Hiroki Ito", "Ko Itakura", "Shogo Taniguchi", "Yukinari Sugawara", "Zion Suzuki"],
        "star": "Takefusa Kubo",
        "tactical_style": "displays rapid technical passing and high counter-pressing controlled by midfielder Wataru Endo",
        "defensive_style": "operates a highly coordinated zonal pressing block, anchored by the intelligence of Ko Itakura"
    },
    {
        "name": "Sweden",
        "formation": "4-4-2",
        "lineup": ["Viktor Gyokeres", "Alexander Isak", "Dejan Kulusevski", "Emil Forsberg", "Jens Cajuste", "Hugo Larsson", "Ludwig Augustinsson", "Victor Lindelof", "Isak Hien", "Emil Krafth", "Robin Olsen"],
        "star": "Viktor Gyokeres",
        "tactical_style": "unleashes a potent attacking duo of Viktor Gyokeres and Alexander Isak, supported by Dejan Kulusevski",
        "defensive_style": "retains a classic, compact 4-4-2 structure anchored by captain Victor Lindelof"
    },
    {
        "name": "Tunisia",
        "formation": "4-3-3",
        "lineup": ["Elias Achouri", "Saifeddine Jaziri", "Naïm Sliti", "Ellyes Skhiri", "Aissa Laidouni", "Mohamed Ali Ben Romdhane", "Ali Maaloul", "Yassine Meriah", "Montassar Talbi", "Wajdi Kechrida", "Bechir Ben Said"],
        "star": "Ellyes Skhiri",
        "tactical_style": "focuses on tactical organization, solid midfield screens by Ellyes Skhiri, and counter-attacks",
        "defensive_style": "presents a stubborn, low-block defense anchored by Montassar Talbi, prioritizing clean sheets"
    },
    {
        "name": "Belgium",
        "formation": "4-3-3",
        "lineup": ["Romelu Lukaku", "Kevin De Bruyne", "Jeremy Doku", "Leandro Trossard", "Amadou Onana", "Orel Mangala", "Timothy Castagne", "Wout Faes", "Zeno Debast", "Arthur Theate", "Koen Casteels"],
        "star": "Kevin De Bruyne",
        "tactical_style": "relies on the generational playmaking vision of Kevin De Bruyne and elite speed of Jeremy Doku on the wing",
        "defensive_style": "defends with a high line but drops into a cautious mid-block, organized by Wout Faes"
    },
    {
        "name": "Egypt",
        "formation": "4-3-3",
        "lineup": ["Mohamed Salah", "Mostafa Mohamed", "Trezeguet", "Marwan Attia", "Hamdi Fathi", "Emam Ashour", "Mohamed Abdelmonem", "Ahmed Hegazi", "Mohamed Hany", "Mohamed Hamdy", "Mohamed El Shenawy"],
        "star": "Mohamed Salah",
        "tactical_style": "funnels their entire attacking strategy through the world-class cutting-in runs of Mohamed Salah",
        "defensive_style": "deploys a deep defensive line led by Ahmed Hegazi, focusing on low risk and tight spacing"
    },
    {
        "name": "Iran",
        "formation": "4-4-2",
        "lineup": ["Mehdi Taremi", "Sardar Azmoun", "Alireza Jahanbakhsh", "Saman Ghoddos", "Saeid Ezatolahi", "Mehdi Torabi", "Milad Mohammadi", "Shojae Khalilzadeh", "Hossein Kanaanizadegan", "Ramin Rezaeian", "Alireza Beiranvand"],
        "star": "Mehdi Taremi",
        "tactical_style": "relies on the dangerous partnership of Mehdi Taremi and Sardar Azmoun, playing direct counter-attacking football",
        "defensive_style": "organizes a highly disciplined, narrow defensive shape led by Shojae Khalilzadeh"
    },
    {
        "name": "New Zealand",
        "formation": "4-2-3-1",
        "lineup": ["Chris Wood", "Sarpreet Singh", "Matthew Garbett", "Marko Stamenic", "Joe Bell", "Callum McCowatt", "Liberato Cacace", "Tyler Bindon", "Michael Boxall", "Tommy Smith", "Max Crocombe"],
        "star": "Chris Wood",
        "tactical_style": "plays a direct style, using long balls and crossing targets directed at target-man striker Chris Wood",
        "defensive_style": "deploys a physical, robust defensive block marshaled by veteran Tommy Smith"
    },
    {
        "name": "Spain",
        "formation": "4-3-3",
        "lineup": ["Alvaro Morata", "Lamine Yamal", "Nico Williams", "Rodri", "Pedri", "Fabian Ruiz", "Dani Carvajal", "Robin Le Normand", "Aymeric Laporte", "Marc Cucurella", "Unai Simon"],
        "star": "Rodri",
        "tactical_style": "controls games with elite positional play and passing from Rodri, combined with Lamine Yamal's flair",
        "defensive_style": "presses aggressively high up the pitch, relying on Aymeric Laporte for tactical coverage"
    },
    {
        "name": "Cape Verde",
        "formation": "4-3-3",
        "lineup": ["Ryan Mendes", "Garry Rodrigues", "Jovane Cabral", "Jamiro Monteiro", "Kevin Pina", "Kenny Rocha Santos", "Logan Costa", "Pico", "Steven Moreira", "Joao Paulo", "Vozinha"],
        "star": "Ryan Mendes",
        "tactical_style": "attacks using the speed of Garry Rodrigues and creative runs from Ryan Mendes on the counter",
        "defensive_style": "organizes a compact mid-block focused on closing down spaces in the half-spaces, led by Logan Costa"
    },
    {
        "name": "Saudi Arabia",
        "formation": "3-5-2",
        "lineup": ["Salem Al-Dawsari", "Firas Al-Buraikan", "Saleh Al-Shehri", "Mohamed Kanno", "Abdullah Otayf", "Abdulelah Al-Malki", "Yasser Al-Shahrani", "Ali Al-Bulaihi", "Abdulelah Al-Amri", "Saud Abdulhamid", "Mohammed Al-Owais"],
        "star": "Salem Al-Dawsari",
        "tactical_style": "focuses on overloading the midfield and creating opportunities through the creative Salem Al-Dawsari",
        "defensive_style": "utilizes an aggressive offside trap and high-energy defensive line led by Ali Al-Bulaihi"
    },
    {
        "name": "Uruguay",
        "formation": "4-3-3",
        "lineup": ["Darwin Nunez", "Luis Suarez", "Federico Valverde", "Rodrigo Bentancur", "Nicolas de la Cruz", "Manuel Ugarte", "Ronald Araujo", "Jose Maria Gimenez", "Matias Vina", "Nahitan Nandez", "Sergio Rochet"],
        "star": "Federico Valverde",
        "tactical_style": "plays with high intensity, relentless running from Federico Valverde, and explosive attacks by Darwin Nunez",
        "defensive_style": "presents a fierce, aggressive defensive block anchored by Ronald Araujo's physical superiority"
    },
    {
        "name": "France",
        "formation": "4-3-3",
        "lineup": ["Kylian Mbappe", "Antoine Griezmann", "Ousmane Dembele", "Aurelien Tchouameni", "Eduardo Camavinga", "Adrien Rabiot", "Theo Hernandez", "Ibrahima Konate", "Dayot Upamecano", "Jules Kounde", "Mike Maignan"],
        "star": "Kylian Mbappe",
        "tactical_style": "features lightning-fast counter-attacks led by Kylian Mbappe and brilliant tactical link-play from Antoine Griezmann",
        "defensive_style": "defends compactly and relies on the speed of Dayot Upamecano to shut down transition play"
    },
    {
        "name": "Senegal",
        "formation": "4-3-3",
        "lineup": ["Sadio Mane", "Nicolas Jackson", "Ismaila Sarr", "Lamine Camara", "Pape Matar Sarr", "Idrissa Gueye", "Kalidou Koulibaly", "Abdou Diallo", "Youssouf Sabaly", "Ismail Jakobs", "Edouard Mendy"],
        "star": "Sadio Mane",
        "tactical_style": "blends physical power in midfield through Pape Matar Sarr and explosive runs by Sadio Mane and Sarr",
        "defensive_style": "anchors their backline with the leadership and strength of veteran defender Kalidou Koulibaly"
    },
    {
        "name": "Iraq",
        "formation": "4-2-3-1",
        "lineup": ["Aymen Hussein", "Mohanad Ali", "Ali Jasim", "Amir Al-Ammari", "Osama Rashid", "Ibrahim Bayesh", "Rebin Sulaka", "Saad Natiq", "Merchas Doski", "Hussein Ali", "Jalal Hassan"],
        "star": "Aymen Hussein",
        "tactical_style": "combines organized midfield passing and high crosses directed toward their key striker Aymen Hussein",
        "defensive_style": "establishes a compact structure led by Rebin Sulaka, prioritizing central defensive stability"
    },
    {
        "name": "Norway",
        "formation": "4-3-3",
        "lineup": ["Erling Haaland", "Martin Odegaard", "Alexander Sorloth", "Antonio Nusa", "Sander Berge", "Patrick Berg", "Julian Ryerson", "Leo Ostigard", "Kristoffer Ajer", "Birger Meling", "Orjan Nyland"],
        "star": "Erling Haaland",
        "tactical_style": "utilizes the elite playmaking of Martin Odegaard to feed the clinical, record-breaking runs of Erling Haaland",
        "defensive_style": "relies on a physical, aerially dominant defense led by Leo Ostigard and Kristoffer Ajer"
    },
    {
        "name": "Argentina",
        "formation": "4-3-3",
        "lineup": ["Lionel Messi", "Lautaro Martinez", "Julian Alvarez", "Alexis Mac Allister", "Enzo Fernandez", "Rodrigo De Paul", "Cristian Romero", "Lisandro Martinez", "Nahuel Molina", "Nicolas Tagliafico", "Emiliano Martinez"],
        "star": "Lionel Messi",
        "tactical_style": "flows through the genius playmaker movement of Lionel Messi, with energetic central supports from De Paul and Alvarez",
        "defensive_style": "relies on the aggressive, high-anticipation defending of Cristian Romero and Lisandro Martinez"
    },
    {
        "name": "Algeria",
        "formation": "4-3-3",
        "lineup": ["Baghdad Bounedjah", "Riyad Mahrez", "Said Benrahma", "Ismael Bennacer", "Nabil Bentaleb", "Houssem Aouar", "Ramy Bensebaini", "Aissa Mandi", "Youcef Atal", "Rayan Ait-Nouri", "Anthony Mandrea"],
        "star": "Riyad Mahrez",
        "tactical_style": "relies on technical wing play from Riyad Mahrez and midfield dictation from playmaker Ismael Bennacer",
        "defensive_style": "features a standard back-four system anchored by Ramy Bensebaini, protecting the inner channels"
    },
    {
        "name": "Austria",
        "formation": "4-2-3-1",
        "lineup": ["Michael Gregoritsch", "Marcel Sabitzer", "Konrad Laimer", "Christoph Baumgartner", "Nicolas Seiwald", "Florian Grillitsch", "Stefan Posch", "Kevin Danso", "Maximilian Wober", "Phillipp Mwene", "Patrick Pentz"],
        "star": "Marcel Sabitzer",
        "tactical_style": "employs a highly intense, coordinated counter-press system led by Konrad Laimer and Marcel Sabitzer",
        "defensive_style": "defends aggressively in a high-intensity mid-block led by the physical Kevin Danso"
    },
    {
        "name": "Jordan",
        "formation": "3-4-2-1",
        "lineup": ["Musa Al-Taamari", "Yazan Al-Naimat", "Ali Olwan", "Nizar Al-Rashdan", "Noor Al-Rawabdeh", "Mahmoud Al-Mardi", "Yazan Al-Arab", "Salem Al-Ajalin", "Abdallah Nasib", "Ihsan Haddad", "Yazid Abu Layla"],
        "star": "Musa Al-Taamari",
        "tactical_style": "exploits transition opportunities with the electric pace and trickery of winger Musa Al-Taamari",
        "defensive_style": "retreats into a solid five-back low block led by Yazan Al-Arab, focusing on defensive numbers"
    },
    {
        "name": "Portugal",
        "formation": "4-3-3",
        "lineup": ["Cristiano Ronaldo", "Rafael Leao", "Bruno Fernandes", "Bernardo Silva", "Joao Palhinha", "Vitinha", "Diogo Dalot", "Ruben Dias", "Pepe", "Joao Cancelo", "Diogo Costa"],
        "star": "Cristiano Ronaldo",
        "tactical_style": "controls play with Bernardo Silva and Bruno Fernandes, delivering service to legendary striker Cristiano Ronaldo",
        "defensive_style": "builds around the elite positioning and tackle timing of key defender Ruben Dias"
    },
    {
        "name": "DR Congo",
        "formation": "4-2-3-1",
        "lineup": ["Yoane Wissa", "Cedric Bakambu", "Theo Bongonda", "Samuel Moutoussamy", "Charles Pickel", "Gael Kakuta", "Chancel Mbemba", "Henoc Inonga", "Gedeon Kalulu", "Arthur Masuaku", "Lionel Mpasi"],
        "star": "Yoane Wissa",
        "tactical_style": "focuses on direct attacking transitions, using the physical power of Cedric Bakambu and pace of Yoane Wissa",
        "defensive_style": "sets up a physical, robust defensive line anchored by captain Chancel Mbemba"
    },
    {
        "name": "Uzbekistan",
        "formation": "3-4-2-1",
        "lineup": ["Eldor Shomurodov", "Abbosbek Fayzullaev", "Oston Urunov", "Otabek Shukurov", "Odiljon Hamrobekov", "Jaloliddin Masharipov", "Husniddin Aliqulov", "Abdukodir Khusanov", "Rustam Ashurmatov", "Farrukh Sayfiev", "Utkir Yusupov"],
        "star": "Eldor Shomurodov",
        "tactical_style": "attacks with highly technical play from Fayzullaev, looking to find Eldor Shomurodov in the penalty area",
        "defensive_style": "deploys a deep five-man defense anchored by the rising star defender Abdukodir Khusanov"
    },
    {
        "name": "Colombia",
        "formation": "4-2-3-1",
        "lineup": ["Luis Diaz", "James Rodriguez", "Jhon Duran", "Jefferson Lerma", "Richard Rios", "Jhon Arias", "Davinson Sanchez", "Carlos Cuesta", "Daniel Munoz", "Johan Mojica", "Camilo Vargas"],
        "star": "Luis Diaz",
        "tactical_style": "attacks down the left wing through the explosive dribbling of Luis Diaz and playmaker crossing from James Rodriguez",
        "defensive_style": "deploys a high-tempo, aggressive defensive line anchored by Davinson Sanchez and Carlos Cuesta"
    },
    {
        "name": "England",
        "formation": "4-2-3-1",
        "lineup": ["Harry Kane", "Jude Bellingham", "Bukayo Saka", "Phil Foden", "Declan Rice", "Kobbie Mainoo", "Kyle Walker", "John Stones", "Marc Guehi", "Kieran Trippier", "Jordan Pickford"],
        "star": "Harry Kane",
        "tactical_style": "relies on Harry Kane dropping deep to link up with Jude Bellingham and speed on the wings from Bukayo Saka",
        "defensive_style": "maintains structural control in defensive transitions under the command of John Stones"
    },
    {
        "name": "Croatia",
        "formation": "4-3-3",
        "lineup": ["Andrej Kramaric", "Luka Modric", "Mateo Kovacic", "Marcelo Brozovic", "Mario Pasalic", "Ivan Perisic", "Josko Gvardiol", "Josip Sutalo", "Domagoj Vida", "Josip Stanisic", "Dominik Livakovic"],
        "star": "Luka Modric",
        "tactical_style": "dominates the pace of play through the legendary midfield trio of Luka Modric, Kovacic, and Brozovic",
        "defensive_style": "anchors their defensive line with the world-class physicality and versatility of Josko Gvardiol"
    },
    {
        "name": "Ghana",
        "formation": "4-2-3-1",
        "lineup": ["Inaki Williams", "Mohammed Kudus", "Jordan Ayew", "Thomas Partey", "Salis Abdul Samed", "Majeed Ashimeru", "Tariq Lamptey", "Mohammed Salisu", "Alexander Djiku", "Gideon Mensah", "Lawrence Ati-Zigi"],
        "star": "Mohammed Kudus",
        "tactical_style": "features rapid transitions through the technical intelligence of Mohammed Kudus and pace of Inaki Williams",
        "defensive_style": "establishes a compact block anchored by Thomas Partey in the screen, protecting the center backs"
    },
    {
        "name": "Panama",
        "formation": "3-4-2-1",
        "lineup": ["Cecilio Waterman", "Ismael Diaz", "Jose Luis Rodriguez", "Adalberto Carrasquilla", "Anibal Godoy", "Cristian Martinez", "Michael Amir Murillo", "Jose Cordoba", "Fidel Escobar", "Eric Davis", "Orlando Mosquera"],
        "star": "Adalberto Carrasquilla",
        "tactical_style": "attacks with structural width, driven by the playmaking vision of midfielder Adalberto Carrasquilla",
        "defensive_style": "presents a disciplined, physical three-back defense anchored by Jose Cordoba"
    }
]

# Unique set of teams based on name to avoid duplicate definition problems
UNIQUE_TEAMS = []
seen = set()
for t in TEAMS:
    if t["name"] not in seen:
        UNIQUE_TEAMS.append(t)
        seen.add(t["name"])

# 2026 World Cup official stadiums
STADIUMS = [
    "MetLife Stadium (New York/New Jersey)",
    "SoFi Stadium (Los Angeles)",
    "AT&T Stadium (Dallas)",
    "Arrowhead Stadium (Kansas City)",
    "Mercedes-Benz Stadium (Atlanta)",
    "Lincoln Financial Field (Philadelphia)",
    "Lumen Field (Seattle)",
    "Levi's Stadium (San Francisco)",
    "Gillette Stadium (Boston)",
    "NRG Stadium (Houston)",
    "Hard Rock Stadium (Miami)",
    "BC Place (Vancouver)",
    "BMO Field (Toronto)",
    "Estadio Azteca (Mexico City)",
    "Estadio BBVA (Monterrey)",
    "Estadio Akron (Guadalajara)"
]

# Match stages distribution
STAGES = ["Group Stage", "Round of 32", "Round of 16", "Quarter-Final", "Semi-Final", "Final"]

def generate_xml_posts():
    xml_file_path = "e:\\Live Tv App - Copy\\world_cup_blogger_import.xml"
    
    # 48 unique teams generate combinations of 2. Number of unique matchups = 48 * 47 / 2 = 1,128 combinations
    matchups = list(itertools.combinations(UNIQUE_TEAMS, 2))
    total_matches = len(matchups)
    
    print(f"Total Unique Matchups to generate: {total_matches}")
    
    # Tournament dates: June 11, 2026 to July 19, 2026
    start_date = datetime(2026, 6, 11, 2, 0) # 02:00 AM BDT base
    
    # XML Header
    xml_header = """<?xml version='1.0' encoding='UTF-8'?>
<feed xmlns='http://www.w3.org/2005/Atom' xmlns:openSearch='http://a9.com/-/spec/opensearchrss/1.0/' xmlns:georss='http://www.georss.org/georss' xmlns:gd='http://schemas.google.com/g/2005' xmlns:thr='http://purl.org/syndication/thread/1.0'>
  <id>tag:blogger.com,1999:blog-worldcup2026.feed</id>
  <title type='text'>FIFA World Cup 2026 Live Stream Directory</title>
  <subtitle type='text'>Watch FIFA World Cup 2026 Live Matches Free HD Online</subtitle>
  <updated>2026-06-18T14:30:00Z</updated>
"""
    
    with open(xml_file_path, "w", encoding="utf-8") as f:
        f.write(xml_header)
        
        for idx, (team1, team2) in enumerate(matchups):
            # Deterministic/random assignment of stage, date, venue to make it look realistic
            # We will distribute the match dates starting from June 11 up to July 19
            # Spread matches evenly across the 39-day tournament window
            day_offset = (idx * 38) // total_matches
            hour_offset = (idx * 22) % 24
            match_datetime = start_date + timedelta(days=day_offset, hours=hour_offset)
            
            # Determine stage based on day offset
            if day_offset <= 16:
                stage = "Group Stage"
            elif day_offset <= 22:
                stage = "Round of 32"
            elif day_offset <= 28:
                stage = "Round of 16"
            elif day_offset <= 33:
                stage = "Quarter-Final"
            elif day_offset <= 36:
                stage = "Semi-Final"
            else:
                stage = "Final"
                
            venue = STADIUMS[idx % len(STADIUMS)]
            date_str = match_datetime.strftime("%B %d, %I:%M %p BDT")
            iso_date = match_datetime.isoformat() + "+06:00" # Bangladesh time timezone offset
            
            title = f"{team1['name']} vs {team2['name']} Live Stream: Watch FIFA World Cup {stage} Free HD"
            
            # Shortened title for blogger category/search matches
            t1_name = team1['name']
            t2_name = team2['name']
            
            meta_description = f"Watch {t1_name} vs {t2_name} live online free on mobile, PC, and TV. Stream FIFA World Cup {stage} match today in HD. Kickoff {date_str}."
            
            # HTML content body
            html_content = f"""<p>Welcome to the ultimate digital broadcasting portal to watch <strong>{t1_name} vs {t2_name} live online</strong>. Football enthusiasts worldwide are converging to witness this historic FIFA World Cup {stage} face-off. If you are tracking a high-speed <strong>live football streaming link</strong> or searching for how to stream the <strong>{t1_name} match today free</strong> on mobile, iOS, or PC, your search ends here.</p>

<table border="1" style="width:100%; border-collapse: collapse; margin: 20px 0; text-align: left; font-family: Arial, sans-serif;">
  <tr style="background: #222; color: #fff;"><th style="padding: 12px;" colspan="2">MATCH DAY OFFICIAL DIRECTORY</th></tr>
  <tr><th style="padding: 10px; background: #f9f9f9; width: 30%;">Tournament Stage</th><td style="padding: 10px;">{stage}</td></tr>
  <tr><th style="padding: 10px; background: #f9f9f9;">Fixture</th><td style="padding: 10px; font-weight: bold;">{t1_name} vs {t2_name}</td></tr>
  <tr><th style="padding: 10px; background: #f9f9f9;">Kick-Off Time</th><td style="padding: 10px; color: red; font-weight: bold;">{date_str} (Bangladesh Time)</td></tr>
  <tr><th style="padding: 10px; background: #f9f9f9;">Venue Arena</th><td style="padding: 10px;">{venue}</td></tr>
</table>

<h2>Where to Watch {t1_name} vs {t2_name} Live Broadcast Globally</h2>
<p>This high-stakes {stage} encounter is being streamed via premium geo-restricted networks. To ensure zero buffering and uninterrupted 4K/HD streaming, our server provides direct server-to-player access. Click the verified streaming gateway button below to activate the live feed instantly.</p>

<div style="text-align:center; margin:35px 0;">
  <a href="YOUR_STREAM_LINK_HERE" style="background: #e50914; color: #fff; padding: 18px 36px; font-weight: bold; text-decoration: none; border-radius: 4px; font-size: 22px; display: inline-block; box-shadow: 0px 5px 20px rgba(229,9,20,0.5); text-transform: uppercase; letter-spacing: 1px;">▶ CLICK HERE TO WATCH LIVE STREAM HD</a>
</div>

<h2>Tactical Intelligence & Match Preview</h2>
<p>The tactical battle between {t1_name} and {t2_name} is set to be one of the highlights of this {stage}. In their current form, {t1_name} {team1['tactical_style']}. This offensive strategy will be tested by {t2_name}'s defensive system, which {team2['defensive_style']}. Midfield battles will likely dictate the flow, as {t1_name} looks to dominate transition plays via their key playmaker {team1['star']}, while {t2_name} seeks control using the influence of {team2['star']}. Defensively, {t1_name} must stay alert, as their strategy of {team1['defensive_style']} will face direct challenges from {t2_name}'s attack, which {team2['tactical_style']}. Expect a highly competitive, tactical matchup from kick-off to the final whistle.</p>

<h2>Predicted Starting XI Lineups</h2>
<h3>{t1_name} Expected Formation & XI ({team1['formation']})</h3>
<p>{", ".join(team1['lineup'])}</p>

<h3>{t2_name} Expected Formation & XI ({team2['formation']})</h3>
<p>{", ".join(team2['lineup'])}</p>

<h2>Google SERP People Also Ask (PAA) Search Solutions</h2>
<h3>What time does the {t1_name} vs {t2_name} match start in Bangladesh?</h3>
<p>The highly anticipated World Cup match triggers its official kick-off on {date_str} live from {venue}.</p>

<h3>How can I access {t1_name} vs {t2_name} live stream link free?</h3>
<p>You can seamlessly bypass subscription paywalls by utilizing our secure, embedded HD player via the red streaming button above.</p>

<h3>Which international channels are broadcasting the {t1_name} game?</h3>
<p>While global networks like Fox Sports, Telemundo, and BBC Sport hold broadcasting rights, our platform aggregates these feeds into a single free, responsive mobile stream link.</p>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BroadcastEvent",
  "name": "{t1_name} vs {t2_name} Live Streaming - FIFA World Cup 2026",
  "description": "Premium real-time HD coverage of the FIFA World Cup {stage} match between {t1_name} and {t2_name}.",
  "isLiveBroadcast": true,
  "videoFormat": "HD",
  "startDate": "{iso_date}",
  "competitor": [
    {{
      "@type": "SportsTeam",
      "name": "{t1_name}"
    }},
    {{
      "@type": "SportsTeam",
      "name": "{t2_name}"
    }}
  ]
}}
</script>"""
            
            # Escape HTML to make it valid inside Atom feed <content type="html">
            escaped_html = html.escape(html_content)
            
            # Entry structure
            entry = f"""  <entry>
    <category scheme='http://schemas.google.com/g/2005#kind' term='http://schemas.google.com/blogger/2008/kind#post' />
    <category scheme='http://www.blogger.com/atom/ns#' term='FIFA World Cup 2026' />
    <category scheme='http://www.blogger.com/atom/ns#' term='Live Stream' />
    <category scheme='http://www.blogger.com/atom/ns#' term='{t1_name}' />
    <category scheme='http://www.blogger.com/atom/ns#' term='{t2_name}' />
    <title type='html'>{html.escape(title)}</title>
    <content type='html'>{escaped_html}</content>
    <published>{iso_date}</published>
  </entry>
"""
            f.write(entry)
            
            # Log progress in small increments to prevent spamming
            if (idx + 1) % 200 == 0:
                print(f"Generated {idx + 1} posts...")
                
        f.write("</feed>\n")
        
    print(f"Successfully generated Blogger import XML file at: {xml_file_path}")

if __name__ == "__main__":
    generate_xml_posts()
