from calendar import c
from operator import methodcaller
from unittest import result
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from itsdangerous import json
app = Flask(__name__)

current_id = 11

books = {
    "1": {
        "id": "1",
        "title": "The Way of Kings",
        "image": "http://prodimage.images-bn.com/pimages/9780765376671_p0_v5_s1200x630.jpg",
        "alt": "Two soldiers staring at each other across a massive chasm while a storm brews in the distance",
        "year": "2010",
        "summary": "Roshar is a world of stone and storms. Uncanny tempests of incredible power sweep across the rocky terrain so frequently that they have shaped ecology and civilization alike. Animals hide in shells, trees pull in branches, and grass retracts into the soilless ground. Cities are built only where the topography offers shelter.\n"

        "It has been centuries since the fall of the ten consecrated orders known as the Knights Radiant, but their Shardblades and Shardplate remain: mystical swords and suits of armor that transform ordinary men into near-invincible warriors. Men trade kingdoms for Shardblades. Wars were fought for them, and won by them."

        "One such war rages on a ruined landscape called the Shattered Plains. There, Kaladin, who traded his medical apprenticeship for a spear to protect his little brother, has been reduced to slavery. In a war that makes no sense, where ten armies fight separately against a single foe, he struggles to save his men and to fathom the leaders who consider them expendable."

        "Brightlord Dalinar Kholin commands one of those other armies. Like his brother, the late king, he is fascinated by an ancient text called The Way of Kings. Troubled by over-powering visions of ancient times and the Knights Radiant, he has begun to doubt his own sanity."

        "Across the ocean, an untried young woman named Shallan seeks to train under an eminent scholar and notorious heretic, Dalinar's niece, Jasnah. Though she genuinely loves learning, Shallan's motives are less than pure. As she plans a daring theft, her research for Jasnah hints at secrets of the Knights Radiant and the true cause of the war.",
        "author": "Brandon Sanderson",
        "score": "4.8",
        "pages": "1137 ",
        "similar": ["Mistborn: The Final Empire", "Words of Radiance", "Eye Of The World", "Oathbringer", "The Gathering Storm"]
    },
    "2": {
        "id": "2",
        "title": "The Eye of The World",
        "image": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/hostedimages/1555156262i/27358048.jpg",
        "alt": "Young red haired man stares into the distance while holding on to the mast of a boat with a big white tower in the background.",
        "year": "1990",
        "summary": "The Eye of the World, the first novel in Robert Jordan's #1 New York Times bestselling epic fantasy series, The Wheel of Time®, follows Moiraine Damodred as she arrives in Emond's Field on a quest to find the one prophesized to stand against The Dark One. \n"

        "The Wheel of Time turns and Ages come and pass, leaving memories that become legend. Legend fades to myth, and even myth is long forgotten when the Age that gave it birth returns again. What was, what will be, and what is, may yet fall under the Shadow."

        "When a vicious band of half-men, half beasts invade the Two Rivers seeking their master’s enemy, Moiraine persuades Rand al’Thor and his friends to leave their home and enter a larger unimaginable world filled with dangers waiting in the shadows and in the light."

        "Since its debut in 1990, The Wheel of Time® has captivated millions of readers around the globe with its scope, originality, and compelling characters. The last six books in series were all instant #1 New York Times bestsellers, and The Eye of the World was named one of America's best-loved novels by PBS's The Great American Read.",
        "author": "Robert Jordan",
        "score": "4.7",
        "pages": "753 ",
        "similar": ["The Dragon Reborn", "Mistborn: The Final Empire", "The Way of Kings", "Lord of the Rings", "The Blade Itself"]

    },
    "3": {
        "id": "3",
        "title": "The Lord Of The Rings",
        "alt": "Golden ring with something written on it that is not in any language known to main",
        "image": "https://images-na.ssl-images-amazon.com/images/I/51kfFS5-fnL._SX332_BO1,204,203,200_.jpg",
        "year": "1955",
        "summary": "One Ring to rule them all, One Ring to find them, One Ring to bring them all and in the darkness bind them"

        "In ancient times the Rings of Power were crafted by the Elven-smiths, and Sauron, the Dark Lord, forged the One Ring, filling it with his own power so that he could rule all others. But the One Ring was taken from him, and though he sought it throughout Middle-earth, it remained lost to him. After many ages it fell by chance into the hands of the hobbit Bilbo Baggins."

        "From Sauron's fastness in the Dark Tower of Mordor, his power spread far and wide. Sauron gathered all the Great Rings to him, but always he searched for the One Ring that would complete his dominion."

        "When Bilbo reached his eleventy-first birthday he disappeared, bequeathing to his young cousin Frodo the Ruling Ring and a perilous quest: to journey across Middle-earth, deep into the shadow of the Dark Lord, and destroy the Ring by casting it into the Cracks of Doom."

        "The Lord of the Rings tells of the great quest undertaken by Frodo and the Fellowship of the Ring: Gandalf the Wizard; the hobbits Merry, Pippin, and Sam; Gimli the Dwarf; Legolas the Elf; Boromir of Gondor; and a tall, mysterious stranger called Strider.",
        "author": "J.R.R. Tolkien",
        "score": "4.8",
        "pages": "1209 ",
        "similar": ["The Way of Kings", "Three Parts Dead", "The Blade Itself", "The Eye of The World"]
    },
    "4": {
        "id": "4",
        "title": "The Blade Itself",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhhmXsZYtcTAmVMtDe7-OwlthCqVHXl-yHn7LQCJohKkftuY0t1pReM6jGcMnaIEHsjQ8&usqp=CAU",
        "alt": "The words 'The Blade Itself' written on what parchment, with blood fresh on the page.",
        "year": "2015",
        "summary": "Logen Ninefingers, infamous barbarian, has finally run out of luck. Caught in one feud too many, he's on the verge of becoming a dead barbarian -- leaving nothing behind him but bad songs, dead friends, and a lot of happy enemies."

        "Nobleman, dashing officer, and paragon of selfishness, Captain Jezal dan Luthar has nothing more dangerous in mind than fleecing his friends at cards and dreaming of glory in the fencing circle. But war is brewing, and on the battlefields of the frozen North they fight by altogether bloodier rules. "

        "Inquisitor Glokta, cripple turned torturer, would like nothing better than to see Jezal come home in a box. But then Glokta hates everyone: cutting treason out of the Union one confession at a time leaves little room for friendship. His latest trail of corpses may lead him right to the rotten heart of government, if he can stay alive long enough to follow it. "

        "Enter the wizard, Bayaz. A bald old man with a terrible temper and a pathetic assistant, he could be the First of the Magi, he could be a spectacular fraud, but whatever he is, he's about to make the lives of Logen, Jezal, and Glokta a whole lot more difficult. "

        "Murderous conspiracies rise to the surface, old scores are ready to be settled, and the line between hero and villain is sharp enough to draw blood. ",
        "author": "Joe Abercrombie",
        "score": "4.5",
        "pages": "536 ",
        "similar": ["Lord of The Rings", "Eye of the World", "The Way Of Kings", "Mistborn: The Final Empire"]
    },
    "5": {
        "id": "5",
        "title": "Three Parts Dead",
        "image": "https://images-na.ssl-images-amazon.com/images/I/51JG1skVtmL._SX310_BO1,204,203,200_.jpg",
        "alt": "Girl with a blue blade stares menacingly down an alley while a crowd gathers behind her. ",
        "year": "2012",
        "summary": "Max Gladstone's Craft Sequence chronicles the epic struggle to build a just society in a modern fantasy world."

        "A god has died, and it's up to Tara, first-year associate in the international necromantic firm of Kelethres, Albrecht, and Ao, to bring Him back to life before His city falls apart."

        "Her client is Kos, recently deceased fire god of the city of Alt Coulumb. Without Him, the metropolis's steam generators will shut down, its trains will cease running, and its four million citizens will riot."

        "Tara's job: resurrect Kos before chaos sets in. Her only help: Abelard, a chain-smoking priest of the dead god, who's having an understandable crisis of faith."

        "When Tara and Abelard discover that Kos was murdered, they have to make a case in Alt Coulumb's courts?and their quest for the truth endangers their partnership, their lives, and Alt Coulumb's slim hope of survival.",
        "author": "Max Gladstone",
        "score": "4.6",
        "pages": "334 ",
        "similar": ["The Eye of The World", "The Red Knight", "Words of Radiance", "The Gathering Storm", "The Blade Itself"]
    },
    "6": {
        "id": "6",
        "title": "The Red Knight",
        "image": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1348037761l/13616278.jpg",
        "alt": "Dragon stares down at knight while knight brandishes his sword toward the dragon",
        "year": "2013",
        "summary": "Twenty eight florins a month is a huge price to pay, for a man to stand between you and the Wild."

        "Twenty eight florins a month is nowhere near enough when a wyvern's jaws snap shut on your helmet in the hot stink of battle, and the beast starts to rip the head from your shoulders. But if standing and fighting is hard, leading a company of men -- or worse, a company of mercenaries -- against the smart, deadly creatures of the Wild is even harder."

        "It takes all the advantages of birth, training, and the luck of the devil to do it."

        "The Red Knight has all three, he has youth on his side, and he's determined to turn a profit. So when he hires his company out to protect an Abbess and her nunnery, it's just another job. The abby is rich, the nuns are pretty and the monster preying on them is nothing he can't deal with."

        "Only it's not just a job. It's going to be a war. . .",
        "author": "Miles Cameron",
        "score": "4.7",
        "pages": "667 ",
        "similar": ['The Blade Itself', 'Three Parts Dead', 'The Eye of the World', 'Lord of The Rings']
    },
    "7": {
        "id": "7",
        "title": "The Shadow of What Was Lost",
        "image": "https://m.media-amazon.com/images/I/51oul60C3fL.jpg",
        "alt": "Group of people holding weapons walks toward an dark orange sun in the distance, with ruins to the left of them.",
        "year": "2016",
        "summary": "A young man with forbidden magic finds himself drawn into an ancient war against a dangerous enemy in book one of the Licanius Trilogy, the series that fans are heralding as the next Wheel of Time. "

        "As destiny calls, a journey begins."

        "It has been twenty years since the godlike Augurs were overthrown and killed. Now, those who once served them -- the Gifted -- are spared only because they have accepted the rebellion's Four Tenets, vastly limiting their powers."

        "As a Gifted, Davian suffers the consequences of a war lost before he was even born. He and others like him are despised. But when Davian discovers he wields the forbidden power of the Augurs, he and his friends Wirr and Asha set into motion a chain of events that will change everything."

        "To the west, a young man whose fate is intertwined with Davian's wakes up in the forest, covered in blood and with no memory of who he is. . . "

        "And in the far north, an ancient enemy long thought defeated begins to stir.",
        "author": "James Islington",
        "score": "4.8",
        "pages": "604 ",
        "similar": ["The Red Knight", "The Lord Of The Rings", "The Way Of Kings", "Three Parts Dead", "Mistborn: The Final Empire"]
    },
    "8": {
        "id": "8",
        "title": "A Game Of Thrones",
        "image": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1562726234l/13496.jpg",
        "alt": "A wolf stands on two legs against a golden background",
        "year": "2003",
        "summary": "Winter is coming. Such is the stern motto of House Stark, the northernmost of the fiefdoms that owe allegiance to King Robert Baratheon in far-off King’s Landing. There Eddard Stark of Winterfell rules in Robert’s name. There his family dwells in peace and comfort: his proud wife, Catelyn; his sons Robb, Brandon, and Rickon; his daughters Sansa and Arya; and his bastard son, Jon Snow. Far to the north, behind the towering Wall, lie savage Wildings and worse—unnatural things relegated to myth during the centuries-long summer, but proving all too real and all too deadly in the turning of the season."

        "Yet a more immediate threat lurks to the south, where Jon Arryn, the Hand of the King, has died under mysterious circumstances. Now Robert is riding north to Winterfell, bringing his queen, the lovely but cold Cersei, his son, the cruel, vainglorious Prince Joffrey, and the queen’s brothers Jaime and Tyrion of the powerful and wealthy House Lannister—the first a swordsman without equal, the second a dwarf whose stunted stature belies a brilliant mind. All are heading for Winterfell and a fateful encounter that will change the course of kingdoms."

        "Meanwhile, across the Narrow Sea, Prince Viserys, heir of the fallen House Targaryen, which once ruled all of Westeros, schemes to reclaim the throne with an army of barbarian Dothraki—whose loyalty he will purchase in the only coin left to him: his beautiful yet innocent sister, Daenerys.",
        "author": "George R. R. Martin",
        "score": "4.6",
        "pages": "819 ",
        "similar": ["Mistborn: The Final Empire", "Words of Radiance", "Eye Of The World", "Oathbringer", "The Gathering Storm"]
    },
    "9": {
        "id": "9",
        "title": "The Name Of The Wind",
        "image": "https://target.scene7.com/is/image/Target/GUEST_fd542de5-758a-4b64-9a26-cd4864c776f3?wid=488&hei=488&fmt=pjpeg",
        "alt": "A person in flowing robes stares toward a lone tree with a storm coming.",
        "year": "2007",
        "summary": "My name is Kvothe."

        "I have stolen princesses back from sleeping barrow kings. I burned down the town of Trebon. I have spent the night with Felurian and left with both my sanity and my life. I was expelled from the University at a younger age than most people are allowed in. I tread paths by moonlight that others fear to speak of during day. I have talked to Gods, loved women, and written songs that make the minstrels weep."

        "You may have heard of me."

        "So begins a tale unequaled in fantasy literature—the story of a hero told in his own voice. It is a tale of sorrow, a tale of survival, a tale of one man’s search for meaning in his universe, and how that search, and the indomitable will that drove it, gave birth to a legend.  ",
        "author": "Patrick Rothfuss",
        "score": "4.5",
        "pages": "718 ",
        "similar": ["The Dragon Reborn", "Mistborn: The Final Empire", "The Way of Kings", "Lord of the Rings", "The Blade Itself"]
    },
    "10": {
        "id": "10",
        "title": "Gardens of the Moon",
        "image": "https://target.scene7.com/is/image/Target/GUEST_f8de73e1-8f8e-41f8-b99d-f3cf1f3433c5?wid=488&hei=488&fmt=pjpeg",
        "alt": "A dark tower juts out from the ground with clouds and a moon behind it. ",
        "year": "2004",
        "summary": "The Malazan Empire simmers with discontent, bled dry by interminable warfare, bitter infighting and bloody confrontations with the formidable Anomander Rake and his Tiste Andii, ancient and implacable sorcerers. Even the imperial legions, long inured to the bloodshed, yearn for some respite. Yet Empress Laseen's rule remains absolute, enforced by her dread Claw assassins. "

        "For Sergeant Whiskeyjack and his squad of Bridgeburners, and for Tattersail, surviving cadre mage of the Second Legion, the aftermath of the siege of Pale should have been a time to mourn the many dead. But Darujhistan, last of the Free Cities of Genabackis, yet holds out. It is to this ancient citadel that Laseen turns her predatory gaze. "

        "However, it would appear that the Empire is not alone in this great game. Sinister, shadowbound forces are gathering as the gods themselves prepare to play their hand... ",
        "author": "Steven Erikson",
        "score": "4.8",
        "pages": "499 ",
        "similar": ["The Red Knight", "The Lord Of The Rings", "The Way Of Kings", "Three Parts Dead", "Mistborn: The Final Empire"]
    }

}


@ app.route('/', methods=['GET', 'POST'])
def home():
    top_three = [books["7"], books["2"], books["3"]]
    return render_template('home.html', books=top_three)


@ app.route('/view/<id>', methods=['GET', 'POST'])
def page(id=None):
    global books
    books_view = books[id]

    return render_template('book.html', books=books_view)


@app.route('/search_results/<search_text>')
def search_results(search_text=None):
    global books
    results = []
    summary_results = []

    for key, value in books.items():
        lowercase_title = value["title"].lower()
        lowercase_author = value["author"].lower()
        lowercase_summary = value["summary"].lower()
        if not (lowercase_title.find(search_text.lower()) == -1):
            results.append(value)
        elif not (lowercase_author.find(search_text.lower()) == -1):
            results.append(value)
        elif not ((lowercase_summary.find(search_text.lower()) == -1)):
            results.append(value)

    return render_template('search_results.html', books=results, search_for=search_text)


@ app.route('/add', methods=['GET', 'POST'])
def add():
    global books
    return render_template('add.html', books=books, current_id=current_id)


@ app.route('/add_new', methods=['GET', 'POST'])
def add_new():
    global books
    global current_id

    json_data = request.get_json()
    title = json_data["title"]
    author = json_data["author"]
    image = json_data["image"]
    alt = json_data["alt"]
    summary = json_data["summary"]
    score = json_data["score"]
    pages = json_data["pages"]
    similar = json_data["similar"]
    year = json_data["year"]

    new_book = {
        str(current_id): {
            "id": str(current_id),
            "title": title,
            "year": year,
            "author": author,
            "image": image,
            "alt": alt,
            "summary": summary,
            "score": score,
            "pages": pages,
            "similar": similar.split(",")
        }
    }

    books.update(new_book)
    current_id += 1

    return jsonify(books=books, current_id=current_id)


@ app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id=None):
    global books
    books_edit = books[id]
   # books_edit["similar"] = ",".split(books_edit["similar"])

    return render_template('edit.html', books=books_edit)


@ app.route('/new_edit', methods=['GET', 'POST'])
def new_edit():
    global books
    json_data = request.get_json()
    id = json_data["id"]
    title = json_data["title"]
    author = json_data["author"]
    image = json_data["image"]
    alt = json_data["alt"]
    summary = json_data["summary"]
    score = json_data["score"]
    pages = json_data["pages"]

    year = json_data["year"]
    similar = json_data["similar"]
    books[id] = {
        "id": id,
        "title": title,
        "author": author,
        "image": image,
        "alt": alt,
        "summary": summary,
        "score": score,
        "pages": pages,
        "similar": ",".join(similar),
        "year": year
    }
    page(str(id))
    return render_template("book.html", books=books[id])


if __name__ == '__main__':
    app.run(debug=True)
